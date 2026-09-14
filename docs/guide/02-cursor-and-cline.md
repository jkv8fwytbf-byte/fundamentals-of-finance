# Chapter 2. Cursor and Cline: the tool you type into, and the free bench beside it

## What it is (plain words and an analogy)

Cursor is a code editor with an AI agent built in. A code editor is a program for writing code files, the way Word is a program for writing letters. An agent is a model that can read your files, edit them, and run commands when you ask in plain English. Cursor is a modified copy (a "fork") of VS Code, the most common free editor, so it keeps the built-in terminal, the Source Control panel, and side-by-side diffs.

Source: btzaixzyh.txt, CHECK 1, "Terminal, git panel, diff review" (2026-09-14)

Think of Cursor as a workshop with a fast apprentice. The apprentice drafts every change. You are the owner, and nothing is built until you look at it and say yes. Chapter 0 gave you the habits. This chapter gives you the controls.

Cline is a free, open-source extension. An extension is a plug-in that adds a feature to an editor. Cline runs inside the same Cursor window but brings its own connection to a model provider, in our case OpenRouter. Think of Cline as a test bench next to the workshop: a place to try a tool before it goes onto the production line.

Source: btzaixzyh.txt, CHECK 1, section 2, Cline (2026-09-14)

## Why this tool now (for this project)

- You already pay for Cursor Pro at $20 a month. The plan says: do not add a second paid harness. A harness is the program that wraps a model with tools and a screen.
- You are a beginner building a system you will not fully understand on day one. Reviewing each change as a diff, and reading a plan in English before code is written, is the difference between learning and copying.
- Privacy is a stated requirement. With Privacy Mode on, Cursor holds zero-data-retention agreements with all its model providers.
- The budget ceiling is $200 a month, and the Cursor line is fixed at $20. Every other dollar is better spent on the system's own model calls.

Source: btzaixzyh.txt, CHECK 1, "RECOMMENDATION for you specifically" (2026-09-14); read-this-first.md sections 11 and 12 (2026-09-14)

There are two separate places where an AI model is used, and this chapter is only about the first. Place 1 is while you write code: that is Cursor, on the models Cursor includes. Place 2 is inside the product when it runs at night: that is our own TypeScript code calling GLM-5.3 and friends through OpenRouter. Document A section 4 explains the split. Keep it in your head while reading the rest.

Source: read-this-first.md section 4 (2026-09-14); plan section 2b (2026-09-14)

## How it is used in this project

### The plan you are on, and what the two token pools mean

Cursor stopped counting "requests" in June 2025. It now bills tokens, which are word pieces of roughly four characters, against two monthly pools. A pool is an allowance that refills each month.

| Pool | Which models | How it bills |
|---|---|---|
| Cursor Models pool | Composer 2.5, Grok 4.6, Grok 4.5 | Very generous; in practice it does not run out |
| Other Models pool | Anthropic, OpenAI, Google, Meta, Moonshot, Z.ai | Charged at each model's raw API price per million tokens; this is the pool that empties |

On Pro you get the Cursor Models pool plus roughly $20 of Other Models usage. Third-party trackers report the $20 figure consistently, but Cursor's own pages no longer print it, so treat it as approximate. Heavy agent work on frontier models can use it up in days, after which you pay overage. Auto mode has three settings, Cost, Balance and Intelligence, and bills at the price of whichever model it picks.

Source: btzaixzyh.txt, CHECK 1, "Plans and prices" and "Requests no longer exist" (2026-09-14)

The ladder is Hobby (free), Start (India only, ₹649 a month), Pro ($20, about $20 of usage), Pro+ ($60, about $70) and Ultra ($200, about $400). You stay on Pro. Your bottleneck is your learning rate and the pipeline's token spend, not editor capacity. Use Auto or Composer for routine edits, and a frontier model only when a plan needs deep reasoning.

Source: btzaixzyh.txt, CHECK 1, plans table and recommendation point 4 (2026-09-14)

### Privacy Mode, and why no API key ever goes into Cursor

Privacy Mode is a setting under Settings, then General. With it on, your code is never used for training, and Cursor's zero-data-retention agreements apply. Zero data retention (ZDR) means the model provider deletes your prompt and files after answering instead of storing them. Privacy Mode is on by default only for Enterprise accounts. Individuals must switch it on themselves. Do this before you open the repo for the first time.

Source: btzaixzyh.txt, CHECK 1, "Privacy / ZDR" (2026-09-14); read-this-first.md section 11, step 1 (2026-09-14)

Cursor lets you paste your own provider key, called BYOK, "bring your own key". Do not. The BYOK help page says, in Cursor's own words, that its Zero Data Retention policy does not apply when you use your own keys. Three more things break: Tab completion never uses your key, Auto and Composer may not route through it, and OpenRouter is not officially supported at all. Routing open-weight models into Cursor would also waste the pools you already pay for. So the rule is simple: your OpenRouter key goes into the repo's `.env` file, into GitHub secrets, and into Cline's own settings. It never goes into Cursor's settings.

Source: btzaixzyh.txt, CHECK 1, "BYOK and OpenRouter" and "Is open-weight via OpenRouter still meaningful inside Cursor" (2026-09-14); read-this-first.md section 10 (2026-09-14)

### Plan mode and Agent mode (Shift+Tab)

The agent panel has two modes, and Shift+Tab switches between them. In Plan mode the agent asks clarifying questions, reads the code, and writes an implementation plan in English. You edit that plan in the chat or as a markdown file, and nothing on disk changes until you hand it to Agent mode. In Agent mode the agent edits files and runs commands. Use Plan mode for anything larger than a one-line edit. This is the workflow that lets you approve the idea before you see the code.

Source: btzaixzyh.txt, CHECK 1, "Agent mode / Plan mode" (2026-09-14); read-this-first.md section 11, step 4 (2026-09-14)

### Reading diffs hunk by hunk

Every agent edit lands as a diff: old lines in red, new lines in green. A diff is split into hunks, and a hunk is one contiguous block of changed lines. Cursor lets you accept or reject each hunk before anything is committed. Rejecting is free and leaves the file as it was. Chapter 0, rule 5, says read the diff, not the summary. This is where you do it. When a hunk touches a calculator formula, read it twice, then check the golden test still passes (chapter 3).

Source: btzaixzyh.txt, CHECK 1, "Terminal, git panel, diff review" (2026-09-14); read-this-first.md section 11, step 5 (2026-09-14)

### The rules file

The folder `.cursor/rules/` will hold the hard rules of the project on one page: golden test, vintage, source and license class, India fallback, ranges not points, no advice. Cursor reads these rules on every request, so the agent cannot "forget" them between chats. The repo will also carry `AGENTS.md`, a plain file with the same rules that Cursor, Cline and Claude all read. Both files arrive with the repo in M2.

Source: read-this-first.md sections 3 and 11, step 3 (2026-09-14); plan, M2 step 1 (2026-09-14)

### MCP and `.cursor/mcp.json`

MCP stands for Model Context Protocol. It is a standard plug that lets an AI tool call other programs, the way a USB port lets any laptop use any keyboard. A program that offers tools this way is an MCP server. Cursor reads the list of servers from `.cursor/mcp.json` in the repo (or `~/.cursor/mcp.json` for all repos) and supports three ways of connecting to a server (called transports): over a local process, or over the network by SSE or Streamable HTTP. The repo's file will use the local one. The repo will ship this file, and the agent panel will then list the system's own tools: `value_company`, `write_memo`, `review_memo`, `get_industry_stats`, `search_corpus` and `report`. The same server will serve Cline and Claude, so there is one calculator with several callers, not several drifting copies.

Source: btzaixzyh.txt, CHECK 1, "MCP" (2026-09-14); read-this-first.md section 11, step 2 (2026-09-14); plan, M2 step 7 (2026-09-14)

### Cloud agents, BugBot and Automations

Cursor offers three services that run away from your laptop. Each draws on your usage pool; the table shows how each one is charged.

| Service | What it does | How it bills | Our use |
|---|---|---|---|
| Cloud agents | Comment `@cursor` on a GitHub pull request or issue; it clones the repo in a cloud machine, works on a branch, and pushes back for review | API price of the model chosen, from your pool, with a spend limit you set | Occasional, for a chore you describe in a PR comment |
| BugBot | Reviews PR diffs on GitHub, leaves inline comments with fixes, can spawn a cloud agent to apply them | Usage-based since about 8 June 2026; a third-party estimate is $1.00 to $1.50 per run, and a run is every push, not every PR | Turn on manually for big PRs, not on every push |
| Automations | Scheduled agents, shipped 5 March 2026: cron expressions (a compact way of writing a schedule such as 'every night at 02:15'), GitHub events, Slack, webhooks (a URL another service calls to trigger a run), Linear, Sentry, PagerDuty; each run gets a cloud sandbox, your MCP servers, and a memory across runs | Billed as cloud-agent usage from your pool | Repo chores only: summarize what changed, triage a PR |

Source: btzaixzyh.txt, CHECK 1, "Cloud / Background Agents", "BugBot", "Scheduled jobs" (2026-09-14)

Why the nightly pipeline still lives on GitHub Actions and not in Automations: Automations bill through Cursor, tie the data pipeline to your editor vendor, and cost more than a plain GitHub Actions cron job calling OpenRouter directly. GitHub Actions keeps the keys in repo secrets and stays independent of whichever editor you use in 2028. Chapter 3 covers that side.

Source: btzaixzyh.txt, CHECK 1, "How it pairs with GitHub Actions" (2026-09-14); plan section 2b (2026-09-14)

### Cline, the free bench

Cline is licensed Apache 2.0, had about 1.5 million VS Code Marketplace installs by April 2026, and costs $0 as a tool. You install it from the Extensions panel inside Cursor, because Cursor runs VS Code extensions. In Cline's provider settings you pick OpenRouter and paste your OpenRouter key. That key lives in Cline, and Cline talks to OpenRouter under the settings you set there in M1: monthly limit $75, prompt logging off, zero-data-retention routing on.

Source: btzaixzyh.txt, CHECK 1, section 2, Cline (2026-09-14); read-this-first.md section 10, row 3 (2026-09-14)

Cline has two modes, Plan and Act. Plan can read the code, search and discuss, but cannot write files or run commands. Act executes. History carries across the switch. The useful trick is under Settings, "Use different models for Plan and Act": one model to think, a cheaper one to type. The plan pairs GLM-5.3 for Plan with GLM-5.3-Flash for Act. This is your bench for feeling what an open-weight model does on your code before its id goes into a nightly robot. Typical BYOK spend cited for individuals is $5 to $50 a month; used sparingly, yours sits inside the $75 OpenRouter cap.

Source: btzaixzyh.txt, CHECK 1, section 2 and recommendation (2026-09-14); plan, M1 step 5 (2026-09-14)

### Kilo and pi, in one paragraph each

Kilo is a fork of Roo Code, which is itself a fork of Cline. Anaconda acquired it in July 2026. It is free for individuals, offers 500 or more models at zero markup through its gateway, and works in VS Code, JetBrains and a CLI. It is a fair substitute for Cline if you prefer its modes, but it is the youngest and fastest-moving of the three, so Cline is the safer bench.

Source: btzaixzyh.txt, CHECK 1, section 3, Kilo (2026-09-14)

pi (pi.dev) is a minimal terminal-only agent, MIT-licensed, that ships four tools, read, write, edit and bash, and treats everything else as an extension you write in TypeScript. It has no permission pop-ups by design. It is deferred, not rejected: the runtime here is a scheduled TypeScript program, not a chat harness, so you do not need to build a coding tool. pi is worth a look later for scripted agent runs inside a nightly job, since it can also run non-interactively, printing its output or streaming it as machine-readable JSON for another program to read.

Source: btzaixzyh.txt, CHECK 1, section 4, pi (2026-09-14); plan section 2b (2026-09-14); bkm2kob5x.txt, learning path section 9 (2026-09-14)

## Learn it

Hours are my estimates unless a source is named. All free.

| Resource | Format | Hours | Why |
|---|---|---|---|
| Cursor docs, Agent modes: https://cursor.com/docs/agent/modes | Web page | 0.5 | Plan mode versus Agent mode, the one control you use daily |
| Cursor docs, Models and pricing: https://cursor.com/docs/models-and-pricing | Web page | 0.5 | Read the two pools yourself, and find the Auto setting |
| Cursor privacy page: https://cursor.com/docs/enterprise/privacy-and-data-governance and the BYOK page: https://cursor.com/help/models-and-usage/api-keys | Web pages | 0.5 | Confirm the ZDR promise and the sentence that BYOK voids it |
| Cursor docs, MCP: https://cursor.com/docs/context/mcp, plus the MCP intro: https://modelcontextprotocol.io/docs/getting-started/intro | Web pages | 1 (MCP intro about 0.5 per the learning path) | Understand `.cursor/mcp.json` before the repo ships it |
| Cursor docs, Rules page (cursor.com/docs, search "Rules"; verify the exact URL) | Web page | 0.5 | How `.cursor/rules/` is read on every request |
| Cline docs, Plan and Act: https://docs.cline.bot/features/plan-and-act | Web page | 0.5 | The per-mode model split, and what Plan cannot do |
| Optional: BugBot https://cursor.com/docs/bugbot and Automations https://cursor.com/docs/cloud-agent/automations | Web pages | 0.5 | Skim so you know what you are choosing not to use for the pipeline |

Source: URLs from btzaixzyh.txt, CHECK 1, Sources list (verified 2026-09-14); MCP hours from bkm2kob5x.txt, learning path section 10 (2026-09-14)

## 10-minute exercise

You can do this today, before the repo exists.

1. Open Cursor. Settings, then General, then Privacy Mode: on. Two minutes.
2. Open the folder `~/Valuation/docs`. Open the agent panel. Press Shift+Tab until the mode reads Plan. Ask: "Plan a change that adds a one-line glossary entry for the word hunk to read-this-first.md, section 15. Do not make the change." Read the plan. Note which file it says it would touch. Four minutes.
3. Press Shift+Tab to Agent mode. Ask for the same one-line change. When the diff appears, read the red and green lines, then reject the hunk. Open the Source Control panel and confirm no file is modified. Three minutes.
4. Add one line to your decisions log from chapter 0 saying what Plan mode showed you. One minute.

In M1, when your OpenRouter key exists, add the second half: install Cline from the Extensions panel, choose OpenRouter as provider, paste the key, and set GLM-5.3 for Plan and GLM-5.3-Flash for Act.

Source: plan, M1 steps 4 and 5 (2026-09-14)

## Done when

- Privacy Mode shows as on, and you checked it yourself.
- You can switch modes with Shift+Tab and explain in one sentence what Plan mode cannot do.
- You have rejected a hunk and seen the file unchanged in Source Control.
- You can say where an API key goes (`.env`, GitHub secrets, Cline's provider setting) and where it never goes (Cursor's settings).
- You can say why the nightly pipeline runs on GitHub Actions and not on Cursor Automations.
- After M2: the agent panel lists the six tools from `.cursor/mcp.json`, and Cline runs with different models for Plan and Act.
