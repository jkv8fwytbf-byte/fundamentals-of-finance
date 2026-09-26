import type { NarrativeId, PhilosophyId, PolicyAxisId } from "./types";

export const NARRATIVES: Record<
  NarrativeId,
  { name: string; color: string; blurb: string }
> = {
  "ai-platform": {
    name: "AI platform",
    color: "#c4a574",
    blurb: "A handful of firms capture intelligence as infrastructure.",
  },
  "energy-transition": {
    name: "Energy transition",
    color: "#7a9e7e",
    blurb: "Policy and capital force the world off hydrocarbons on a timetable.",
  },
  "fossil-endurance": {
    name: "Fossil endurance",
    color: "#8a6a4a",
    blurb: "Oil and gas remain the swing fuel for longer than the slide decks say.",
  },
  "us-exceptionalism": {
    name: "US exceptionalism",
    color: "#6b8cae",
    blurb: "American institutions, capital markets, and brands keep compounding.",
  },
  "china-coupling": {
    name: "China coupling",
    color: "#b85c5c",
    blurb: "Access to Chinese demand or manufacturing stays open enough to matter.",
  },
  reindustrialization: {
    name: "Reindustrialization",
    color: "#d4784a",
    blurb: "Factories, machines, and domestic capacity are the new scarce assets.",
  },
  "consumer-brand": {
    name: "Consumer brand",
    color: "#c48a9a",
    blurb: "Taste, habit, and trust still mint cash through cycles.",
  },
  "healthcare-aging": {
    name: "Aging & care",
    color: "#7a9eae",
    blurb: "Demography, not elections, drives drug and insurance cash flows.",
  },
  "defense-multipolar": {
    name: "Multipolar defense",
    color: "#6a7a5a",
    blurb: "A world of several powers pays a standing tax to its arsenals.",
  },
  "payments-rails": {
    name: "Payments rails",
    color: "#a09070",
    blurb: "Tollbooths on money movement, with network effects as the moat.",
  },
  "commodity-cycle": {
    name: "Commodity cycle",
    color: "#b89858",
    blurb: "The physical world reasserts itself: copper, gold, bulk, scarcity.",
  },
  "software-subscription": {
    name: "Software rent",
    color: "#8a9cb8",
    blurb: "Recurring code, switching costs, and operating leverage.",
  },
  "cheap-money-duration": {
    name: "Cheap-money duration",
    color: "#9a8ab0",
    blurb: "Long-dated cash flows that only look cheap when rates are friendly.",
  },
};

export const PHILOSOPHIES: Record<
  PhilosophyId,
  { name: string; color: string; blurb: string }
> = {
  "tech-optimism": {
    name: "Tech optimism",
    color: "#c4a574",
    blurb: "Intelligence, networks, and code are the binding constraint. Scale wins.",
  },
  "hard-assets": {
    name: "Hard assets",
    color: "#b89858",
    blurb: "The physical world is not a rounding error. Stuff, energy, metal, land.",
  },
  "american-fortress": {
    name: "American fortress",
    color: "#6b8cae",
    blurb: "Power, production, and security concentrate inside a hardened US.",
  },
  "global-consumer": {
    name: "Global consumer",
    color: "#c48a9a",
    blurb: "A middle class somewhere still wants brands, calories, and convenience.",
  },
  "moat-compounder": {
    name: "Moat compounder",
    color: "#7a9e7e",
    blurb: "Buy wonderful businesses. Time is the friend of the wonderful business.",
  },
  "industrial-policy": {
    name: "Industrial policy",
    color: "#d4784a",
    blurb: "States pick sectors. Subsidies, tariffs, and procurement write returns.",
  },
  abundance: {
    name: "Abundance",
    color: "#7a9eae",
    blurb: "The bottleneck is permission and building, not demand or ideas.",
  },
  financialization: {
    name: "Financialization",
    color: "#a09070",
    blurb: "The rake on capital and payments is a more durable business than making.",
  },
};

export const POLICY_AXES: Record<
  PolicyAxisId,
  { name: string; plus: string; minus: string }
> = {
  climate: {
    name: "Climate regime",
    plus: "Accelerated transition, carbon price, green industrial policy",
    minus: "Status-quo hydrocarbons, slower mandates, cheaper gasoline politics",
  },
  defense: {
    name: "Defense spend",
    plus: "Higher budgets, hot peace, multipolar arms race",
    minus: "Drawdown, isolation, procurement freeze",
  },
  trade: {
    name: "Open trade",
    plus: "Globalization, cheap imports, integrated supply chains",
    minus: "Tariffs, friend-shoring, bloc economics",
  },
  techReg: {
    name: "Light-touch tech",
    plus: "Weak antitrust, loose AI and privacy rules",
    minus: "Breakups, app-store laws, model liability, data limits",
  },
  china: {
    name: "China engagement",
    plus: "Market access, manufacturing, capital links stay open",
    minus: "Decoupling, export controls, consumer boycotts",
  },
  rates: {
    name: "Easy money",
    plus: "Lower rates, abundant duration, high multiples",
    minus: "Restrictive policy, value over growth, banks over dreams",
  },
};

export const NARRATIVE_FAMILIES: Record<
  string,
  { name: string; members: NarrativeId[] }
> = {
  intelligence: {
    name: "Intelligence & duration",
    members: ["ai-platform", "software-subscription", "cheap-money-duration"],
  },
  "american-brand": {
    name: "American brands & tolls",
    members: ["us-exceptionalism", "consumer-brand", "payments-rails"],
  },
  hydrocarbon: {
    name: "Hydrocarbons",
    members: ["fossil-endurance"],
  },
  transition: {
    name: "Transition timetable",
    members: ["energy-transition"],
  },
  "hard-power": {
    name: "Hard power & factories",
    members: ["defense-multipolar", "reindustrialization"],
  },
  china: {
    name: "China coupling",
    members: ["china-coupling"],
  },
  body: {
    name: "Aging & care",
    members: ["healthcare-aging"],
  },
  stuff: {
    name: "Physical stuff",
    members: ["commodity-cycle"],
  },
};

export const REGIMES = [
  {
    id: "green-abundance",
    name: "Green abundance",
    note: "Transition policy, building, and still-functioning global capital.",
  },
  {
    id: "fortress",
    name: "National fortress",
    note: "Tariffs, defense, domestic energy, suspicion of China and platforms.",
  },
  {
    id: "cheap-money",
    name: "Financial ease",
    note: "The 2010s again: duration, software, and patience for unprofitable growth.",
  },
  {
    id: "hard-world",
    name: "Hard world",
    note: "War, commodities, inflation, and the physical constraint.",
  },
] as const;
