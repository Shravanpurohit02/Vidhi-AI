import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../api/client";
import { useAuth } from "../providers/AuthProvider";
import type {
  LoginRequest,
  LoginResponse,
} from "../types/auth";

export default function LoginPage() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [form, setForm] = useState<LoginRequest>({
    email: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(
    e: React.FormEvent,
  ) {
    e.preventDefault();

    setLoading(true);
    setError("");

    try {
      const { data } =
        await api.post<LoginResponse>(
          "/auth/login",
          form,
        );

      login(
        data.access_token,
        data.refresh_token,
      );

      navigate("/", { replace: true });
    } catch (err: any) {
      setError(
        err?.response?.data?.detail ??
          "Login failed.",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        minHeight: "100vh",
      }}
    >
      <form
        onSubmit={handleSubmit}
        style={{
          width: 360,
          display: "flex",
          flexDirection: "column",
          gap: 12,
        }}
      >
        <h1>Vidhi AI</h1>

        <input
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={(e) =>
            setForm({
              ...form,
              email: e.target.value,
            })
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={(e) =>
            setForm({
              ...form,
              password: e.target.value,
            })
          }
        />

        <button
          type="submit"
          disabled={loading}
        >
          {loading ? "Signing in..." : "Login"}
        </button>

        {error && (
          <p style={{ color: "red" }}>
            {error}
          </p>
        )}
      </form>
    </div>
  );
}
