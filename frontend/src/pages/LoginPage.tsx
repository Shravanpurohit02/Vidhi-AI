import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/client";
import { useAuth } from "../providers/AuthProvider";

export default function LoginPage() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");

    try {
      const { data } = await api.post(
        "/auth/login",
        {
          email,
          password,
        },
      );

      login(data.access_token);
      navigate("/");
    } catch (err: any) {
      console.log("LOGIN ERROR", err);
      console.log("RESPONSE", err?.response);
      console.log("DATA", err?.response?.data);

      setError(
        JSON.stringify(err?.response?.data ?? err.message)
      );
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
          width: 340,
          display: "flex",
          flexDirection: "column",
          gap: 12,
        }}
      >
        <h1>Vidhi AI</h1>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button type="submit">
          Login
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
