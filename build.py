"""Build index.html: the start page that shows every handout on one page.

Run after editing any .md file:
    pip install markdown
    python build.py
"""
import html
from pathlib import Path

import markdown

ROOT = Path(__file__).parent

# (file, title, audience) in the order they appear on the page
PAGES = [
    ("participant/concepts.md", "Concepts", "Participants"),
    ("participant/examples.md", "Examples", "Participants"),
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
  overflow-wrap: anywhere; }
th { background: #161b22; }
code { background: #161b22; padding: 1px 5px; border-radius: 4px; }
blockquote { margin: 10px 0; padding: 8px 14px; border-left: 4px solid #3fb950; background: #161b22; }
img { max-width: min(100%, 900px); height: auto; }
"""


def render(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    # Image paths in handouts are relative to their own folder.
    folder = Path(path).parent.as_posix()
    return body.replace('src="venn.svg"', f'src="{folder}/venn.svg"')


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
