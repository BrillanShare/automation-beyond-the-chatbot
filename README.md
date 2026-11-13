# Automation beyond the chatbot (development copy)

Private development copy of the workshop materials. Only the `participant/` folder is published: its contents are copied into a public repo, and that's all the instructor and participants use.

## Start here

**Open `participant/html/index.html`** in a browser. It shows every handout on one page.

## What's here

| Path | Published? | What it is |
|---|---|---|
| `participant/` | ✅ Yes | Everything participants and the instructor use; see `participant/README.md` |
| `participant/html/` | ✅ Yes | One-page view of the handouts, rebuilt with `python participant/html/build.py` |
| `instructor/run-of-show.md` | ❌ No | 60-minute timeline |
| `tools/make_illustrations.py` | ❌ No | Draws the document illustrations in `participant/` |
| `CLAUDE.md` | ❌ No | Instructions for Claude when working on this repo |

## Editing

1. Edit the Markdown files in `participant/`.
2. Run `python participant/html/build.py` to rebuild the one-page view. It stamps the build time in the page's banner.
3. Commit both.

## Publishing

Copy the contents of `participant/` (not the folder itself) into the root of the public repo.
