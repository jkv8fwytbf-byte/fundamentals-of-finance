"use client";

import Link from "next/link";
import { SAMPLES } from "../lib/library";
import { usePortfolio } from "../lib/store";

export function SampleGrid({
  actionLabel = "Open this book",
}: {
  actionLabel?: string;
}) {
  const { loadSample, sampleId } = usePortfolio();
  return (
    <div className="grid gap-4 md:grid-cols-2">
      {SAMPLES.map((sample) => {
        const active = sampleId === sample.id;
        return (
          <article
            key={sample.id}
            className={`rounded-2xl border p-5 transition-colors ${
              active ? "border-brass/50 bg-raised" : "border-line bg-raised/60"
            }`}
          >
            <p className="kicker">{sample.epithet}</p>
            <h3 className="serif mt-2 text-2xl text-ink">{sample.name}</h3>
            <p className="mt-2 text-sm leading-relaxed text-muted">{sample.thesis}</p>
            <p className="mt-3 font-mono text-[0.7rem] tracking-wide text-faint">
              {sample.holdings.map((h) => h.ticker).join(" · ")}
            </p>
            <div className="mt-4 flex gap-2">
              <button
                type="button"
                onClick={() => loadSample(sample.id)}
                className="rounded-full bg-ink px-3.5 py-1.5 text-sm text-paper hover:bg-brass hover:text-paper"
              >
                {active ? "Loaded" : actionLabel}
              </button>
              <Link
                href="/map"
                onClick={() => loadSample(sample.id)}
                className="rounded-full border border-line px-3.5 py-1.5 text-sm text-muted hover:text-ink"
              >
                See the map
              </Link>
            </div>
          </article>
        );
      })}
    </div>
  );
}
