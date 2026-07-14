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
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area";
import { useAuth } from "../../providers/AuthProvider";

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

  return (
    <aside className="flex h-screen w-64 flex-col border-r bg-background">
      <div className="p-6">
        <h1 className="text-2xl font-bold">⚖️ Vidhi AI</h1>
        <p className="text-sm text-muted-foreground">
          Legal Intelligence Platform
        </p>
      </div>

      <Separator />

      <ScrollArea className="flex-1">
        <nav className="space-y-1 p-4">
          {items.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  [
                    "flex items-center gap-3 rounded-lg px-3 py-2 transition-colors",
                    isActive
                      ? "bg-primary text-primary-foreground"
                      : "hover:bg-muted",
                  ].join(" ")
                }
              >
                <Icon className="h-4 w-4" />
                {item.label}
              </NavLink>
            );
          })}
        </nav>
      </ScrollArea>

      <div className="border-t p-4">
        <Button
          variant="outline"
          className="w-full justify-start"
          onClick={logout}
        >
          <LogOut className="mr-2 h-4 w-4" />
          Logout
        </Button>
      </div>
    </aside>
  );
}