import { Router, Route, Link, Switch } from "wouter";
import { DefaultLayout } from "./layouts/DefaultLayout";
import { CollectionPage } from "./pages/CollectionPage";
import { ArticlePage } from "./pages/ArticlePage";
import { NotFoundPage } from "./pages/NotFoundPage";
import { collections } from "./content/manifest";

const rawBasePath = process.env.BASE_PATH || "/";
const basePath = rawBasePath === "/" ? "" : rawBasePath;

function HomePage() {
  const rootCollections = collections.filter((c) => c.parentPath === null);
  return (
    <div>
      <h1>Telnyx Support Knowledge Base</h1>
      <ul>
        {rootCollections.map((c) => (
          <li key={c.path}>
            <Link to={`/collection/${c.path}`}>{c.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function App() {
  return (
    <Router base={basePath}>
      <DefaultLayout>
        <Switch>
          <Route path="/" component={HomePage} />
          <Route path="/collection/:rest*" component={CollectionPage} />
          <Route path="/article/:slug" component={ArticlePage} />
          <Route path="/:rest*" component={NotFoundPage} />
        </Switch>
      </DefaultLayout>
    </Router>
  );
}
