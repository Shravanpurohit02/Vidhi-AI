import axios from "axios";

import {
  ACCESS_TOKEN_KEY,
  REFRESH_TOKEN_KEY,
} from "../types/auth";

const api = axios.create({
  baseURL:
    import.meta.env.VITE_API_BASE_URL ??
    "http://127.0.0.1:8000",
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem(
    ACCESS_TOKEN_KEY,
  );

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

let refreshing: Promise<string> | null = null;

async function refreshAccessToken(): Promise<string> {
  if (!refreshing) {
    refreshing = axios
      .post(
        (
          import.meta.env.VITE_API_BASE_URL ??
          "http://127.0.0.1:8000"
        ) + "/auth/refresh",
        {
          refresh_token:
            localStorage.getItem(
              REFRESH_TOKEN_KEY,
            ),
        },
      )
      .then(({ data }) => {
        localStorage.setItem(
          ACCESS_TOKEN_KEY,
          data.access_token,
        );

        localStorage.setItem(
          REFRESH_TOKEN_KEY,
          data.refresh_token,
        );

        return data.access_token;
      })
      .finally(() => {
        refreshing = null;
      });
  }

  return refreshing;
}

api.interceptors.response.use(
  (response) => response,

  async (error) => {
    const original = error.config;

    if (
      error.response?.status === 401 &&
      !original._retry
    ) {
      original._retry = true;

      try {
        const token =
          await refreshAccessToken();

        original.headers.Authorization =
          `Bearer ${token}`;

        return api(original);
      } catch {
        localStorage.removeItem(
          ACCESS_TOKEN_KEY,
        );

        localStorage.removeItem(
          REFRESH_TOKEN_KEY,
        );

        window.location.href = "/";
      }
    }

    return Promise.reject(error);
  },
);

export default api;
