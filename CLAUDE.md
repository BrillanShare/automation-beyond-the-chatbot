# Working on this repo

- Only `participant/` is published: its contents are copied into a public repo, and that's all the instructor and participants use. Anything they need must live in `participant/`.
- `participant/CLAUDE.md` is the starter file for participants, not instructions for working on this repo.
- Don't link to Claude chats or artifacts from this repo.
- After editing any Markdown file in `participant/`, run `python participant/html/build.py` and commit the refreshed `participant/html/text.html` with it. This applies to any agent or automation that changes the Markdown, not only people: rebuild so the page and its "last built" banner stay current.
- To add a handout, add it to the `PAGES` list in `participant/html/text.html`, then rebuild.
- `participant/html/index.html` is the infographic start page, drawn by hand. When a concept it shows changes in the Markdown, update it too. Keep it visual: short labels, no paragraphs; animations only where they show a verb being taught or help identify a noun.
- Keep one open pull request at a time; add new changes to it.
- Pull request text and GitHub comments must say they're from Claude.
- The document illustrations in `participant/` are drawn by `tools/make_illustrations.py`. Edit the script and rerun it rather than editing those SVGs by hand.
