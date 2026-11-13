"""Rebuild the copies of the Markdown that the web pages carry.

legacy-text-only.html shows a copy of the Markdown files in the folder above, and
index.html shows a copy of the prompts in prompt-card.md. Neither updates by
itself. Run this when you've edited the Markdown and want the pages to match:

    python rebuild_pages.py

It needs only Python; nothing to install. It also stamps the date and time it
ran into each page, so readers can see how current the copy is.
"""
import json
import re
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARKDOWN_FOLDER = HERE.parent
PAGE = HERE / "legacy-text-only.html"
INDEX = HERE / "index.html"


def stamp(html, built, name):
    html, count = re.subn(
        r"<!--BUILT-AT-->.*?<!--/BUILT-AT-->",
        lambda m: "<!--BUILT-AT-->" + built + "<!--/BUILT-AT-->",
        html,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit(f"Couldn't find the built-at marker in {name}")
    return html


def rebuild_index(built):
    """Copy each prompt's title and text from prompt-card.md into index.html."""
    card = (MARKDOWN_FOLDER / "prompt-card.md").read_text(encoding="utf-8")
    prompts = {int(n): (title, text) for n, title, text in
               re.findall(r"^## (\d+)\. (.+?)\n\n> (.+?)\n", card, re.M)}
    html = INDEX.read_text(encoding="utf-8")
    js = lambda x: json.dumps(x, ensure_ascii=False)
    for n, (title, text) in prompts.items():
        if n <= 12:  # [number, icon, title, text, ideas] in PROMPTS
            pattern = r'^(  \[%d, "[^"]*", )".*?", ".*?"(, \[)' % n
            repl = lambda m: m.group(1) + js(title) + ", " + js(text) + m.group(2)
        else:  # number: text in CTL_PROMPTS
            pattern = r'^(  %d: )".*?"(,?)$' % n
            repl = lambda m: m.group(1) + js(text) + m.group(2)
        html, count = re.subn(pattern, repl, html, count=1, flags=re.M)
        if count != 1:
            raise SystemExit(f"Couldn't find prompt {n} in index.html")
    INDEX.write_text(stamp(html, built, "index.html"), encoding="utf-8")
    return len(prompts)


def main():
    html = PAGE.read_text(encoding="utf-8")
    # The page's own list of Markdown files, so there's only one list to keep.
    files = re.findall(r'\["([\w./-]+\.md)",', html)
    saved = {f: (MARKDOWN_FOLDER / f).read_text(encoding="utf-8") for f in files}
    data = json.dumps(saved, ensure_ascii=False)
    data = data.replace("</", "<\\/").replace("<!--", "\\u003c!--")
    html, count = re.subn(
        r"/\*SAVED-COPY-START\*/.*?/\*SAVED-COPY-END\*/",
        lambda m: "/*SAVED-COPY-START*/" + data + "/*SAVED-COPY-END*/",
        html,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit("Couldn't find the saved-copy markers in legacy-text-only.html")
    built = datetime.now().astimezone().strftime("%b %d, %Y %I:%M %p %Z").replace(" 0", " ")
    PAGE.write_text(stamp(html, built, "legacy-text-only.html"), encoding="utf-8")
    print(f"Rebuilt legacy-text-only.html from {len(files)} Markdown files ({built})")
    n = rebuild_index(built)
    print(f"Copied {n} prompts from prompt-card.md into index.html")


if __name__ == "__main__":
    main()
