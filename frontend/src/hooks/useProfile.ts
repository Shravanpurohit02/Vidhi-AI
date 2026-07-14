import { useQuery } from "@tanstack/react-query";
import { getCurrentUser } from "../api/profile";

export function useProfile() {
  return useQuery({
    queryKey: ["profile"],
    queryFn: getCurrentUser,
    retry: 1,
  });
}
