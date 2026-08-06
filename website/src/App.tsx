import { Router, Route, Switch } from "wouter";
import { DefaultLayout } from "./layouts/DefaultLayout";
import { HomePage } from "./pages/HomePage";
import { CollectionPage } from "./pages/CollectionPage";
import { ArticlePage } from "./pages/ArticlePage";
import { NotFoundPage } from "./pages/NotFoundPage";

const rawBasePath = process.env.BASE_PATH || "/";
const basePath = rawBasePath === "/" ? "" : rawBasePath;

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
