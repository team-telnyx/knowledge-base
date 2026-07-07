import { useState } from "react";
import { Link } from "wouter";
import { articles } from "../content/manifest";
import "./Search.css";

export function Search() {
  const [query, setQuery] = useState("");

  const trimmed = query.trim();
  const results =
    trimmed.length === 0
      ? []
      : articles
          .filter((article) =>
            article.title.toLowerCase().includes(trimmed.toLowerCase())
          )
          .slice(0, 10);

  return (
    <div className="search">
      <input
        type="search"
        className="search-input"
        placeholder="Search articles..."
        value={query}
        onChange={(event) => setQuery(event.target.value)}
        aria-label="Search articles"
      />
      {results.length > 0 && (
        <ul className="search-dropdown" role="listbox">
          {results.map((article) => (
            <li key={article.slug} className="search-dropdown-item">
              <Link to={`/article/${article.slug}`} className="search-dropdown-link">
                {article.title}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
