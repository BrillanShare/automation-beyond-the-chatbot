# Working on this repo

This file is for Claude when it maintains this repo. The starter file for your own work is `starter-claude-md/CLAUDE.md`.

- Everything in this repo is shared with workshop participants. Keep client data, personal information, passwords and keys out of it.
- Don't link to Claude chats or artifacts from this repo.
- After editing any Markdown handout, run `python web-pages/rebuild_pages.py` and commit the refreshed `web-pages/legacy-text-only.html` and `web-pages/index.html` with it (the script also copies the prompts from `prompt-card.md` into `index.html`). This applies to any agent or automation that changes the Markdown, not only people: rebuild so the page and its "last built" banner stay current.
- To add a handout, add it to the `PAGES` list in `web-pages/legacy-text-only.html`, then rebuild.
- `web-pages/index.html` is the infographic start page, drawn by hand. When a concept it shows changes in the Markdown, update it too. Keep it visual: short labels, no paragraphs; animations only where they show a verb being taught or help identify a noun.
- The document illustrations (`images/*.svg`) are drawn by `images/make_illustrations.py`. Edit the script and rerun it rather than editing those SVGs by hand.
- Every folder has a README saying what it holds and what to do with it. When you add, remove or repurpose a file, update that folder's README.
