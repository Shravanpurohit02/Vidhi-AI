export interface UserProfile {
  id: number;
  email: string;
  full_name?: string;
  role?: string;
  is_active?: boolean;
}
