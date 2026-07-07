import { Link } from "wouter";

export function NotFoundPage() {
  return (
    <div>
      <h1>Page not found</h1>
      <p>
        <Link to="/">Back to home</Link>
      </p>
    </div>
  );
}
