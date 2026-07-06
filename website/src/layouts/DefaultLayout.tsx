import "./DefaultLayout.css";

export function DefaultLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="default-layout">
      <header className="default-layout-header">
        <span className="default-layout-title">Telnyx Support</span>
      </header>
      <div className="default-layout-body">
        <aside className="default-layout-sidebar">
          <nav>
            <ul className="default-layout-nav-list" />
          </nav>
        </aside>
        <main className="default-layout-content">{children}</main>
      </div>
    </div>
  );
}
