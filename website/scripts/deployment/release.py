"""Publish/verify routing for the production support site. No AWS calls on import."""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.request
import uuid

ACCOUNT = '144076755730'
DISTRIBUTION = 'E3TMOKZN8HQ7AZ'
ORIGIN = 'https://support.telnyx.com'
DISTRIBUTION_DOMAIN = 'd27az1l5lty0u1.cloudfront.net'
BUCKET = 'support.telnyx.com'
READY = '_meta:ready'
PROTOCOL = 'support-v2-origin-fallback-v1'
EXTERNAL_KEY = 'article:11409065'
EXTERNAL = 'https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to'


class ConcurrentUpdate(RuntimeError):
    pass


def save(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, indent=2) + '\n')


def aws(service, operation, **kwargs):
    args = ['aws', service, operation, '--output', 'json', '--no-cli-pager', '--no-paginate']
    for k, v in kwargs.items():
        args += ['--' + k.replace('_', '-'), json.dumps(v) if isinstance(v, (dict, list)) else str(v)]
    for attempt in range(5):
        result = subprocess.run(args, text=True, capture_output=True)
        if result.returncode == 0:
            return json.loads(result.stdout or '{}')
        if 'PreconditionFailed' in result.stderr or 'ConflictException' in result.stderr:
            raise ConcurrentUpdate('Store changed concurrently; refusing to overwrite or roll back another writer')
        # ETag conflicts are not retried blindly: a different writer must be investigated.
        if not any(code in result.stderr for code in ['Throttling', 'TooManyRequests', 'ServiceUnavailable', 'InternalServerError']) or attempt == 4:
            raise RuntimeError(f'{service} {operation}: {result.stderr.strip()}')
        time.sleep(2 ** attempt)


def configuration():
    distribution = os.environ.get('CLOUDFRONT_DISTRIBUTION_ID', '')
    arn = os.environ.get('CLOUDFRONT_KVS_ARN', '')
    if distribution != DISTRIBUTION:
        raise ValueError('Missing or unexpected temporary distribution ID')
    if not re.fullmatch(r'arn:aws:cloudfront::' + ACCOUNT + r':key-value-store/[a-zA-Z0-9-]+', arn):
        raise ValueError('Missing or unexpected dedicated KeyValueStore ARN')
    return arn


def read_store(call, arn):
    result, token = {}, None
    while True:
        args = {'kvs_arn': arn, 'max_results': 50}
        if token:
            args['next_token'] = token
        page = call('cloudfront-keyvaluestore', 'list-keys', **args)
        for item in page.get('Items', []):
            if item['Key'] in result:
                raise ValueError('Duplicate key while reading store; possible concurrent writer')
            result[item['Key']] = item['Value']
        token = page.get('NextToken')
        if not token:
            return result


def validate_registry(routes, dist):
    if not isinstance(routes, dict) or not routes:
        raise ValueError('Empty or invalid route registry')
    root = Path(dist).resolve()
    canonical = set()
    for directory in ['en/articles', 'en/collections']:
        canonical.update('/' + str(p.relative_to(root)) for p in (root / directory).glob('*') if p.is_file() and p.suffix != '.md')
    if not canonical:
        raise ValueError('Release has no canonical pages')
    for key, target in routes.items():
        if not isinstance(target, str) or not re.fullmatch(r'(article|collection):\d+|path:/collection/[a-z-]+', key):
            raise ValueError(f'Invalid route key/value: {key}')
        if len(key.encode()) > 512 or len(target.encode()) > 1024:
            raise ValueError('Route exceeds KeyValueStore size limits')
        if target == EXTERNAL and key == EXTERNAL_KEY:
            continue
        if not re.fullmatch(r'/en/(articles|collections)/\d+-[a-zA-Z0-9-]+', target) or target not in canonical:
            raise ValueError(f'Unbuilt or unsafe redirect target: {key} -> {target}')
        kind, identity = re.match(r'/en/(articles|collections)/(\d+)', target).groups()
        if routes.get(('article:' if kind == 'articles' else 'collection:') + identity) != target:
            raise ValueError(f'Redirect chain or missing canonical route: {key}')
    for target in canonical:
        match = re.fullmatch(r'/en/(articles|collections)/(\d+)-[a-zA-Z0-9-]+', target)
        if not match or routes.get(('article:' if match[1] == 'articles' else 'collection:') + match[2]) != target:
            raise ValueError(f'Canonical page omitted from generated registry: {target}')
    if sum(len(k.encode()) + len(v.encode()) for k, v in routes.items()) > 4_500_000:
        raise ValueError('Route store too close to the 5 MB limit')
    return canonical


def sync(call, arn, before, desired, allow_remove=False):
    removed = set(before) - set(desired)
    if removed and not allow_remove:
        raise ValueError('Previously published identities disappeared; preserve them with repository redirects: ' + ', '.join(sorted(removed)))
    description = call('cloudfront-keyvaluestore', 'describe-key-value-store', kvs_arn=arn)
    etag = description['ETag']
    if read_store(call, arn) != before or call('cloudfront-keyvaluestore', 'describe-key-value-store', kvs_arn=arn)['ETag'] != etag:
        raise ConcurrentUpdate('Store changed while preparing synchronization')
    operations = [('put', k, v) for k, v in sorted(desired.items()) if before.get(k) != v]
    operations += [('delete', k, None) for k in sorted(removed)]
    for offset in range(0, len(operations), 50):
        batch = operations[offset:offset + 50]
        args = {'kvs_arn': arn, 'if_match': etag}
        puts = [{'Key': k, 'Value': v} for op, k, v in batch if op == 'put']
        deletes = [{'Key': k} for op, k, _ in batch if op == 'delete']
        if puts:
            args['puts'] = puts
        if deletes:
            args['deletes'] = deletes
        etag = call('cloudfront-keyvaluestore', 'update-keys', **args)['ETag']
    after = read_store(call, arn)
    if after != desired:
        raise RuntimeError('Stored routing data does not match the intended release')


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def request(url, method='GET'):
    try:
        response = urllib.request.build_opener(NoRedirect).open(urllib.request.Request(url, method=method), timeout=20)
    except urllib.error.HTTPError as e:
        response = e
    return response.code, dict(response.headers), response.read()


def check_http(path, status, location=None, method='GET', expected_hash=None):
    last = None
    for attempt in range(4):
        try:
            code, headers, body = request(ORIGIN + path, method)
            actual_location = next((v for k, v in headers.items() if k.lower() == 'location'), None)
            if code != status or (location is not None and actual_location != location):
                raise ValueError(f'Expected {status} {location}, got {code} {actual_location}')
            if method == 'HEAD' and body:
                raise ValueError('HEAD response contained a body')
            if method == 'GET' and status == 200 and (b'<h1' not in body or b'<meta name="robots"' not in body):
                raise ValueError('Missing rendered content or robots metadata')
            if expected_hash and hashlib.sha256(body).hexdigest() != expected_hash:
                raise ValueError('Live HTML does not match the uploaded release')
            if method == 'GET' and status == 404 and b'Page not found' not in body:
                raise ValueError('Missing useful 404 page')
            return {'url': ORIGIN + path, 'method': method, 'status': code, 'location': actual_location}
        except Exception as e:
            last = e
            if attempt < 3:
                time.sleep(2 ** attempt)
    raise RuntimeError(f'{method} {path}: {last}')


def verify(routes, canonical, bootstrap, dist):
    tasks = [(p, 200, None, 'GET', hashlib.sha256((Path(dist) / ('index.html' if p == '/' else p.lstrip('/'))).read_bytes()).hexdigest()) for p in sorted(canonical | {'/'})]
    for p in ['/en/articles/99999999-nonexistent', '/en/collections/99999999-nonexistent', '/nonexistent-migration-test']:
        tasks += [(p, 404, None, method) for method in ['GET', 'HEAD']]
    if not bootstrap:
        for key, target in routes.items():
            if key.startswith('path:'):
                aliases = [key[5:]]
            else:
                kind, identity = key.split(':')
                aliases = [f'/en/{kind}s/{identity}', f'/en/{kind}s/{identity}-migration-check/']
            for alias in aliases:
                tasks.append((alias, 301, target, 'HEAD'))
        for p in ['/en', '/en/', '/en/index.html', '/index.html']:
            tasks.append((p, 301, '/', 'GET'))
        tasks.append(('/en/articles/4230755-old?q=a%2Fb&q=c%26d', 301, routes['article:4230755'] + '?q=a%2Fb&q=c%26d', 'GET'))
        code, _, _ = request(EXTERNAL)
        if code != 200:
            raise ValueError('Approved external redirect target is not direct HTTP 200')
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        checks = list(pool.map(lambda args: check_http(*args), tasks))
        checks.extend(pool.map(lambda file: verify_download(file, dist), sorted((Path(dist) / 'downloads').glob('*'))))
        return checks


def verify_download(file, dist):
    url = ORIGIN + '/' + str(file.relative_to(dist))
    code, _, body = request(url)
    if code != 200 or hashlib.sha256(body).digest() != hashlib.sha256(file.read_bytes()).digest():
        raise ValueError('Live download does not match release: ' + url)
    return {'url': url, 'method': 'GET', 'status': code, 'sha256': hashlib.sha256(body).hexdigest()}


def invalidate(call):
    # Use the service's structured batch: CLI --paths is a custom argument
    # that treats a JSON list as a literal path, producing InvalidArgument.
    result = call('cloudfront', 'create-invalidation', distribution_id=DISTRIBUTION, invalidation_batch={
        'Paths': {'Quantity': 1, 'Items': ['/*']},
        'CallerReference': 'knowledge-base-' + uuid.uuid4().hex,
    })
    identity = result['Invalidation']['Id']
    for _ in range(90):
        if call('cloudfront', 'get-invalidation', distribution_id=DISTRIBUTION, id=identity)['Invalidation']['Status'] == 'Completed':
            return identity
        time.sleep(10)
    raise TimeoutError('CloudFront invalidation did not finish within 15 minutes')


def preflight(call, arn, routes, dist, bootstrap, rollback):
    validate_registry(routes, dist)
    if call('sts', 'get-caller-identity')['Account'] != ACCOUNT:
        raise ValueError('Unexpected AWS account')
    distribution = call('cloudfront', 'get-distribution', id=DISTRIBUTION)['Distribution']
    if distribution['DomainName'] != DISTRIBUTION_DOMAIN:
        raise ValueError('Unexpected CloudFront domain')
    config = distribution['DistributionConfig']
    if 'support.telnyx.com' not in config.get('Aliases', {}).get('Items', []):
        raise ValueError('Production hostname is not attached to the expected distribution')
    origins = config['Origins']['Items']
    if len(origins) != 1 or not origins[0]['DomainName'].startswith(BUCKET + '.s3.'):
        raise ValueError('Unexpected S3 origin')
    associations = config['DefaultCacheBehavior'].get('FunctionAssociations', {}).get('Items', [])
    active = any(x['EventType'] == 'viewer-request' and x['FunctionARN'].endswith('/support-v2-kb-routing') for x in associations)
    if bootstrap and active:
        raise ValueError('Bootstrap is only permitted before routing activation')
    if not bootstrap and not active:
        raise ValueError('Routing not activated; complete the bundled infra bootstrap and activation first')
    description = call('cloudfront-keyvaluestore', 'describe-key-value-store', kvs_arn=arn)
    if description.get('KvsARN') != arn or description.get('Status') != 'READY':
        raise ValueError('Wrong store or store not ready')
    before = read_store(call, arn)
    if before.get(READY) not in (None, PROTOCOL):
        raise ValueError('Incompatible store protocol')
    if not bootstrap and before.get(READY) != PROTOCOL:
        raise ValueError('Normal publication requires a verified bootstrap marker')
    previous = {k: v for k, v in before.items() if k != READY}
    if not rollback and set(previous) - set(routes):
        raise ValueError('Route removal requires a retained redirect or an explicit verified rollback release')
    return before


def restore_routes(call, arn, before, desired):
    current = read_store(call, arn)
    missing = object()
    # A failed batch may leave a mix of the old and intended release. Any other
    # value belongs to a concurrent writer and must never be overwritten.
    for key in set(before) | set(desired) | set(current):
        if current.get(key, missing) not in (before.get(key, missing), desired.get(key, missing)):
            raise ConcurrentUpdate('Unexpected routing data during recovery; manual review required')
    sync(call, arn, current, before, allow_remove=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['prepare', 'publish'])
    parser.add_argument('--bootstrap', action='store_true')
    parser.add_argument('--rollback', action='store_true')
    args = parser.parse_args()
    arn = configuration()
    root = Path(__file__).resolve().parents[2]
    routes = json.loads((root / 'dist-edge/routes.json').read_text())
    dist, reports = root / 'dist', root / 'release-report'
    canonical = validate_registry(routes, dist)
    if args.phase == 'prepare':
        before = preflight(aws, arn, routes, dist, args.bootstrap, args.rollback)
        save(reports / 'before.json', before)
        save(reports / 'release.json', {'store': arn, 'distribution': DISTRIBUTION, 'protocol': PROTOCOL, 'bootstrap': args.bootstrap, 'rollback': args.rollback, 'source_sha': os.environ.get('RELEASE_SHA', ''), 'registry_sha256': hashlib.sha256(json.dumps(routes, sort_keys=True).encode()).hexdigest()})
        return
    metadata = json.loads((reports / 'release.json').read_text())
    if metadata != {'store': arn, 'distribution': DISTRIBUTION, 'protocol': PROTOCOL, 'bootstrap': args.bootstrap, 'rollback': args.rollback, 'source_sha': os.environ.get('RELEASE_SHA', ''), 'registry_sha256': hashlib.sha256(json.dumps(routes, sort_keys=True).encode()).hexdigest()}:
        raise ValueError('Release/configuration changed after preflight')
    before = json.loads((reports / 'before.json').read_text())
    if read_store(aws, arn) != before:
        raise ValueError('Store changed since preflight; refusing to overwrite another release')
    try:
        # Preserve the readiness marker during routine updates; bootstrap writes it last.
        desired = {**routes, **({READY: PROTOCOL} if READY in before else {})}
        sync(aws, arn, before, desired, args.rollback)
        invalidation = invalidate(aws)
        save(reports / 'http.json', verify(routes, canonical, args.bootstrap, dist))
        if READY not in desired:
            sync(aws, arn, desired, {**desired, READY: PROTOCOL})
        save(reports / 'success.json', {'invalidation': invalidation, 'source_sha': metadata['source_sha'], 'mode': 'bootstrap-ready-for-infra-activation' if args.bootstrap else 'release-verified'})
        if os.environ.get('GITHUB_STEP_SUMMARY'):
            with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
                summary.write(f"\nVerified production release: `{metadata['source_sha']}`\n")
    except ConcurrentUpdate:
        save(reports / 'failure.json', {'routing_restored': False, 'reason': 'Concurrent writer detected; stopped without overwriting its changes.'})
        raise
    except Exception as error:
        # Content uploads retain old objects; recover routing even after a partial batch.
        try:
            restore_routes(aws, arn, before, {**desired, READY: PROTOCOL})
            invalidate(aws)
        except Exception as recovery_error:
            save(reports / 'failure.json', {'routing_restored': False, 'reason': str(error), 'recovery_error': str(recovery_error), 'action': 'Inspect store/content and recover the prior verified release; automatic recovery did not complete.'})
            raise RuntimeError('Publication and automatic recovery failed; inspect release-report/failure.json') from recovery_error
        save(reports / 'failure.json', {'routing_restored': True, 'content_rollback': 'Rerun workflow with the prior successful release run ID to restore overwritten content.'})
        raise


if __name__ == '__main__':
    main()
