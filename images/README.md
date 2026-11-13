# images/

Diagrams and illustrations used in the handouts (`../handout.md`, `../demo.md`) and the web pages in `../web-pages/`.

**Don't edit these by hand.** They're drawn by `make_illustrations.py` in this folder (all except `buckets.svg` and `venn.svg`, which are hand-written SVG). To change one, edit the script, or ask an LLM to, and run it from the repo root:

    python images/make_illustrations.py

**Scripting in action:** an LLM wrote `make_illustrations.py`. Now anyone can change it by hand, or ask any LLM to change it, and redrawing every diagram uses no tokens.
