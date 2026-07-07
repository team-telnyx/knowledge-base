import { Search } from "../components/Search";
import { Sidebar } from "../components/Sidebar";
import "./DefaultLayout.css";

export function DefaultLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="default-layout">
      <header className="default-layout-header">
        <span className="default-layout-title">Telnyx Support</span>
        <Search />
      </header>
      <div className="default-layout-body">
        <aside className="default-layout-sidebar">
          <Sidebar />
        </aside>
        <main className="default-layout-content">{children}</main>
      </div>
    </div>
  );
}
