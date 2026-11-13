# Working on this repo

- Only `participant/` is published: its contents are copied into a public repo, and that's all the instructor and participants use. Anything they need must live in `participant/`.
- `participant/CLAUDE.md` is the starter file for participants, not instructions for working on this repo.
- Don't link to Claude chats or artifacts from this repo.
- After editing any Markdown file in `participant/`, run `python build.py` and commit the refreshed `participant/index.html` with it.
- To add a handout, add it to the `PAGES` list in `participant/index.html`, then run `python build.py`.
- Keep one open pull request at a time; add new changes to it.
- Pull request text and GitHub comments must say they're from Claude.
