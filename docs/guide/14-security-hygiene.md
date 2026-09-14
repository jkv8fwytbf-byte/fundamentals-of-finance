# Chapter 14. Security hygiene for a solo builder

## What it is (plain words and an analogy)

Security hygiene is the set of small, boring habits that stop one stolen key from ruining the project. Hygiene is the right word. It is brushing your teeth, not surgery. Each habit takes minutes. Skipping them costs an evening at best and a month at worst.

Think of the system as a building. Your GitHub account is the master key to the whole building. Each vendor key (OpenRouter, Neon, Pinecone) opens one room. This chapter puts two locks on the front door, a spare key in a safe, and room keys that open one door and expire.

Terms, defined once:

- **2FA** (two-factor authentication): a second proof of identity after your password, usually a six-digit code from a phone app. **TOTP** is the standard those codes follow.
- **Recovery codes**: one-time codes GitHub gives you when you turn on 2FA. They are the spare key for the day you lose the phone.
- **Token** (or PAT, personal access token): a long random string that lets a program act as you. **Fine-grained** means it opens one repository, with chosen permissions, and expires.
- **Secret**: any key, token, password, or database address. **Push protection**: a GitHub setting that refuses a push containing a secret.
- **gitleaks**: a free program that scans files and git history for strings that look like secrets. A **pre-commit hook** is a small script git runs before every commit.
- **`.env`**: a plain text file of secrets that git is told to ignore through `.gitignore`.
- **Rotation**: replacing a key with a new one and retiring the old.
- **BYOK** (bring your own key): pasting your own API key into a tool such as Cursor. **ZDR** (zero data retention): the provider deletes your prompts after answering.

## Why this tool now (for this project)

M1 is the milestone where you will create every account. All keys exist at once and none is guarded yet. The accounts checklist calls GitHub "your root of trust" and says compromise there means everything. That is the account this chapter protects first.

Source: bj0fbejiq.txt, CHECK 2, accounts checklist row 1 (2026-09-14); plan section 5, M1.

Money is the second reason. The whole system has a $200 per month ceiling. The checklist names four vendors that can run away with your budget: OpenRouter, Mistral, Parallel, and Cohere. A leaked OpenRouter key with no cap can spend the month in one night.

Source: bj0fbejiq.txt, CHECK 2, "Secrets hygiene for this build"; read-this-first.md section 12.

Privacy is the third. Open-weight models run through OpenRouter with ZDR so that no prompt lingers anywhere. A key pasted into a chat window, or into Cursor's BYOK box, quietly breaks that promise. Cursor's own help page says "Cursor's Zero Data Retention policy does not apply when you use your own API keys."

Source: btzaixzyh.txt, CHECK 1, "BYOK and OpenRouter", quoting https://cursor.com/help/models-and-usage/api-keys (2026-09-14).

## How it is used in this project

Eleven habits, each with where it will live.

| Habit | What you do | Where |
|---|---|---|
| 2FA on every vendor | Authenticator app on your phone; GitHub requires it | Every account in Document A, section 10 |
| Recovery codes offline | Download GitHub's codes; print them or store them on a drive that is not synced | Not in the repo, not in a chat |
| Fine-grained GitHub token | One token, one repo, 90-day expiry, named `GITHUB_TOKEN` | Repo secrets and local `.env` |
| Push protection | Secret scanning and push protection switched on | Repo settings, when the repo is handed over in M2 |
| gitleaks | Runs before each commit and as a job in CI | Pre-commit hook and Actions workflow, from M2 |
| `.env` discipline | Real values in `.env`, empty names in a committed `.env.example`, `.env*` in `.gitignore` | Repo root |
| One email alias per vendor | `you+neon@gmail.com`, `you+voyage@gmail.com` | Each signup |
| Spend caps | OpenRouter limit $75 a month; Actions cap $25; Voyage billing alert; a cap at Mistral | Vendor billing pages |
| Rotation drill | Rotate the OpenRouter key and the Neon connection string once, on purpose; 90-day reminders for the GitHub token and the OpenRouter key | Calendar |
| No keys in chats or BYOK | Never paste a key into Cursor's model settings, into Claude, or into any chat | Your fingers |
| Sensitive session logs | Treat AI tool transcript folders like `.env` | Your laptop |

Source: read-this-first.md sections 10, 11 and 12; plan section 5, M1; bj0fbejiq.txt, CHECK 2; bkm2kob5x.txt, section 15 (all 2026-09-14).

A few rows need one more sentence.

**Why an alias per vendor.** Gmail delivers `you+neon@gmail.com` to your normal inbox. If Neon's user list leaks, the attacker learns an address that works nowhere else. For the same reason, sign up to Neon with email and a separate password, not only "Continue with GitHub". If GitHub falls, Neon should not fall with it.

Source: bj0fbejiq.txt, CHECK 2, accounts checklist row 2; read-this-first.md section 10.

**Push protection on a private repo.** The learning note says secret scanning is free on public repos. Whether the toggle appears on a private repo inside a free organization is a thing to verify in the repo's Code security settings when the repo is handed over in M2. If it is missing, gitleaks in a pre-commit hook does the same job on your machine. That is why the plan has both.

Source: bkm2kob5x.txt, section 15; plan section 5, M1.

**Session logs.** Every AI coding tool writes a transcript of your session to disk. The pi note says its transcripts live in `~/.pi/agent/`, next to an `auth.json` that holds live tokens, including an OpenRouter key. pi is deferred, but the lesson transfers to Cursor and to any terminal tool. Rotate the OpenRouter key if a log ever leaves your machine.

Source: bkm2kob5x.txt, section 15.

**Cline is the allowed exception.** The plan lets you give Cline your OpenRouter key inside Cline's own settings. Cline sends prompts straight to OpenRouter under OpenRouter's terms, with logging off and ZDR routing on. Cursor's own model settings never see the key.

Source: plan section 5, M1 step 5; read-this-first.md section 11; btzaixzyh.txt, CHECK 1.

**The agent's blast radius.** Never give an AI agent a key with write access to anything you cannot restore. Neon branching is the undo button. Create a branch before any schema change the agent proposes. The private repo inside a free organization (Chapter 3) helps here too. It gives you one page to check who and what has access.

Source: bj0fbejiq.txt, CHECK 2, "Secrets hygiene for this build"; read-this-first.md section 10.

## Learn it

Chapter 1 lists the first three under "Security, week 1". They are repeated so this chapter stands alone. All are free.

| Resource | Format | Hours | Why |
|---|---|---|---|
| About 2FA, https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication | Docs | 0.5 | The one page to read before the exercise below |
| Managing personal access tokens, https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens | Docs | 0.5 | How to make a fine-grained token scoped to one repo with an expiry; never a classic token with `repo` on everything |
| About secret scanning, https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning | Docs | 0.5 | What push protection catches and what it does not |
| gitleaks, https://github.com/gitleaks/gitleaks | Tool readme | 1 | Install, scan the repo once, wire the pre-commit hook |
| github/gitignore, https://github.com/github/gitignore | Template file | 0.5 | Start from `Node.gitignore`; add `.env*`, `*.xlsx` caches, and any raw licensed data dumps |
| Cursor, bring your own API key, https://cursor.com/help/models-and-usage/api-keys | Help page | 0.25 | Read the one sentence that says ZDR does not apply with BYOK, then never do it |

About 3.25 hours in total. The learning path budgets about 4 hours and $0 for this set.

Source: bkm2kob5x.txt, section 15; btzaixzyh.txt, CHECK 1 (both 2026-09-14).

## 10-minute exercise

Turn on 2FA for GitHub and store the recovery codes offline. No AI tool.

1. Install an authenticator app on your phone if you do not have one.
2. Sign in to GitHub in a browser. Open Settings, then the Password and authentication page. Labels move, so verify them on the page.
3. Choose to enable two-factor authentication with an authenticator app. Scan the code the page shows. Type the six-digit code back.
4. GitHub then shows recovery codes. Download them. Print them, or copy them to a drive that is not synced to any cloud. Do not save them in the repo, in a notes app, or in a chat.
5. Sign out. Sign in again with your password and a fresh code. If that works, the lock is on.
6. Write one line in your decisions log: the date, "GitHub 2FA on, recovery codes stored at [place]." Do not write the codes themselves.

Source: bkm2kob5x.txt, section 15; bj0fbejiq.txt, CHECK 2, row 1.

## Done when

- GitHub asks you for a code at sign-in, and you can name the offline place where the recovery codes sit.
- Every vendor account in Document A, section 10, has 2FA on and its own email alias.
- The repo has `.env*` in `.gitignore`, a committed `.env.example`, and push protection on, or gitleaks in a pre-commit hook if the toggle is not offered.
- OpenRouter shows a $75 monthly limit, prompt logging off, and ZDR routing on. GitHub shows a $25 Actions spending cap. Voyage has a billing alert.
- You have rotated the OpenRouter key once on purpose, and the nightly job still ran afterward.
- Two calendar reminders exist, 90 days out, for the GitHub token and the OpenRouter key.
- You can explain to someone else why a key never goes into a chat or into Cursor's BYOK box.

Source: read-this-first.md sections 10 and 12; bkm2kob5x.txt, section 15; bj0fbejiq.txt, CHECK 2.
