import fs from "fs";
import path from "path";
import type { Article, Collection } from "../src/content/types";
import { cleanArticle } from "../src/utils/clean-article";

const supportDocsDir = path.resolve(import.meta.dir, "..", "..", "support-docs");
const treePath = path.join(supportDocsDir, "_tree.json");
const manifestPath = path.join(supportDocsDir, "_manifest.json");
const outPath = path.resolve(import.meta.dir, "..", "src", "content", "manifest.ts");
const publicDir = path.resolve(import.meta.dir, "..", "public");
const bootstrapDistDir = path.resolve(
  import.meta.dir,
  "..",
  "node_modules",
  "@telnyx-private",
  "bootstrap",
  "dist",
);

type TreeCollection = {
  path: string;
  source_file?: string;
  title?: string;
  source_url?: string;
  intercom_collection_id?: string;
  source_slug?: string;
  metadata_stub?: boolean;
};

type ManifestData = {
  files: string[];
};

function readJson<T>(p: string): T {
  return JSON.parse(fs.readFileSync(p, "utf8")) as T;
}

function parseFrontmatter(content: string): {
  fm: Record<string, string>;
  body: string;
} {
  if (!content.startsWith("---")) return { fm: {}, body: content };
  const lines = content.split("\n");
  if (lines[0].trim() !== "---") return { fm: {}, body: content };
  let i = 1;
  const fmLines: string[] = [];
  while (i < lines.length && lines[i].trim() !== "---") {
    fmLines.push(lines[i]);
    i++;
  }
  const fm: Record<string, string> = {};
  for (const line of fmLines) {
    const idx = line.indexOf(":");
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    const val = line.slice(idx + 1).trim();
    if (key) fm[key] = val;
  }
  const body = lines.slice(i + 1).join("\n");
  return { fm, body };
}

function firstH1(body: string): string | null {
  for (const line of body.split("\n")) {
    const m = line.match(/^#\s+(.+?)\s*$/);
    if (m) return m[1].trim();
  }
  return null;
}

function parentOf(p: string): string | null {
  const idx = p.lastIndexOf("/");
  return idx === -1 ? null : p.slice(0, idx);
}

const imagesSrcDir = path.join(supportDocsDir, "_images");
const imagesDestDir = path.join(publicDir, "_images");
const IMAGE_REF = /_images\/([A-Za-z0-9._-]+)/g;
const articleJsonDir = path.join(publicDir, "content", "articles");

// Article bodies are fetched on demand as JSON rather than bundled into the
// JS entry (all 898 bodies inlined made the bundle ~5 MB). The directory is
// rebuilt from scratch so removed articles don't leave stale files behind.
function writeArticleBodies(articles: Article[]) {
  fs.rmSync(articleJsonDir, { recursive: true, force: true });
  fs.mkdirSync(articleJsonDir, { recursive: true });
  for (const a of articles) {
    fs.writeFileSync(
      path.join(articleJsonDir, `${a.slug}.json`),
      JSON.stringify({ slug: a.slug, title: a.title, body: a.body }),
      "utf8",
    );
  }
  console.log(`Article bodies: ${articles.length} JSON files`);
}

// Article bodies reference screenshots as _images/<hash>.<ext>. Copy the
// referenced files into public/_images so they ship with the build. Filenames
// are content hashes, so existing destination files never need re-copying.
function copyArticleImages(referenced: Set<string>) {
  fs.mkdirSync(imagesDestDir, { recursive: true });
  let copied = 0;
  let missing = 0;
  for (const name of referenced) {
    const src = path.join(imagesSrcDir, name);
    const dest = path.join(imagesDestDir, name);
    if (fs.existsSync(dest)) continue;
    if (!fs.existsSync(src)) {
      missing++;
      continue;
    }
    fs.copyFileSync(src, dest);
    copied++;
  }
  console.log(
    `Article images: ${referenced.size} referenced, ${copied} copied, ${missing} missing`,
  );
}

// theme.css references its fonts at root-absolute URLs (e.g. /inter-latin-400-normal.woff2),
// so they must exist at the served root. Vite copies public/ there verbatim.
function copyThemeFonts() {
  const fonts = fs
    .readdirSync(bootstrapDistDir)
    .filter((f) => f.endsWith(".woff") || f.endsWith(".woff2"));
  fs.mkdirSync(publicDir, { recursive: true });
  let copied = 0;
  for (const font of fonts) {
    const dest = path.join(publicDir, font);
    if (!fs.existsSync(dest)) {
      fs.copyFileSync(path.join(bootstrapDistDir, font), dest);
      copied++;
    }
  }
  console.log(`Theme fonts: ${fonts.length} found, ${copied} copied`);
}

function main() {
  copyThemeFonts();
  const tree = fs.existsSync(treePath)
    ? readJson<{ collections: TreeCollection[] }>(treePath)
    : {
        collections: [
          {
            path: "support-articles",
            title: "Support Articles",
            source_url: "https://support.telnyx.com/",
          },
        ],
      };
  const manifestData = readJson<ManifestData>(manifestPath);

  const collections: Collection[] = tree.collections.map((c) => {
    const parentPath = parentOf(c.path);
    let title = c.title ?? null;
    if (!title) {
      try {
        const stubContent = fs.readFileSync(
          path.join(supportDocsDir, c.path, "_collection.md"),
          "utf8",
        );
        title = firstH1(parseFrontmatter(stubContent).body) ?? null;
      } catch {
        title = null;
      }
    }
    return {
      path: c.path,
      title: title ?? c.path,
      sourceUrl: c.source_url ?? null,
      sourceSlug: c.source_slug ?? null,
      intercomCollectionId: c.intercom_collection_id ?? null,
      metadataStub: Boolean(c.metadata_stub),
      parentPath,
      childCollectionPaths: [],
      articleSlugs: [],
    };
  });

  for (const c of collections) {
    c.childCollectionPaths = collections
      .filter((c2) => c2.parentPath === c.path)
      .map((c2) => c2.path);
  }

  const articles: Article[] = [];
  const referencedImages = new Set<string>();
  let skippedCollectionMd = 0;
  let skippedUncategorized = 0;
  let missingFile = 0;

  for (const relPath of manifestData.files) {
    const segments = relPath.split("/");
    if (path.basename(relPath) === "_collection.md") {
      skippedCollectionMd++;
      continue;
    }
    if (segments.includes("_uncategorized")) {
      skippedUncategorized++;
      continue;
    }
    if (relPath === "_tree.json" || relPath === "_manifest.json") continue;

    const absPath = path.join(supportDocsDir, relPath);
    let content: string;
    try {
      content = fs.readFileSync(absPath, "utf8");
    } catch {
      missingFile++;
      continue;
    }

    const { fm, body } = parseFrontmatter(content);
    const cleanedBody = cleanArticle(body);
    for (const m of cleanedBody.matchAll(IMAGE_REF)) {
      referencedImages.add(m[1]);
    }
    const slug = path.basename(relPath, ".md");
    const articleDir = path.dirname(relPath).split(path.sep).join("/");
    const collectionPath = articleDir === "." ? "support-articles" : articleDir;
    const title = firstH1(body) ?? slug;

    articles.push({
      slug,
      title,
      sourceUrl: fm.source_url ?? null,
      scraped: fm.scraped ?? null,
      collectionPath,
      body: cleanedBody,
    });

    const col = collections.find((c) => c.path === collectionPath);
    if (col) col.articleSlugs.push(slug);
  }

  copyArticleImages(referencedImages);
  writeArticleBodies(articles);

  const buildTimestamp = new Date().toISOString();
  const articlesPublic = articles.map((a) => ({
    slug: a.slug,
    title: a.title,
    sourceUrl: a.sourceUrl,
    scraped: a.scraped,
    collectionPath: a.collectionPath,
  }));

  const output =
    "/* eslint-disable */\n" +
    "// @generated by scripts/build-content.ts — do not edit manually\n" +
    'import type { Article, Collection } from "./types";\n\n' +
    `export const collections: Collection[] = ${JSON.stringify(collections)} as Collection[];\n\n` +
    `export const articles: Omit<Article, "body">[] = ${JSON.stringify(articlesPublic)} as Omit<Article, "body">[];\n\n` +
    "export const manifest = {\n" +
    "  collections,\n" +
    "  articles,\n" +
    `  buildTimestamp: ${JSON.stringify(buildTimestamp)},\n` +
    "};\n";

  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, output, "utf8");

  console.log(`Collections: ${collections.length}`);
  console.log(`Articles: ${articles.length}`);
  console.log(`Skipped _collection.md: ${skippedCollectionMd}`);
  console.log(`Skipped _uncategorized: ${skippedUncategorized}`);
  console.log(`Missing files on disk: ${missingFile}`);
  console.log(`Output: ${outPath}`);
}

main();
