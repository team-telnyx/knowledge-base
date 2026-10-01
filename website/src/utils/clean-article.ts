const SKIP_LINK = "[Skip to main content](#main-content)";
const SUPPORT_LINK =
  /https?:\/\/support\.telnyx\.com(\/en\/(?:articles|collections)\/[A-Za-z0-9][A-Za-z0-9-]*)/g;

// Scraped bodies cross-reference same-host support pages through absolute URLs.
// Rewriting only their hostname-qualified path keeps navigation client-side and
// leaves query strings and fragments untouched.
export function rewriteLegacyArticleLinks(body: string): string {
  // Relative paths are not Markdown autolinks. Convert angle-bracket links
  // before removing the hostname, including any already damaged imports.
  return body.replace(/<((?:https?:\/\/(?:support\.telnyx\.com|intercom\.help\/telnyx))?\/en\/(?:articles|collections)\/[^<>\s]+)>/g,
    (_, url: string) => `[${url}](${url})`).replace(SUPPORT_LINK, "$1");
}

const FEEDBACK_PROMPT = "Did this answer your question?";
const EMOJI_REACTIONS = /^[\s😞😐😃]+$/u;
// A scraped link label can contain bracketed text, such as "[BETA]".
const LINK_ONLY_LINE = /^\s*(\[(?:[^\[\]]|\[[^\[\]]*\])*\]\([^)]*\)\s*)+$/;

// Every scraped body ends with Intercom's feedback widget ("Did this answer
// your question?" + emoji reactions), usually preceded by a plain-text
// "Related Articles" trailer — the site renders its own related-articles
// section, so both are noise. The trailer is only removed when the heading
// is actually found; link lines elsewhere are untouched.
export function stripFeedbackTrailer(body: string): string {
  const lines = body.split("\n");
  const skipBlanks = (i: number): number => {
    while (i > 0 && lines[i - 1].trim() === "") i--;
    return i;
  };

  let end = skipBlanks(lines.length);
  while (end > 0 && EMOJI_REACTIONS.test(lines[end - 1])) {
    end = skipBlanks(end - 1);
  }
  if (end === 0 || lines[end - 1].trim() !== FEEDBACK_PROMPT) {
    return body;
  }
  end = skipBlanks(end - 1);

  let cursor = end;
  while (cursor > 0 && LINK_ONLY_LINE.test(lines[cursor - 1])) {
    cursor = skipBlanks(cursor - 1);
  }
  if (cursor > 0 && lines[cursor - 1].trim() === "Related Articles") {
    cursor = skipBlanks(cursor - 1);
    if (cursor > 0 && lines[cursor - 1].trim() === "---") {
      cursor = skipBlanks(cursor - 1);
    }
    end = cursor;
  }

  return lines.slice(0, end).join("\n").trimEnd();
}
const TOC_HEADER = "Table of contents";
const TITLE_BAR_SUFFIX = "| Telnyx Help Center";
const BYLINE_PREFIX = "Written by ";
const NAV_ICON_IMAGE =
  /^!\[[^\]]*\]\([^)]*intercom\.help[^)]*\/assets\/svg\/icon:[^)]*\)$/;
export function cleanArticle(raw: string): string {
  const kept: string[] = [];
  let strippedH1 = false;
  let fence: string | null = null;
  let reachedSection = false;
  for (const line of raw.split("\n")) {
    const t = line.trim();
    const marker = t.match(/^(`{3,}|~{3,})/)?.[0];
    if (marker) {
      if (!fence) fence = marker;
      else if (marker[0] === fence[0] && marker.length >= fence.length) fence = null;
      kept.push(line); continue;
    }
    if (fence) { kept.push(line); continue; }
    if (/^#{2,6} /.test(t)) reachedSection = true;
    if (!reachedSection && /^[A-Z]$/.test(t)) continue;
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
    if (/^Updated (?:over |about )?(?:\d+ |a |an )?(?:seconds?|minutes?|hours?|days?|weeks?|months?|years?) ago[. ]*$/.test(t)) continue;
    // Zero-width-space-only lines left behind by the scraper.
    if (/^[​﻿]+$/.test(t)) continue;
    if (!strippedH1 && t.startsWith("# ")) {
      strippedH1 = true;
      continue;
    }
    kept.push(t.startsWith("# ") ? line.replace("# ", "## ") : line);
  }
  return kept.join("\n").trim();
}
