// Shared by local preview/tests and the generated CloudFront Function.
async function routeRequest(request, lookup) {
  var uri = request.uri;
  function response(status, title, message) {
    return { statusCode: status, statusDescription: title,
      headers: { 'content-type': { value: 'text/html; charset=utf-8' }, 'x-robots-tag': { value: 'noindex' } },
      body: request.method === 'HEAD' ? '' : '<!doctype html><html lang="en"><head><meta name="viewport" content="width=device-width"><title>' + title + ' | Telnyx Help Center</title></head><body><main><h1>' + title + '</h1><p>' + message + '</p><a href="/">Browse all topics</a></main></body></html>' };
  }
  function redirect(target) {
    var parts = [], query = request.querystring || {};
    Object.keys(query).forEach(function (key) {
      (query[key].multiValue || [query[key]]).forEach(function (item) { parts.push(key + '=' + item.value); });
    });
    return { statusCode: 301, statusDescription: 'Moved Permanently', headers: {
      location: { value: target + (parts.length ? '?' + parts.join('&') : '') },
      'cache-control': { value: 'public, max-age=300' }
    } };
  }
  if (request.method && request.method !== 'GET' && request.method !== 'HEAD') {
    var rejected = response(405, 'Method Not Allowed', 'Use GET or HEAD to read this page.');
    rejected.headers.allow = { value: 'GET, HEAD' }; return rejected;
  }
  if (uri === '/en' || uri === '/en/' || uri === '/en/index.html' || uri === '/index.html') return redirect('/');
  if (uri === '/favicon.ico') return redirect('/favicon.svg');
  if (uri === '/' || uri === '/llms.txt' || uri === '/robots.txt' || uri === '/sitemap.xml' || uri === '/favicon.svg' || /^\/(assets|_images|content)\//.test(uri) || /^\/[^/]+\.woff2?$/.test(uri)) return request;
  var normalized = uri.replace(/\/+$/, '');
  var match = normalized.match(/^\/en\/(articles|collections)\/(\d+)(?:-[^/]*)?$/);
  if (!match) {
    var old = normalized.match(/^\/article\/(?:en--(articles|collections)--)?(\d+)(?:-[^/]*)?$/);
    if (old) match = [old[0], old[1] || 'articles', old[2]];
    var oldCollection = normalized.match(/^\/collection\/(\d+)(?:-[^/]*)?$/);
    if (oldCollection) match = [oldCollection[0], 'collections', oldCollection[1]];
  }
  var key = match ? (match[1] === 'articles' ? 'article:' : 'collection:') + match[2] : 'path:' + normalized;
  var target;
  try { target = await lookup(key); }
  catch (_) { return response(503, 'Temporarily unavailable', 'Please try again shortly.'); }
  // The registry resolves historical URLs; it is not a publication allowlist.
  // Newly uploaded pages work before their IDs appear in the store. The origin
  // decides whether an unmapped object exists and supplies genuine 404s.
  if (!target) return request;
  // Permit only the explicitly approved external article destination.
  if (key === "article:11409065" && target === "https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to") return redirect(target);
  if (!/^\/en\/(articles|collections)\/\d+-[A-Za-z0-9-]+$/.test(target)) return response(503, 'Temporarily unavailable', 'Please try again shortly.');
  return target === uri ? request : redirect(target);
}
