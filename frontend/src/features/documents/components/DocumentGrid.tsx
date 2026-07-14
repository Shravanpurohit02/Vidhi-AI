import type { DocumentRow } from "../types";

import DocumentCard from "./DocumentCard";

type Props = {
  documents: DocumentRow[];
};

export default function DocumentGrid({
  documents,
}: Props) {
  if (!documents.length) {
    return (
      <div className="rounded-xl border border-dashed p-12 text-center text-slate-500">
        No documents found.
      </div>
    );
  }

  return (
    <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
      {documents.map((doc) => (
        <DocumentCard
          key={doc.id}
          document={doc}
        />
      ))}
    </div>
  );
}
