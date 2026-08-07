import { Link } from "wouter";
import { collections, articles } from "../content/manifest";
import { Search } from "../components/Search";
import { useDocumentTitle } from "../utils/document-title";
import "./HomePage.css";

export function HomePage() {
  useDocumentTitle();
  const rootCollections = collections.filter((c) => c.parentPath === null);

  return (
    <div className="home">
      <section className="hero">
        <div className="container hero-inner">
          <p className="hero-eyebrow">Telnyx Support Center</p>
          <h1 className="hero-title">
            How can we help?
            <span className="hero-cursor" aria-hidden="true" />
          </h1>
          <Search variant="hero" />
          <p className="hero-hint">
            {articles.length} articles on messaging, voice, numbers, and the
            Telnyx platform — or browse by topic below.
          </p>
        </div>
      </section>

      <section className="container home-topics" aria-label="Browse by topic">
        <h2 className="home-topics-heading eyebrow">Browse by topic</h2>
        <div className="topic-grid">
          {rootCollections.map((collection) => (
            <Link
              key={collection.path}
              to={`/collection/${collection.path}`}
              className="topic-card"
            >
              <h3 className="topic-card-title">{collection.title}</h3>
              {collection.description && (
                <p className="topic-card-description">
                  {collection.description}
                </p>
              )}
              <span className="topic-card-count">
                {collection.articleSlugs.length}{" "}
                {collection.articleSlugs.length === 1 ? "article" : "articles"}
                <span className="topic-card-arrow" aria-hidden="true">
                  →
                </span>
              </span>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
