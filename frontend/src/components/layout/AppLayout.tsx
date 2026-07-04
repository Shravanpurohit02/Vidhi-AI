import { Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";

export default function AppLayout() {
  return (
    <div className="flex min-h-screen bg-slate-50">
      <Sidebar />

      <div className="flex min-w-0 flex-1 flex-col">
        <header className="sticky top-0 z-20 flex h-16 items-center justify-between border-b bg-white px-6">
          <div>
            <h2 className="text-xl font-semibold">
              Vidhi AI
            </h2>
            <p className="text-sm text-slate-500">
              Legal Intelligence Platform
            </p>
          </div>

          <div className="rounded-full border bg-slate-100 px-4 py-2 text-sm">
            Administrator
          </div>
        </header>

        <main className="flex-1 overflow-auto p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
