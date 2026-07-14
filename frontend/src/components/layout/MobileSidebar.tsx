import { NavLink } from "react-router-dom";
import {
  X,
  LayoutDashboard,
  Users,
  FileText,
  Search,
  Bot,
  Scale,
  PenSquare,
  Workflow,
} from "lucide-react";

import { Button } from "@/components/ui/button";
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

export default function MobileSidebar() {

  const {
    mobileOpen,
    closeMobile,
  } = useLayout();

  if (!mobileOpen) return null;

  return (
    <div className="fixed inset-0 z-50 md:hidden">

      <div
        className="absolute inset-0 bg-black/40 backdrop-blur-sm"
        onClick={closeMobile}
      />

      <aside className="relative h-full w-72 bg-white shadow-2xl">

        <div className="flex items-center justify-between border-b p-5">

          <div>
            <h1 className="text-xl font-bold">
              ⚖️ Vidhi AI
            </h1>

            <p className="text-xs text-muted-foreground">
              Legal Intelligence
            </p>
          </div>

          <Button
            variant="ghost"
            size="icon"
            onClick={closeMobile}
          >
            <X className="h-5 w-5"/>
          </Button>

        </div>

        <nav className="space-y-2 p-4">

          {items.map((item)=>{

            const Icon=item.icon;

            return(
              <NavLink
                key={item.to}
                to={item.to}
                onClick={closeMobile}
                className={({isActive})=>
                  [
                    "flex items-center gap-3 rounded-lg px-3 py-3",
                    isActive
                    ? "bg-primary text-primary-foreground"
                    : "hover:bg-muted",
                  ].join(" ")
                }
              >
                <Icon className="h-5 w-5"/>
                {item.label}
              </NavLink>
            );

          })}

        </nav>

      </aside>

    </div>
  );
}
