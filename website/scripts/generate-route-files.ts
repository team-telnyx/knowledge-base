import fs from "fs";
import path from "path";
import { collections, articles } from "../src/content/manifest";

// The site is a client-side-routed SPA deployed to S3 as static files. A deep
// link like /article/<slug> only works if an object exists at that exact key,
// so after `vite build` we materialize every route as a copy of index.html.
// Routes are written as extensionless files (matching the URL) unless another
// route nests beneath them, in which case they must be directories on disk and
// get a <route>/index.html instead.

const distDir = path.resolve(import.meta.dir, "..", "dist");
const indexHtmlPath = path.join(distDir, "index.html");

function main() {
  const indexHtml = fs.readFileSync(indexHtmlPath, "utf8");

  // Legacy Intercom URLs (/en/articles/<id>-<slug>) still arrive from search
  // results and external links; serve the app there too so its redirect
  // routes can forward to the new scheme.
  const legacyRoutes = articles
    .filter((a) => a.slug.startsWith("en--articles--"))
    .map((a) => `en/articles/${a.slug.slice("en--articles--".length)}`);

  const routes = [
    ...articles.map((a) => `article/${a.slug}`),
    ...collections.map((c) => `collection/${c.path}`),
    ...legacyRoutes,
    "en",
  ];

  let plainFiles = 0;
  let indexFiles = 0;
  for (const route of routes) {
    const prefix = `${route}/`;
    const hasChildRoute = routes.some((r) => r.startsWith(prefix));
    const dest = hasChildRoute
      ? path.join(distDir, route, "index.html")
      : path.join(distDir, route);
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.writeFileSync(dest, indexHtml);
    if (hasChildRoute) indexFiles++;
    else plainFiles++;
  }

  // Copy for the S3 website error document (and CloudFront custom error
  // response) so unknown URLs load the app's styled 404 page instead of
  // returning raw S3 XML.
  fs.writeFileSync(path.join(distDir, "404.html"), indexHtml);

  console.log(
    `Route files: ${routes.length} routes (${plainFiles} plain, ${indexFiles} as index.html) + 404.html`,
  );
}

main();
