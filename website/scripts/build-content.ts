import fs from "fs";
import path from "path";
import type { Article, Collection } from "../src/content/types";
import {
  cleanArticle,
  rewriteLegacyArticleLinks,
  stripFeedbackTrailer,
} from "../src/utils/clean-article";

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
  description?: string;
  source_url?: string;
  intercom_collection_id?: string;
  source_slug?: string;
  metadata_stub?: boolean;
};

type ManifestData = {
  files: string[];
};

// The scraped snapshot is flat (no _tree.json), so there is no collection
// hierarchy to render. These keyword buckets reconstruct a browsable topic
// structure mirroring the taxonomy of the original Intercom help center.
// First matching rule wins; unmatched articles land in "general". The rules
// only apply when _tree.json is absent — a restored tree takes precedence.
type FallbackTopic = {
  path: string;
  title: string;
  description: string;
  pattern: RegExp;
};

const FALLBACK_TOPICS: FallbackTopic[] = [
  {
    path: "messaging",
    title: "Messaging",
    description:
      "SMS and MMS, 10DLC and toll-free verification, WhatsApp, and country-specific messaging rules.",
    pattern:
      /\bsms\b|\bmms\b|messag|10 ?dlc|toll[- ]?free verification|whatsapp|short ?code|campaign|alphanumeric|sender id|\btext(s|ing)?\b/i,
  },
  {
    path: "voice-sip-trunking",
    title: "Voice & SIP Trunking",
    description:
      "SIP trunk configuration, softphone and PBX setup guides, TeXML, WebRTC, fax, and call troubleshooting.",
    pattern:
      /\bsip\b|trunk|voice|call|texml|webrtc|\bfax\b|dial|\bpbx\b|asterisk|freepbx|3cx|codec|\brtp\b|dtmf|\bivr\b|softphone|polycom|zoiper|audiocodes|acrobits|snom|grandstream|bria|yealink|sansay|\bsbc\b|\bn11\b|routing|termination|obihai|fanvil|cisco|linphone|zoho|vitalpbx/i,
  },
  {
    path: "numbers-porting",
    title: "Numbers & Porting",
    description:
      "Number search and management, porting in and out, E911, CNAM, caller ID, and international coverage.",
    pattern:
      /number|porting|\bport\b|port[- ](out|in)|fastport|e911|cnam|caller id|\bdid\b|\bdids\b|emergency|\blrn\b|coverage/i,
  },
  {
    path: "iot-wireless",
    title: "IoT & Wireless",
    description: "IoT SIM cards, eSIM, and global wireless connectivity.",
    pattern: /\biot\b|\bsim\b|wireless|esim/i,
  },
  {
    path: "networking-storage",
    title: "Networking & Storage",
    description:
      "Private networks, VPN, cloud storage buckets, and IP address management.",
    pattern: /storage|network|\bvpn\b|cloud|bucket|\bip\b|\bips\b/i,
  },
  {
    path: "account-billing",
    title: "Account, Billing & Portal",
    description:
      "Account setup and verification, billing and payments, API keys, teams, and portal management.",
    pattern:
      /account|billing|payment|invoice|portal|api key|\bteam\b|\bsso\b|2fa|refund|balance|pricing|rate sheet|verification/i,
  },
  {
    path: "ai-automation",
    title: "AI & Automation",
    description: "AI assistants, inference, and automation tools.",
    pattern: /\bai\b|assistant|inference|insight/i,
  },
];

const FALLBACK_GENERAL: Omit<FallbackTopic, "pattern"> = {
  path: "general",
  title: "General",
  description:
    "Getting started, debugging tools, policies, and everything else about working with Telnyx.",
};

function fallbackTopicFor(title: string, slug: string): string {
  const haystack = `${title} ${slug}`;
  for (const topic of FALLBACK_TOPICS) {
    if (topic.pattern.test(haystack)) return topic.path;
  }
  return FALLBACK_GENERAL.path;
}

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
    const val = line
      .slice(idx + 1)
      .trim()
      .replace(/^"(.*)"$/, "$1");
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
  const usingFallbackTopics = !fs.existsSync(treePath);
  const tree = usingFallbackTopics
    ? {
        collections: [...FALLBACK_TOPICS, FALLBACK_GENERAL].map((t) => ({
          path: t.path,
          title: t.title,
          description: t.description,
          source_url: "https://support.telnyx.com/en/",
        })),
      }
    : readJson<{ collections: TreeCollection[] }>(treePath);
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
      description: c.description ?? null,
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
    const cleanedBody = rewriteLegacyArticleLinks(
      stripFeedbackTrailer(cleanArticle(body)),
    );
    for (const m of cleanedBody.matchAll(IMAGE_REF)) {
      referencedImages.add(m[1]);
    }
    const slug = path.basename(relPath, ".md");
    const articleDir = path.dirname(relPath).split(path.sep).join("/");
    const title = firstH1(body) ?? slug;
    const collectionPath = usingFallbackTopics
      ? fallbackTopicFor(title, slug)
      : articleDir === "."
        ? FALLBACK_GENERAL.path
        : articleDir;

    articles.push({
      slug,
      title,
      description: fm.description ?? null,
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
    description: a.description,
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
  for (const c of collections) {
    console.log(`  ${c.path}: ${c.articleSlugs.length} articles`);
  }
  console.log(`Articles: ${articles.length}`);
  console.log(`Skipped _collection.md: ${skippedCollectionMd}`);
  console.log(`Skipped _uncategorized: ${skippedUncategorized}`);
  console.log(`Missing files on disk: ${missingFile}`);
  console.log(`Output: ${outPath}`);
}

main();
