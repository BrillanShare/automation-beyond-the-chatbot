# Cheat sheet

## Three buckets

| Bucket | At run time | Tokens per run |
|---|---|---|
| 📜 Scripting | Code runs; AI may have written it, but no LLM runs now | None |
| 🤖 AI in the loop | An LLM is called every run | Small to large |
| 🔀 Hybrid | Script for the routine part, LLM for the slice that needs judgment | Only the slice |

## The question to ask

**Does any step need an LLM's judgment at run time?**

- Same shape every time, known cases → 📜 Scripting
- Open-ended wording, varied documents, judgment calls → 🤖 AI in the loop
- Mostly the same shape, some messy cases → 🔀 Hybrid

## Words

- **Deterministic:** same inputs → same output, every time. AI in the loop never is.
- **Data type doesn't decide the bucket.** Numbers can need AI; language can be scripted.
- **Input/output defines the task, not the bucket.** Same statements in, same form out: scripting for one bank's text PDFs, hybrid for scans from many banks.

## ⚠️ Hard inputs we forget

- Scans and phone photos instead of text PDFs
- One vendor, many spellings
- Rules lists that keep growing
- Merged cells, extra header rows, totals mid-table
- A layout that changed
- Duplicates and password-protected files

## Tokens

- AI in the loop: every run. Scripting: once, to build.
- Big files: a script reads them for free; pasting them into chat burns tokens.
- Hybrid: send the LLM only the slice that needs judgment.

## Is it worth converting?

- Return = the shape of today's token line × your volume (how many per run × how often)
- Volume first, chart second
- Converting that changes the shape beats converting that nudges it
- Below break-even: leave it with AI, check again when volume grows
- Ask Claude to plot it for your task ("Plot it" on the prompt card)

## Before you rely on a script

- Fail loudly: rows it can't process go on a list, never skipped silently
- Control totals: rows in = rows out + rejected; amounts tie
- Money math: how is it rounded, and does it match Excel?
- Safe to run twice; never overwrites an input without asking first

## The prompt to use first

> Before building anything: restate this task as inputs → outputs. List the hard inputs, not only the typical ones. Propose the design with the least AI in the loop. Label each step Scripting, Local model or AI in the loop, and say why. Rate each step's tokens per run: none, small or large. Wait for my OK.
