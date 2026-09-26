"use client";

import Link from "next/link";
import { RowBar, SignedBar, StackedBar } from "../../components/bars";
import { NARRATIVES, PHILOSOPHIES, POLICY_AXES } from "../../lib/catalog";
import { COMPANY_BY_TICKER } from "../../lib/companies";
import { useAudit, usePortfolio, useSuggestions } from "../../lib/store";
import type { PolicyAxisId } from "../../lib/types";

const POLICY_ORDER: PolicyAxisId[] = [
  "climate",
  "defense",
  "trade",
  "techReg",
  "china",
  "rates",
];

export default function MapPage() {
  const { holdings, hydrated, addTicker } = usePortfolio();
  const audit = useAudit();
  const suggestions = useSuggestions();

  if (!hydrated) {
    return <main className="mx-auto max-w-6xl px-5 py-16 text-muted">Drawing the map…</main>;
  }

  if (!audit) {
    return (
      <main className="mx-auto max-w-3xl px-5 py-20">
        <p className="kicker">The map</p>
        <h1 className="serif mt-2 text-4xl">Nothing to map yet</h1>
        <p className="mt-3 text-muted">Load a sample or add holdings first.</p>
        <Link href="/portfolio" className="mt-6 inline-block text-brass">
          Open the book →
        </Link>
      </main>
    );
  }

  const animalColor = audit.animal === "fox" ? "var(--fox)" : "var(--hedge)";

  return (
    <main className="mx-auto max-w-6xl px-5 py-12">
      <p className="kicker">The map</p>
      <h1 className="serif mt-2 text-4xl text-ink">Where the weight actually sits</h1>
      <p className="mt-3 max-w-2xl text-muted">
        Sector charts are the surface. Stories, philosophies, and policy axes are
        the terrain. {holdings.length} names in the book.
      </p>

      <section className="mt-10 grid gap-4 md:grid-cols-4">
        <Stat
          label="Animal"
          value={audit.animal}
          hint={
            audit.animal === "fox"
              ? "More than one book of the world"
              : audit.animal === "hedgehog"
                ? "One organizing sermon"
                : "Still choosing a nature"
          }
          color={animalColor}
        />
        <Stat
          label="False diversification"
          value={`${Math.round(audit.falseDiversification)}`}
          hint={`${audit.holdingCount} tickers · ${audit.effectiveFamilies.toFixed(1)} story families`}
        />
        <Stat
          label="Hedgehog"
          value={`${Math.round(audit.hedgehogScore)}`}
          hint="Story concentration"
        />
        <Stat
          label="Policy amplitude"
          value={`${Math.round(audit.policyAmplitude * 100)}`}
          hint="How loud the political surface is"
        />
      </section>

      <section className="mt-10 grid gap-8 lg:grid-cols-2">
        <div className="rounded-2xl border border-line bg-raised/60 p-6">
          <p className="kicker">Narratives</p>
          <h2 className="serif mt-2 text-2xl">The sermons</h2>
          <div className="mt-4">
            <StackedBar slices={audit.familySlices} height={18} />
          </div>
          <p className="mt-2 text-xs text-muted">
            Costumes below. The family of sermons above. Several tickers can
            still be one family.
          </p>
          <div className="mt-5 space-y-3">
            {audit.narrativeSlices.slice(0, 7).map((s) => (
              <RowBar
                key={s.id}
                label={s.name}
                value={s.weight}
                color={s.color}
                hint={NARRATIVES[s.id as keyof typeof NARRATIVES]?.blurb}
              />
            ))}
          </div>
        </div>

        <div className="rounded-2xl border border-line bg-raised/60 p-6">
          <p className="kicker">Philosophies</p>
          <h2 className="serif mt-2 text-2xl">The books behind the book</h2>
          <div className="mt-4 grid gap-3 sm:grid-cols-2">
            {audit.philosophySlices.map((s) => (
              <div key={s.id} className="rounded-xl border border-line bg-sunken/40 p-3">
                <div className="flex items-baseline justify-between">
                  <span className="text-sm text-ink">{s.name}</span>
                  <span className="font-mono text-xs text-muted">
                    {Math.round(s.weight * 100)}%
                  </span>
                </div>
                <p className="mt-1 text-xs leading-relaxed text-faint">
                  {PHILOSOPHIES[s.id as keyof typeof PHILOSOPHIES]?.blurb}
                </p>
              </div>
            ))}
          </div>
          <div className="mt-6">
            <p className="text-xs uppercase tracking-wider text-faint">Sectors, for contrast</p>
            <div className="mt-2">
              <StackedBar
                slices={audit.sectorSlices.map((s, i) => ({
                  ...s,
                  color: ["#8a8278", "#6b8cae", "#7a9e7e", "#c4a574", "#d4784a", "#9a8ab0"][i % 6],
                }))}
              />
            </div>
            <p className="mt-2 text-xs text-muted">
              Effective sectors {audit.effectiveSectors.toFixed(1)} vs story
              families {audit.effectiveFamilies.toFixed(1)}. If the family count
              is the small number, the ticker list is a costume.
            </p>
          </div>
        </div>
      </section>

      <section className="mt-8 rounded-2xl border border-line bg-raised/60 p-6">
        <p className="kicker">Policy surface</p>
        <h2 className="serif mt-2 text-2xl">Not a team jersey. A grocery list.</h2>
        <p className="mt-2 max-w-3xl text-sm text-muted">
          Each axis is a simplified exposure: who eats if this regime arrives.
          Zero is mute. Large numbers mean your cash flows are already on a
          coalition's list.
        </p>
        <div className="mt-6 grid gap-6 md:grid-cols-2">
          {POLICY_ORDER.map((axis) => (
            <SignedBar
              key={axis}
              label={POLICY_AXES[axis].name}
              value={audit.policy[axis]}
              plus={POLICY_AXES[axis].plus}
              minus={POLICY_AXES[axis].minus}
            />
          ))}
        </div>
        <div className="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {audit.regimeSensitivities.map((r) => (
            <div key={r.id} className="rounded-xl border border-line bg-sunken/50 p-4">
              <p className="text-sm text-ink">{r.name}</p>
              <p
                className="mt-1 font-mono text-2xl"
                style={{ color: r.score >= 0 ? "var(--brass)" : "var(--fox)" }}
              >
                {r.score >= 0 ? "+" : ""}
                {Math.round(r.score * 100)}
              </p>
              <p className="mt-2 text-xs leading-relaxed text-faint">{r.note}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="mt-8 grid gap-8 lg:grid-cols-2">
        <div className="rounded-2xl border border-line bg-raised/60 p-6">
          <p className="kicker">Buffett snapshot</p>
          <h2 className="serif mt-2 text-2xl">Quality is not a map</h2>
          <div className="mt-4 space-y-3">
            <RowBar label="Moat" value={audit.buffett.moat / 5} color="var(--hedge)" />
            <RowBar label="Understandability" value={audit.buffett.understandability / 5} />
            <RowBar label="Business quality" value={audit.buffett.quality / 5} color="var(--brass)" />
          </div>
          <p className="mt-4 text-sm leading-relaxed text-muted">
            High quality can still be one story. Omaha concentration in brands and
            tolls is a choice. Consensus concentration in a single technological
            sermon is a mood.
          </p>
        </div>
        <div className="rounded-2xl border border-line bg-raised/60 p-6">
          <p className="kicker">Missing stories</p>
          <h2 className="serif mt-2 text-2xl">A second book, if you want one</h2>
          <p className="mt-2 text-sm text-muted">
            Not recommendations. Names whose implicit worlds disagree with what
            you already own.
          </p>
          <ul className="mt-4 space-y-2">
            {suggestions.map((c) => (
              <li
                key={c.ticker}
                className="flex items-start justify-between gap-3 rounded-xl border border-line px-3 py-2"
              >
                <div>
                  <p className="text-sm text-ink">
                    <span className="font-mono text-brass">{c.ticker}</span> {c.name}
                  </p>
                  <p className="text-xs text-muted">{c.damodaran.story}</p>
                </div>
                <button
                  type="button"
                  onClick={() => addTicker(c.ticker)}
                  className="text-xs text-brass hover:text-ink"
                >
                  Add
                </button>
              </li>
            ))}
          </ul>
          <p className="mt-4 text-xs text-faint">
            Underweight:{" "}
            {audit.missingNarratives
              .map((id) => NARRATIVES[id].name)
              .join(" · ") || "nothing obvious"}
          </p>
        </div>
      </section>

      <p className="mt-10 text-sm text-muted">
        Then read it as prose.{" "}
        <Link href="/audit" className="text-brass">
          The letter →
        </Link>
      </p>
      <p className="mt-2 text-xs text-faint">
        {holdings
          .map((h) => `${h.ticker} ${COMPANY_BY_TICKER[h.ticker]?.name ?? ""}`)
          .join(" · ")}
      </p>
    </main>
  );
}

function Stat({
  label,
  value,
  hint,
  color,
}: {
  label: string;
  value: string;
  hint: string;
  color?: string;
}) {
  return (
    <div className="rounded-2xl border border-line bg-raised/60 p-4">
      <p className="text-[0.68rem] uppercase tracking-[0.16em] text-faint">{label}</p>
      <p className="serif mt-1 text-3xl capitalize" style={{ color: color ?? "var(--ink)" }}>
        {value}
      </p>
      <p className="mt-1 text-xs text-muted">{hint}</p>
    </div>
  );
}
