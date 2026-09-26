# Diversify

A small website that treats a list of companies as a set of stories rather than a set of tickers. It follows Damodaran on stories and numbers, Buffett on owning businesses for a long time, and borrows from political science the idea that beliefs come in bundles. The home page calls it "a thinking tool, not a trading desk". It gives no advice and knows no prices.

You load or type a list of companies with weights. The site then shows which narratives, philosophies and policy bets the list leans on. It writes a short letter about the list and suggests books that argue with it.

## Words you will see

- Next.js: a framework, that is, a ready-made structure, for building websites with React and TypeScript. React draws the screen from small reusable pieces; TypeScript is JavaScript with types added.
- Page: in Next.js, one screen of the site. Each folder under `src/app/` that contains a `page.tsx` file is one address, so `src/app/map/page.tsx` is `/map`.
- Component: a reusable piece of screen, such as the top navigation bar, written once and used on several pages.
- `npm run dev`: the command that starts the site on your own machine in development mode, where it reloads as you edit. npm is the package manager that comes with Node.js.
- `node_modules`: the folder where npm downloads the libraries the site depends on. It is large, rebuilt by `npm install`, and never committed.

## What is in this folder

`src/app/` contains the five pages, in the order the navigation bar shows them:

- `page.tsx`: the home page, labelled Thesis. Three short teachers (Damodaran, Buffett, "the partisan"), the hedgehog and the fox, and six sample lists to load.
- `portfolio/page.tsx`: labelled Book. Search the company list, add names, set weights, and press "Normalize" to turn them into percentages.
- `map/page.tsx`: labelled Map. Where the weight sits: narratives, philosophies and six policy axes, named on screen "Climate regime", "Defense spend", "Open trade", "Light-touch tech", "China engagement" and "Easy money", and whether the list is a fox or a hedgehog.
- `audit/page.tsx`: labelled Letter. An audit written like a shareholder letter, with three numbers: names, effective families, and a false-diversification score.
- `library/page.tsx`: labelled Library. Twenty books; the featured ones are chosen against whatever the list is overweight in.

`src/lib/` contains the data and the arithmetic:

- `companies.ts`: 39 companies, from NVDA to NFLX. Each carries its narratives with weights, its philosophies, its exposure on the six policy axes, a Buffett block (moat, understandability, quality, a note) and a Damodaran block (story, risk).
- `catalog.ts`: the 13 narratives, 8 philosophies and 6 policy axes, with names, colours and one-line blurbs.
- `library.ts`: the 20 books and the six sample lists: The Consensus, The Hydrocarbon, The Omaha Letter, The Fortress, The Timetable and A Fox.
- `scoring.ts`: `auditPortfolio`, which turns a list into the map and the letter using a concentration index, and `suggestHedge`, which proposes names that pull the other way.
- `store.tsx`: keeps your list in the browser's local storage under the key `diversify.holdings.v1`. Nothing is sent anywhere.
- `types.ts`: the TypeScript shapes for companies, list entries, books and the audit.

`src/components/` contains `nav.tsx` (the top bar), `bars.tsx` (stacked and signed bars for the map), `sample-grid.tsx` (the six sample cards) and `providers.tsx` (wires the store into every page). `src/app/layout.tsx` sets the fonts and wraps every page; `globals.css` is the styling, built with Tailwind CSS (a library of ready-made styling classes).

The top level has the usual Next.js configuration: `package.json` (dependencies and scripts), `package-lock.json`, `next.config.ts`, `tsconfig.json`, `postcss.config.mjs`, `eslint.config.mjs`, `public/` (a few SVG icons, a text-based image format, from the scaffold) and `.gitignore`. `AGENTS.md` and `CLAUDE.md` are a short note that `next dev` writes for AI coding tools; `CLAUDE.md` only points at `AGENTS.md`.

Versions: Next.js 16.3.5, React 19.2.8, Tailwind CSS 4, TypeScript 5.

## How to run it

You need Node.js installed. Then, in this folder:

```
npm install
npm run dev
```

Open http://localhost:3000 in your browser. `localhost` means your own machine; 3000 is the port Next.js uses by default. Load a sample list on the home page, then open Map and Letter.

## Status

- Two commits. A commit is one saved version of the folder with a message. The first, 77be89c on 17 September 2026, is the empty scaffold from create-next-app. The second, 7053ec2 on 26 September 2026, adds the pages, components and data.
- The pages were written on 17 September and sat uncommitted until 26 September, when they were saved so the project could come into this repository.
- Never deployed. It has only ever run on this Mac.
- The footer says the company tags are simplified research labels, not truth. Treat every number on the map the same way.

## Not in git

Git is the program that keeps this repository's history. `node_modules/` and `.next/` (the build cache) are listed in `.gitignore`, the file that tells git which files to leave out. `npm install` recreates the first and `npm run dev` the second. Any `.env` file is ignored too; this project does not need one.
