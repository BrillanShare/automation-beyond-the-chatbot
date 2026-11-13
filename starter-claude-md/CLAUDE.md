# Starter CLAUDE.md: Automation beyond the chatbot

Instructions for Claude. Put this file in the folder you work in with Claude Code, or paste it into a Claude Project's instructions.

## Words we use

- **Scripting:** AI may write the script, its tests and its sample data. No LLM runs when the script runs.
- **AI in the loop:** an LLM is called every time the task runs.
- **Hybrid:** some steps are scripting, some are AI in the loop.
- **Local model:** a machine learning model that runs on my computer (optical character recognition, speech-to-text, a classifier). Not an LLM. Zero tokens. Counts as scripting.
- **Deterministic:** the same inputs always give the same output. AI in the loop is never deterministic.

## Before building anything

1. Restate the task as inputs → outputs.
2. List the hard inputs, not only the typical ones, and ask me which ones actually happen and how often:
    - a. blurry or scanned PDFs, photos, handwriting
    - b. layout changes, extra header rows, merged cells, totals inside the data
    - c. the same name spelled several ways, negative numbers in parentheses
    - d. missing, duplicate or password-protected files
3. Propose the design with the least AI in the loop.
4. Label every step: **Scripting**, **Local model** or **AI in the loop**, and say why.
5. Rate each step's tokens per run: **none / small / large**. Say what makes the cost grow (number of documents, file size).
6. If more than one design is reasonable, compare two or three. Rank them by tokens per run, reliability on the hard inputs, and how hard they are to maintain.
7. Say whether converting is worth it at my volume:
    - a. Ask me how many lines, documents or clients each run handles and how often I run it. My volume over a year is the two multiplied. Don't guess.
    - b. Describe how the tokens grow with that volume today, and under the design you propose. Flag any step that compares every item with every other item.
    - c. Say whether my volume is past break-even, in relative terms. If it isn't, say so and suggest leaving the task as it is.
    - d. Only discuss growth for steps that use tokens.
    - e. Don't show me a chart before you know my volume, or when the designs differ too little at my volume to matter. Say so in a sentence instead.
    - f. For a step that compares every item with every other, use the count in one run, not the yearly total.
8. Wait for my OK before building.

## When building

- Write Python unless I ask for something else.
- Explain each script in plain language for someone without a computer science background: what it reads, what it does, what it writes, what can go wrong.
- Let the script read large files on my computer. Don't ask me to paste large files into chat.
- Keep fetching (internet, clock, files) separate from calculating, so the calculations can be tested on fixed inputs.
- Between steps, use a fixed hand-off format, such as a CSV with named columns.
- Check AI-in-the-loop output before a script uses it. Send anything that fails the check to a review list for me.
- Before writing the script, agree with me on what "done" looks like: sample inputs, including hard ones, and the expected outputs.
- Give me numbered steps to run it.
- Keep client personal information and passwords or keys out of scripts and out of prompts.

## Controls every script needs

- **Fail loudly.** Never skip a row silently. Write rows the script can't process to a review list, with the reason.
    - When the script fails or doesn't finish, say so in **RED, BOLD CAPITAL LETTERS**.
    - When it worked but I should know something, use **⚠️ yellow bold** text.
- **Control totals.** After each run, report rows in, rows out and rows rejected, and whether the amounts tie.
- **Money math.** Store money as exact decimals, not floating point. State the rounding rule, and match Excel's ROUND unless I say otherwise.
- **Safe to run twice.** A rerun must not create duplicate entries.
- **Never overwrite or delete an input file without asking first.** Write results to a new file.
- **Text that looks like numbers.** Read account numbers, IDs and ZIP codes as text. Tell me how dates are read.
- **Settings and rules out of the code.** Keep rates, thresholds, cutoff dates and rules in a settings file, not inside the script.
    - I review and approve the written rules before the script uses them, so they're fixed, not reinvented on each run.
    - Each settings file has a "review by" date. After that date, the script shows a ⚠️ yellow warning that some inputs may be out of date and need my review.
- **Run log.** Each run records the date, input file, row counts and script version.
- **What it installs and sends.** Before running, tell me what the script installs and whether it sends data anywhere.
- **Short output when you run it.** When you run a script for me, especially with AI in the loop before or after it, have it print only a short summary (counts, the leftovers). Write full results to a file. Everything you read back uses tokens.

## Tests

- Save the agreed sample inputs and expected outputs as files in a `tests` folder next to the script, with a way to run them all at once.
- Put a `CLAUDE.md` in the script's folder that explains the testing strategy, so any future Claude that changes the script finds it.
- Before changing the script, agree with me on which cases the tests should cover, including any new ones.
- After any change, rerun all the tests and tell me if any result changed.
- When a bug turns up, add a test for it before fixing it.
- Tell me what the tests don't cover yet.

## When I ask you to do a task directly in chat

- If it looks repeatable and would cost fewer tokens as a script, say so before doing it.
- If a file is large, offer a script that pulls out only the part that needs your judgment.
