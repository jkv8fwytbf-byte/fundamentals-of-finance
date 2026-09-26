export type PolicyAxisId =
  | "climate"
  | "defense"
  | "trade"
  | "techReg"
  | "china"
  | "rates";

export type NarrativeId =
  | "ai-platform"
  | "energy-transition"
  | "fossil-endurance"
  | "us-exceptionalism"
  | "china-coupling"
  | "reindustrialization"
  | "consumer-brand"
  | "healthcare-aging"
  | "defense-multipolar"
  | "payments-rails"
  | "commodity-cycle"
  | "software-subscription"
  | "cheap-money-duration";

export type PhilosophyId =
  | "tech-optimism"
  | "hard-assets"
  | "american-fortress"
  | "global-consumer"
  | "moat-compounder"
  | "industrial-policy"
  | "abundance"
  | "financialization";

export type PolicyExposure = Record<PolicyAxisId, number>;

export type Company = {
  ticker: string;
  name: string;
  sector: string;
  geography: string;
  summary: string;
  narratives: { id: NarrativeId; weight: number }[];
  philosophies: PhilosophyId[];
  policy: PolicyExposure;
  buffett: {
    moat: number;
    understandability: number;
    quality: number;
    note: string;
  };
  damodaran: {
    story: string;
    risk: string;
  };
};

export type Holding = {
  ticker: string;
  weight: number;
};

export type SamplePortfolio = {
  id: string;
  name: string;
  epithet: string;
  thesis: string;
  holdings: Holding[];
};

export type Book = {
  id: string;
  title: string;
  author: string;
  year: number;
  why: string;
  challenges: PhilosophyId[];
  ifYouAreHeavyIn: NarrativeId[];
};

export type Slice = {
  id: string;
  name: string;
  weight: number;
  color: string;
};

export type Audit = {
  holdingCount: number;
  totalWeight: number;
  tickerHHI: number;
  sectorHHI: number;
  narrativeHHI: number;
  philosophyHHI: number;
  effectiveTickers: number;
  effectiveSectors: number;
  effectiveNarratives: number;
  effectivePhilosophies: number;
  effectiveFamilies: number;
  familyHHI: number;
  falseDiversification: number;
  hedgehogScore: number;
  foxScore: number;
  animal: "hedgehog" | "fox" | "confused";
  dominantNarrative: Slice | null;
  dominantPhilosophy: Slice | null;
  sectorSlices: Slice[];
  narrativeSlices: Slice[];
  philosophySlices: Slice[];
  familySlices: Slice[];
  policy: PolicyExposure;
  policyAmplitude: number;
  regimeSensitivities: { id: string; name: string; score: number; note: string }[];
  buffett: {
    moat: number;
    understandability: number;
    quality: number;
  };
  letter: {
    headline: string;
    kicker: string;
    paragraphs: string[];
  };
  challengeBookIds: string[];
  missingNarratives: NarrativeId[];
};
