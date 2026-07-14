import { Button } from "@/components/ui/button";

type Props = {
  onRefresh(): void;
};

export default function DocumentsToolbar({
  onRefresh,
}: Props) {
  return (
    <div className="flex flex-wrap gap-3">
      <Button onClick={onRefresh}>
        Refresh
      </Button>

      <Button variant="outline">
        Upload
      </Button>
    </div>
  );
}
