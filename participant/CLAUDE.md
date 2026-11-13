# Starter CLAUDE.md: Automation beyond the chatbot

Instructions for Claude. Put this file in the folder you work in with Claude Code, or paste it into a Claude Project's instructions.

## Words we use

- **Scripting:** AI may write the script, its tests and its sample data. No LLM runs when the script runs.
- **AI in the loop:** an LLM is called every time the task runs.
- **Hybrid:** some steps are scripting, some are AI in the loop.
- **Local model:** a machine learning model that runs on my computer (OCR, speech-to-text, a classifier). Not an LLM. Zero tokens. Counts as scripting.
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
7. Wait for my OK before building.

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

## When I ask you to do a task directly in chat

- If it looks repeatable and would cost fewer tokens as a script, say so before doing it.
- If a file is large, offer a script that pulls out only the part that needs your judgment.
