# Web pages

| File | What it is |
|---|---|
| `index.html` | **Start here.** The workshop as a series of animated infographics. Double-click to open. |
| `text.html` | All the Markdown handouts on one page, with colored tables and hint buttons |

**`text.html` is a copy of the Markdown handouts in the folder above.** It doesn't update by itself; its banner says when it was last built. If you edit the Markdown and want it to match, open a terminal in this folder and run `python build.py`. If you don't need it to match, ignore it.

`index.html` is drawn by hand. It summarizes the handouts; the Markdown files have the full text.

`vendor/` holds [marked](https://github.com/markedjs/marked), the library `text.html` uses to show Markdown (MIT license).
