import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import release


class Store:
    def __init__(self, values=None):
        self.values = dict(values or {})
        self.etag = 1
        self.batches = []

    def __call__(self, service, operation, **kwargs):
        if operation == 'describe-key-value-store':
            return {'ETag': str(self.etag), 'KvsARN': kwargs['kvs_arn'], 'Status': 'READY'}
        if operation == 'list-keys':
            return {'Items': [{'Key': k, 'Value': v} for k, v in self.values.items()]}
        if operation == 'update-keys':
            if kwargs['if_match'] != str(self.etag):
                raise release.ConcurrentUpdate('ETag mismatch')
            self.batches.append(kwargs)
            for item in kwargs.get('puts', []):
                self.values[item['Key']] = item['Value']
            for item in kwargs.get('deletes', []):
                del self.values[item['Key']]
            self.etag += 1
            return {'ETag': str(self.etag)}
        raise AssertionError(operation)


class ReleaseTests(unittest.TestCase):
    def test_batches_conditional_writes_and_idempotence(self):
        store = Store()
        target = {f'article:{i}': f'/en/articles/{i}-page' for i in range(123)}
        release.sync(store, 'arn', {}, target)
        self.assertEqual([len(b['puts']) for b in store.batches], [50, 50, 23])
        self.assertEqual([b['if_match'] for b in store.batches], ['1', '2', '3'])
        release.sync(store, 'arn', target, target)
        self.assertEqual(len(store.batches), 3)

    def test_missing_retired_identity_blocks_removal_before_writes(self):
        store = Store({'article:1': '/en/articles/1-page'})
        with self.assertRaises(ValueError):
            release.sync(store, 'arn', dict(store.values), {})
        self.assertEqual(store.batches, [])

    def test_explicit_rollback_restores_snapshot(self):
        original = {'article:1': '/en/articles/1-before', release.READY: release.PROTOCOL}
        store = Store(original)
        release.sync(store, 'arn', original, {**original, 'article:1': '/en/articles/1-after', 'article:2': '/en/articles/2-new'})
        release.sync(store, 'arn', dict(store.values), original, allow_remove=True)
        self.assertEqual(store.values, original)

    def test_concurrent_writer_is_not_overwritten(self):
        store = Store({'article:1': '/en/articles/1-outside-change'})
        with self.assertRaises(release.ConcurrentUpdate):
            release.sync(store, 'arn', {'article:1': '/en/articles/1-before'}, {'article:1': '/en/articles/1-after'})
        self.assertEqual(store.batches, [])

    def test_recovery_accepts_partial_batch_but_not_another_writer(self):
        before = {'article:1': 'one', 'article:2': 'two'}
        desired = {'article:1': 'new-one', 'article:2': 'new-two'}
        store = Store({**before, 'article:1': 'new-one'})
        release.restore_routes(store, 'arn', before, desired)
        self.assertEqual(store.values, before)
        store = Store({**before, 'article:1': 'someone-else'})
        with self.assertRaises(release.ConcurrentUpdate):
            release.restore_routes(store, 'arn', before, desired)
        self.assertEqual(store.batches, [])

    def test_paginated_store_reads(self):
        pages = iter([{'Items': [{'Key': 'a', 'Value': '1'}], 'NextToken': 'next'}, {'Items': [{'Key': 'b', 'Value': '2'}]}])
        args = []
        def call(*a, **kw):
            args.append(kw)
            return next(pages)
        self.assertEqual(release.read_store(call, 'arn'), {'a': '1', 'b': '2'})
        self.assertEqual(args[1]['next_token'], 'next')

    def test_registry_requires_real_direct_targets_and_full_coverage(self):
        with tempfile.TemporaryDirectory() as temp:
            page = Path(temp, 'en/articles/1-one')
            page.parent.mkdir(parents=True)
            page.write_text('<h1>One</h1>')
            valid = {'article:1': '/en/articles/1-one', 'article:2': '/en/articles/1-one', release.EXTERNAL_KEY: release.EXTERNAL}
            self.assertEqual(release.validate_registry(valid, temp), {'/en/articles/1-one'})
            for invalid in [{}, {'article:1': '/en/articles/3-missing'}, {'article:1': 'https://evil.test/'}, {'article:2': '/en/articles/1-one'}, {'article:1': '/../x'}, {'article:1': release.EXTERNAL}]:
                with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                    release.validate_registry(invalid, temp)

    def test_registry_ignores_markdown_siblings(self):
        with tempfile.TemporaryDirectory() as temp:
            page = Path(temp, 'en/articles/1-one')
            page.parent.mkdir(parents=True)
            page.write_text('<h1>One</h1>')
            Path(temp, 'en/articles/1-one.md').write_text('# One')
            valid = {'article:1': '/en/articles/1-one', release.EXTERNAL_KEY: release.EXTERNAL}
            self.assertEqual(release.validate_registry(valid, temp), {'/en/articles/1-one'})

    def test_bootstrap_preflight_and_marker_only_after_verification(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            page = root / 'dist/en/articles/1-one'
            page.parent.mkdir(parents=True)
            page.write_text('<h1>One</h1>')
            routes = {'article:1': '/en/articles/1-one'}
            (root / 'dist-edge').mkdir()
            (root / 'dist-edge/routes.json').write_text(json.dumps(routes))
            store = Store()
            active = False
            def call(service, operation, **kwargs):
                if service == 'sts':
                    return {'Account': release.ACCOUNT}
                if operation == 'get-distribution':
                    return {'Distribution': {'DomainName': release.DISTRIBUTION_DOMAIN, 'DistributionConfig': {
                        'Aliases': {'Items': ['support.telnyx.com']},
                        'Origins': {'Items': [{'DomainName': release.BUCKET + '.s3.us-east-1.amazonaws.com'}]},
                        'DefaultCacheBehavior': {'FunctionAssociations': {'Items': [{'EventType': 'viewer-request', 'FunctionARN': 'arn/function/support-v2-kb-routing'}] if active else []}}
                    }}}
                return store(service, operation, **kwargs)
            release.preflight(call, 'arn', routes, root / 'dist', True, False)
            with self.assertRaises(ValueError):
                release.preflight(call, 'arn', routes, root / 'dist', False, False)
            active = True
            with self.assertRaises(ValueError):
                release.preflight(call, 'arn', routes, root / 'dist', True, False)
            active = False
            with patch('release.configuration', return_value='arn'), patch('release.aws', side_effect=call), patch('release.__file__', str(root / 'scripts/deployment/release.py')), patch('release.invalidate', return_value='invalidation'), patch('release.upload_content'):
                with patch('sys.argv', ['release.py', 'prepare', '--bootstrap']):
                    release.main()
                with patch('sys.argv', ['release.py', 'publish', '--bootstrap']), patch('release.verify', side_effect=RuntimeError('bad HTTP')):
                    with self.assertRaises(RuntimeError):
                        release.main()
                self.assertEqual(store.values, {})
                def verified(*args):
                    self.assertEqual(store.values, routes)
                    self.assertNotIn(release.READY, store.values)
                    return []
                with patch('sys.argv', ['release.py', 'publish', '--bootstrap']), patch('release.verify', side_effect=verified):
                    release.main()
                self.assertEqual(store.values, {**routes, release.READY: release.PROTOCOL})

    def test_partial_upload_failure_records_full_recovery_requirement(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            page = root / 'dist/en/articles/1-one'
            page.parent.mkdir(parents=True)
            page.write_text('<h1>One</h1>')
            routes = {'article:1': '/en/articles/1-one'}
            (root / 'dist-edge').mkdir()
            (root / 'dist-edge/routes.json').write_text(json.dumps(routes))
            before = {**routes, release.READY: release.PROTOCOL}
            store = Store(before)
            with patch('release.configuration', return_value='arn'), patch('release.aws', side_effect=store), patch('release.__file__', str(root / 'scripts/deployment/release.py')), patch('release.preflight', return_value=before), patch('release.invalidate', return_value='invalidation') as invalidation:
                with patch('sys.argv', ['release.py', 'prepare']):
                    release.main()
                with patch('sys.argv', ['release.py', 'publish']), patch('release.upload_content', side_effect=RuntimeError('partial S3 upload')), patch('release.verify') as verify:
                    with self.assertRaisesRegex(RuntimeError, 'partial S3 upload'):
                        release.main()
                    verify.assert_not_called()
                failure = json.loads((root / 'release-report/failure.json').read_text())
                self.assertTrue(failure['routing_restored'])
                self.assertFalse(failure['content_restored'])
                self.assertIn('rollback_run_id=', failure['action'])
                self.assertFalse((root / 'release-report/success.json').exists())
                self.assertEqual(store.values, before)
                invalidation.assert_called_once()

    def test_partial_route_publication_and_failed_recovery_evidence(self):
        for recovery_fails in [False, True]:
            with self.subTest(recovery_fails=recovery_fails), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                routes = {}
                for i in range(51):
                    page = root / f'dist/en/articles/{i}-new'
                    page.parent.mkdir(parents=True, exist_ok=True)
                    page.write_text('<h1>New</h1>')
                    routes[f'article:{i}'] = f'/en/articles/{i}-new'
                (root / 'dist-edge').mkdir()
                (root / 'dist-edge/routes.json').write_text(json.dumps(routes))
                before = {f'article:{i}': f'/en/articles/{i}-old' for i in range(51)}
                before[release.READY] = release.PROTOCOL
                store = Store(before)
                updates = []
                def call(service, operation, **kwargs):
                    if operation == 'update-keys':
                        updates.append(kwargs)
                        if len(updates) == 2:
                            raise RuntimeError('second publication batch failed')
                        if recovery_fails and len(updates) > 2:
                            raise RuntimeError('recovery batch failed')
                    return store(service, operation, **kwargs)
                with patch('release.configuration', return_value='arn'), patch('release.aws', side_effect=call), patch('release.__file__', str(root / 'scripts/deployment/release.py')), patch('release.preflight', return_value=before), patch('release.invalidate', return_value='invalidation'), patch('release.upload_content') as upload:
                    with patch('sys.argv', ['release.py', 'prepare']):
                        release.main()
                    with patch('sys.argv', ['release.py', 'publish']), patch('release.verify') as verify:
                        with self.assertRaises(RuntimeError):
                            release.main()
                        verify.assert_not_called()
                    upload.assert_called_once()
                self.assertEqual(len(updates), 3)
                self.assertEqual(len(updates[0]['puts']), 50)
                failure = json.loads((root / 'release-report/failure.json').read_text())
                self.assertEqual(failure['routing_restored'], not recovery_fails)
                self.assertFalse(failure['content_restored'])
                self.assertIn('second publication batch failed', failure['reason'])
                self.assertIn('rollback_run_id=', failure['action'])
                self.assertFalse((root / 'release-report/success.json').exists())
                if recovery_fails:
                    self.assertEqual(failure['recovery_error'], 'recovery batch failed')
                    self.assertNotEqual(store.values, before)
                else:
                    self.assertEqual(store.values, before)

    def test_upload_order_and_failure_stop(self):
        commands = []
        def run(args, **kwargs):
            self.assertTrue(kwargs['check'])
            commands.append(args)
        release.upload_content(Path('/dist'), run)
        self.assertEqual([c[3] for c in commands[:4]], ['/dist/assets', '/dist/_images', '/dist/downloads', '/dist/content'])
        self.assertIn('text/html; charset=utf-8', commands[-2])
        self.assertIn('text/markdown; charset=utf-8', commands[-1])
        self.assertTrue(all('--delete' not in c for c in commands))
        def fail(args, **kwargs):
            raise RuntimeError('upload failed')
        with self.assertRaisesRegex(RuntimeError, 'upload failed'):
            release.upload_content(Path('/dist'), fail)

    def test_wrong_distribution_and_store_rejected(self):
        for env in [{}, {'CLOUDFRONT_DISTRIBUTION_ID': 'OTHER'}, {'CLOUDFRONT_DISTRIBUTION_ID': release.DISTRIBUTION, 'CLOUDFRONT_KVS_ARN': 'arn:aws:cloudfront::000000000000:key-value-store/x'}]:
            with patch.dict('os.environ', env, clear=True), self.assertRaises(ValueError):
                release.configuration()

    def test_invalidation_waits_for_completion(self):
        calls = []
        def call(service, operation, **kw):
            calls.append(operation)
            return {'Invalidation': {'Id': 'test', 'Status': 'Completed' if len(calls) == 3 else 'InProgress'}}
        with patch('release.time.sleep'):
            self.assertEqual(release.invalidate(call), 'test')
        self.assertEqual(calls, ['create-invalidation', 'get-invalidation', 'get-invalidation'])

    def test_invalidation_cli_uses_structured_api_batch(self):
        import subprocess
        responses = [
            {'Invalidation': {'Id': 'test'}},
            {'Invalidation': {'Status': 'Completed'}},
        ]
        commands = []
        def run(args, **kwargs):
            commands.append(args)
            return subprocess.CompletedProcess(args, 0, json.dumps(responses.pop(0)), '')
        with patch('release.subprocess.run', side_effect=run):
            release.invalidate(release.aws)
        command = commands[0]
        self.assertNotIn('--paths', command)
        batch = json.loads(command[command.index('--invalidation-batch') + 1])
        self.assertEqual(batch['Paths'], {'Quantity': 1, 'Items': ['/*']})
        self.assertTrue(batch['CallerReference'].startswith('knowledge-base-'))

    def test_invalidation_timeout_fails(self):
        with patch('release.time.sleep'), self.assertRaises(TimeoutError):
            release.invalidate(lambda *a, **k: {'Invalidation': {'Id': 'test', 'Status': 'InProgress'}})

    def test_live_download_must_match_archived_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / 'downloads/example.docx'
            file.parent.mkdir()
            file.write_bytes(b'archived-document')
            with patch('release.request', return_value=(200, {}, b'archived-document')):
                self.assertEqual(release.verify_download(file, temp)['status'], 200)
            for response in [(200, {}, b'wrong-document'), (404, {}, b'archived-document')]:
                with patch('release.request', return_value=response), self.assertRaises(ValueError):
                    release.verify_download(file, temp)

    def test_production_checks_allow_indexed_and_explicitly_excluded_pages(self):
        import hashlib
        for directive in ['index,follow', 'noindex,nofollow']:
            body = ('<h1>Article</h1><meta name="robots" content="' + directive + '">').encode()
            with patch('release.request', return_value=(200, {}, body)):
                release.check_http('/article', 200, expected_hash=hashlib.sha256(body).hexdigest())
            with patch('release.request', return_value=(200, {}, body)), patch('release.time.sleep'), self.assertRaises(RuntimeError):
                release.check_http('/article', 200, expected_hash='stale-build')

    def test_http_requires_exact_redirect_without_following_chain(self):
        with patch('release.request', return_value=(301, {'Location': '/expected'}, b'')):
            self.assertEqual(release.check_http('/old', 301, '/expected')['status'], 301)
        with patch('release.request', return_value=(302, {'Location': '/intermediate'}, b'')), patch('release.time.sleep'), self.assertRaises(RuntimeError):
            release.check_http('/old', 301, '/expected')

    def test_http_rejects_soft_404_and_missing_content(self):
        with patch('release.request', return_value=(200, {}, b'homepage')), patch('release.time.sleep'), self.assertRaises(RuntimeError):
            release.check_http('/missing', 404)
        with patch('release.request', return_value=(200, {}, b'<h1>Preview</h1>')), patch('release.time.sleep'), self.assertRaises(RuntimeError):
            release.check_http('/new', 200)


if __name__ == '__main__':
    unittest.main()
