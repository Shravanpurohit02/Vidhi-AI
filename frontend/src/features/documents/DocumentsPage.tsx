import { useState } from "react";

import { useDocuments } from "../../hooks/useDocuments";
import { useDocumentSearch } from "../../hooks/useDocumentSearch";

import DocumentSearch from "./components/DocumentSearch";
import DocumentsToolbar from "./components/DocumentsToolbar";
import DocumentGrid from "./components/DocumentGrid";

export default function DocumentsPage() {
  const [query, setQuery] = useState("");

  const list = useDocuments();

  const search = useDocumentSearch(query);

  const documents =
    query.trim()
      ? search.data ?? []
      : list.data ?? [];

  if (list.isLoading) {
    return (
      <div className="flex h-72 items-center justify-center">
        Loading documents...
      </div>
    );
  }

  return (
    <div className="space-y-6">

      <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">

        <div>
          <h1 className="text-3xl font-bold">
            Documents
          </h1>

          <p className="text-muted-foreground">
            Manage all legal documents.
          </p>
        </div>

        <DocumentsToolbar
          onRefresh={() => list.refetch()}
        />

      </div>

      <DocumentSearch
        value={query}
        onChange={setQuery}
      />

      <DocumentGrid
        documents={documents}
      />

    </div>
  );
}
