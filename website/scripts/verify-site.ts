import fs from "node:fs";
import {findSearchResults, type SearchEntry} from "../src/utils/search";
import path from "node:path";
import {createHash} from "node:crypto";
import {gzipSync} from "node:zlib";
import {articles, collections} from "../src/content/manifest";
import {collectionArticleCounts} from "../src/utils/collection-articles";
const decode=(s:string)=>s.replace(/&quot;/g,'"').replace(/&lt;/g,"<").replace(/&gt;/g,">").replace(/&amp;/g,"&");
const origin = new URL(process.env.SITE_ORIGIN || "https://d27az1l5lty0u1.cloudfront.net").origin;
const indexable = process.env.SITE_INDEXABLE === "true";
const dist=path.resolve(import.meta.dir,"../dist");
const routes=["/",...articles.map(a=>"/en/articles/"+a.slug),...collections.map(c=>"/en/collections/"+c.path)];
const pages=new Map<string,{ids:Set<string>;text:string}>();
const links:{from:string;href:string}[]=[], failures:string[]=[], knownEditorialLinks:{from:string;href:string}[]=[];
const pendingIds=new Set<string>();
for(const route of routes){
 const expectedRobots=articles.find(a=>route===`/en/articles/${a.slug}`)?.robots ?? (indexable ? "index,follow" : "noindex,follow");
 const html=fs.readFileSync(path.join(dist,route==="/"?"index.html":route.slice(1)),"utf8");
 const ids=new Set<string>();let h1=0,canonical=0,description=0,robots=0,bodyText="";
 const parser=new HTMLRewriter()
 .on("[id]",{element(e){const id=e.getAttribute("id")!;if(ids.has(id))failures.push(`Duplicate ID ${route}#${id}`);ids.add(id);}})
 .on("h1",{element(){h1++;}})
 .on('link[rel="canonical"]',{element(e){canonical++;if(e.getAttribute("href")!==`${origin}${route}`)failures.push(`Wrong canonical ${route}`);}})
 .on('meta[name="description"]',{element(e){description++;const n=decode(e.getAttribute("content")??"").length;if(n<100||n>160)failures.push(`Description length ${n}: ${route}`);}})
 .on('meta[name="robots"]',{element(e){robots++;if(e.getAttribute("content")!==expectedRobots)failures.push(`Wrong robots directive ${route}`);}})
 .on('a[href]',{element(e){const href=e.getAttribute("href")!;if(href.startsWith("/")||href.startsWith("#"))links.push({from:route,href});if(/^https?:\/\/support\.telnyx\.com/.test(href))failures.push(`Old hostname link ${route}: ${href}`);}})
 .on('img[src]',{element(e){const src=e.getAttribute("src")!;if(src.startsWith("/")&&!fs.existsSync(path.join(dist,src.slice(1))))failures.push(`Missing image ${src}`);if(!e.getAttribute("width")||!e.getAttribute("height"))failures.push(`Image dimensions missing ${route}: ${src}`);}})
 .on('.article-content',{text(chunk){bodyText+=chunk.text;}});
 await parser.transform(new Response(html)).text();
 if(h1!==1||canonical!==1||description!==1||robots!==1)failures.push(`Invalid initial metadata/H1: ${route}`);
 if(route.startsWith("/en/articles/")&&bodyText.trim().length<20)failures.push(`Missing initial article body: ${route}`);
 if(/<\/en\/(?:articles|collections)\//.test(decode(bodyText)))failures.push(`Malformed support autolink: ${route}`);
 pages.set(route,{ids,text:html.replace(/<[^>]*>/g," ")});
}
const searchIndex = JSON.parse(fs.readFileSync(path.join(dist,"content/search-index.json"),"utf8")) as SearchEntry[];
if(searchIndex.length !== articles.length || new Set(searchIndex.map(a=>a.slug)).size !== articles.length)failures.push("Search index coverage mismatch");
for(const article of articles){
 const entry=searchIndex.find(e=>e.slug===article.slug);
 if(!entry?.terms || entry.title!==article.title)failures.push(`Missing full-text search entry: ${article.slug}`);
}
if(!findSearchResults(searchIndex,"gambling")[0]?.slug.startsWith("14286763-"))failures.push("Gambling search no longer prioritizes forbidden messaging use cases");
const downloadManifest=JSON.parse(fs.readFileSync(path.resolve(import.meta.dir,"../downloads-manifest.json"),"utf8")) as {files:{path:string;sha256:string;size:number}[]};
for(const file of downloadManifest.files){
 const target=path.join(dist,file.path.slice(1));
 if(!fs.existsSync(target)){failures.push(`Missing archived download ${file.path}`);continue;}
 const data=fs.readFileSync(target);
 if(data.length!==file.size||createHash("sha256").update(data).digest("hex")!==file.sha256)failures.push(`Corrupted archived download ${file.path}`);
}
for(const {from,href} of links){
 const target=new URL(href,"https://preview.invalid"+from), dest=pages.get(target.pathname);
 if(target.pathname.startsWith("/downloads/")&&!fs.existsSync(path.join(dist,target.pathname.slice(1))))failures.push(`Missing download ${from} -> ${href}`);
 if(!dest){
  if(target.pathname.startsWith("/en/")){
   const id=target.pathname.match(/\/articles\/(\d+)/)?.[1];
   if(id&&pendingIds.has(id))knownEditorialLinks.push({from,href});else failures.push(`Missing route ${from} -> ${href}`);
  }
  continue;
 }
 const fragment=decodeURIComponent(target.hash.slice(1));
 if(fragment.startsWith(":~:text=")){
  const text=fragment.slice(8);if(!dest.text.includes(text))failures.push(`Missing text fragment ${href}`);
 }else if(fragment&&!dest.ids.has(fragment))failures.push(`Missing anchor ${from} -> ${href}`);
}
const counts=collectionArticleCounts(collections,articles);
for(const c of collections)if(!counts.get(c.path))failures.push(`Empty collection ${c.path}`);
const scripts=fs.readdirSync(path.join(dist,"assets")).filter(n=>n.endsWith(".js"));
const jsBytes=scripts.reduce((sum,name)=>sum+fs.statSync(path.join(dist,"assets",name)).size,0);
const jsGzipBytes=scripts.reduce((sum,name)=>sum+gzipSync(fs.readFileSync(path.join(dist,"assets",name))).length,0);
if(jsBytes>30000)failures.push(`Client JS exceeds 30 KB budget: ${jsBytes}`);
const xml=fs.readFileSync(path.join(dist,"sitemap.xml"),"utf8");
if((xml.match(/<loc>/g)??[]).length!==routes.length-articles.filter(a=>a.robots?.includes("noindex")).length)failures.push("Sitemap coverage does not match indexable pages");
for(const a of articles){const included=xml.includes(`<loc>${origin}/en/articles/${a.slug}</loc>`);if(included===Boolean(a.robots?.includes("noindex")))failures.push(`Wrong sitemap inclusion ${a.slug}`);}
if(process.env.REQUIRE_CLEAN_LINKS === "true" && knownEditorialLinks.length) failures.push(`${knownEditorialLinks.length} retired-content links still need verified replacements`);
// Verify .md files were generated for every article.
for(const a of articles){const mdPath=path.join(dist,"en","articles",a.slug+".md");if(!fs.existsSync(mdPath))failures.push(`Missing .md file: /en/articles/${a.slug}.md`);}
const summary={pages:routes.length,articles:articles.length,collections:collections.length,links:links.length,emptyCollections:collections.filter(c=>!counts.get(c.path)).length,jsBytes,jsGzipBytes,knownEditorialLinks,failures};
fs.writeFileSync(path.resolve(dist, process.env.REQUIRE_CLEAN_LINKS === "true" ? "../dist-edge/verification-strict.json" : "../dist-edge/verification.json"),JSON.stringify(summary,null,2));
console.log(JSON.stringify(summary,null,2));
if(failures.length)process.exit(1);
