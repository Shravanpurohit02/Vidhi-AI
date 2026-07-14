import {
  createContext,
  useContext,
  useState,
  type ReactNode,
} from "react";

import { useSidebar } from "../../hooks/useSidebar";

type LayoutContextType = ReturnType<typeof useSidebar> & {
  mobileOpen: boolean;
  openMobile(): void;
  closeMobile(): void;
};

const LayoutContext=createContext<LayoutContextType|undefined>(undefined);

export function LayoutProvider({
  children,
}:{
  children:ReactNode;
}){

  const sidebar=useSidebar();

  const [mobileOpen,setMobileOpen]=useState(false);

  return(
    <LayoutContext.Provider
      value={{
        ...sidebar,
        mobileOpen,
        openMobile:()=>setMobileOpen(true),
        closeMobile:()=>setMobileOpen(false),
      }}
    >
      {children}
    </LayoutContext.Provider>
  );

}

export function useLayout(){

  const ctx=useContext(LayoutContext);

  if(!ctx){
    throw new Error("LayoutProvider missing");
  }

  return ctx;

}
