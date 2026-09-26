"use client";

import { PortfolioProvider } from "../lib/store";

export function Providers({ children }: { children: React.ReactNode }) {
  return <PortfolioProvider>{children}</PortfolioProvider>;
}
