import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

const activities = [
  {
    title: "System Ready",
    description: "Vidhi AI is connected successfully.",
  },
];

export default function RecentActivity() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>
          Recent Activity
        </CardTitle>
      </CardHeader>

      <CardContent>
        <div className="space-y-4">
          {activities.map((activity) => (
            <div
              key={activity.title}
              className="border-l-2 pl-4"
            >
              <div className="font-medium">
                {activity.title}
              </div>

              <div className="text-sm text-muted-foreground">
                {activity.description}
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
