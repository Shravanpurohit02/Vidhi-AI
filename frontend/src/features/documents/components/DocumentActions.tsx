import { Cpu, Trash2 } from "lucide-react";
import { Button } from "@/components/ui/button";

import {
  useDeleteDocument,
  useProcessDocument,
} from "../../../api/documentMutations";

export default function DocumentActions({
  id,
}: {
  id: number;
}) {
  const del = useDeleteDocument();
  const process = useProcessDocument();

  return (
    <div className="mt-4 flex gap-2">

      <Button
        size="sm"
        variant="outline"
        disabled={process.isPending}
        onClick={() =>
          process.mutate({
            id,
            text: "",
          })
        }
      >
        <Cpu className="mr-2 h-4 w-4"/>
        {process.isPending ? "Processing..." : "Process"}
      </Button>

      <Button
        size="sm"
        variant="destructive"
        disabled={del.isPending}
        onClick={() => del.mutate(id)}
      >
        <Trash2 className="mr-2 h-4 w-4"/>
        {del.isPending ? "Deleting..." : "Delete"}
      </Button>

    </div>
  );
}
