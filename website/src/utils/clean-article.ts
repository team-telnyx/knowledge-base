const SKIP_LINK = "[Skip to main content](#main-content)";
const LEGACY_ARTICLE_LINK =
  /https?:\/\/support\.telnyx\.com\/en\/articles\/([A-Za-z0-9][A-Za-z0-9-]*)/g;

// Scraped bodies cross-reference other articles through the legacy Intercom
// URL scheme (https://support.telnyx.com/en/articles/<id>-<slug>). This site
// deploys to that same domain but serves articles at /article/en--articles--
// <id>-<slug>, so rewrite the links to the new scheme (anchors survive: the
// match stops before any #fragment).
export function rewriteLegacyArticleLinks(body: string): string {
  return body.replace(LEGACY_ARTICLE_LINK, "/article/en--articles--$1");
}
const TOC_HEADER = "Table of contents";
const TITLE_BAR_SUFFIX = "| Telnyx Help Center";
const BYLINE_PREFIX = "Written by ";
const NAV_ICON_IMAGE =
  /^!\[[^\]]*\]\([^)]*intercom\.help[^)]*\/assets\/svg\/icon:[^)]*\)$/;
// The scrape dropped Intercom's heading ids, so links to #h_… fragments
// ("Jump to…", "Back to Top", inline tables of contents) have no target.
const DEAD_ANCHOR_LINK = /\[([^\]]*)\]\(#h_[^)]*\)/g;

// True for lines that are nothing but dead anchor links (optionally as a
// list item) — navigation scaffolding worth dropping wholesale.
function isDeadAnchorNavLine(trimmed: string): boolean {
  if (!trimmed.includes("](#h_")) return false;
  const remainder = trimmed
    .replace(DEAD_ANCHOR_LINK, "")
    .replace(/^([-*+]|\d+[.)])\s*/, "")
    .trim();
  return remainder === "";
}

export function cleanArticle(raw: string): string {
  const kept: string[] = [];
  let strippedH1 = false;
  for (const line of raw.split("\n")) {
    const t = line.trim();
    if (t === SKIP_LINK) continue;
    if (t === TOC_HEADER) continue;
    if (t.endsWith(TITLE_BAR_SUFFIX)) continue;
    if (
      t.startsWith(BYLINE_PREFIX) &&
      t.length <= 80 &&
      /^[A-Z]/.test(t.slice(BYLINE_PREFIX.length))
    )
      continue;
    if (NAV_ICON_IMAGE.test(t)) continue;
    if (isDeadAnchorNavLine(t)) continue;
    if (!strippedH1 && t.startsWith("# ")) {
      strippedH1 = true;
      continue;
    }
    // Inline dead anchors unwrap to their text so the sentence still reads.
    kept.push(line.replace(DEAD_ANCHOR_LINK, "$1"));
  }
  return kept.join("\n").trim();
}
