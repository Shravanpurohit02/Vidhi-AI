import { useQuery } from "@tanstack/react-query";
import {
  Users,
  FileText,
  Scale,
} from "lucide-react";

import api from "../../api/client";
import StatCard from "../../components/dashboard/StatCard";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export default function DashboardPage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["dashboard-summary"],
    queryFn: async () => {
      const res = await api.get("/dashboard/summary");
      return res.data;
    },
  });

  if (isLoading) {
    return <h2>Loading dashboard...</h2>;
  }

  if (error) {
    return <h2>Unable to load dashboard.</h2>;
  }

  const summary = data ?? {};

  return (
    <div className="space-y-6 p-6">
      <div>
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <p className="text-muted-foreground">
          Welcome to Vidhi AI Legal Intelligence Platform
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <StatCard title="Clients" value={summary.clients ?? 0} icon={Users} />
        <StatCard title="Documents" value={summary.documents ?? 0} icon={FileText} />
        <StatCard title="Hearings" value={summary.hearings ?? 0} icon={Scale} />
      </div>

      <div className="grid gap-6 lg:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Recent Activity</CardTitle>
          </CardHeader>
          <CardContent>
            <p>No activity yet.</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Quick Actions</CardTitle>
          </CardHeader>
          <CardContent>
            <p>Ready.</p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
