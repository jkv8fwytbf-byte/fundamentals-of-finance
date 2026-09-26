"use client";

import Link from "next/link";
import { BOOKS } from "../../lib/library";
import { NARRATIVES, PHILOSOPHIES } from "../../lib/catalog";
import { useAudit } from "../../lib/store";

export default function LibraryPage() {
  const audit = useAudit();
  const challenged = new Set(audit?.challengeBookIds ?? []);
  const featured = BOOKS.filter((b) => challenged.has(b.id));
  const rest = BOOKS.filter((b) => !challenged.has(b.id));

  return (
    <main className="mx-auto max-w-6xl px-5 py-12">
      <p className="kicker">The library</p>
      <h1 className="serif mt-2 text-4xl text-ink">Books that argue with the book</h1>
      <p className="mt-3 max-w-2xl text-muted">
        Philosophy here is not décor. If a portfolio is a set of beliefs with
        tickers attached, the reading list should attack those beliefs. Featured
        titles are chosen from whatever you are currently overweight.
      </p>

      {featured.length > 0 ? (
        <section className="mt-10">
          <p className="kicker">Against your present sermon</p>
          <div className="mt-4 grid gap-4 md:grid-cols-2">
            {featured.map((book) => (
              <BookCard key={book.id} book={book} featured />
            ))}
          </div>
        </section>
      ) : (
        <p className="mt-8 text-sm text-muted">
          Load a book of holdings to get a combative reading list.{" "}
          <Link href="/portfolio" className="text-brass">
            Open the book →
          </Link>
        </p>
      )}

      <section className="mt-14">
        <p className="kicker">The shelf</p>
        <div className="mt-4 grid gap-4 md:grid-cols-2">
          {rest.map((book) => (
            <BookCard key={book.id} book={book} />
          ))}
        </div>
      </section>
    </main>
  );
}

function BookCard({
  book,
  featured = false,
}: {
  book: (typeof BOOKS)[number];
  featured?: boolean;
}) {
  return (
    <article
      className={`rounded-2xl border p-5 ${
        featured ? "border-brass/40 bg-raised" : "border-line bg-raised/50"
      }`}
    >
      <p className="font-mono text-[0.7rem] text-faint">{book.year}</p>
      <h2 className="serif mt-1 text-2xl leading-snug text-ink">{book.title}</h2>
      <p className="mt-1 text-sm text-brass">{book.author}</p>
      <p className="mt-3 text-sm leading-relaxed text-muted">{book.why}</p>
      <p className="mt-3 text-[0.7rem] uppercase tracking-wider text-faint">
        Argues with{" "}
        {book.challenges.map((id) => PHILOSOPHIES[id].name).join(" · ")}
      </p>
      <p className="mt-1 text-[0.7rem] text-faint">
        If heavy in {book.ifYouAreHeavyIn.map((id) => NARRATIVES[id].name).join(", ")}
      </p>
    </article>
  );
}
