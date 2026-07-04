import { Navigate, Route, Routes } from "react-router-dom";

import { useAuth } from "./providers/AuthProvider";
import LoginPage from "./pages/LoginPage";
import AppLayout from "./components/layout/AppLayout";

import DashboardPage from "./features/dashboard/DashboardPage";

function Placeholder({ title }: { title: string }) {
  return <h1>{title} (Coming Soon)</h1>;
}

export default function App() {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return (
      <Routes>
        <Route path="*" element={<LoginPage />} />
      </Routes>
    );
  }

  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route index element={<DashboardPage />} />
        <Route path="clients" element={<Placeholder title="Clients" />} />
        <Route path="documents" element={<Placeholder title="Documents" />} />
        <Route path="research" element={<Placeholder title="Research" />} />
        <Route path="drafting" element={<Placeholder title="Drafting" />} />
        <Route path="reasoning" element={<Placeholder title="Reasoning" />} />
        <Route path="ai" element={<Placeholder title="AI Chat" />} />
        <Route path="workflow" element={<Placeholder title="Workflow" />} />
      </Route>

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
