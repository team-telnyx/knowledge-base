import type { CSSProperties } from "react";
import { Link, useLocation } from "wouter";
import { collections } from "../content/manifest";
import type { Collection } from "../content/types";
import "./Sidebar.css";

function isActiveCollection(location: string, path: string): boolean {
  const prefix = `/collection/${path}`;
  return location === prefix || location.startsWith(`${prefix}/`);
}

function CollectionNode({
  collection,
  location,
  depth,
}: {
  collection: Collection;
  location: string;
  depth: number;
}) {
  const children = collections.filter((c) => c.parentPath === collection.path);
  const active = isActiveCollection(location, collection.path);
  const className = active
    ? "sidebar-link sidebar-link-active"
    : "sidebar-link";
  return (
    <li className="sidebar-item">
      <Link
        to={`/collection/${collection.path}`}
        className={className}
        style={{ "--sidebar-depth": depth } as CSSProperties}
      >
        {collection.title}
      </Link>
      {children.length > 0 ? (
        <ul className="sidebar-list">
          {children.map((child) => (
            <CollectionNode
              key={child.path}
              collection={child}
              location={location}
              depth={depth + 1}
            />
          ))}
        </ul>
      ) : null}
    </li>
  );
}

export function Sidebar() {
  const [location] = useLocation();
  const roots = collections.filter((c) => c.parentPath === null);
  return (
    <nav className="sidebar">
      <ul className="sidebar-list">
        {roots.map((root) => (
          <CollectionNode
            key={root.path}
            collection={root}
            location={location}
            depth={0}
          />
        ))}
      </ul>
    </nav>
  );
}
