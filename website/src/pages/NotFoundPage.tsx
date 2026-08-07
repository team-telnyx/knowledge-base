import { Link } from "wouter";
import "./NotFoundPage.css";

export function NotFoundPage() {
  return (
    <div className="container not-found">
      <p className="eyebrow">404</p>
      <h1 className="not-found-title">Page not found</h1>
      <p className="not-found-text">
        The page you're looking for doesn't exist or may have moved.
      </p>
      <Link to="/" className="not-found-link">
        Browse all topics
      </Link>
    </div>
  );
}
