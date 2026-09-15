# Chapter 13. Figma and FigJam: the whiteboard where the system is drawn

## What it is (plain words and an analogy)

Figma is a website for drawing what software will look like. A designer draws every screen and every button in Figma before a programmer builds it. Think of an architect's blueprint. The blueprint is not the house, but the builder works from it.

FigJam is Figma's whiteboard. It is made for boxes, arrows and sticky notes, not for pixel-perfect screens. Think of a meeting-room wall covered in sticky notes. The difference is that this wall lives online and never gets wiped.

Both run in a browser and both save to Figma's cloud. One Figma drawing is called a file. One FigJam drawing is called a board. Files and boards belong to a team. A team sits on a plan, which is the pricing tier. A seat is your role on that plan, and it decides what you may edit.

| | Figma | FigJam |
|---|---|---|
| Made for | Screens and buttons | Diagrams, flows, notes |
| Basic unit | A file made of frames (a frame is one screen) | A board |
| Typical objects | Rectangles, text, reusable components | Shapes, connector lines, sticky notes |
| You use it when | You are building a screen | You are thinking, planning or explaining |
| In this project | Not before a screen exists | Now, for all five system diagrams |

Source: general product knowledge of Figma, which the local reports do not cover (2026-09-14)

## Why this tool now (for this project)

The approved plan puts the FigJam diagrams inside milestone zero (M0), next to the four documents. M0 is the "explain everything" milestone, and nothing past it is built yet. The five boards are pictures of the system you will build later. If you can redraw a board in your own words, you understand that part of the system. That is why the plan makes editing the architecture board your first exercise.

Source: docs/plan.md, M0 deliverables and the "Figma, concretely" note (2026-09-14)

## How it is used in this project

### The five boards

Each board below is live in your Figma account. A copy of each also sits as a PNG image in /Users/siddharth/Valuation/docs/diagrams/png/. A PNG is a plain picture file. It opens anywhere, but you cannot move its boxes.

- System architecture, https://www.figma.com/board/DtFTvDZeSQpuKLM5tavDUT. The seven parts of the system and how they talk to each other. PNG: architecture.png.
- Nightly data flow, https://www.figma.com/board/6LSfZZfWAnbQVY0twr7OMw. What the GitHub Actions robot does each night, from checking for new filings to writing a heartbeat row. PNG: nightly-data-flow.png.
- The valuation chain, https://www.figma.com/board/SNaMV0lrKHeDRQgelrbPsp. Left to right, from revenue growth through free cash flow and cost of capital to value per share. PNG: valuation-chain.png.
- The memo pipeline, https://www.figma.com/board/LGcrXp6yT3fh4O2IV3mEY8. How a company story becomes numbers and then a written memo. PNG: memo-pipeline.png.
- The milestone map, https://www.figma.com/board/LXcGUT7C2ArsRkwsUvRBWt. The order of work from M0 onward. PNG: milestone-map.png.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, the board table and sections 1, 7, 8, 9 and 14 (2026-09-14); directory listing of docs/diagrams/png/ (2026-09-14)

### The Figma connector in the Claude app

A connector is a plug that lets an AI app use another service on your behalf. Connectors speak a shared language called MCP, short for Model Context Protocol. MCP is a standard way for an AI tool to ask a service "what can you do?" and then call those functions.

The Figma connector in this app is signed in as you. Asked "who am I?" on 2026-09-14, it answered: handle Siddharth, team "Siddharth's team", plan tier starter, seat View. Web knowledge says the starter tier is Figma's free plan. The local reports do not confirm that, so check figma.com/pricing before you rely on it.

What the connector can do, in plain words:

- Create a FigJam board from a text description of a diagram. That is how the five boards were made.
- Read a board back, so an AI session can see what you changed on it.
- Read a Figma design file and hand its layout to a coding tool as context. That is how a drawn screen becomes a real screen later.
- Take a screenshot of a file or a board.

What to keep in mind:

- It acts as you. Anything it creates lands in your account, under your name.
- Your seat says View. Creating the boards still worked, so they exist. If a board ever opens read-only, the plan mentions a one-click seat upgrade. Check the budget in read-this-first section 12 before paying for anything.
- Boards live in Figma's cloud, not on your Mac. Keep API keys, passwords and account numbers off every board. Chapter 14 covers security hygiene.

Source: docs/plan.md, "Figma, concretely" and section 8 (2026-09-14); Figma connector whoami call and its tool list in this session (2026-09-14)

### When to draw a screen

Only when you are about to build one. The plan places screens at v3, and M0 has no screens at all. Until then, every drawing you make is a FigJam board, not a Figma design. Drawing screens early is like choosing curtains before the walls are up.

Source: docs/plan.md, section 8, Figma bullet (2026-09-14)

## Learn it (a two-hour starter path)

All of these are free. The minutes are my estimates, not figures from a source. Where I am not sure of an exact web address, I give the site and mark it "verify".

| Step | Resource | Where | Format | Time | Why |
|---|---|---|---|---|---|
| 1 | Figma Help Center, the FigJam guide | https://help.figma.com/ then search "Guide to FigJam" (exact article URL: verify) | Reading | 20 min | Names every tool: sticky note, shape, connector line, section, stamp. |
| 2 | Figma's official YouTube channel, beginner and FigJam tutorials | https://www.youtube.com/@Figma (playlist names: verify) | Video | 40 min | Watch someone drag boxes before you drag your own. |
| 3 | Figma Learn, the short courses inside the Help Center | help.figma.com, "Figma Learn" section (exact address: verify) | Guided course | 30 min | Structured path; take only the FigJam basics course. |
| 4 | Figma Community, FigJam templates | https://www.figma.com/community (filter to FigJam: verify) | Browsing | 15 min | See how other people lay out flows and borrow a layout. |
| 5 | Figma developer docs, the MCP server page | developers.figma.com (verify) | Reading | 10 min | Understand what the connector can and cannot touch. |
| 6 | The five boards above | Links in this chapter | Doing | 15 min | Real diagrams of your own system, not a toy example. |

Steps 1 to 6 total about two hours. Add the 10-minute exercise below and you are done for the evening.

Source: docs/plan.md, M0 deliverable 4, "a two-hour starter path (Figma's own free tutorials, then editing the architecture board)" (2026-09-14); web knowledge for the site addresses

## 10-minute exercise

Do this on the architecture board. Work on your own copy so the original stays as delivered.

1. Open https://www.figma.com/board/DtFTvDZeSQpuKLM5tavDUT in your browser while signed in to Figma.
2. Duplicate it. Click the board name at the top, or the main menu at the top left, and look for "Duplicate" or "Duplicate to your drafts". Duplicating means making your own copy. Rename the copy "architecture, my notes".
3. Add one sticky note per box. Press S for a sticky note, or pick it from the toolbar at the bottom (shortcut: verify). Drag each note next to its box.
4. Write one question on each sticky note. Not a summary, a question. For example, "what happens if this part is down for a night?" or "where does this read its inputs from?"
5. Pick one box and rename it in your own words. Double-click the box text to edit it. If the label says something technical, replace it with what it does for you.
6. Read your questions back. Bring the ones you cannot answer to your next session with the AI tool, and to chapter 3 of "Damodaran, the important parts" for the valuation boxes.

If the copy will not save, or the board opens read-only, stop. Note what the screen says and raise it in your next session. Do not upgrade the seat on the spot.

Source: docs/plan.md, "the first exercise is on the architecture board" (2026-09-14)

## Done when

- You can say in one sentence what Figma is for and what FigJam is for.
- All five board links open in your Figma account, or you have written down which ones do not.
- You have a duplicated architecture board with one question per box and one box renamed in your own words.
- You can name the four things the connector can do without looking.
- You have not drawn a single screen, and you know why that is correct for M0.
