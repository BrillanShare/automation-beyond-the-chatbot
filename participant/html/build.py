"""Rebuild index.html from the Markdown files in the folder above.

index.html shows a copy of those Markdown files. It doesn't update by itself.
Run this when you've edited the Markdown and want the page to match:

    python build.py

It needs only Python; nothing to install. It also stamps the date and time it
ran into the banner at the top of the page.
"""
import json
import re
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARKDOWN_FOLDER = HERE.parent
PAGE = HERE / "index.html"


def main():
    html = PAGE.read_text(encoding="utf-8")
    # The page's own list of Markdown files, so there's only one list to keep.
    files = re.findall(r'\["([\w.-]+\.md)",', html)
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
        raise SystemExit("Couldn't find the saved-copy markers in index.html")
    built = datetime.now().astimezone().strftime("%b %d, %Y %I:%M %p %Z").replace(" 0", " ")
    html, count = re.subn(
        r"<!--BUILT-AT-->.*?<!--/BUILT-AT-->",
        lambda m: "<!--BUILT-AT-->" + built + "<!--/BUILT-AT-->",
        html,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit("Couldn't find the built-at marker in index.html")
    PAGE.write_text(html, encoding="utf-8")
    print(f"Rebuilt index.html from {len(files)} Markdown files ({built})")


if __name__ == "__main__":
    main()
