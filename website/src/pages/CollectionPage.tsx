import { useState } from "react";
import { useParams, Link } from "wouter";
import { collections, articles } from "../content/manifest";
import type { Article, Collection } from "../content/types";
import { Breadcrumbs } from "../components/Breadcrumbs";
import { useDocumentTitle } from "../utils/document-title";
import "./CollectionPage.css";

function findCollection(path: string): Collection | undefined {
  return collections.find((collection) => collection.path === path);
}

type ArticleMeta = Omit<Article, "body">;

// wouter passes params raw, so a malformed percent-sequence in the URL
// (e.g. /collection/100%zz) would make decodeURIComponent throw mid-render.
function safeDecode(value: string): string {
  try {
    return decodeURIComponent(value);
  } catch {
    return value;
  }
}

export function CollectionPage() {
  const { rest } = useParams<{ rest?: string }>();
  const collectionPath = rest ? safeDecode(rest) : "";
  const collection = findCollection(collectionPath);
  const [filter, setFilter] = useState("");

  useDocumentTitle(collection?.title);

  if (!collection) {
    return (
      <div className="container collection-missing">
        <p className="eyebrow">Not found</p>
        <h1 className="collection-missing-title">Collection not found</h1>
        <p>
          <Link to="/">Browse all topics</Link>
        </p>
      </div>
    );
  }

  const childCollections = collection.childCollectionPaths
    .map((path) => findCollection(path))
    .filter((child): child is Collection => child !== undefined);

  const collectionArticles = collection.articleSlugs
    .map((slug) => articles.find((article) => article.slug === slug))
    .filter((article): article is ArticleMeta => article !== undefined);

  const q = filter.trim().toLowerCase();
  const visibleArticles =
    q.length === 0
      ? collectionArticles
      : collectionArticles.filter(
          (article) =>
            article.title.toLowerCase().includes(q) ||
            article.description?.toLowerCase().includes(q),
        );

  return (
    <div className="container collection">
      <header className="collection-header">
        <Breadcrumbs collectionPath={collectionPath} />
        <h1 className="collection-title">{collection.title}</h1>
        {collection.description && (
          <p className="collection-description">{collection.description}</p>
        )}
        <p className="collection-count eyebrow">
          {collectionArticles.length}{" "}
          {collectionArticles.length === 1 ? "article" : "articles"}
        </p>
      </header>

      {childCollections.length > 0 && (
        <section className="collection-children">
          <h2 className="collection-section-heading eyebrow">Collections</h2>
          <ul className="collection-children-list">
            {childCollections.map((child) => (
              <li key={child.path}>
                <Link to={`/collection/${child.path}`}>{child.title}</Link>
              </li>
            ))}
          </ul>
        </section>
      )}

      {collectionArticles.length > 0 && (
        <section aria-label="Articles in this collection">
          {collectionArticles.length > 10 && (
            <input
              type="search"
              className="collection-filter"
              placeholder={`Filter ${collectionArticles.length} articles…`}
              value={filter}
              onChange={(event) => setFilter(event.target.value)}
              aria-label="Filter articles in this collection"
            />
          )}
          {visibleArticles.length > 0 ? (
            <ul className="article-list">
              {visibleArticles.map((article) => (
                <li key={article.slug} className="article-list-item">
                  <Link
                    to={`/article/${article.slug}`}
                    className="article-list-link"
                  >
                    <span className="article-list-text">
                      <span className="article-list-title">
                        {article.title}
                      </span>
                      {article.description && (
                        <span className="article-list-description">
                          {article.description}
                        </span>
                      )}
                    </span>
                    <span className="article-list-arrow" aria-hidden="true">
                      →
                    </span>
                  </Link>
                </li>
              ))}
            </ul>
          ) : (
            <p className="collection-filter-empty">
              No articles match “{filter.trim()}”. Clear the filter or try the
              search above.
            </p>
          )}
        </section>
      )}
    </div>
  );
}
