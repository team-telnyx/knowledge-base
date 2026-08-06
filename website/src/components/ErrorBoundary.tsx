import { Component } from "react";
import type { ErrorInfo, ReactNode } from "react";
import "./ErrorBoundary.css";

type Props = { children: ReactNode };
type State = { hasError: boolean };

// Plain href (not a wouter Link): navigating out of a crashed tree should be
// a full reload, which also resets whatever state caused the error.
const homeHref = process.env.BASE_PATH || "/";

export class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false };

  static getDerivedStateFromError(): State {
    return { hasError: true };
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error("Unhandled render error:", error, info.componentStack);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <p className="eyebrow">Something went wrong</p>
          <h1 className="error-boundary-title">This page failed to render</h1>
          <p className="error-boundary-text">
            Reload the page to try again, or head back to the start.
          </p>
          <a href={homeHref} className="error-boundary-link">
            Go to the homepage
          </a>
        </div>
      );
    }
    return this.props.children;
  }
}
