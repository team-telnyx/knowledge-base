import { Link } from "wouter";
import { collections } from "../content/manifest";
import type { Collection } from "../content/types";
import "./Breadcrumbs.css";

function findCollection(path: string): Collection | undefined {
  return collections.find((collection) => collection.path === path);
}

export function Breadcrumbs({ collectionPath }: { collectionPath: string }) {
  const trail: Collection[] = [];
  const seen = new Set<string>();
  let current = findCollection(collectionPath);
  while (current && !seen.has(current.path)) {
    seen.add(current.path);
    trail.push(current);
    current = current.parentPath ? findCollection(current.parentPath) : undefined;
  }
  trail.reverse();

  return (
    <nav className="breadcrumbs" aria-label="Breadcrumb">
      <Link to="/" className="breadcrumbs-home">
        Home
      </Link>
      {trail.map((collection, index) => {
        const isLast = index === trail.length - 1;
        return (
          <span key={collection.path} className="breadcrumbs-item">
            <span className="breadcrumbs-separator" aria-hidden="true">
              /
            </span>
            {isLast ? (
              <span className="breadcrumbs-current">{collection.title}</span>
            ) : (
              <Link to={`/collection/${collection.path}`}>
                {collection.title}
              </Link>
            )}
          </span>
        );
      })}
    </nav>
  );
}
