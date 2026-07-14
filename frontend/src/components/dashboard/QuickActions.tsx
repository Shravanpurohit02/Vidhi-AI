import { Button } from "@/components/ui/button";

const actions = [
  "New Client",
  "Upload Document",
  "Legal Research",
  "AI Drafting",
];

export default function QuickActions() {
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {actions.map(action => (
        <Button
          key={action}
          variant="outline"
          className="justify-start h-12"
        >
          {action}
        </Button>
      ))}
    </div>
  );
}
