import { useQuery } from "@tanstack/react-query";
import { Search } from "lucide-react";
import CreateCaseDialog from "./components/CreateCaseDialog";
import ImportECourtsDialog from "./components/ImportECourtsDialog";

import api from "../../api/client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

type Case = {
  id: number;
  title: string;
  case_number: string;
  status: string;
  priority: string;
  court: string;
};

export default function CasesPage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["cases"],
    queryFn: async () => {
      const res = await api.get("/cases");
      return res.data as Case[];
    },
  });

  if (isLoading) {
    return (
      <div className="p-6">
        Loading cases...
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-6 text-red-500">
        Failed to load cases.
      </div>
    );
  }

  const cases = data ?? [];

  return (
    <div className="space-y-6">

      <div className="flex items-center justify-between">

        <div>
          <h1 className="text-3xl font-bold">
            Cases
          </h1>

          <p className="text-muted-foreground">
            Manage all legal matters.
          </p>
        </div>

        <div className="flex gap-2">
        <ImportECourtsDialog />
        <CreateCaseDialog />
      </div>

      </div>

      <Card>

        <CardHeader>
          <CardTitle>
            Case Registry
          </CardTitle>
        </CardHeader>

        <CardContent className="space-y-4">

          <div className="relative">
            <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
            <Input
              placeholder="Search case..."
              className="pl-10"
            />
          </div>

          <div className="overflow-x-auto">

            <table className="w-full">

              <thead>

                <tr className="border-b">

                  <th className="py-3 text-left">Case No.</th>
                  <th className="text-left">Title</th>
                  <th className="text-left">Court</th>
                  <th className="text-left">Status</th>
                  <th className="text-left">Priority</th>

                </tr>

              </thead>

              <tbody>

                {cases.length === 0 && (
                  <tr>
                    <td
                      colSpan={5}
                      className="py-10 text-center text-muted-foreground"
                    >
                      No cases available.
                    </td>
                  </tr>
                )}

                {cases.map((c) => (
                  <tr
                    key={c.id}
                    className="border-b"
                  >
                    <td className="py-4">{c.case_number}</td>
                    <td>{c.title}</td>
                    <td>{c.court}</td>

                    <td>
                      <Badge>{c.status}</Badge>
                    </td>

                    <td>
                      <Badge variant="secondary">
                        {c.priority}
                      </Badge>
                    </td>

                  </tr>
                ))}

              </tbody>

            </table>

          </div>

        </CardContent>

      </Card>

    </div>
  );
}
