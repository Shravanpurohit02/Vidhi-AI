import { User } from "lucide-react";

import { useAuth } from "../../providers/AuthProvider";

export default function UserBadge() {
  const { user } = useAuth();

  return (
    <div className="flex items-center gap-3 rounded-full border bg-white px-3 py-2 shadow-sm">

      <div className="flex h-9 w-9 items-center justify-center rounded-full bg-slate-100">
        <User className="h-5 w-5" />
      </div>

      <div className="hidden sm:block">
        <div className="text-sm font-medium">
          {user?.full_name ?? "Administrator"}
        </div>

        <div className="text-xs text-slate-500">
          {user?.email ?? ""}
        </div>
      </div>

    </div>
  );
}
