# Chapter 4. TypeScript for a Python brain

## What it is (plain words and an analogy)

JavaScript is the language that web browsers run. Node.js is a program that runs JavaScript outside a browser, on a server or on your Mac. TypeScript is JavaScript plus a type system. You write small annotations such as `growth: number`. A compiler called `tsc` checks them, then strips them out and produces plain JavaScript. The types never reach the running program.

Analogy: TypeScript is Python with `mypy` switched on for every file and no way to turn it off. The type hints are removed before the program runs, exactly as Python ignores its own hints at runtime.

One more framing helps a Python brain. TypeScript types are structural. Two things with the same shape are the same type, whatever they are called. That is duck typing, the same idea as Python's `Protocol`. There is no official "TypeScript for Python programmers" page, so the closest useful starting point is the page written for JavaScript programmers.

Source: bkm2kob5x.txt, learning path section 3 (verified 2026-09-14).

## Why this tool now (for this project)

The plan builds the whole system in one language: the calculator, the database layer, the librarian, the memo writer, the MCP server (the small program that lets an AI tool call the engine; chapter 10 explains it), and the nightly jobs. Python in the production path is an explicit non-goal. One language means one test runner, one build, one set of rules for Cursor to follow, and no glue between two worlds.

Source: plan sections 9 and 10.2 (2026-09-14).

There is also an arithmetic reason, and it matters more than the convenience. Excel stores every number as an IEEE-754 float64. So does JavaScript. IEEE-754 is the international standard for how computers store decimal fractions in binary, and float64 is its 64-bit size. Because both sides use the same format, a port that performs the spreadsheet's operations in the same order agrees with it far more tightly than the golden test requires. The golden test only asks for 1e-6. That is why a program written in a language with "no Decimal type" can still match Damodaran's workbook to six decimal places.

Source: plan sections 10.1 and 10.2 (2026-09-14); bkm2kob5x.txt, section 3.

## How it is used in this project

The repo is a pnpm workspace, which is one folder holding several packages that share tools. A package is a folder with its own `package.json`, the file that names a package and lists what it depends on. The plan's packages are `engine`, `db`, `rag`, `memo`, `mcp-server`, and `models`, all under `packages/`.

The engine is pure functions. A pure function takes inputs, returns an output, and touches nothing else: no network, no database, no clock. Modules mirror the spreadsheet's sheets: `rating.ts`, `costOfCapital.ts`, `fcff.ts`, `terminal.ts`, `failure.ts`, `india.ts`, `reverseDcf.ts`, `monteCarlo.ts`, `impliedErp.ts`. Everything else, such as reading a filing or writing a row, sits outside the engine so the arithmetic stays testable.

Source: plan section 10.2 and "Critical files" (2026-09-14).

## The eight things that bite

Each item names the Python habit, the TypeScript reality, and what it does to a valuation if you get it wrong.

### 1. There are two kinds of nothing: `null` and `undefined`

Python has one `None`. JavaScript has `undefined` (never set) and `null` (set to nothing on purpose). Turn on `strictNullChecks`, which `strict` includes, and the compiler forces you to handle both.

The trap is the default operator. Python's `x or default` has a JavaScript twin, `x || default`, and it fires on `0` and on the empty string as well as on the two nothings. Use `??` instead, which fires only on `null` and `undefined`.

```ts
const g = input.growth || 0.05;   // a real 0% growth silently becomes 5%
const g = input.growth ?? 0.05;   // 0 stays 0; only a missing value gets the default
```

Source: bj0fbejiq.txt, CHECK 3 section 8, item 1 (2026-09-14).

### 2. Always `===`, never `==`

`==` converts types before comparing. `'' == 0` is true and `'1' == 1` is true. `===` compares without conversion, the way Python's `==` behaves. Use `===` everywhere. The one accepted exception is `x == null`, which catches both nothings in one test.

Source: bj0fbejiq.txt, CHECK 3 section 8, item 2.

### 3. `number` is float64, and there is no `int` and no `Decimal`

Python has `int`, `float`, and `Decimal`. JavaScript has `number`, which is float64, and that is it for ordinary arithmetic. `0.1 + 0.2 !== 0.3` holds, exactly as it does for Python floats. For the engine this is fine and even desirable, because the spreadsheet is float64 too, as explained above.

It is not fine for money totals or share counts that you add up over many rows. For those, keep integers in minor units, or use the `decimal.js` library. And note a related surprise: the `node-postgres` driver returns Postgres `NUMERIC` and `BIGINT` columns as strings, on purpose, so that precision is not lost. Do not "fix" that with `Number()` until you have decided where rounding is allowed.

Source: bj0fbejiq.txt, CHECK 3 section 8, item 3; plan section 10.2 (2026-09-14).

### 4. `async` and `await` are everywhere, and a missing `await` is silent

Almost every input or output call returns a Promise. A Promise is an object that says "the value will arrive later." Python has `asyncio`, but you can avoid it. In Node you cannot. Forgetting `await` does not raise an error. It hands you the Promise object, which looks fine and turns into `NaN` three functions later. Enable the lint rule `@typescript-eslint/no-floating-promises` so ESLint catches it (ESLint is the linter, a second checker that runs alongside `tsc`). Use `Promise.all` to run fetches in parallel. Node has no GIL, but it also has one thread; it is an event loop, not threads.

Source: bj0fbejiq.txt, CHECK 3 section 8, item 4.

### 5. Modules: ESM and the `.js` extension rule

JavaScript has two module systems. CommonJS is the old one with `require`. ESM, for ECMAScript Modules, is the standard one with `import` and `export`. Set `"type": "module"` in `package.json` and you are in ESM. Then three things change: no `require`, no `__dirname` (use `import.meta.url`), and under `moduleResolution: "NodeNext"` every relative import must end in `.js` even though the file on disk is `.ts`.

```ts
import { terminalCostOfCapital } from "./terminal.js";   // the file is terminal.ts; this is correct
import { terminalCostOfCapital } from "./terminal";      // fails at build or run time
```

The report calls this the cause of most first-week build failures. Tape it to the monitor.

Source: bj0fbejiq.txt, CHECK 3 section 8, item 5.

### 6. `strict` mode, and the fact that types vanish at runtime

Because `tsc` erases types, a typed API response is a promise, not a check. Nothing stops a JSON file from putting a string where the type says number. Two settings and one library close the gap. In `tsconfig.json`, which is the compiler's settings file, keep `strict: true` (on by default in TypeScript 6.0) and add `noUncheckedIndexedAccess`. Then validate every external input at the boundary with Zod. Zod is a library that checks a value against a schema at runtime and throws if it does not match. It is the TypeScript twin of `pydantic`. External inputs here are filing JSON from EDGAR (the US regulator's public filing database), text produced by OCR (software that reads scanned pages), vendor data, and every model output. The engine only ever sees values that passed Zod.

Source: bj0fbejiq.txt, CHECK 3 section 8, item 6.

### 7. pnpm workspaces instead of virtual environments

Python gives each project a virtual environment with its own interpreter. Node gives each project a `node_modules` folder. pnpm is a package manager that is strict about it. A workspace is a `pnpm-workspace.yaml` file listing package folders. One package depends on another by writing `"@valuation/engine": "workspace:*"`. pnpm links packages with symlinks and refuses an import you did not declare. That is good, but it surprises anyone used to Python's flat `site-packages`. Run one package's tests with `pnpm -F engine test`.

Source: bj0fbejiq.txt, CHECK 3 section 8, item 7; https://pnpm.io/workspaces.

### 8. Vitest is pytest

Vitest is the test runner. `describe` groups tests, `it` is one test, `expect` is the assertion. `vi.mock()` is monkeypatching. `--coverage` is built in. It runs TypeScript directly, so there is no build step before tests.

```ts
import { describe, it, expect } from "vitest";
import { terminalCostOfCapital } from "./terminal.js";

describe("terminal cost of capital", () => {
  it("is the risk-free rate plus the mature-market ERP", () => {
    expect(terminalCostOfCapital(0.0458, 0.0423)).toBeCloseTo(0.0881, 6);
  });
});
```

Use `toBeCloseTo`, not `toBe`, for any float. The two inputs are the workbook's own January 2026 values, and 8.81% is the workbook's own answer.

Source: bj0fbejiq.txt, CHECK 3 section 8, item 8; bkdrkpfng.txt (model schema report), the terminal cost of capital row: 4.58% + 4.23% = 8.81%.

### The translation table

| Python | TypeScript | Watch for |
|---|---|---|
| `None` | `null` and `undefined` | Use `??` for defaults, not `\|\|`. |
| `==` | `===` | Never `==` except `x == null`. |
| `int`, `float`, `Decimal` | `number` (float64), `bigint`, `decimal.js` | Fine for the engine; not for money totals. |
| `asyncio` | Built in; every I/O call returns a Promise | A missing `await` is silent. |
| `import x from pkg.mod` | `import { x } from "./mod.js"` | The `.js` is required, even for a `.ts` file. |
| `mypy` | `tsc` with `strict: true` | Types are erased at runtime. |
| `pydantic` | Zod | Validate at the boundary. |
| `venv` and `pip` | pnpm and `node_modules` | Undeclared imports fail loudly. |
| `pytest` | Vitest | `describe`, `it`, `expect`, `vi.mock`. |

Source: the mapping is a summary of bj0fbejiq.txt, CHECK 3 section 8 (2026-09-14).

## Learn it

Skip everything aimed at people who have never programmed. You have the concepts; you need the type system and the module story. All free. Total about 18 hours if you read the Handbook and the Essentials chapters listed, plus about 5 hours for the tools.

| # | Resource | Format | Hours | Why |
|---|---|---|---|---|
| 1 | https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html | Official page | 0.5 | Written for JavaScript programmers; the closest thing to a Python track. |
| 2 | https://www.typescriptlang.org/docs/handbook/2/basic-types.html, then in order: Everyday Types, Narrowing, More on Functions, Object Types, Generics | Official Handbook | 6 to 8 | Narrowing is the chapter that makes TypeScript click. Read it twice. |
| 3 | https://www.totaltypescript.com/books/total-typescript-essentials | Free book with exercises, 16 chapters | 10 to 12 for the whole book | Do chapters 1 (tsconfig), 5 (unions, literals, narrowing), 10 (deriving types), 13 (modules and declaration files), 14 (configuring TypeScript) first. Chapters 13 and 14 alone repay the time because of the `.js` rule. |
| 4 | https://www.typescriptlang.org/tsconfig/ and https://github.com/tsconfig/bases | Official reference | 1 | Every flag explained; `bases` gives a correct Node config to copy instead of inventing one. |
| 5 | https://vitest.dev/guide/ | Official docs | 2 | Getting started, mocking, coverage, with direct pytest analogies. |
| 6 | https://zod.dev/ | Official docs | 1.5 | Runtime validation; the boundary layer that makes model output safe to store. |

Not recommended for now: Execute Program's TypeScript course. It is live in 2026 and good, but it is paid and its spaced-repetition shape is wrong for someone shipping an engine in twelve weeks.

Source: bkm2kob5x.txt, learning path section 3 (URLs verified 2026-09-14); bj0fbejiq.txt, CHECK 3 section 8 resource table.

## 10-minute exercise

Inside the repo, or in a scratch folder with `pnpm init` and `pnpm add -D typescript vitest`:

1. Create `terminal.ts` containing one exported pure function, `terminalCostOfCapital(rf: number, matureErp: number): number`, that returns `rf + matureErp`. Terminal cost of capital is the discount rate the model uses for the years after the explicit forecast, and the workbook sets it to the risk-free rate plus the mature-market equity risk premium.
2. Create `terminal.test.ts` with the Vitest test shown in item 8 above.
3. Run `pnpm vitest run`. It should pass.
4. Change `toBeCloseTo(0.0881, 6)` to `toBe(0.0881)`. Run again. If it fails, you have just seen float64 in person. If it passes, change the inputs to `0.1` and `0.2` with an expected `0.3` and try again.
5. Remove the `.js` from the import in the test file. Run again. Read the error message slowly. That is the message you will see in week one.
6. Put the `.js` back and leave both files green.

Source: bkdrkpfng.txt, the stable cost of capital row (rf 4.58% + mature ERP 4.23% = 8.81%); plan section 10.2; bj0fbejiq.txt, CHECK 3 section 8 items 3, 5 and 8.

## Done when

- You can explain, without notes, why `||` is dangerous for a growth rate and `??` is not.
- You can say in one sentence why a float64 language can still match the spreadsheet to 1e-6.
- You have seen the missing `.js` error once and fixed it.
- You can name the Zod schema that guards each external input the engine consumes.
- You have run `pnpm -F engine test` and read the output.
