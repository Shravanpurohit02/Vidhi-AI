import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import type { LucideIcon } from "lucide-react";

type Props = {
  title: string;
  value: string | number;
  icon: LucideIcon;
};

export default function StatCard({
  title,
  value,
  icon: Icon,
}: Props) {
  return (
    <Card className="shadow-sm">
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-sm text-muted-foreground">
          {title}
        </CardTitle>

        <Icon className="h-5 w-5 text-slate-500" />
      </CardHeader>

      <CardContent>
        <div className="text-3xl font-bold">
          {value}
        </div>
      </CardContent>
    </Card>
  );
}
