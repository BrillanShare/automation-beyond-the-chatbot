# Automation beyond the chatbot (development copy)

Private development copy of the workshop materials. Only the `participant/` folder is published: its contents are copied into a public repo, and that's all the instructor and participants use.

## Start here

**Open `participant/index.html`** in a browser. It shows every handout on one page.

- Double-click it to see the copy saved inside the page.
- To see edits to the Markdown files as soon as you refresh, serve the folder:
    - `cd participant`
    - `python -m http.server 8000`
    - open http://localhost:8000

## What's here

| Path | Published? | What it is |
|---|---|---|
| `participant/` | ✅ Yes | Everything participants and the instructor use; see `participant/README.md` |
| `instructor/run-of-show.md` | ❌ No | 60-minute timeline |
| `build.py` | ❌ No | Refreshes the saved copy inside `participant/index.html` |
| `CLAUDE.md` | ❌ No | Instructions for Claude when working on this repo |

## Editing

1. Edit the Markdown files in `participant/`.
2. Run `python build.py` to refresh the saved copy inside `participant/index.html`.
3. Commit both.

## Publishing

Copy the contents of `participant/` (not the folder itself) into the root of the public repo.
