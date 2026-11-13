# Automation beyond the chatbot

Workshop materials for advanced AI users in accounting: when to script, when to put AI in the loop, and how to combine them (hybrid) to save tokens.

## Start here

**Open `index.html`** in a browser. It shows every handout on one page, with a menu on the left.

- On GitHub: download the repo (Code → Download ZIP), unzip it, then double-click `index.html`.
- In a clone: double-click `index.html`, or run `start index.html` (Windows) / `open index.html` (Mac).

## What's here

| Path | For | What it is |
|---|---|---|
| `participant/concepts.md` | Participants | The lessons: three buckets, "deterministic", data type, input/output, rules and their limits, tokens |
| `participant/venn.svg` | Participants | Venn diagram used in the concepts handout |
| `participant/examples.md` | Participants | Clear-cut examples, hard inputs, hybrid patterns, zero-token helpers |
| `participant/prompt-card.md` | Participants | Prompts to copy |
| `participant/CLAUDE.md` | Participants | Starter CLAUDE.md promised in the class description |
| `participant/homework.md` | Participants | Homework: a Python script as the output |
| `instructor/run-of-show.md` | Instructor | 60-minute timeline |
| `build.py` | Maintainers | Rebuilds `index.html` from the Markdown files |

The `participant/` folder is what will be copied to the public participant repo. `instructor/` stays private.

## Editing

1. Edit the Markdown files.
2. Rebuild the start page:
   a. `pip install markdown` (once)
   b. `python build.py`
3. Commit both the Markdown changes and `index.html`.

## Repo rules

- Keep people's names and personal information out of this repo.
- Don't link to Claude chats or artifacts from this repo.
