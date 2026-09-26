# 001. One public repository for everything

Date: 2026-09-26. The call is Siddharth's. Status: draft, not yet approved by him. Claude Code wrote this note and merged it with the rest of the move in PR #11; issue #20 asks him to read it and approve or correct it.

Decided: one public GitHub repository, `jkv8fwytbf-byte/fundamentals-of-finance`, for everything. The folder `/Users/siddharth/Desktop/Valuation` is its working copy (the local folder that git, the history-keeping program, tracks) and stays at the root. Side projects go in `projects/`, one-off reports in `reports/`, plan drafts in `history/plan/`. Each import came in on its own branch (a separate line of commits, a commit being one saved snapshot), was merged into `main` with a merge commit (a commit that joins two branches), and was kept, so the branch list stays a map. Three archive branches (`archive/dev-2026-09-15`, `archive/first-attempt-plan-v5`, `archive/cursor-cloud-agent`) are frozen: never commit to them, never merge them. `main` is protected: it changes only through pull requests (a request to merge a branch, shown as a diff with comments), with no force push (overwriting its history) and no deletion. Daily changes go by branch, pull request and squash merge (the branch's commits become one commit on `main`). The future code repository `valuation` (plan section 5, M2) stays separate and private. The private `Valuation` copy on GitHub from the morning of 26 September is kept, his choice.

Rejected: a fresh root with `Valuation` in a subfolder, because hundreds of absolute paths in the documents would break. Long-lived per-project branches never merged, the pattern of his July learning repositories on GitHub, because `main` would then be empty. A private repository, because he chose to learn in the open.

Why, in his words on 26 September: "jam everything into github repo ... with branches and iterations and readmes and everything", and "everything in different branches".

This decision replaces the rules of 15 September (local, private, never push). `CLAUDE.md` and `HANDOFF.md` now carry the new rules.
