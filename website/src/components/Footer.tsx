import "./Footer.css";

export function Footer() {
  return (
    <footer className="site-footer">
      <div className="container site-footer-inner">
        <div className="site-footer-brand">
          <span className="site-footer-wordmark">telnyx</span>
          <p className="site-footer-tagline">
            Support Center for the Telnyx connectivity platform.
          </p>
        </div>
        <nav className="site-footer-links" aria-label="Telnyx resources">
          <a href="https://telnyx.com" target="_blank" rel="noopener noreferrer">
            telnyx.com
          </a>
          <a
            href="https://developers.telnyx.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            Developer Docs
          </a>
          <a
            href="https://status.telnyx.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            Platform status
          </a>
          <a
            href="https://telnyx.com/contact-us"
            target="_blank"
            rel="noopener noreferrer"
          >
            Contact us
          </a>
        </nav>
        <div className="site-footer-support">
          <span className="eyebrow">24/7 support</span>
          <a className="site-footer-phone" href="tel:+18889809750">
            +1 888 980 9750
          </a>
        </div>
      </div>
      <div className="container site-footer-legal">
        © {new Date().getFullYear()} Telnyx LLC. All rights reserved.
      </div>
    </footer>
  );
}
