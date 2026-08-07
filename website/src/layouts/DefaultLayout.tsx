import { Link, useLocation } from "wouter";
import { Search } from "../components/Search";
import { Footer } from "../components/Footer";
import "./DefaultLayout.css";

export function DefaultLayout({ children }: { children: React.ReactNode }) {
  const [location] = useLocation();
  const isHome = location === "/";

  return (
    <div className="layout">
      <a className="skip-link" href="#main-content">
        Skip to content
      </a>
      <header className="site-header">
        <div className="container site-header-inner">
          <Link to="/" className="wordmark">
            <span className="wordmark-brand">telnyx</span>
            <span className="wordmark-divider" aria-hidden="true" />
            <span className="wordmark-product">Support</span>
          </Link>
          {!isHome && (
            <div className="site-header-search">
              <Search variant="header" />
            </div>
          )}
          <nav className="site-nav" aria-label="Telnyx sites">
            <a
              href="https://developers.telnyx.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              Developer Docs
            </a>
            <a
              href="https://telnyx.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              telnyx.com
            </a>
          </nav>
        </div>
      </header>
      <main id="main-content" className="site-main">
        {children}
      </main>
      <Footer />
    </div>
  );
}
