import { useQuery } from "@tanstack/react-query";

import {
  searchDocuments,
} from "../api/documents";

export function useDocumentSearch(
  query: string,
) {
  return useQuery({
    queryKey: ["documents", query],
    queryFn: () => searchDocuments(query),
    enabled: query.trim().length > 0,
  });
}
