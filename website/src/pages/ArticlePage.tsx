import { useParams, Link } from "wouter";
import { articles, articlesBySlug } from "../content/manifest";
import { ArticleContent } from "../components/ArticleContent";
import { Breadcrumbs } from "../components/Breadcrumbs";

export function ArticlePage() {
  const { slug } = useParams<{ slug: string }>();

  const article = slug ? articles.find((a) => a.slug === slug) : undefined;
  const body = slug ? articlesBySlug[slug] : undefined;

  if (!article || typeof body !== "string") {
    return (
      <div>
        <p>Article not found</p>
        <Link to="/">Back to home</Link>
      </div>
    );
  }

  return (
    <div>
      <Breadcrumbs collectionPath={article.collectionPath} />
      <h1>{article.title}</h1>
      {article.sourceUrl ? (
        <a href={article.sourceUrl} target="_blank" rel="noopener noreferrer">
          View original
        </a>
      ) : null}
      <ArticleContent body={body} />
    </div>
  );
}
