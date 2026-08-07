import { useEffect, useState } from "react";
import { useParams, Link } from "wouter";
import { articles, collections } from "../content/manifest";
import { ArticleContent } from "../components/ArticleContent";
import { Breadcrumbs } from "../components/Breadcrumbs";
import { useDocumentTitle } from "../utils/document-title";
import { assetBase } from "../utils/base-path";
import "./ArticlePage.css";

const bodyCache = new Map<string, string>();

type BodyState = {
  slug: string;
  body: string | null;
  error: boolean;
};

function formatDate(iso: string): string | null {
  const date = new Date(`${iso}T00:00:00Z`);
  if (Number.isNaN(date.getTime())) return null;
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
    timeZone: "UTC",
  });
}

function relatedArticles(slug: string, collectionPath: string, count: number) {
  const collection = collections.find((c) => c.path === collectionPath);
  if (!collection) return [];
  const siblings = collection.articleSlugs.filter((s) => s !== slug);
  const index = collection.articleSlugs.indexOf(slug);
  // Take neighbors around the article's position so the picks are stable.
  const start = Math.max(0, Math.min(index, siblings.length - count));
  return siblings
    .slice(start, start + count)
    .map((s) => articles.find((a) => a.slug === s))
    .filter((a): a is (typeof articles)[number] => a !== undefined);
}

export function ArticlePage() {
  const { slug } = useParams<{ slug: string }>();

  const article = slug ? articles.find((a) => a.slug === slug) : undefined;
  const [state, setState] = useState<BodyState | null>(null);

  useDocumentTitle(article?.title);

  useEffect(() => {
    if (!slug || !article) return;
    const cached = bodyCache.get(slug);
    if (cached !== undefined) {
      setState({ slug, body: cached, error: false });
      return;
    }
    let cancelled = false;
    fetch(`${assetBase}content/articles/${slug}.json`)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json() as Promise<{ body: string }>;
      })
      .then((data) => {
        bodyCache.set(slug, data.body);
        if (!cancelled) setState({ slug, body: data.body, error: false });
      })
      .catch(() => {
        if (!cancelled) setState({ slug, body: null, error: true });
      });
    return () => {
      cancelled = true;
    };
  }, [slug, article]);

  if (!slug || !article) {
    return (
      <div className="container article-missing">
        <p className="eyebrow">Not found</p>
        <h1 className="article-missing-title">Article not found</h1>
        <p>
          <Link to="/">Browse all topics</Link>
        </p>
      </div>
    );
  }

  const current = state?.slug === slug ? state : null;
  const scrapedDate = article.scraped ? formatDate(article.scraped) : null;
  const related = relatedArticles(slug, article.collectionPath, 4);

  return (
    <div className="container article">
      <header className="article-header">
        <Breadcrumbs collectionPath={article.collectionPath} />
        <h1 className="article-title">{article.title}</h1>
        <p className="article-meta">
          {scrapedDate && (
            <span className="article-meta-item">As of {scrapedDate}</span>
          )}
          {article.sourceUrl && (
            <a
              className="article-meta-item article-meta-source"
              href={article.sourceUrl}
              target="_blank"
              rel="noopener noreferrer"
            >
              View original ↗
            </a>
          )}
        </p>
      </header>

      <div className="article-card">
        {current === null ? (
          <p className="article-status" role="status">
            Loading article…
          </p>
        ) : current.error || current.body === null ? (
          <p className="article-status">
            This article failed to load. Refresh the page to try again.
          </p>
        ) : (
          <ArticleContent body={current.body} />
        )}
      </div>

      {related.length > 0 && (
        <section className="article-related" aria-label="Related articles">
          <h2 className="article-related-heading eyebrow">Related articles</h2>
          <div className="article-related-grid">
            {related.map((a) => (
              <Link
                key={a.slug}
                to={`/article/${a.slug}`}
                className="article-related-card"
              >
                <span className="article-related-title">{a.title}</span>
                {a.description && (
                  <span className="article-related-description">
                    {a.description}
                  </span>
                )}
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
