"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const LINKS = [
  { href: "/", label: "Thesis" },
  { href: "/portfolio", label: "Book" },
  { href: "/map", label: "Map" },
  { href: "/audit", label: "Letter" },
  { href: "/library", label: "Library" },
];

export function Nav() {
  const path = usePathname();
  return (
    <header className="sticky top-0 z-40 border-b border-line/80 bg-paper/80 backdrop-blur-md">
      <div className="mx-auto flex max-w-6xl items-center justify-between gap-6 px-5 py-3.5">
        <Link href="/" className="flex items-baseline gap-2">
          <span className="serif text-xl tracking-tight text-ink">Diversify</span>
          <span className="hidden text-[0.65rem] uppercase tracking-[0.22em] text-faint sm:inline">
            not a trading desk
          </span>
        </Link>
        <nav className="flex items-center gap-1 sm:gap-2">
          {LINKS.map((link) => {
            const active =
              link.href === "/" ? path === "/" : path.startsWith(link.href);
            return (
              <Link
                key={link.href}
                href={link.href}
                className={`rounded-full px-2.5 py-1 text-sm transition-colors sm:px-3 ${
                  active
                    ? "bg-raised text-brass"
                    : "text-muted hover:text-ink"
                }`}
              >
                {link.label}
              </Link>
            );
          })}
        </nav>
      </div>
    </header>
  );
}
