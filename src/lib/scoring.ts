import { NARRATIVES, NARRATIVE_FAMILIES, PHILOSOPHIES } from "./catalog";
import { COMPANY_BY_TICKER, COMPANIES } from "./companies";
import { BOOKS } from "./library";
import type {
  Audit,
  Holding,
  NarrativeId,
  PhilosophyId,
  PolicyAxisId,
  PolicyExposure,
  Slice,
} from "./types";

const POLICY_KEYS: PolicyAxisId[] = [
  "climate",
  "defense",
  "trade",
  "techReg",
  "china",
  "rates",
];

function hhi(weights: number[]): number {
  const sum = weights.reduce((a, b) => a + b, 0);
  if (sum <= 0) return 0;
  return weights.reduce((acc, w) => acc + (w / sum) ** 2, 0);
}

function effectiveN(index: number): number {
  if (index <= 0) return 0;
  return 1 / index;
}

function round1(n: number): number {
  return Math.round(n * 10) / 10;
}

function clamp(n: number, min: number, max: number): number {
  return Math.min(max, Math.max(min, n));
}

function slicesFromMap(
  map: Record<string, number>,
  nameOf: (id: string) => string,
  colorOf: (id: string) => string,
): Slice[] {
  const total = Object.values(map).reduce((a, b) => a + b, 0);
  if (total <= 0) return [];
  return Object.entries(map)
    .map(([id, weight]) => ({
      id,
      name: nameOf(id),
      weight: weight / total,
      color: colorOf(id),
    }))
    .sort((a, b) => b.weight - a.weight);
}

function regimeScore(policy: PolicyExposure) {
  return [
    {
      id: "green-abundance",
      name: "Green abundance",
      score: clamp(
        policy.climate * 0.45 +
          policy.rates * 0.15 +
          policy.trade * 0.15 +
          policy.techReg * 0.1 -
          policy.defense * 0.05,
        -1,
        1,
      ),
      note: "Transition policy, still-open trade, and enough financial ease to fund the build.",
    },
    {
      id: "fortress",
      name: "National fortress",
      score: clamp(
        policy.defense * 0.35 -
          policy.climate * 0.2 -
          policy.trade * 0.25 -
          policy.china * 0.2 +
          policy.techReg * 0.05,
        -1,
        1,
      ),
      note: "Tariffs, arsenals, domestic energy, suspicion of China and of platforms.",
    },
    {
      id: "cheap-money",
      name: "Financial ease",
      score: clamp(
        policy.rates * 0.55 + policy.techReg * 0.25 + policy.trade * 0.1,
        -1,
        1,
      ),
      note: "Duration, software, and patience for cash that arrives later.",
    },
    {
      id: "hard-world",
      name: "Hard world",
      score: clamp(
        policy.defense * 0.3 -
          policy.rates * 0.25 -
          policy.climate * 0.05 +
          Math.abs(policy.china) * 0.15,
        -1,
        1,
      ),
      note: "Conflict, commodities, inflation, and the physical constraint.",
    },
  ];
}

function buildLetter(input: {
  holdingCount: number;
  effectiveTickers: number;
  effectiveSectors: number;
  effectiveNarratives: number;
  falseDiversification: number;
  hedgehogScore: number;
  foxScore: number;
  animal: Audit["animal"];
  dominantNarrative: Slice | null;
  dominantPhilosophy: Slice | null;
  sectorSlices: Slice[];
  policyAmplitude: number;
  regimes: ReturnType<typeof regimeScore>;
  buffett: Audit["buffett"];
}): Audit["letter"] {
  const story = input.dominantNarrative;
  const phil = input.dominantPhilosophy;
  const topRegime = [...input.regimes].sort(
    (a, b) => Math.abs(b.score) - Math.abs(a.score),
  )[0];
  const topSector = input.sectorSlices[0];

  const kicker =
    input.animal === "hedgehog"
      ? "A hedgehog portfolio"
      : input.animal === "fox"
        ? "A fox portfolio"
        : "A portfolio still choosing a nature";

  let headline = "Your diversification is mostly typography.";
  if (input.animal === "fox") {
    headline = "You are running more than one book of the world.";
  } else if (input.hedgehogScore >= 70 && story) {
    headline = `You own a congregation of ${story.name.toLowerCase()}.`;
  } else if (input.falseDiversification >= 55) {
    headline = `${input.holdingCount} names. About ${round1(input.effectiveNarratives)} stories.`;
  }

  const paragraphs: string[] = [];

  paragraphs.push(
    `Isaiah Berlin split thinkers into hedgehogs, who know one big thing, and foxes, who know many. Markets pretend this is a personality test. It is a risk test. You hold ${input.holdingCount} names, which behave like ${round1(input.effectiveTickers)} concentrated bets, in ${round1(input.effectiveSectors)} sectors, but they collapse into ${round1(input.effectiveNarratives)} living stories. The gap between ticker count and story-family count is the false diversification: ${Math.round(input.falseDiversification)}.`,
  );

  if (story && phil) {
    paragraphs.push(
      `The organizing sermon is ${story.name} (${Math.round(story.weight * 100)}% of narrative weight). The philosophy underneath is ${phil.name}. Damodaran's warning is not "avoid stories." It is that every number already has one, and that paying eight times for the same story does not make you a diversified person. It makes you a devout one.`,
    );
  }

  if (topSector) {
    paragraphs.push(
      `Traditional risk software will mostly see ${topSector.name.toLowerCase()}. That is the surface. Buffett would not mind concentration in wonderful businesses — your book scores ${round1(input.buffett.quality)} for quality and ${round1(input.buffett.moat)} for moat, on a five-point scale — but he would mind concentration in an assumption. Circle of competence is not the same as circle of newsletters.`,
    );
  }

  if (input.policyAmplitude >= 0.22 && topRegime) {
    const direction = topRegime.score >= 0 ? "for" : "against";
    paragraphs.push(
      `Partisans do not merely vote together. Haidt and Mason both describe identities that stack until beliefs stop being independent draws. Investors do this with industries. Your policy amplitude is ${Math.round(input.policyAmplitude * 100)}, which is a polite way of saying the book is not politically mute. It is most sensitive ${direction} a "${topRegime.name.toLowerCase()}" regime: ${topRegime.note} This is not a forecast of an election. It is a map of whose grocery list your cash flows are already on.`,
    );
  } else {
    paragraphs.push(
      `The political surface of the book is relatively quiet. That can mean genuine fox-like disagreement among the names, or it can mean you have not yet tagged the statutes your cash flows depend on. Policy risk is often just a coalition's grocery list, as selectorate theory would have it — not a cable-news argument.`,
    );
  }

  if (input.animal === "hedgehog") {
    paragraphs.push(
      `A hedgehog can get very rich. It can also discover that the one big thing was a decade, not a law of nature. Tetlock's foxes beat hedgehogs at prediction because they keep more than one model alive. You do not need forty stocks. You need a second story that can still pay you if the first one is merely late, or merely fashionable, or merely tribal.`,
    );
  } else if (input.animal === "fox") {
    paragraphs.push(
      `Foxes look messy in a sector chart. Some of these names will underperform in any single year, because they cannot all be right at once. That is the point. Damodaran wants consistency inside a company. Across a life, inconsistency of stories is how you avoid becoming a captive of one book, one party, one capital cycle.`,
    );
  } else {
    paragraphs.push(
      `The book is not yet a character. Add weight, or add disagreement. A portfolio of one idea with seven tickers is a hedgehog. A portfolio of ideas that cannot all be true is a fox. Either can be honest. What is not honest is calling ticker count a philosophy.`,
    );
  }

  return { headline, kicker, paragraphs };
}

export function auditPortfolio(holdings: Holding[]): Audit | null {
  const live = holdings
    .map((h) => ({
      ...h,
      company: COMPANY_BY_TICKER[h.ticker],
    }))
    .filter((h) => h.company && h.weight > 0);

  if (!live.length) return null;

  const totalWeight = live.reduce((a, h) => a + h.weight, 0);
  const tickerHHI = hhi(live.map((h) => h.weight));

  const sectorMap: Record<string, number> = {};
  const narrativeMap: Record<string, number> = {};
  const philosophyMap: Record<string, number> = {};
  const policy: PolicyExposure = {
    climate: 0,
    defense: 0,
    trade: 0,
    techReg: 0,
    china: 0,
    rates: 0,
  };
  let moat = 0;
  let understandability = 0;
  let quality = 0;

  for (const { weight, company } of live) {
    const w = weight / totalWeight;
    sectorMap[company.sector] = (sectorMap[company.sector] ?? 0) + w;
    for (const n of company.narratives) {
      narrativeMap[n.id] = (narrativeMap[n.id] ?? 0) + w * n.weight;
    }
    if (company.philosophies.length === 1) {
      philosophyMap[company.philosophies[0]] =
        (philosophyMap[company.philosophies[0]] ?? 0) + w;
    } else {
      company.philosophies.forEach((p, i) => {
        const share =
          i === 0 ? 0.55 : 0.45 / (company.philosophies.length - 1);
        philosophyMap[p] = (philosophyMap[p] ?? 0) + w * share;
      });
    }
    for (const key of POLICY_KEYS) {
      policy[key] += w * company.policy[key];
    }
    moat += w * company.buffett.moat;
    understandability += w * company.buffett.understandability;
    quality += w * company.buffett.quality;
  }

  const familyMap: Record<string, number> = {};
  for (const [narrativeId, weight] of Object.entries(narrativeMap)) {
    const family =
      Object.entries(NARRATIVE_FAMILIES).find(([, f]) =>
        f.members.includes(narrativeId as NarrativeId),
      )?.[0] ?? "other";
    familyMap[family] = (familyMap[family] ?? 0) + weight;
  }

  const sectorHHI = hhi(Object.values(sectorMap));
  const narrativeHHI = hhi(Object.values(narrativeMap));
  const philosophyHHI = hhi(Object.values(philosophyMap));
  const familyHHI = hhi(Object.values(familyMap));
  const effectiveTickers = effectiveN(tickerHHI);
  const effectiveSectors = effectiveN(sectorHHI);
  const effectiveNarratives = effectiveN(narrativeHHI);
  const effectivePhilosophies = effectiveN(philosophyHHI);
  const effectiveFamilies = effectiveN(familyHHI);

  const falseDiversification = clamp(
    (1 - effectiveFamilies / Math.max(live.length, 1)) * 100,
    0,
    100,
  );

  const dominantFamilyWeight = Math.max(0, ...Object.values(familyMap));
  const hedgehog = clamp(familyHHI * 50 + dominantFamilyWeight * 55, 0, 100);
  const foxScore = clamp(100 - hedgehog, 0, 100);

  const animal: Audit["animal"] =
    live.length < 3
      ? "confused"
      : hedgehog >= 56 || dominantFamilyWeight >= 0.52
        ? "hedgehog"
        : "fox";

  const sectorSlices = slicesFromMap(
    sectorMap,
    (id) => id,
    () => "#8a8278",
  );
  const narrativeSlices = slicesFromMap(
    narrativeMap,
    (id) => NARRATIVES[id as NarrativeId]?.name ?? id,
    (id) => NARRATIVES[id as NarrativeId]?.color ?? "#8a8278",
  );
  const philosophySlices = slicesFromMap(
    philosophyMap,
    (id) => PHILOSOPHIES[id as PhilosophyId]?.name ?? id,
    (id) => PHILOSOPHIES[id as PhilosophyId]?.color ?? "#8a8278",
  );
  const familySlices = slicesFromMap(
    familyMap,
    (id) => NARRATIVE_FAMILIES[id]?.name ?? id,
    (id) => NARRATIVE_FAMILIES[id]?.members[0]
      ? NARRATIVES[NARRATIVE_FAMILIES[id].members[0]].color
      : "#8a8278",
  );

  const policyAmplitude =
    POLICY_KEYS.reduce((a, k) => a + Math.abs(policy[k]), 0) / POLICY_KEYS.length;

  const regimes = regimeScore(policy);
  const buffett = {
    moat: round1(moat),
    understandability: round1(understandability),
    quality: round1(quality),
  };

  const allNarratives = Object.keys(NARRATIVES) as NarrativeId[];
  const missingNarratives = allNarratives
    .filter((id) => (narrativeMap[id] ?? 0) < 0.04)
    .slice(0, 6);

  const challengeBookIds = BOOKS.filter((book) => {
    const storyHit = book.ifYouAreHeavyIn.some((id) => (narrativeMap[id] ?? 0) >= 0.18);
    const philHit = book.challenges.some((id) => (philosophyMap[id] ?? 0) >= 0.18);
    return storyHit || philHit;
  })
    .slice(0, 6)
    .map((b) => b.id);

  const letter = buildLetter({
    holdingCount: live.length,
    effectiveTickers,
    effectiveSectors,
    effectiveNarratives,
    falseDiversification,
    hedgehogScore: hedgehog,
    foxScore,
    animal,
    dominantNarrative: narrativeSlices[0] ?? null,
    dominantPhilosophy: philosophySlices[0] ?? null,
    sectorSlices,
    policyAmplitude,
    regimes,
    buffett,
  });

  return {
    holdingCount: live.length,
    totalWeight,
    tickerHHI,
    sectorHHI,
    narrativeHHI,
    philosophyHHI,
    effectiveTickers,
    effectiveSectors,
    effectiveNarratives,
    effectivePhilosophies,
    effectiveFamilies,
    familyHHI,
    falseDiversification,
    hedgehogScore: hedgehog,
    foxScore,
    animal,
    dominantNarrative: narrativeSlices[0] ?? null,
    dominantPhilosophy: philosophySlices[0] ?? null,
    sectorSlices,
    narrativeSlices,
    philosophySlices,
    familySlices,
    policy,
    policyAmplitude,
    regimeSensitivities: regimes,
    buffett,
    letter,
    challengeBookIds,
    missingNarratives,
  };
}

export function suggestHedge(holdings: Holding[]): typeof COMPANIES {
  const result = auditPortfolio(holdings);
  if (!result) return COMPANIES.slice(0, 4);
  const owned = new Set(holdings.map((h) => h.ticker));
  const missing = new Set(result.missingNarratives);
  const scored = COMPANIES.filter((c) => !owned.has(c.ticker)).map((c) => {
    const overlap = c.narratives
      .filter((n) => missing.has(n.id))
      .reduce((a, n) => a + n.weight, 0);
    return { c, overlap };
  });
  scored.sort((a, b) => b.overlap - a.overlap);
  return scored.slice(0, 5).map((s) => s.c);
}
