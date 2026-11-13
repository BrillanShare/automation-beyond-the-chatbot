# Automation beyond the chatbot

Workshop materials for advanced AI users in accounting: when to script, when to put AI in the loop, and how to combine them (hybrid) to save tokens.

## For participants

**Start here: open `html/index.html`** in a browser. It's the workshop as a series of animated infographics.

1. Get the files.
    - a. On GitHub: **Code → Download ZIP**, then unzip it.
    - b. Or clone the repo with GitHub Desktop.
2. Double-click `html/index.html`.

| File | What it is |
|---|---|
| `html/index.html` | The workshop as animated infographics |
| `cheat-sheet.md` | One page: the three buckets, the question to ask, hard inputs, tokens, the first prompt |
| `handout.md` | The full text: concepts, examples, hard inputs, tokens, cost growth, which task to convert first, hybrid patterns, local models, controls, tests, and a vote |
| `prompt-card.md` | Prompts to copy and adapt |
| `starter/CLAUDE.md` | Starter instructions for Claude that apply the workshop's principles |
| `homework.md` | Homework: a Python script as the output |
| `html/text.html` | All the Markdown handouts on one page |

GitHub and Claude both show the `.md` files formatted, with the diagrams.

**Using the starter CLAUDE.md:**

- **Claude Code:** copy `starter/CLAUDE.md` into the folder you work in. Claude reads it automatically.
- **Claude app:** paste its contents into a Project's instructions.
- **Learn more:** [How Claude remembers your project](https://code.claude.com/docs/en/memory)

## For the instructor and facilitator

| File | What it is |
|---|---|
| `facilitator/run-of-show.md` | 60-minute timeline, roles, what to skip if time runs short, live-demo checklist |
| `demo.md`, `demo/` | Two live demos (all AI → all script, all AI → hybrid) with prompts, sample files and backup scripts |
| `html/index.html` | Panels to show on screen; each animated panel has a Replay button |

## For agents and maintainers

Instructions for Claude when it works on this repo are in the root `CLAUDE.md`. In short:

| File | What it is |
|---|---|
| `CLAUDE.md` | Rules for working on this repo (not the starter file) |
| `html/build.py` | Rebuilds `html/text.html` from the Markdown and stamps the build time in its banner. Python only. |
| `tools/make_illustrations.py` | Draws the document illustrations (`*.svg`) |
| `html/vendor/` | [marked](https://github.com/markedjs/marked), used by `text.html` to show Markdown (MIT license) |

After editing a Markdown handout, run `python html/build.py`.
