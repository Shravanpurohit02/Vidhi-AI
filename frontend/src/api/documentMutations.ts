import { toast } from "sonner";
import { useMutation, useQueryClient } from "@tanstack/react-query";

import {
  deleteDocument,
  processDocument,
} from "./documents";

export function useDeleteDocument() {
  const qc = useQueryClient();

  return useMutation({
    mutationFn: deleteDocument,

    onSuccess: () => {
      toast.success("Document deleted.");
      qc.invalidateQueries({
        queryKey: ["documents"],
      });
    },

    onError: () => {
      toast.error("Unable to delete document.");
    },
  });
}

export function useProcessDocument() {
  const qc = useQueryClient();

  return useMutation({
    mutationFn: ({
      id,
      text,
    }: {
      id: number;
      text: string;
    }) => processDocument(id, text),

    onSuccess: () => {
      toast.success("Document processed.");
      qc.invalidateQueries({
        queryKey: ["documents"],
      });
    },

    onError: () => {
      toast.error("Document processing failed.");
    },
  });
}
