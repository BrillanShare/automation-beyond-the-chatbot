"""Build index.html: the start page that shows every handout on one page.

Run after editing any .md file:
    pip install markdown
    python build.py
"""
import html
from pathlib import Path

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent

# (file, title, audience) in the order they appear on the page
PAGES = [
    ("participant/handout.md", "Concepts and examples", "Participants"),
    ("participant/prompt-card.md", "Prompt card", "Participants"),
    ("participant/CLAUDE.md", "Starter CLAUDE.md", "Participants"),
    ("participant/homework.md", "Homework", "Participants"),
    ("instructor/run-of-show.md", "Run of show", "Instructor only"),
]

CSS = """
:root { color-scheme: dark; }
body { margin: 0; background: #0d1117; color: #e6edf3;
  font: 16px/1.55 "Segoe UI", Helvetica, Arial, sans-serif; display: flex; }
nav { position: sticky; top: 0; height: 100vh; width: 230px; flex: none;
  padding: 20px 16px; box-sizing: border-box; background: #161b22; border-right: 1px solid #30363d; }
nav h1 { font-size: 17px; margin: 0 0 14px; }
nav .group { color: #8b949e; font-size: 12px; text-transform: uppercase; margin: 16px 0 4px; }
nav a { display: block; color: #58a6ff; text-decoration: none; padding: 3px 0; }
main { flex: 1; min-width: 0; padding: 24px 40px 80px; max-width: 1200px; }
section { border-bottom: 1px solid #30363d; padding-bottom: 28px; margin-bottom: 28px; }
.badge { display: inline-block; font-size: 12px; padding: 2px 8px; border-radius: 10px; margin-bottom: 6px; }
.Participants { background: #1f6feb33; color: #58a6ff; }
.Instructor { background: #f8514933; color: #f85149; }
.src { color: #8b949e; font-size: 13px; }
h1, h2, h3 { line-height: 1.25; }
table { border-collapse: collapse; width: 100%; table-layout: auto; margin: 10px 0; }
th, td { border: 1px solid #30363d; padding: 6px 10px; text-align: left; vertical-align: top;
  overflow-wrap: break-word; }
th { background: #161b22; }
code { background: #161b22; padding: 1px 5px; border-radius: 4px; }
blockquote { margin: 10px 0; padding: 8px 14px; border-left: 4px solid #3fb950; background: #161b22; }
img { max-width: min(100%, 900px); height: auto; }
ol ul { list-style: none; padding-left: 1.4em; }
.c-script { background: #1f6feb26; } .c-script-h { background: #1f6feb55; }
.c-ai { background: #f8514926; } .c-ai-h { background: #f8514955; }
.c-hybrid { background: #8957e530; } .c-hybrid-h { background: #8957e560; }
.c-local { background: #2ea2a326; } .c-local-h { background: #2ea2a355; }
.c-warn { background: #d2992226; } .c-warn-h { background: #d2992255; }
.t-good { background: #2ea04333; color: #56d364; font-weight: 600; }
.t-bad { background: #f8514926; }
details { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 8px 14px; }
summary { cursor: pointer; color: #58a6ff; font-weight: 600; }
"""


def render(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
    # Image paths in handouts are relative to their own folder.
    folder = Path(path).parent.as_posix()
    for svg in ("venn.svg", "buckets.svg"):
        body = body.replace(f'src="{svg}"', f'src="{folder}/{svg}"')
    return color_tables(body)


# Color carries meaning: blue = scripting, red = AI in the loop,
# purple = hybrid, teal = local model, amber = hard input.
HEADER_CLASSES = [
    ("ai-in-the-loop", "c-ai"), ("ai in the loop", "c-ai"),
    ("scripting", "c-script"), ("hybrid", "c-hybrid"),
    ("local model", "c-local"), ("hard input", "c-warn"),
]
CELL_PREFIXES = [("📜", "c-script"), ("🤖", "c-ai"), ("🔀", "c-hybrid"), ("💻", "c-local")]


def color_tables(body):
    soup = BeautifulSoup(body, "html.parser")
    for table in soup.find_all("table"):
        headers = [th.get_text().strip().lower() for th in table.find_all("th")]
        col_class = {}
        for i, h in enumerate(headers):
            for key, cls in HEADER_CLASSES:
                if key in h:
                    col_class[i] = cls
                    break
        for i, th in enumerate(table.find_all("th")):
            if i in col_class:
                th["class"] = th.get("class", []) + [col_class[i] + "-h"]
        for tr in table.find_all("tr"):
            for i, td in enumerate(tr.find_all("td")):
                text = td.get_text().strip()
                cls = col_class.get(i)
                for prefix, pcls in CELL_PREFIXES:
                    if text.startswith(prefix):
                        cls = pcls
                if text in ("None", "✅ Yes"):
                    cls = "t-good"
                if text.startswith("❌"):
                    cls = "t-bad"
                if cls:
                    td["class"] = td.get("class", []) + [cls]
    return str(soup)


def main():
    nav, sections = [], []
    last_group = None
    for i, (path, title, audience) in enumerate(PAGES):
        if audience != last_group:
            nav.append(f'<div class="group">{html.escape(audience)}</div>')
            last_group = audience
        anchor = f"s{i}"
        nav.append(f'<a href="#{anchor}">{html.escape(title)}</a>')
        cls = audience.split()[0]
        sections.append(
            f'<section id="{anchor}"><span class="badge {cls}">{html.escape(audience)}</span>'
            f' <span class="src">{html.escape(path)}</span>{render(path)}</section>'
        )
    page = (
        "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "<title>Automation beyond the chatbot</title>"
        f"<style>{CSS}</style></head><body>"
        f"<nav><h1>Automation beyond the chatbot</h1>{''.join(nav)}</nav>"
        f"<main>{''.join(sections)}</main></body></html>\n"
    )
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    print("Wrote index.html")


if __name__ == "__main__":
    main()
