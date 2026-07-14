import { Navigate, Outlet } from "react-router-dom";

import AuthLoader from "../components/common/AuthLoader";
import { useAuth } from "../providers/AuthProvider";

export default function ProtectedRoute() {
  const { isAuthenticated } = useAuth();

  return (
    <AuthLoader>
      {isAuthenticated ? (
        <Outlet />
      ) : (
        <Navigate to="/login" replace />
      )}
    </AuthLoader>
  );
}
