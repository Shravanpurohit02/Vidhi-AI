export function clearSession() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
}
