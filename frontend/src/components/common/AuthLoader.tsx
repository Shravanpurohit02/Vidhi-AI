import type { ReactNode } from "react";
import { useAuth } from "../../providers/AuthProvider";

export default function AuthLoader({
  children,
}: {
  children: ReactNode;
}) {
  const { loading } = useAuth();

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center text-lg">
        Loading...
      </div>
    );
  }

  return <>{children}</>;
}
