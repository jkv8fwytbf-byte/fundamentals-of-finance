# Chapter 6. Pinecone, Voyage and RAG in plain words

## What it is (plain words and an analogy)

Picture a librarian who has read every paragraph Damodaran ever wrote or said. She does not remember page numbers. She remembers what each paragraph is about. You ask, "why does he subtract a default spread from the Indian bond yield?" She walks to the eight paragraphs that answer it, even though none contains your exact words. That librarian is what we are building. The technical name is RAG, retrieval-augmented generation. "Retrieval" is the librarian finding the paragraphs. "Generation" is a language model writing an answer from them, with a footnote to each one.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 6 (2026-09-14)

Here are the words you will meet, each with the librarian's version.

| Term | Plain meaning | The librarian's version |
|---|---|---|
| Token | A word piece, roughly four characters. | The unit she counts in. |
| Chunk (passage) | One paragraph-sized slice of a document, 800 to 1,200 tokens here. | One card in her memory. |
| Embedding (vector) | A list of numbers that places a chunk where similar meanings sit close together. | Where the card sits on a shelf sorted by meaning, not alphabet. |
| Dimensions | How many numbers are in that list. Ours have 1,024. | How many directions the shelf runs in. |
| Cosine similarity | How closely two vectors point the same way. 1.0 is same meaning, 0 is unrelated. | How near two cards sit. |
| Vector database (index) | A service that stores the vectors and returns the nearest ones to a question, fast. | Her shelf, plus her speed. |
| Dense search | Search by meaning, using the vectors. | "Cards about this idea." |
| Sparse search (BM25) | Search by exact words: does the phrase appear? | "Cards containing the word Almarai." |
| Hybrid search | Dense and sparse run together and the lists are merged. | Memory and card catalog, both. |
| Reranker | A slower model that reads the question and each candidate together and re-scores them. | Fifty cards on the desk, the best eight kept. |
| Citation | Document id, page and position stored with every chunk. | The stamp on the back of every card. |
| Context window | The most tokens a model can read in one call. | How much fits on the desk. |

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 6; docs/plan.md, section 10.4 (2026-09-14)

Why a second pass? Nearest in meaning is not always most useful. So the system over-fetches, say the top 50, and lets the reranker read each one properly. Keeping 5 to 8 is the 2026 default. Why hybrid? Embeddings are fuzzy about exact names. In our corpus, 101 files say "sales to capital", 97 say "sales/capital" and 4 say "sales-to-capital". Meaning-based search treats all three as one idea, which is good. But a ticker, a rating like "Baa3" or a file name like "fcffsimpleginzu" must match letter for letter. Keyword search does that.

Source: grep over /Users/siddharth/Downloads/financeMD/ (2026-09-14); /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, section 5d

## Why this tool now (for this project)

The corpus is too big to read in one go. The markdown mirror of Damodaran's site, blog and packets is about 21.0 million tokens across 3,916 files. His 1,477 YouTube transcripts add about 18.0 million. After the recommended drops the total is about 29.7 million tokens. The largest context window for sale today is 2,000,000 tokens (Grok 4.20 on OpenRouter). The corpus is fifteen times larger than that window. No model can read it in a single call, at any price.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bfxevcj1s.txt, section 1; bcy86uopa.txt, section 6 (2026-09-14)

Even where a window is big enough, the price is not. One question, answered three ways:

| Strategy | Input tokens | On GLM-5.3-Flash | On GLM-5.3 |
|---|---|---|---|
| RAG: 8 chunks of 800 tokens, a 1,500-token system prompt, a 100-token question | 8,000 | $0.00155 | $0.0143 |
| Stuff one 200,000-token lecture packet | 200,000 | $0.0304 | $0.283 |
| Stuff the whole corpus, 15 calls plus a synthesis | 30,000,000 | $4.50 | not quoted |

Stuffing a packet costs 19.6 times a RAG answer on the same model. Stuffing the corpus costs about 2,900 times. The same question on Claude Fable 5.1 would cost $300. Building the whole index costs $0 on Voyage's free allowance. So RAG pays for itself on the first question.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, section 6 (2026-09-14)

Three more reasons are about correctness. RAG returns chunk ids you can print as footnotes, and every claim here must be cited. Chunks carry a vintage label, so the system filters to one dated snapshot before the model sees anything. That is how you avoid mixing the 3.95%, 4.58% and 4.75% risk-free rates from the three 2026 files. And a question costs the same whether the index holds 30 million or 300 million tokens, because it only fetches eight chunks. That is the honest answer to "does it scale".

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, section 6; /Users/siddharth/Valuation/docs/read-this-first.md, sections 3.2 and 5 (2026-09-14)

One practical fact decides the vendor list. OpenRouter, which serves every language model in this system, offers zero embedding models and zero rerankers, verified across all 445 models in its catalog. So embeddings and reranking need a second vendor. That vendor is Voyage, and the vectors live in Pinecone.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, section 4 and 5 (2026-09-14)

## How it is used in this project

Nothing below is built yet. Milestone 2 will build it, and this section describes what it will do. The librarian is one box on the Architecture board (https://www.figma.com/board/DtFTvDZeSQpuKLM5tavDUT) and the "retrieve passages" step on the Memo pipeline board (https://www.figma.com/board/LGcrXp6yT3fh4O2IV3mEY8).

### The corpus, in tiers

The corpus goes in by tiers, best answers per token first. Tier 1 is the blog posts. Tier 2 is the book, the lecture packets with speaker notes, and the exams. Tier 3 is the dataset rows rewritten as sentences. Tier 4 is the transcripts, after a punctuation pass. Milestone 2 will index tiers 1 and 3 first and prove the pipeline on those. Transcripts come last because YouTube's machine-made captions have no punctuation, are all lowercase, and carry 10 to 20 percent classroom chatter. Cleaning 18 million transcript tokens with GLM-5.3-Flash in batch mode, a slower queue at half price, is priced at about $11.25.

Source: docs/plan.md, sections 5 (M2) and 10.4; bfxevcj1s.txt, section 2(f); bcy86uopa.txt, section 7 row (b) (2026-09-14)

### Cleaning before indexing

The corpus survey found rubbish that would poison retrieval if indexed as is. The cleaning steps are:

- Drop the 194 blog `index.md` archive pages. They reprint full posts and are exactly half of the blog bucket by bytes.
- Drop `damodaran/pc/archives/`, 1,647 files of historical numeric tables. They belong in the database, not the index.
- Strip in place: Blogger `<div>` wrappers, dead image links, the "An error occurred" YouTube embed blocks, the navigation header, and `**Damodaran<N>Aswath**` header artifacts in packets.
- Repair the book's broken ligatures before indexing it. A ligature is a joined letter pair such as "fi", which the converter turned into the replacement symbol U+FFFD. Also skip its first 682 lines of contents and lists.
- In transcripts, remove `[Music]` markers and bare "yes / right / okay" filler lines.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bfxevcj1s.txt, sections 4 and 5 (2026-09-14)

### Chunks and their labels

Chunking follows the shape of each source. A blog post is split on its sub-headings, never across posts, with the title and date prepended to every chunk. A slide deck keeps one slide and its speaker notes together, because the `### Notes:` block under a slide is where he explains why. Exams join a question with its solution. Transcripts become 60 to 90 seconds of speech, about 800 tokens, with 20 percent overlap. Every chunk carries metadata: `source_url`, `title`, `date`, `doc_type`, `license_class`, `vintage`, `asr`, `region` and `company`. Two labels do the most work. `author` is Damodaran only for his own words, so a filing or press clipping can never be quoted as his view. `year` lets the reranker prefer a 2026 packet over a 2025 one.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bfxevcj1s.txt, section 6; docs/plan.md, section 10.4; /Users/siddharth/Downloads/financeMD/damodaran/pptfiles/val3E/valpacket2spr25.md (2026-09-14)

### The license fence

Every chunk has a license class, and the index admits four of the seven. `public_domain` (SEC filings), `damodaran_public` (his posts and datasets), `open_access` (RBI yields, arXiv, SSRN author copies) and `asr_youtube` (auto-captions, marked as approximate wording) go in. `licensed_personal` (EODHD, a broker's API), `proprietary_personal` (your Bloomberg notes) and `link_only` (books, paid newsletters) stay out. The fence is a database rule on the `chunk_manifest` table in Neon, a CHECK constraint that refuses a row with a forbidden class. It is not a habit you must remember. Think of an allergen label on every ingredient rather than on the finished cake. Because the label is on each chunk, "can I show this answer to someone else?" becomes a query, not an audit.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, section 3.3; docs/plan.md, sections 10.1 and 10.3; bj0fbejiq.txt, CHECK 3 section 7 (2026-09-14)

### Pinecone's role, Voyage's role, and what is free

Voyage turns text into vectors and re-scores candidates. The embedding model is `voyage-context-4`. It produces 1,024-number vectors, accepts up to 32,000 tokens of input, and embeds each chunk aware of its neighbors. That neighbor awareness is what rescues a transcript chunk that makes no sense on its own. The reranker is `rerank-3`. Voyage gives 200 million free tokens per account across its v4 models. Embedding our 30 million tokens would cost 30 × $0.12, which is $3.60 at list price, and $0 inside the free allowance. Reranking 50 candidates of 800 tokens is 40,000 tokens per question, about $0.002 at list price, and free for roughly the first 5,000 questions.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, sections 5b, 5c and 5d (2026-09-14)

Pinecone stores the vectors and answers "which are the nearest?" It is a serverless index, meaning you never run or size a machine. Document A specifies one index, 1,024 dimensions, cosine similarity, region `us-east-1`. The Starter plan costs $0, needs no card, and includes 2 GB of storage, 2 million write units and 1 million read units a month. Our 60,000 chunks at 1,024 dimensions are about 245 MB of raw vectors, perhaps 400 to 600 MB with metadata, so they fit. Loading them uses about 3 percent of a month's free writes. A sparse companion model, `pinecone-sparse-english-v0`, provides the keyword half of hybrid search. If storage or reads ever overflow, the upgrade is Builder at $20 a month.

Source: /Users/siddharth/Valuation/docs/read-this-first.md, sections 10 and 12; bcy86uopa.txt, sections 5a, 5c and 5d (2026-09-14)

### Answering a question, step by step

1. Classify the question. If it is about one document ("summarize this packet"), fetch the whole document and give it to the model in one call. GLM-5.3-Flash's 1.31-million-token window holds a packet, and chopping one argument into chunks would lose it.
2. If it spans the corpus ("when did he change the India ERP?"), embed the question with Voyage.
3. Hybrid retrieve the top 50 chunks from Pinecone, filtered by license class, and by vintage or region when the question needs it.
4. Rerank the 50 down to 8 with `rerank-3`.
5. Send the 8 chunks, a system prompt and the question to GLM-5.3 through OpenRouter. The answer must cite chunk ids. An uncited claim is rejected.
6. Log the call in Langfuse, the tracing and evals tool covered in the evals chapter. About 40 of his exam questions, with solutions, are held out as the test paper, and Kimi K3 grades the answers as judge.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bcy86uopa.txt, section 6; bfxevcj1s.txt, section 5 item 10; docs/plan.md, sections 10.4 and 10.5 (2026-09-14)

### The rule: retrieval finds the paragraph; the database holds the number

This is the one rule to carry out of the chapter. RAG is for narrative and reasoning: why he treats country risk the way he does, what "sales to capital" means, how a story becomes a driver. The database in Neon is the system of record for anything the calculator multiplies. System of record means the one place where a fact is the truth, and everything else is a copy. A figure never travels from a retrieved chunk into a valuation directly. It is first written to a Postgres row with its source, license class and vintage, and the memo writer's numbers go to `valuation_inputs`, never parsed from prose. "What is the India default spread today?" is routed to the database tool, not the index. Tables retrieve badly as text, and the database will hold the July 2026 value of 1.75% once Milestone 2 seeds it.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 sections 6 and 7; bfxevcj1s.txt, section 6 retrieval notes; docs/plan.md, section 10.5; bafb6h9rb.txt, India rows (2026-09-14)

A concrete example. The July 2026 country-risk post says that "country risk exposure comes less from where the company is incorporated and more from where it operates". That is a paragraph the librarian should find when you ask how to treat a Siemens factory in India. The 1.75% default spread that goes with it is a number, and it will live in the `country_risk` table with a vintage id.

Source: /Users/siddharth/Downloads/financeMD/damodaran/blog/2026/07/country-risk-drivers-measures-and.md, line 172 (2026-07-15); docs/plan.md, section 10.3

### Why Pinecone, and not vectors inside Neon

One research report argued for `pgvector`, a Postgres extension that keeps vectors in the same database as the fundamentals. At 60,000 vectors, it said, we are about 200 times below the point where a dedicated vector database pays for itself, and SQL joins against the fundamentals tables come free. The plan chose Pinecone anyway: it was your preference, it is free at this size, and hybrid sparse-plus-dense search comes built in. The retriever sits behind one interface, so pgvector on Neon remains the fallback if two systems ever feel like a burden.

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/b31x0pyot.txt, section 6; docs/plan.md, section 7 (2026-09-14)

## Learn it

All free. Hours are rough reading-and-tinkering estimates.

| # | Resource | Format | Hours | Why this one |
|---|---|---|---|---|
| 1 | https://www.pinecone.io/learn/series/rag/ | Article series | 3 | The best plain-English sequence from embeddings through chunking, retrieval and generation. Read it first. |
| 2 | https://www.pinecone.io/learn/series/rag/rerankers/ | Article with a notebook | 1 | Shows, with code, how much a reranking pass improves the chunks that reach the model. |
| 3 | https://docs.pinecone.io/guides/search/hybrid-search | Official docs | 1 | Sparse plus dense in one index, the pattern we need for tickers, ratings and file names. |
| 4 | https://docs.voyageai.com/docs/pricing | Official docs | 0.5 | Read the free allowance and prices yourself, then set the billing alert from Document A. |
| 5 | https://github.com/pgvector/pgvector | Repository README | 1.5 | The alternative we did not pick. Reading it explains what Pinecone does for us. |
| 6 | https://www.anthropic.com/news/contextual-retrieval | Article | 1 | Why a chunk embedded with knowledge of its neighbors retrieves better, the idea behind `voyage-context-4`. From my web knowledge, not the local reports; verify. |

Source: /Users/siddharth/.claude/projects/-Users-siddharth-Downloads/edcdeb19-7793-4e1b-9e73-4cf6186716bf/tool-results/bj0fbejiq.txt, CHECK 3 section 6 resource table; bcy86uopa.txt, source table (2026-09-14)

## 10-minute exercise

The point is to feel the difference between exact words and meaning, on the real corpus.

1. Run the three keyword searches below and note the counts. A keyword engine treats these as three different things.

```bash
cd /Users/siddharth/Downloads/financeMD
grep -ril "sales to capital" . | wc -l
grep -ril "sales/capital" . | wc -l
grep -ril "sales-to-capital" . | wc -l
```

2. Open one blog post and read one paragraph:

```bash
sed -n '172p' damodaran/blog/2026/07/country-risk-drivers-measures-and.md
```

3. On paper, write the question that paragraph answers, in your own words, without reusing his. That rewrite is what an embedding captures: the idea, not the spelling.

4. Write the citation you would store: file path, line number, the date from the front matter (the header block between `---` lines at the top of the file), and the license class (`damodaran_public`).

5. Decide: is anything in that paragraph a number the calculator would multiply? If not, it belongs to the librarian. If yes, it belongs in a database row first.

## Done when

- You can explain chunk, embedding, cosine similarity, reranker and hybrid search using the librarian, without notes.
- You can say why the corpus cannot be read in one call, and what a RAG answer costs on GLM-5.3-Flash versus stuffing a packet.
- You can name the four license classes that enter the index and the three that never do, and you know the fence is a database rule.
- You can state which Voyage model embeds, which reranks, and what the free allowance is.
- You can repeat "retrieval finds the paragraph; the database holds the number" and give one example of each.
- You have done the exercise and kept the paper.
