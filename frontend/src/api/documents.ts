import api from "./client";

export interface Document {
  id: number;
  title: string;
  document_type: string;
  case_id: number | null;
  created_at: string;
}

export async function listDocuments() {
  const { data } = await api.get<Document[]>("/documents/");
  return data;
}

export async function searchDocuments(query: string) {
  const { data } = await api.get<Document[]>("/documents/search", {
    params: { q: query },
  });

  return data;
}

export async function deleteDocument(id: number) {
  return api.delete(`/documents/${id}`);
}

export async function processDocument(
  id: number,
  text: string,
) {
  const { data } = await api.post(
    `/documents/process/${id}`,
    { text },
  );

  return data;
}
