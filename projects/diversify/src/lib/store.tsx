"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
} from "react";
import { COMPANY_BY_TICKER } from "./companies";
import { SAMPLES } from "./library";
import { auditPortfolio, suggestHedge } from "./scoring";
import type { Holding } from "./types";

const STORAGE_KEY = "diversify.holdings.v1";

type Store = {
  holdings: Holding[];
  sampleId: string | null;
  hydrated: boolean;
  setWeight: (ticker: string, weight: number) => void;
  addTicker: (ticker: string) => void;
  removeTicker: (ticker: string) => void;
  loadSample: (id: string) => void;
  clear: () => void;
  normalize: () => void;
};

const Ctx = createContext<Store | null>(null);

export function PortfolioProvider({ children }: { children: React.ReactNode }) {
  const [holdings, setHoldings] = useState<Holding[]>([]);
  const [sampleId, setSampleId] = useState<string | null>(null);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw) as {
          holdings?: Holding[];
          sampleId?: string | null;
        };
        if (Array.isArray(parsed.holdings)) {
          setHoldings(
            parsed.holdings.filter((h) => COMPANY_BY_TICKER[h.ticker]),
          );
        }
        setSampleId(parsed.sampleId ?? null);
      } else {
        const fox = SAMPLES.find((s) => s.id === "consensus");
        if (fox) {
          setHoldings(fox.holdings);
          setSampleId(fox.id);
        }
      }
    } catch {
      /* ignore */
    }
    setHydrated(true);
  }, []);

  useEffect(() => {
    if (!hydrated) return;
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ holdings, sampleId }));
  }, [holdings, sampleId, hydrated]);

  const setWeight = useCallback((ticker: string, weight: number) => {
    setSampleId(null);
    setHoldings((prev) =>
      prev.map((h) => (h.ticker === ticker ? { ...h, weight } : h)),
    );
  }, []);

  const addTicker = useCallback((ticker: string) => {
    if (!COMPANY_BY_TICKER[ticker]) return;
    setSampleId(null);
    setHoldings((prev) => {
      if (prev.some((h) => h.ticker === ticker)) return prev;
      const nextWeight = prev.length ? 8 : 20;
      return [...prev, { ticker, weight: nextWeight }];
    });
  }, []);

  const removeTicker = useCallback((ticker: string) => {
    setSampleId(null);
    setHoldings((prev) => prev.filter((h) => h.ticker !== ticker));
  }, []);

  const loadSample = useCallback((id: string) => {
    const sample = SAMPLES.find((s) => s.id === id);
    if (!sample) return;
    setHoldings(sample.holdings.map((h) => ({ ...h })));
    setSampleId(id);
  }, []);

  const clear = useCallback(() => {
    setHoldings([]);
    setSampleId(null);
  }, []);

  const normalize = useCallback(() => {
    setHoldings((prev) => {
      const sum = prev.reduce((a, h) => a + h.weight, 0);
      if (sum <= 0) return prev;
      return prev.map((h) => ({
        ...h,
        weight: Math.round((h.weight / sum) * 1000) / 10,
      }));
    });
  }, []);

  const value = useMemo(
    () => ({
      holdings,
      sampleId,
      hydrated,
      setWeight,
      addTicker,
      removeTicker,
      loadSample,
      clear,
      normalize,
    }),
    [
      holdings,
      sampleId,
      hydrated,
      setWeight,
      addTicker,
      removeTicker,
      loadSample,
      clear,
      normalize,
    ],
  );

  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function usePortfolio() {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error("usePortfolio outside provider");
  return ctx;
}

export function useAudit() {
  const { holdings } = usePortfolio();
  return useMemo(() => auditPortfolio(holdings), [holdings]);
}

export function useSuggestions() {
  const { holdings } = usePortfolio();
  return useMemo(() => suggestHedge(holdings), [holdings]);
}
