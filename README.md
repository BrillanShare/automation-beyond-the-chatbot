# Automation beyond the chatbot (development copy)

Private development copy of the workshop materials. Only the `participant/` folder is published: its contents are copied into a public repo, and that's all the instructor and participants use.

## Start here

**Open `participant/html/index.html`** in a browser: the workshop as animated infographics. `participant/html/text.html` has every handout on one page.

## What's here

| Path | Published? | What it is |
|---|---|---|
| `participant/` | ✅ Yes | Everything participants and the instructor use; see `participant/README.md` |
| `participant/html/` | ✅ Yes | `index.html` (infographics, drawn by hand) and `text.html` (the handouts, rebuilt with `python participant/html/build.py`) |
| `instructor/run-of-show.md` | ❌ No | 60-minute timeline |
| `tools/make_illustrations.py` | ❌ No | Draws the document illustrations in `participant/` |
| `CLAUDE.md` | ❌ No | Instructions for Claude when working on this repo |

## Editing

1. Edit the Markdown files in `participant/`.
2. Run `python participant/html/build.py` to rebuild `text.html`. It stamps the build time in the page's banner.
3. If the change affects a concept shown in `participant/html/index.html`, update that page too.
4. Commit them together.

## Publishing

Copy the contents of `participant/` (not the folder itself) into the root of the public repo.
