import api from "./client";

export interface DashboardSummary {
  clients: number;
  documents: number;
  hearings: number;
}

export async function getDashboardSummary() {
  const { data } =
    await api.get<DashboardSummary>(
      "/dashboard/summary",
    );

  return data;
}
