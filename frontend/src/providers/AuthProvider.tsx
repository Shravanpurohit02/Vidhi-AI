import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";

import {
  ACCESS_TOKEN_KEY,
  REFRESH_TOKEN_KEY,
} from "../types/auth";

import { getCurrentUser } from "../api/profile";
import type { UserProfile } from "../types/user";

type AuthContextType = {
  accessToken: string | null;
  refreshToken: string |null;
  user: UserProfile | null;
  loading: boolean;
  isAuthenticated: boolean;

  login: (accessToken: string, refreshToken: string) => Promise<void>;
  logout: () => Promise<void>;
  setTokens: (accessToken: string, refreshToken: string) => void;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [accessToken, setAccessToken] = useState<string | null>(null);
  const [refreshToken, setRefreshToken] = useState<string | null>(null);
  const [user, setUser] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const access = localStorage.getItem(ACCESS_TOKEN_KEY);
    const refresh = localStorage.getItem(REFRESH_TOKEN_KEY);

    setAccessToken(access);
    setRefreshToken(refresh);

    async function bootstrap() {
      if (!access || !refresh) {
        setLoading(false);
        return;
      }

      try {
        const profile = await getCurrentUser();
        setUser(profile);
      } catch {
        localStorage.removeItem(ACCESS_TOKEN_KEY);
        localStorage.removeItem(REFRESH_TOKEN_KEY);
        setAccessToken(null);
        setRefreshToken(null);
        setUser(null);
      }

      setLoading(false);
    }

    bootstrap();
  }, []);

  const setTokens = (
    newAccessToken: string,
    newRefreshToken: string,
  ) => {
    localStorage.setItem(
      ACCESS_TOKEN_KEY,
      newAccessToken,
    );

    localStorage.setItem(
      REFRESH_TOKEN_KEY,
      newRefreshToken,
    );

    setAccessToken(newAccessToken);
    setRefreshToken(newRefreshToken);
  };
  const login = async (
    newAccessToken: string,
    newRefreshToken: string,
  ) => {
    setTokens(
      newAccessToken,
      newRefreshToken,
    );

    const profile = await getCurrentUser();
    setUser(profile);
  };

  const logout = async () => {
    const token = localStorage.getItem(
      REFRESH_TOKEN_KEY,
    );

    try {
      if (token) {
        const { logout } = await import("../services/logout");
        await logout(token);
      }
    } catch {}

    localStorage.removeItem(ACCESS_TOKEN_KEY);
    localStorage.removeItem(REFRESH_TOKEN_KEY);

    setAccessToken(null);
    setRefreshToken(null);
    setUser(null);
  };

  const value = useMemo(
    () => ({
      accessToken,
      refreshToken,
      user,
      loading,
      isAuthenticated: !!accessToken,
      login,
      logout,
      setTokens,
    }),
    [
      accessToken,
      refreshToken,
      user,
      loading,
    ],
  );

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error(
      "useAuth must be used within an AuthProvider",
    );
  }

  return context;
}
