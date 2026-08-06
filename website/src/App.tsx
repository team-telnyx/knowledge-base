import { useEffect } from "react";
import { Router, Route, Switch, useLocation } from "wouter";
import { DefaultLayout } from "./layouts/DefaultLayout";
import { HomePage } from "./pages/HomePage";
import { CollectionPage } from "./pages/CollectionPage";
import { ArticlePage } from "./pages/ArticlePage";
import { NotFoundPage } from "./pages/NotFoundPage";

const rawBasePath = process.env.BASE_PATH || "/";
const basePath = rawBasePath === "/" ? "" : rawBasePath;

// wouter doesn't reset scroll on navigation, so without this a click deep in
// a long list opens the next page at the same scroll offset.
function ScrollToTop() {
  const [location] = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location]);
  return null;
}

export function App() {
  return (
    <Router base={basePath}>
      <ScrollToTop />
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
