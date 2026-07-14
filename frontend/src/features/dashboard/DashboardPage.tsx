import {
  Users,
  FileText,
  Scale,
} from "lucide-react";

import { useDashboard } from "../../hooks/useDashboard";
import StatCard from "../../components/dashboard/StatCard";
import QuickActions from "../../components/dashboard/QuickActions";
import RecentActivity from "../../components/dashboard/RecentActivity";

export default function DashboardPage() {

  const {
    data,
    isLoading,
    error,
    refetch,
  } = useDashboard();

  if (isLoading) {
    return (
      <div className="flex h-[70vh] items-center justify-center">
        Loading Dashboard...
      </div>
    );
  }

  if (error) {
    return (
      <div className="space-y-4">

        <h2 className="text-2xl font-semibold">
          Unable to load dashboard
        </h2>

        <button
          className="rounded border px-4 py-2"
          onClick={() => refetch()}
        >
          Retry
        </button>

      </div>
    );
  }

  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-3xl font-bold">
          Dashboard
        </h1>

        <p className="text-muted-foreground">
          Welcome to Vidhi AI
        </p>
      </div>

      <div className="grid gap-6 sm:grid-cols-2 xl:grid-cols-3">

        <StatCard
          title="Clients"
          value={data?.clients ?? 0}
          icon={Users}
        />

        <StatCard
          title="Documents"
          value={data?.documents ?? 0}
          icon={FileText}
        />

        <StatCard
          title="Hearings"
          value={data?.hearings ?? 0}
          icon={Scale}
        />

      </div>

      <div className="grid gap-6 xl:grid-cols-2">

        <QuickActions />

        <RecentActivity />

      </div>

    </div>
  );
}
