import { useParams, Link } from "wouter";
import { collections, articles } from "../content/manifest";
import type { Article, Collection } from "../content/types";
import { Breadcrumbs } from "../components/Breadcrumbs";

function findCollection(path: string): Collection | undefined {
  return collections.find((collection) => collection.path === path);
}

export function CollectionPage() {
  const { rest } = useParams<{ rest?: string }>();
  const collectionPath = rest ? decodeURIComponent(rest) : "";
  const collection = findCollection(collectionPath);

  if (!collection) {
    return (
      <div className="collection-page collection-page-not-found">
        <h1>Collection not found</h1>
        <p>
          <Link to="/">Back to home</Link>
        </p>
      </div>
    );
  }

  const childCollections = collection.childCollectionPaths
    .map((path) => findCollection(path))
    .filter((child): child is Collection => child !== undefined);

  const collectionArticles = collection.articleSlugs
    .map((slug) => articles.find((article) => article.slug === slug))
    .filter((article): article is Omit<Article, "body"> => article !== undefined);

  return (
    <div className="collection-page">
      <Breadcrumbs collectionPath={collectionPath} />
      <h1>{collection.title}</h1>
      {collection.sourceUrl && (
        <p className="collection-page-source">
          <a href={collection.sourceUrl} target="_blank" rel="noopener noreferrer">
            View on Telnyx Support
          </a>
        </p>
      )}

      {childCollections.length > 0 && (
        <section className="collection-page-section collection-page-child-collections">
          <h2>Collections</h2>
          <ul>
            {childCollections.map((child) => (
              <li key={child.path}>
                <Link to={`/collection/${child.path}`}>{child.title}</Link>
              </li>
            ))}
          </ul>
        </section>
      )}

      {collectionArticles.length > 0 && (
        <section className="collection-page-section collection-page-articles">
          <h2>Articles</h2>
          <ul>
            {collectionArticles.map((article) => (
              <li key={article.slug}>
                <Link to={`/article/${article.slug}`}>{article.title}</Link>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
