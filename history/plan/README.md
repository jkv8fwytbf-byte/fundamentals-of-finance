# The plan, draft by draft

This folder holds every version of the project plan exactly as it was shown to Siddharth, with
his comments on each. The plan the project runs on today is `docs/plan.md` (version 4 of
14 September 2026 plus dated status notes). These files exist because the drafts he rejected, and
what he said about them, explain why the plan looks the way it does, and they lived only in chat
records until 26 September 2026.

A "version" here is one submission for approval. Version 4 was submitted five times. The third submission was the approval of the plan; the fourth, which only added a status section, was approved too. The text of each file was recovered word for word from the chat record; only the
header table and the comments section at the top of each file were added on 26 September.

| Version | Submitted (India time) | Verdict | File |
|---|---|---|---|
| v1 | 13 September 2026, 21:27 IST | Rejected with review comments | [v1.md](v1.md) |
| v2 | 14 September 2026, 11:36 IST | Rejected with review comments | [v2.md](v2.md) |
| v3 | 14 September 2026, 12:14 IST | Rejected with review comments | [v3.md](v3.md) |
| v4, first submission | 14 September 2026, 13:05 IST | Rejected with questions | [v4-1.md](v4-1.md) |
| v4, second submission | 14 September 2026, 14:27 IST | Rejected: "do M0 then save the rest" | [v4-2.md](v4-2.md) |
| v4, third submission | 14 September 2026, 14:28 IST | APPROVED (M0 only) | [v4-3-approved.md](v4-3-approved.md) |
| v4, fourth submission | 14 September 2026, 15:43 IST | Approved (adds the M0 status and resume plan section) | [v4-4-resume-plan.md](v4-4-resume-plan.md) |
| v4, fifth submission | 14 September 2026, 17:13 IST | Stopped by him before approval | [v4-5-addendum-stopped.md](v4-5-addendum-stopped.md) |
| v5 (draft) | 15 September 2026, about 15:08 IST, never submitted | Removed in the next commit, 86 seconds later | [v5-withdrawn.md](v5-withdrawn.md) |

## What changed from one version to the next

- **v1 to v2.** He dumped the old projects and local files, asked for everything to be outsourced
  to managed services, and named pi.dev (a bare-bones AI coding assistant) with OpenRouter (one key for many AI models) as the tools. Version 2 became a TypeScript system (TypeScript is JavaScript with types) on Vercel, Neon and Pinecone (hosted services for the website, the database and the search index) with a public repository.
- **v2 to v3.** He found version 2 unreadable, wanted it private, asked for PDFs, a Damodaran
  refresher, a critics reader and help learning Figma. Version 3 was rewritten in plain English,
  private, without Vercel, with a $200 ceiling and four documents before any code.
- **v3 to v4.** He pointed at his Cursor subscription and asked for diversification, accuracy,
  bias and variance views. Version 4 made Cursor the daily tool, put the open-weight models
  inside the product, and added the Hex dashboard (a hosted notebook and dashboard service), the memo writer, the scoreboard and the market
  panel.
- **v4, submission 1 to 2.** His questions ("so you are saying we ditch pi.dev? why", "head up my ass I don't understand") produced section 0, the five steps, and section 2b, plain answers.
- **v4, submission 2 to 3.** "We need to do the m0 then you save the rest so I can come back and
  think." The approval was narrowed to M0 only, the documents and diagrams.
- **v4, submissions 4 and 5.** Status sections added the same afternoon: the resume plan for the
  22 missing chapters (approved), and the addendum for document 5 (he stopped the approval, and
  the document was written that evening anyway).
- **v5.** A "public repository" variant drafted on 15 September and withdrawn at once. It is here
  for the record; the 26 September decision in `docs/decisions/001-one-public-repo-for-everything.md`
  made the repository public for a different reason.

## Tags

Each version's commit (one saved snapshot in git, the program that keeps the folder's history) carries a git tag (a fixed name for one commit): `plan-v1`, `plan-v2`, `plan-v3`, `plan-v4` (the approved
third submission) and `plan-v5-draft`. `git show plan-v3:history/plan/v3.md` prints a version
without leaving the terminal.

## A note on the em-dashes

The project's own documents avoid the em-dash character. The early drafts did not, and they are kept
as they were written.
