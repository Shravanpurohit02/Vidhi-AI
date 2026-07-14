export interface DocumentRow {
  id: number;
  title: string;
  document_type: string;
  case_id: number | null;
  created_at: string;
}
