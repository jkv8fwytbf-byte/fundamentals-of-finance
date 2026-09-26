"use client";

import Link from "next/link";
import { useAudit, usePortfolio } from "../../lib/store";

export default function AuditPage() {
  const { hydrated, sampleId } = usePortfolio();
  const audit = useAudit();

  if (!hydrated) {
    return <main className="mx-auto max-w-3xl px-5 py-16 text-muted">Writing…</main>;
  }

  if (!audit) {
    return (
      <main className="mx-auto max-w-3xl px-5 py-20">
        <p className="kicker">The letter</p>
        <h1 className="serif mt-2 text-4xl">No book, no letter</h1>
        <Link href="/portfolio" className="mt-6 inline-block text-brass">
          Open the book →
        </Link>
      </main>
    );
  }

  return (
    <main className="mx-auto max-w-3xl px-5 py-16">
      <p className="kicker">{audit.letter.kicker}</p>
      <h1 className="serif mt-3 text-4xl leading-tight text-ink sm:text-5xl">
        {audit.letter.headline}
      </h1>
      <p className="mt-4 text-sm text-faint">
        An audit in the spirit of a shareholder letter, not a push notification.
        {sampleId ? " You are looking at a sample book." : ""}
      </p>

      <div className="mt-8 grid grid-cols-3 gap-3 border-y border-line py-4 text-center">
        <Metric n={audit.holdingCount.toString()} l="names" />
        <Metric n={audit.effectiveFamilies.toFixed(1)} l="families" />
        <Metric n={Math.round(audit.falseDiversification).toString()} l="false div." />
      </div>

      <article className="mt-10 space-y-6">
        {audit.letter.paragraphs.map((p) => (
          <p key={p.slice(0, 40)} className="serif text-lg leading-[1.7] text-ink/95">
            {p}
          </p>
        ))}
      </article>

      <aside className="mt-12 rounded-2xl border border-line bg-raised/50 p-6">
        <p className="kicker">Damodaran, in one line</p>
        <p className="mt-3 text-sm leading-relaxed text-muted">
          A company should not mix incompatible stories. A life can. If this
          letter stings, the usual error is not that you own too little. It is
          that you own one idea in several costumes.
        </p>
        <div className="mt-5 flex flex-wrap gap-3 text-sm">
          <Link href="/map" className="text-brass">
            Back to the map
          </Link>
          <Link href="/library" className="text-muted hover:text-ink">
            Books that argue with you
          </Link>
        </div>
      </aside>
    </main>
  );
}

function Metric({ n, l }: { n: string; l: string }) {
  return (
    <div>
      <div className="serif text-2xl text-ink">{n}</div>
      <div className="text-[0.68rem] uppercase tracking-[0.16em] text-faint">{l}</div>
    </div>
  );
}
