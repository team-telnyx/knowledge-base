import { useEffect } from "react";
import { Router, Route, Switch, Redirect, useLocation } from "wouter";
import { DefaultLayout } from "./layouts/DefaultLayout";
import { ErrorBoundary } from "./components/ErrorBoundary";
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
        <ErrorBoundary>
          <Switch>
            <Route path="/" component={HomePage} />
            <Route path="/collection/:rest*" component={CollectionPage} />
            <Route path="/article/:slug" component={ArticlePage} />
            {/* Legacy Intercom help-center URLs — the site replaces an indexed
                help center, so inbound links and search results still use the
                old scheme. Article URLs map 1:1; everything else goes home. */}
            <Route path="/en/articles/:slug">
              {(params: { slug: string }) => (
                <Redirect to={`/article/en--articles--${params.slug}`} replace />
              )}
            </Route>
            <Route path="/en">{() => <Redirect to="/" replace />}</Route>
            <Route path="/en/:rest*">{() => <Redirect to="/" replace />}</Route>
            <Route path="/:rest*" component={NotFoundPage} />
          </Switch>
        </ErrorBoundary>
      </DefaultLayout>
    </Router>
  );
}
