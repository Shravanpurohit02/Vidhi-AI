import api from "../api/client";

export async function logout(refreshToken: string) {
  await api.post("/auth/logout", {
    refresh_token: refreshToken,
  });
}
