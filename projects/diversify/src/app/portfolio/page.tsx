"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { COMPANIES, COMPANY_BY_TICKER } from "../../lib/companies";
import { NARRATIVES } from "../../lib/catalog";
import { SampleGrid } from "../../components/sample-grid";
import { usePortfolio } from "../../lib/store";

export default function PortfolioPage() {
  const {
    holdings,
    addTicker,
    removeTicker,
    setWeight,
    clear,
    normalize,
    hydrated,
  } = usePortfolio();
  const [query, setQuery] = useState("");
  const owned = useMemo(() => new Set(holdings.map((h) => h.ticker)), [holdings]);
  const total = holdings.reduce((a, h) => a + h.weight, 0);

  const matches = useMemo(() => {
    const q = query.trim().toLowerCase();
    return COMPANIES.filter((c) => {
      if (owned.has(c.ticker)) return false;
      if (!q) return true;
      return (
        c.ticker.toLowerCase().includes(q) ||
        c.name.toLowerCase().includes(q) ||
        c.sector.toLowerCase().includes(q) ||
        c.summary.toLowerCase().includes(q)
      );
    }).slice(0, 8);
  }, [query, owned]);

  if (!hydrated) {
    return <main className="mx-auto max-w-6xl px-5 py-16 text-muted">Opening the book…</main>;
  }

  return (
    <main className="mx-auto max-w-6xl px-5 py-12">
      <p className="kicker">The book</p>
      <h1 className="serif mt-2 text-4xl text-ink">Holdings as a worldview</h1>
      <p className="mt-3 max-w-2xl text-muted">
        Weights are shares of your attention, not a brokerage sync. Normalize to
        100 when you want percentages. Then go to the map.
      </p>

      <div className="mt-8 grid gap-8 lg:grid-cols-[1.15fr_0.85fr]">
        <section className="space-y-3">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <p className="text-sm text-muted">
              {holdings.length} names · weight {total.toFixed(1)}
            </p>
            <div className="flex gap-2">
              <button
                type="button"
                onClick={normalize}
                className="rounded-full border border-line px-3 py-1 text-xs text-muted hover:text-ink"
              >
                Normalize to 100
              </button>
              <button
                type="button"
                onClick={clear}
                className="rounded-full border border-line px-3 py-1 text-xs text-muted hover:text-danger"
              >
                Clear
              </button>
            </div>
          </div>

          {holdings.length === 0 ? (
            <div className="rounded-2xl border border-dashed border-line p-8 text-sm text-muted">
              Empty book. Add names from the universe, or load a sample on the right.
            </div>
          ) : (
            <ul className="space-y-2">
              {holdings.map((h) => {
                const c = COMPANY_BY_TICKER[h.ticker];
                if (!c) return null;
                const lead = c.narratives[0];
                return (
                  <li
                    key={h.ticker}
                    className="rounded-2xl border border-line bg-raised/70 p-4"
                  >
                    <div className="flex items-start justify-between gap-3">
                      <div>
                        <div className="flex items-baseline gap-2">
                          <span className="font-mono text-sm text-brass">{c.ticker}</span>
                          <span className="text-ink">{c.name}</span>
                        </div>
                        <p className="mt-1 text-sm text-muted">{c.summary}</p>
                        <p className="mt-2 text-[0.7rem] uppercase tracking-wider text-faint">
                          {c.sector} · {c.geography}
                          {lead ? ` · ${NARRATIVES[lead.id].name}` : ""}
                        </p>
                      </div>
                      <button
                        type="button"
                        onClick={() => removeTicker(h.ticker)}
                        className="text-xs text-faint hover:text-danger"
                      >
                        Remove
                      </button>
                    </div>
                    <div className="mt-3 flex items-center gap-3">
                      <input
                        type="range"
                        min={0}
                        max={40}
                        step={0.5}
                        value={Math.min(h.weight, 40)}
                        onChange={(e) => setWeight(h.ticker, Number(e.target.value))}
                        className="w-full accent-brass"
                      />
                      <input
                        type="number"
                        min={0}
                        step={0.5}
                        value={h.weight}
                        onChange={(e) => setWeight(h.ticker, Number(e.target.value))}
                        className="w-20 rounded-lg border border-line bg-sunken px-2 py-1 font-mono text-sm text-ink"
                      />
                    </div>
                    <p className="mt-2 text-xs italic text-faint">
                      Buffett: {c.buffett.note}
                    </p>
                  </li>
                );
              })}
            </ul>
          )}

          <div className="pt-4">
            <label className="kicker" htmlFor="search">
              Add from the universe
            </label>
            <input
              id="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Ticker, name, sector…"
              className="mt-2 w-full rounded-xl border border-line bg-sunken px-3 py-2 text-sm text-ink outline-none placeholder:text-faint focus:border-brass/50"
            />
            <ul className="mt-2 divide-y divide-line overflow-hidden rounded-xl border border-line">
              {matches.map((c) => (
                <li key={c.ticker}>
                  <button
                    type="button"
                    onClick={() => {
                      addTicker(c.ticker);
                      setQuery("");
                    }}
                    className="flex w-full items-start justify-between gap-3 px-3 py-2.5 text-left hover:bg-raised"
                  >
                    <span>
                      <span className="font-mono text-xs text-brass">{c.ticker}</span>
                      <span className="ml-2 text-sm text-ink">{c.name}</span>
                      <span className="mt-0.5 block text-xs text-muted">{c.summary}</span>
                    </span>
                    <span className="text-xs text-faint">{c.sector}</span>
                  </button>
                </li>
              ))}
            </ul>
          </div>
        </section>

        <aside className="space-y-6">
          <div className="rounded-2xl border border-line bg-raised/60 p-5">
            <p className="kicker">Next</p>
            <p className="serif mt-2 text-2xl text-ink">The map and the letter</p>
            <p className="mt-2 text-sm text-muted">
              After the names are in, look at stories, policy, and the written audit.
            </p>
            <div className="mt-4 flex flex-wrap gap-2">
              <Link
                href="/map"
                className="rounded-full bg-ink px-3.5 py-1.5 text-sm text-paper hover:bg-brass"
              >
                Open the map
              </Link>
              <Link
                href="/audit"
                className="rounded-full border border-line px-3.5 py-1.5 text-sm text-muted hover:text-ink"
              >
                Read the letter
              </Link>
            </div>
          </div>
          <div>
            <p className="kicker mb-3">Samples</p>
            <SampleGrid actionLabel="Load" />
          </div>
        </aside>
      </div>
    </main>
  );
}
