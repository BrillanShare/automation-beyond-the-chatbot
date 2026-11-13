# Automation beyond the chatbot

Materials for advanced AI users in accounting: when to script, when to put AI in the loop, and how to combine them (hybrid) to save tokens.

## Start here

**Open `index.html`** in a browser. It shows every handout on one page, with a menu on the left.

1. Get the files.
    - a. On GitHub: **Code → Download ZIP**, then unzip it.
    - b. Or clone the repo with GitHub Desktop.
2. Double-click `index.html`.

## What's here

| File | What it is |
|---|---|
| `index.html` | Start page: all the handouts on one page |
| `cheat-sheet.md` | One page: the three buckets, the question to ask, hard inputs, tokens, the first prompt |
| `handout.md` | Concepts with examples: three buckets, "deterministic", what a script can't do, hard inputs, tokens, hybrid patterns, local models, and a vote with hints |
| `demo.md`, `demo/` | One task three ways (all AI, hybrid, all script) with sample files and a backup script |
| `prompt-card.md` | Prompts to copy and adapt |
| `CLAUDE.md` | Starter instructions for Claude that apply the workshop's principles |
| `homework.md` | Homework: a Python script as the output |
| `*.svg` | Diagrams and illustrations used in the handout |
| `vendor/` | [marked](https://github.com/markedjs/marked), the library the start page uses to show Markdown (MIT license) |

## Using the starter CLAUDE.md

- **Claude Code:** copy `CLAUDE.md` into the folder you work in. Claude reads it automatically.
- **Claude app:** paste its contents into a Project's instructions.
- **Learn more:** [How Claude remembers your project](https://code.claude.com/docs/en/memory)

## Editing the handouts

The start page reads the Markdown files directly when it's served by a web server, so edits show up when you refresh:

1. Open a terminal in this folder.
2. Run `python -m http.server 8000`.
3. Open http://localhost:8000 in a browser.

When opened by double-clicking, the page shows the version of the handouts saved inside it, and edits to the .md files won't appear there. When it's served, the bottom of the menu says "Live".
