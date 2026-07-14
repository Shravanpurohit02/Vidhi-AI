import { Menu } from "lucide-react";
import { Outlet } from "react-router-dom";

import { Button } from "@/components/ui/button";

import Sidebar from "./Sidebar";
import MobileSidebar from "./MobileSidebar";
import UserBadge from "../common/UserBadge";
import { useLayout } from "./LayoutContext";

export default function AppLayout() {
  const { openMobile } = useLayout();

  return (
    <div className="flex min-h-screen bg-slate-50">

      <Sidebar />
      <MobileSidebar />

      <div className="flex min-w-0 flex-1 flex-col">

        <header className="sticky top-0 z-20 flex h-16 items-center justify-between border-b bg-white px-4 md:px-6">

          <div className="flex items-center gap-3">

            <Button
              variant="ghost"
              size="icon"
              className="md:hidden"
              onClick={openMobile}
            >
              <Menu className="h-5 w-5"/>
            </Button>

            <div>
              <h2 className="text-xl font-semibold">
                Vidhi AI
              </h2>

              <p className="hidden text-sm text-slate-500 sm:block">
                Legal Intelligence Platform
              </p>
            </div>

          </div>

          <UserBadge />

        </header>

        <main className="flex-1 overflow-auto p-4 md:p-6">
          <Outlet />
        </main>

      </div>

    </div>
  );
}
