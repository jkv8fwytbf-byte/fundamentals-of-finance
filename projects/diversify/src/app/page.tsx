import Link from "next/link";
import { SampleGrid } from "../components/sample-grid";

export default function HomePage() {
  return (
    <main>
      <section className="mx-auto max-w-6xl px-5 pb-8 pt-16 sm:pt-24">
        <p className="kicker">A thinking tool, not a trading desk</p>
        <h1 className="serif mt-4 max-w-4xl text-4xl leading-[1.12] tracking-tight text-ink sm:text-6xl">
          Your tickers can be different.
          <span className="italic text-brass"> Your story is usually the same.</span>
        </h1>
        <p className="mt-6 max-w-2xl text-lg leading-relaxed text-muted">
          Diversify is a long-horizon book of the world: Damodaran on stories and
          numbers, Buffett on owning businesses, and the political science of how
          partisans quietly cluster what they are willing to believe.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Link
            href="/portfolio"
            className="rounded-full bg-ink px-5 py-2.5 text-sm text-paper hover:bg-brass"
          >
            Open the book
          </Link>
          <Link
            href="/audit"
            className="rounded-full border border-line px-5 py-2.5 text-sm text-muted hover:text-ink"
          >
            Read the letter
          </Link>
        </div>
      </section>

      <div className="hairline my-6" />

      <section className="mx-auto grid max-w-6xl gap-10 px-5 py-12 lg:grid-cols-3">
        <Teacher
          kicker="Damodaran"
          title="Every number already has a story."
          body="If eight holdings require the same growth narrative to be true, you do not have eight investments. You have a congregation. Valuation is the discipline of asking whether the numbers can carry the sermon."
        />
        <Teacher
          kicker="Buffett"
          title="Concentration in quality is not the sin."
          body="Owning wonderful businesses for a long time is the point. The sin is concentration in an assumption — one regime, one rate path, one tribe's map of the future — while calling the ticker list diversified."
        />
        <Teacher
          kicker="The partisan"
          title="Identities stack. So do stocks."
          body="Haidt, Mason, Chua: people do not hold independent beliefs. They hold bundles. Portfolios do the same. Climate, defense, China, antitrust, easy money — your cash flows already belong to someone's grocery list."
        />
      </section>

      <section className="mx-auto max-w-6xl px-5 py-8">
        <div className="rounded-3xl border border-line bg-raised/70 p-8 sm:p-10">
          <p className="kicker">Berlin, 1953</p>
          <h2 className="serif mt-3 max-w-3xl text-3xl leading-snug text-ink sm:text-4xl">
            The hedgehog knows one big thing. The fox knows many.
          </h2>
          <p className="mt-4 max-w-3xl leading-relaxed text-muted">
            Most modern books of stocks are hedgehogs in fox clothing: a dozen
            technology names that all need cheap money, American exceptionalism,
            light-touch regulation, and the same five customers. This tool does
            not tell you what to buy tomorrow. It asks whether you are running
            one worldview and calling it a portfolio.
          </p>
          <ul className="mt-6 grid gap-3 text-sm text-muted sm:grid-cols-2">
            <li className="rounded-xl border border-line bg-sunken/50 px-4 py-3">
              Not day trading. No candles, no leverage, no tips.
            </li>
            <li className="rounded-xl border border-line bg-sunken/50 px-4 py-3">
              Not a left/right scoreboard. Regimes, not team jerseys.
            </li>
            <li className="rounded-xl border border-line bg-sunken/50 px-4 py-3">
              False diversification: many tickers, few stories.
            </li>
            <li className="rounded-xl border border-line bg-sunken/50 px-4 py-3">
              A library that argues with whatever you are overweight.
            </li>
          </ul>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-5 py-16">
        <p className="kicker">Try a famous shape</p>
        <h2 className="serif mt-2 text-3xl text-ink">Six books of the world</h2>
        <p className="mt-3 mb-8 max-w-2xl text-muted">
          Load one, then read the map and the letter. The Consensus is the usual
          trap: it looks like seven businesses. It is mostly one sermon.
        </p>
        <SampleGrid />
      </section>

      <footer className="border-t border-line px-5 py-10 text-center text-xs leading-relaxed text-faint">
        A thinking aid, not financial advice, not a political forecast.
        Company tags are simplified research labels, not truth.
        Damodaran and Buffett would want you to do the work yourself.
      </footer>
    </main>
  );
}

function Teacher({
  kicker,
  title,
  body,
}: {
  kicker: string;
  title: string;
  body: string;
}) {
  return (
    <article>
      <p className="kicker">{kicker}</p>
      <h2 className="serif mt-2 text-2xl leading-snug text-ink">{title}</h2>
      <p className="mt-3 text-sm leading-relaxed text-muted">{body}</p>
    </article>
  );
}
