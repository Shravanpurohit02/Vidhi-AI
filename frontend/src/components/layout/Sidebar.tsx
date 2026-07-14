import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Users,
  FileText,
  Search,
  Bot,
  Scale,
  PenSquare,
  Workflow,
  LogOut,
  PanelLeftClose,
  PanelLeftOpen,
} from "lucide-react";

import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area";

import { useAuth } from "../../providers/AuthProvider";
import { useLayout } from "./LayoutContext";

const items = [
  { label: "Dashboard", icon: LayoutDashboard, to: "/" },
  { label: "Clients", icon: Users, to: "/clients" },
  { label: "Documents", icon: FileText, to: "/documents" },
  { label: "Research", icon: Search, to: "/research" },
  { label: "AI Chat", icon: Bot, to: "/ai" },
  { label: "Reasoning", icon: Scale, to: "/reasoning" },
  { label: "Drafting", icon: PenSquare, to: "/drafting" },
  { label: "Workflow", icon: Workflow, to: "/workflow" },
];

export default function Sidebar() {
  const { logout } = useAuth();
  const { collapsed, toggle } = useLayout();

  return (
    <aside
      className={[
        "hidden md:flex",
        "sticky top-0 h-screen flex-col border-r bg-white shadow-sm transition-all duration-300",
        collapsed ? "w-20" : "w-64",
      ].join(" ")}
    >
      <div className="flex items-center justify-between border-b p-4">
        {!collapsed && (
          <div>
            <h1 className="text-xl font-bold">
              ⚖️ Vidhi AI
            </h1>
            <p className="text-xs text-muted-foreground">
              Legal Intelligence
            </p>
          </div>
        )}

        <Button
          variant="ghost"
          size="icon"
          onClick={toggle}
        >
          {collapsed ? (
            <PanelLeftOpen className="h-5 w-5"/>
          ) : (
            <PanelLeftClose className="h-5 w-5"/>
          )}
        </Button>
      </div>

      <ScrollArea className="flex-1">
        <nav className="space-y-2 p-3">
          {items.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  [
                    "flex items-center rounded-lg transition-all",
                    collapsed
                      ? "justify-center p-3"
                      : "gap-3 px-3 py-3",
                    isActive
                      ? "bg-primary text-primary-foreground"
                      : "hover:bg-muted",
                  ].join(" ")
                }
              >
                <Icon className="h-5 w-5 shrink-0"/>

                {!collapsed && (
                  <span>{item.label}</span>
                )}
              </NavLink>
            );
          })}
        </nav>
      </ScrollArea>

      <Separator />

      <div className="p-3">
        <Button
          variant="outline"
          className="w-full"
          onClick={logout}
        >
          <LogOut className="h-4 w-4"/>

          {!collapsed && (
            <span className="ml-2">
              Logout
            </span>
          )}
        </Button>
      </div>
    </aside>
  );
}
