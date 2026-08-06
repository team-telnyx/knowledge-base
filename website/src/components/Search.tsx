import { useEffect, useId, useMemo, useRef, useState } from "react";
import { useLocation } from "wouter";
import { articles } from "../content/manifest";
import "./Search.css";

const MAX_RESULTS = 8;

type Result = {
  slug: string;
  title: string;
  description: string | null;
};

function findResults(query: string): Result[] {
  const q = query.trim().toLowerCase();
  if (q.length === 0) return [];
  const titleMatches: Result[] = [];
  const descriptionMatches: Result[] = [];
  for (const article of articles) {
    if (article.title.toLowerCase().includes(q)) {
      titleMatches.push(article);
    } else if (article.description?.toLowerCase().includes(q)) {
      descriptionMatches.push(article);
    }
    if (titleMatches.length >= MAX_RESULTS) break;
  }
  return [...titleMatches, ...descriptionMatches].slice(0, MAX_RESULTS);
}

export function Search({
  variant = "header",
}: {
  variant?: "header" | "hero";
}) {
  const [query, setQuery] = useState("");
  const [open, setOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(-1);
  const rootRef = useRef<HTMLDivElement>(null);
  const listboxId = useId();
  const [, navigate] = useLocation();

  const results = useMemo(() => findResults(query), [query]);
  const showPanel = open && query.trim().length > 0;

  useEffect(() => {
    if (!showPanel) return;
    function onPointerDown(event: MouseEvent | TouchEvent) {
      if (!rootRef.current?.contains(event.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", onPointerDown);
    document.addEventListener("touchstart", onPointerDown);
    return () => {
      document.removeEventListener("mousedown", onPointerDown);
      document.removeEventListener("touchstart", onPointerDown);
    };
  }, [showPanel]);

  function goTo(slug: string) {
    setQuery("");
    setOpen(false);
    setActiveIndex(-1);
    navigate(`/article/${slug}`);
  }

  function onKeyDown(event: React.KeyboardEvent<HTMLInputElement>) {
    if (!showPanel || results.length === 0) {
      if (event.key === "Escape") {
        setOpen(false);
        event.currentTarget.blur();
      }
      return;
    }
    switch (event.key) {
      case "ArrowDown":
        event.preventDefault();
        setActiveIndex((i) => (i + 1) % results.length);
        break;
      case "ArrowUp":
        event.preventDefault();
        setActiveIndex((i) => (i <= 0 ? results.length - 1 : i - 1));
        break;
      case "Enter":
        if (activeIndex >= 0 && activeIndex < results.length) {
          event.preventDefault();
          goTo(results[activeIndex].slug);
        } else if (results.length > 0) {
          event.preventDefault();
          goTo(results[0].slug);
        }
        break;
      case "Escape":
        setOpen(false);
        setActiveIndex(-1);
        break;
    }
  }

  return (
    <div className={`search search--${variant}`} ref={rootRef}>
      <svg
        className="search-icon"
        viewBox="0 0 16 16"
        aria-hidden="true"
        focusable="false"
      >
        <circle cx="7" cy="7" r="4.6" fill="none" stroke="currentColor" strokeWidth="1.6" />
        <line x1="10.4" y1="10.4" x2="14" y2="14" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
      </svg>
      <input
        type="search"
        className="search-input"
        placeholder={
          variant === "hero"
            ? `Search ${articles.length} articles…`
            : "Search articles…"
        }
        value={query}
        onChange={(event) => {
          setQuery(event.target.value);
          setOpen(true);
          setActiveIndex(-1);
        }}
        onFocus={() => setOpen(true)}
        onKeyDown={onKeyDown}
        role="combobox"
        aria-label="Search articles"
        aria-expanded={showPanel}
        aria-controls={listboxId}
        aria-activedescendant={
          activeIndex >= 0 ? `${listboxId}-option-${activeIndex}` : undefined
        }
        aria-autocomplete="list"
        autoComplete="off"
      />
      {showPanel && (
        <div className="search-panel">
          {results.length > 0 ? (
            <ul className="search-results" role="listbox" id={listboxId}>
              {results.map((result, index) => (
                <li
                  key={result.slug}
                  id={`${listboxId}-option-${index}`}
                  role="option"
                  aria-selected={index === activeIndex}
                  className={
                    index === activeIndex
                      ? "search-result search-result--active"
                      : "search-result"
                  }
                  onMouseEnter={() => setActiveIndex(index)}
                  onMouseDown={(event) => {
                    event.preventDefault();
                    goTo(result.slug);
                  }}
                >
                  <span className="search-result-title">{result.title}</span>
                  {result.description && (
                    <span className="search-result-description">
                      {result.description}
                    </span>
                  )}
                </li>
              ))}
            </ul>
          ) : (
            <div className="search-empty" id={listboxId} role="listbox">
              <p className="search-empty-title">
                No articles match “{query.trim()}”
              </p>
              <p className="search-empty-hint">
                Try a different term, or{" "}
                <a
                  href="https://telnyx.com/contact-us"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  contact support
                </a>
                .
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
