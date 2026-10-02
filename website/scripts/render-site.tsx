import fs from "node:fs";
import {normalizeSearch, type SearchEntry} from "../src/utils/search";
import { parse, parseFragment, serializeOuter, type DefaultTreeAdapterMap } from "parse5";
import path from "node:path";
import { renderToString } from "react-dom/server";
import { Router } from "wouter";
import { AppRoutes } from "../src/App";
import { DefaultLayout } from "../src/layouts/DefaultLayout";
import { articles, collections } from "../src/content/manifest";
import { routeRegistry } from "./content/routes";
const esc = (s: string) => s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
const json = (v: unknown) => JSON.stringify(v).replace(/</g,"\\u003c");
type HtmlNode = DefaultTreeAdapterMap["node"];
function textOf(node: HtmlNode): string {
  if ("tagName" in node && ["script", "style"].includes(node.tagName)) return "";
  if ("value" in node) return node.value;
  return "childNodes" in node ? node.childNodes.map(textOf).join("") : "";
}
const plain = (s: string) => textOf(parseFragment(s.replace(/!\[[^\]]*\]\([^)]*\)/g, "").replace(/\[([^\]]+)\]\([^)]*\)/g, "$1"))).replace(/[*_`#]/g, "").replace(/\s+/g, " ").trim();
function compiledAssetTags(html: string): string {
  const tags: string[] = [];
  function visit(node: HtmlNode) {
    if ("tagName" in node) {
      const attrs = new Map(node.attrs.map(a => [a.name, a.value]));
      if (node.tagName === "link" && attrs.get("rel") === "stylesheet" || node.tagName === "script" && attrs.get("type") === "module" && attrs.has("src")) tags.push(serializeOuter(node));
    }
    if ("childNodes" in node) node.childNodes.forEach(visit);
  }
  visit(parse(html));
  return tags.join("\n");
}
export function descriptionFor(description: string | null, body = "") {
  const candidate = description?.trim() || body.split(/\n\s*\n/).find(p => !/^\s*(?:#|[-|>]|```|!\[)/.test(p) && plain(p).length >= 50) || "Read Telnyx support guides, setup instructions, and troubleshooting advice for your connectivity services.";
  const text = plain(candidate);
  return text.length <= 160 ? text : text.slice(0,157).replace(/\s+\S*$/,"") + "…";
}
export function renderSite(dist: string) {
  const origin = new URL(process.env.SITE_ORIGIN || "https://d27az1l5lty0u1.cloudfront.net");
  if (origin.pathname !== "/" || origin.search || origin.hash || origin.username || origin.password || origin.protocol !== "https:") throw new Error("SITE_ORIGIN must be an HTTPS origin");
  const indexable = process.env.SITE_INDEXABLE === "true";
  if (indexable && origin.hostname !== "support.telnyx.com") throw new Error("Only the approved production origin may be indexable");
  const base = origin.origin;
  const shell = fs.readFileSync(path.join(dist,"index.html"),"utf8");
  const assetTags = compiledAssetTags(shell);
  if (!assetTags.includes("script")) throw new Error("Missing compiled enhancement script");
  const byCollection = new Map(collections.map(c => [c.path,c]));
  function trail(collectionPath?: string) {
    const result: {name: string; item: string}[] = [], seen = new Set<string>();
    let c = collectionPath ? byCollection.get(collectionPath) : undefined;
    while (c && !seen.has(c.path)) {
      seen.add(c.path); result.unshift({name:c.title,item:base+"/en/collections/"+c.path});
      c = c.parentPath ? byCollection.get(c.parentPath) : undefined;
    }
    return [{name:"Home",item:base+"/"},...result];
  }
  function page(route: string, title: string, description: string, body?: string, structured?: unknown, missing = false, robots?: "noindex,nofollow") {
    const content = renderToString(<Router ssrPath={route}><DefaultLayout><AppRoutes articleBody={body}/></DefaultLayout></Router>);
    if ((content.match(/<h1(?:\s|>)/g) ?? []).length !== 1) throw new Error(`Expected exactly one H1: ${route}`);
    const canonical = base+route;
    const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${esc(title)} | Telnyx Help Center</title><meta name="description" content="${esc(description)}"><meta name="robots" content="${robots ?? (indexable&&!missing?"index,follow":"noindex,follow")}">${missing?"":`<link rel="canonical" href="${esc(canonical)}">`}<meta property="og:title" content="${esc(title)} | Telnyx Help Center"><meta property="og:description" content="${esc(description)}"><meta property="og:url" content="${esc(canonical)}"><meta property="og:type" content="${body!==undefined?"article":"website"}"><meta property="og:site_name" content="Telnyx Help Center"><link rel="icon" href="/assets/favicon-black.ico" type="image/x-icon">${structured?`<script type="application/ld+json">${json(structured)}</script>`:""}${assetTags}</head><body><div id="root">${content}</div></body></html>`;
    const dest = path.join(dist,route==="/"?"index.html":route.slice(1));
    fs.mkdirSync(path.dirname(dest),{recursive:true}); fs.writeFileSync(dest,html);
  }
  page("/","Telnyx Support","Guides, troubleshooting, and answers for Telnyx messaging, voice, SIP trunking, phone numbers, IoT, AI assistants, and email.");
  const sitemap: {route: string; lastmod?: string}[] = [{route:"/"}];
  for (const c of collections) {
    const route = "/en/collections/"+c.path;
    page(route,c.title,descriptionFor(c.description),undefined,{"@context":"https://schema.org","@type":"BreadcrumbList",itemListElement:trail(c.path).map((b,i)=>({"@type":"ListItem",position:i+1,...b}))});
    sitemap.push({route});
  }
  const searchIndex: SearchEntry[] = [];
  for (const a of articles) {
    const route = "/en/articles/"+a.slug;
    const body = JSON.parse(fs.readFileSync(path.join(dist,"content/articles/"+a.slug+".json"),"utf8")).body as string;
    const description = descriptionFor(a.description,body);
    const breadcrumbs = [...trail(a.collectionPath),{name:a.title,item:base+route}];
    const modified = a.modifiedAt && !Number.isNaN(Date.parse(a.modifiedAt)) ? new Date(a.modifiedAt).toISOString() : undefined;
    page(route,a.seoTitle||a.title,description,body,{"@context":"https://schema.org","@graph":[
      {"@type":"Article",headline:a.title,description,url:base+route,mainEntityOfPage:base+route,...(modified?{dateModified:modified}:{}),publisher:{"@type":"Organization",name:"Telnyx"}},
      {"@type":"BreadcrumbList",itemListElement:breadcrumbs.map((b,i)=>({"@type":"ListItem",position:i+1,...b}))}
    ]},false,a.robots);
    // Also write a .md file so /en/articles/<slug>.md serves raw markdown.
    const mdDest = path.join(dist, route.slice(1) + ".md");
    fs.writeFileSync(mdDest, body);
    // Index the rendered article only, excluding navigation and related articles.
    const html = parse(fs.readFileSync(path.join(dist, route.slice(1)), "utf8"));
    let content = "", headings: string[] = [];
    function collect(node: HtmlNode, inArticle = false) {
      if ("tagName" in node) {
        inArticle ||= node.attrs.some(attr => attr.name === "class" && attr.value.split(/\s+/).includes("article-content"));
        if (["script", "style"].includes(node.tagName)) return;
        if (inArticle && /^h[1-6]$/.test(node.tagName)) headings.push(textOf(node));
      }
      if (inArticle && "value" in node) content += node.value + " ";
      if ("childNodes" in node) node.childNodes.forEach(child => collect(child, inArticle));
    }
    collect(html);
    searchIndex.push({slug:a.slug,title:a.title,description:a.description,headings:headings.join(" "),
      terms:[...new Set(normalizeSearch(content).split(/\s+/))].join(" ")});
    if (!a.robots?.includes("noindex")) sitemap.push({route,lastmod:modified});
  }
  page("/404.html","Page not found","This page could not be found. Browse Telnyx support topics from the homepage.",undefined,undefined,true);
  fs.mkdirSync(path.join(dist,"en"),{recursive:true});
  fs.writeFileSync(path.join(dist,"en/index.html"),'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=/"><title>Telnyx Support</title></head><body><a href="/">Continue to Telnyx Support</a></body></html>');
  fs.writeFileSync(path.join(dist,"sitemap.xml"),'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+sitemap.map(s=>`<url><loc>${esc(base+s.route)}</loc>${s.lastmod?`<lastmod>${s.lastmod}</lastmod>`:""}</url>`).join("")+'</urlset>');
  // Let crawlers see the preview's noindex directives.
  fs.writeFileSync(path.join(dist,"robots.txt"),`User-agent: *\nAllow: /\nSitemap: ${base}/sitemap.xml\n`);
  fs.writeFileSync(path.join(dist,"content/search-index.json"),JSON.stringify(searchIndex));
  fs.writeFileSync(path.join(dist,"llms.txt"), "# Telnyx Help Center\n\n" + articles.map(a => `- [${a.title}](${base}/en/articles/${a.slug}): ${descriptionFor(a.description)}`).join("\n") + "\n");
  const edgeDir = path.resolve(dist,"../dist-edge"); fs.mkdirSync(edgeDir,{recursive:true});
  const registry = routeRegistry(articles,collections);
  fs.writeFileSync(path.join(edgeDir,"routes.json"),JSON.stringify(registry,null,2));
  fs.writeFileSync(path.join(edgeDir,"key-value-store.json"),JSON.stringify({data:Object.entries(registry).map(([key,value])=>({key,value}))}));
  const handler = fs.readFileSync(path.resolve(import.meta.dir,"../edge/routing.js"),"utf8");
  const bundled = `import cf from 'cloudfront';\nconst store = cf.kvs();\n${handler}\nasync function handler(event) { return routeRequest(event.request, async function(key) { return await store.exists(key) ? await store.get(key) : undefined; }); }\n`;
  if (Buffer.byteLength(bundled)>10000) throw new Error("CloudFront Function exceeds code limit");
  fs.writeFileSync(path.join(edgeDir,"cloudfront-function.js"),bundled);
  console.log(`Prerendered ${sitemap.length} pages; ${Object.keys(registry).length} routing keys; origin ${base}; indexable ${indexable}`);
}
