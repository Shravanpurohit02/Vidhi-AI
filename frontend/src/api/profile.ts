import api from "./client";
import type { UserProfile } from "../types/user";

export async function getCurrentUser(): Promise<UserProfile> {
  const { data } = await api.get<UserProfile>("/profile");
  return data;
}
