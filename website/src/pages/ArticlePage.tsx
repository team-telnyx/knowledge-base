import { useEffect, useState } from "react";
import { useParams, Link } from "wouter";
import { articles } from "../content/manifest";
import { ArticleContent } from "../components/ArticleContent";
import { Breadcrumbs } from "../components/Breadcrumbs";

const rawBasePath = process.env.BASE_PATH || "/";
const basePath = rawBasePath.endsWith("/") ? rawBasePath : `${rawBasePath}/`;

const bodyCache = new Map<string, string>();

type BodyState = {
  slug: string;
  body: string | null;
  error: boolean;
};

export function ArticlePage() {
  const { slug } = useParams<{ slug: string }>();

  const article = slug ? articles.find((a) => a.slug === slug) : undefined;
  const [state, setState] = useState<BodyState | null>(null);

  useEffect(() => {
    if (!slug || !article) return;
    const cached = bodyCache.get(slug);
    if (cached !== undefined) {
      setState({ slug, body: cached, error: false });
      return;
    }
    let cancelled = false;
    fetch(`${basePath}content/articles/${slug}.json`)
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
      <div>
        <p>Article not found</p>
        <Link to="/">Back to home</Link>
      </div>
    );
  }

  const current = state?.slug === slug ? state : null;

  return (
    <div>
      <Breadcrumbs collectionPath={article.collectionPath} />
      <h1>{article.title}</h1>
      {article.sourceUrl ? (
        <a href={article.sourceUrl} target="_blank" rel="noopener noreferrer">
          View original
        </a>
      ) : null}
      {current === null ? (
        <p>Loading…</p>
      ) : current.error || current.body === null ? (
        <p>Failed to load this article. Please try again.</p>
      ) : (
        <ArticleContent body={current.body} />
      )}
    </div>
  );
}
