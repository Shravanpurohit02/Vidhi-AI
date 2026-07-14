import { useEffect, useState } from "react";

const KEY = "vidhi-sidebar-collapsed";

export function useSidebar() {
  const [collapsed, setCollapsed] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem(KEY);
    if (saved) {
      setCollapsed(saved === "true");
    }
  }, []);

  function toggle() {
    setCollapsed((prev) => {
      localStorage.setItem(KEY, String(!prev));
      return !prev;
    });
  }

  return {
    collapsed,
    toggle,
  };
}
