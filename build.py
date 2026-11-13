"""Refresh the saved copy inside participant/index.html.

participant/index.html reads the Markdown files directly when it's served by a
web server. When someone opens it by double-clicking, browsers block that, so
the page falls back to a copy of the Markdown saved inside it. Run this after
editing any Markdown file in participant/ to refresh that copy:

    python build.py
"""
import json
import re
from pathlib import Path

FOLDER = Path(__file__).parent / "participant"
PAGE = FOLDER / "index.html"


def main():
    html = PAGE.read_text(encoding="utf-8")
    # The page's own list of Markdown files, so there's only one list to keep.
    files = re.findall(r'\["([\w.-]+\.md)",', html)
    saved = {f: (FOLDER / f).read_text(encoding="utf-8") for f in files}
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
    PAGE.write_text(html, encoding="utf-8")
    print(f"Saved {len(files)} Markdown files into {PAGE.relative_to(FOLDER.parent)}")


if __name__ == "__main__":
    main()
