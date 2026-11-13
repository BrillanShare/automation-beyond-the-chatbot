"""Draw the document illustrations used in participant/handout.md.

Run from the repo root:  python tools/make_illustrations.py
Writes SVG files into participant/. Not published; only the SVGs are.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "participant"

BG = "#161a1f"
PAPER = "#f4f1ea"
INK = "#3b3f46"
FAINT = "#b9b4aa"
SCRIPT = "#58a6ff"
AI = "#f85149"
HYBRID = "#bc8cff"
AMBER = "#d29922"
GREEN = "#3fb950"
TEXT = "#e6edf3"
MUTED = "#8b949e"
FONT = 'font-family="Segoe UI, Helvetica, Arial, sans-serif"'


def svg(w, h, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" {FONT}>\n'
        f"<title>{title}</title>\n"
        f'<rect width="{w}" height="{h}" fill="{BG}"/>\n{body}</svg>\n'
    )


def t(x, y, s, size=13, fill=TEXT, weight="normal", anchor="start", italic=False, mono=False):
    style = ' font-style="italic"' if italic else ""
    fam = ' font-family="Consolas, Menlo, monospace"' if mono else ""
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}"{style}{fam}>{s}</text>\n')


def paper(x, y, w, h, rot=0, fill=PAPER, stroke="none"):
    tr = f' transform="rotate({rot} {x + w / 2} {y + h / 2})"' if rot else ""
    return (f'<rect x="{x + 3}" y="{y + 4}" width="{w}" height="{h}" rx="3" fill="#00000066"{tr}/>\n'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{stroke}"{tr}/>\n')


def lines(x, y, w, n, gap=9, color=FAINT, ragged=True):
    out = ""
    for i in range(n):
        lw = w * (0.55 + 0.45 * ((i * 37) % 10) / 10) if ragged else w
        out += f'<rect x="{x}" y="{y + i * gap}" width="{lw:.0f}" height="3" rx="1.5" fill="{color}"/>\n'
    return out


def frame(x, y, w, h, color, label):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}14" stroke="{color}" stroke-width="2"/>\n'
            + t(x + 12, y + 22, label, 14, color, "700"))


def grid(x, y, cols, rows, cw=46, rh=17, values=None, header=None, highlight=None, fill=PAPER):
    out = f'<rect x="{x}" y="{y}" width="{cols * cw}" height="{rows * rh}" fill="{fill}"/>\n'
    for r in range(rows):
        for c in range(cols):
            if highlight and (r, c) in highlight:
                out += f'<rect x="{x + c * cw}" y="{y + r * rh}" width="{cw}" height="{rh}" fill="{highlight[(r, c)]}"/>\n'
    if header:
        out += f'<rect x="{x}" y="{y}" width="{cols * cw}" height="{rh}" fill="#d9e2ec"/>\n'
    for r in range(rows + 1):
        out += f'<line x1="{x}" y1="{y + r * rh}" x2="{x + cols * cw}" y2="{y + r * rh}" stroke="#c4bfb5"/>\n'
    for c in range(cols + 1):
        out += f'<line x1="{x + c * cw}" y1="{y}" x2="{x + c * cw}" y2="{y + rows * rh}" stroke="#c4bfb5"/>\n'
    if header:
        for c, s in enumerate(header):
            out += t(x + c * cw + 4, y + rh - 5, s, 10, INK, "700")
    if values:
        for (r, c), s in values.items():
            out += t(x + c * cw + cw - 4, y + r * rh + rh - 5, s, 10, INK, anchor="end")
    return out


def wave(x, y, w, amp, pattern):
    pts = []
    for i in range(int(w)):
        a = pattern(i)
        pts.append(f"{x + i},{y - a * amp:.1f}")
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="#8fd3ff" stroke-width="1.6"/>\n'


def arrow(x1, y1, x2, y2, color=MUTED):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" marker-end="url(#a)"/>\n')


DEFS = (f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker></defs>\n')


# ---------------------------------------------------------------- data types
def data_types():
    import math
    b = DEFS
    b += t(300, 32, "Scripting can handle it", 16, SCRIPT, "700", "middle")
    b += t(720, 32, "Needs AI in the loop", 16, AI, "700", "middle")
    rows = ["Numbers", "Language", "Images", "Audio"]
    for i, name in enumerate(rows):
        y = 50 + i * 150
        b += t(20, y + 75, name, 17, TEXT, "700")
        b += f'<rect x="120" y="{y}" width="370" height="135" rx="12" fill="{SCRIPT}14" stroke="{SCRIPT}" stroke-width="2"/>\n'
        b += f'<rect x="530" y="{y}" width="410" height="135" rx="12" fill="{AI}14" stroke="{AI}" stroke-width="2"/>\n'
    # Numbers
    y = 50
    b += grid(140, y + 16, 4, 6, 50, 17, header=["Date", "Ref", "Debit", "Credit"],
              values={(1, 2): "1,200", (2, 3): "450", (3, 2): "3,100", (4, 3): "75", (5, 2): "4,300"},
              highlight={(5, 0): "#cfe3ff", (5, 1): "#cfe3ff", (5, 2): "#cfe3ff", (5, 3): "#cfe3ff"})

    b += t(146, y + 113, "=SUM()", 10, INK, "700", mono=True)
    b += t(360, y + 50, "Same columns", 13, TEXT)
    b += t(360, y + 68, "every month;", 13, TEXT)
    b += t(360, y + 86, "fixed formulas", 13, TEXT)
    b += paper(550, y + 14, 200, 108)
    b += t(560, y + 31, "Trial balance: consulting firm", 10, INK, "700")
    tb = [("Consulting revenue", "912,000"), ("Salaries", "540,000"), ("Rent", "84,000"),
          ("Office supplies", "48,200"), ("Software", "22,100")]
    for k, (a, v) in enumerate(tb):
        yy = y + 48 + k * 15
        if a == "Office supplies":
            b += f'<rect x="554" y="{yy - 11}" width="192" height="15" fill="#ffd8d3"/>\n'
        b += t(560, yy, a, 10, INK) + t(742, yy, v, 10, INK, anchor="end")
    b += t(770, y + 50, "Is this balance", 13, TEXT)
    b += t(770, y + 68, "plausible for this", 13, TEXT)
    b += t(770, y + 86, "kind of business?", 13, TEXT)
    # Language
    y = 200
    b += paper(140, y + 14, 200, 108)
    b += t(150, y + 34, "Dear {client},", 11, INK, mono=True)
    b += t(150, y + 52, "Your {year} return", 11, INK, mono=True)
    b += t(150, y + 68, "is ready to sign.", 11, INK, mono=True)
    b += t(150, y + 84, "Due: {due_date}", 11, INK, mono=True)
    b += lines(150, y + 96, 150, 2)
    b += t(360, y + 58, "A template with", 13, TEXT)
    b += t(360, y + 76, "blanks to fill", 13, TEXT)
    b += paper(550, y + 14, 200, 108)
    em = ["hi! quick q, we moved the", "shop to my sister's garage in", "march and sold the old van,", "do we still deduct the lease?", "also my kid started college"]
    for k, s in enumerate(em):
        b += t(558, y + 32 + k * 17, s, 10.5, INK, italic=True)
    b += t(770, y + 58, "Free-form message:", 13, TEXT)
    b += t(770, y + 76, "understand it,", 13, TEXT)
    b += t(770, y + 94, "then write a reply", 13, TEXT)
    # Images
    y = 350
    b += f'<rect x="140" y="{y + 14}" width="200" height="108" fill="#ffffff"/>\n'
    b += paper(205, y + 20, 70, 96)
    b += t(240, y + 36, "RECEIPT", 8, INK, "700", "middle") + lines(213, y + 46, 54, 6, 8, ragged=False)
    b += t(360, y + 58, "Plain background:", 13, TEXT)
    b += t(360, y + 76, "remove it by color", 13, TEXT)
    b += f'<rect x="550" y="{y + 14}" width="200" height="108" fill="#6b4f3a"/>\n'
    b += f'<path d="M600,{y + 30} L668,{y + 22} L690,{y + 108} L615,{y + 116} Z" fill="{PAPER}"/>\n'
    b += f'<path d="M620,{y + 40} L660,{y + 70} M612,{y + 85} L680,{y + 78}" stroke="#d6cfc2" stroke-width="2"/>\n'
    for k in range(6):
        b += f'<line x1="{612 + k}" y1="{y + 42 + k * 11}" x2="{660 + k * 1.5}" y2="{y + 37 + k * 11}" stroke="{FAINT}" stroke-width="3"/>\n'
    b += f'<ellipse cx="655" cy="{y + 95}" rx="16" ry="9" fill="#c9a57a88"/>\n'
    b += t(770, y + 58, "Crumpled receipt photo", 13, TEXT)
    b += t(770, y + 76, "on a desk: read the", 13, TEXT)
    b += t(770, y + 94, "vendor, date, total", 13, TEXT)
    # Audio
    y = 500
    b += f'<rect x="140" y="{y + 14}" width="200" height="108" rx="4" fill="#0d1117"/>\n'
    b += wave(150, y + 68, 180, 30, lambda i: (math.sin(i * 0.9) if 80 < i < 100 else 0.03 * math.sin(i)))
    b += t(240, y + 112, "beep", 11, MUTED, anchor="middle")
    b += t(360, y + 58, "Detect a sound:", 13, TEXT)
    b += t(360, y + 76, "a beep or a clap", 13, TEXT)
    b += f'<rect x="550" y="{y + 14}" width="200" height="108" rx="4" fill="#0d1117"/>\n'
    b += wave(560, y + 58, 180, 26, lambda i: math.sin(i * 0.7) * (0.3 + 0.7 * abs(math.sin(i * 0.05))) * (0 if 60 < i < 72 else 1))
    b += t(650, y + 98, "“so um, can you file", 10.5, "#c9d1d9", anchor="middle", italic=True)
    b += t(650, y + 113, "mine by the 15th?”", 10.5, "#c9d1d9", anchor="middle", italic=True)
    b += t(770, y + 58, "Client voicemail:", 13, TEXT)
    b += t(770, y + 76, "a punctuated", 13, TEXT)
    b += t(770, y + 94, "transcript", 13, TEXT)
    return svg(960, 650, "Data type doesn't decide the bucket", b)


# ------------------------------------------------------- what a script can't do
def script_cant():
    b = DEFS
    b += frame(20, 20, 440, 300, SCRIPT, "Monthly Excel export: new values, same shape")
    for k, m in enumerate(["Jan", "Feb", "Mar"]):
        x = 40 + k * 140
        vals = [["1,200", "450"], ["3,100", "75"], ["980", "1,020"]][k]
        b += t(x, 70, m, 13, TEXT, "700")
        b += grid(x, 80, 3, 6, 40, 18, header=["Acct", "Dr", "Cr"],
                  values={(1, 1): vals[0], (2, 2): vals[1], (3, 1): str(400 + k * 75), (4, 2): str(90 + k * 30)})
    b += t(240, 230, "Column C is always the amount.", 13, TEXT, anchor="middle")
    b += t(240, 250, "The steps are always the same.", 13, TEXT, anchor="middle")
    b += t(240, 290, "Script still works", 15, GREEN, "700", "middle")
    b += frame(500, 20, 440, 300, AI, "Two leases: different shape and wording")
    # lease A
    b += paper(530, 50, 170, 220)
    b += t(540, 68, "LEASE AGREEMENT", 9, INK, "700") + lines(540, 78, 150, 4)
    b += f'<rect x="537" y="114" width="156" height="30" fill="#fff1a8"/>\n'
    b += t(541, 126, "4. Rent. Tenant shall pay", 8.5, INK) + t(541, 138, "$4,250 per month on the 1st", 8.5, INK)
    b += lines(540, 152, 150, 10)
    # lease B
    b += paper(740, 50, 170, 220)
    b += t(750, 68, "Commercial Lease", 9, INK, "700") + lines(750, 78, 150, 12)
    b += f'<rect x="747" y="186" width="156" height="30" fill="#fff1a8"/>\n'
    b += t(751, 198, "Sched. B: Base Charge 51,000/yr", 8.5, INK) + t(751, 210, "payable monthly in advance*", 8.5, INK)
    b += lines(750, 224, 150, 2)
    b += f'<rect x="747" y="246" width="156" height="16" fill="#fff1a8"/>\n'
    b += t(751, 257, "*Abated Jan–Mar 2026", 8, INK, italic=True)
    b += t(720, 290, "Finding the rent means understanding the words", 13, AI, "700", "middle")
    return svg(960, 340, "What a script can't do", b)


# ------------------------------------------------------------- input/output lens
def io_lens():
    b = DEFS

    def form(x, y):
        o = paper(x, y, 110, 80)
        o += grid(x + 8, y + 18, 2, 3, 47, 15, header=["Field", "Value"],
                  values={(1, 1): "12,480", (2, 1): "9,315"})
        o += t(x + 8, y + 12, "Excel form", 9, INK, "700")
        return o

    b += frame(20, 20, 920, 150, SCRIPT, "Scripting")
    for k in range(3):
        b += paper(60 + k * 22, 55 + k * 8, 90, 100)
        b += t(68 + k * 22, 72 + k * 8, "FIRST BANK", 8, "#1f4f99", "700") + lines(68 + k * 22, 80 + k * 8, 74, 7)
    b += t(110, 185 - 20, "", 1)
    b += t(240, 100, "Text-based PDF statements,", 14, TEXT)
    b += t(240, 120, "all from one bank", 14, TEXT)
    b += arrow(470, 105, 640, 105)
    b += form(660, 62)
    b += t(478, 92, "Script reads fixed spots", 13, SCRIPT)

    b += frame(20, 190, 920, 170, HYBRID, "Hybrid")
    b += paper(55, 228, 80, 100, rot=-8, fill="#e7e1d4")
    b += t(62, 250, "Cascade CU", 8, "#7a3b1f", "700") + lines(62, 258, 60, 7, color="#a9a294")
    b += f'<rect x="135" y="240" width="72" height="104" rx="8" fill="#222"/>\n' + paper(141, 250, 60, 84, rot=6)
    b += lines(147, 262, 46, 7)
    b += paper(212, 232, 82, 100, rot=3)
    b += t(219, 250, "Northwest Sav.", 8, "#2e6b3a", "700") + lines(219, 258, 64, 7)
    b += t(320, 270, "Scans, phone photos,", 14, TEXT)
    b += t(320, 290, "many banks", 14, TEXT)
    b += arrow(470, 280, 640, 280)
    b += form(660, 240)
    b += t(478, 262, "Local model or AI reads;", 13, HYBRID)
    b += t(478, 308, "script fills the form", 13, HYBRID)
    b += t(800, 108, "Same input,", 13, MUTED) + t(800, 126, "same output,", 13, MUTED) + t(800, 144, "different bucket", 13, TEXT, "700")
    b += t(800, 286, "Same input,", 13, MUTED) + t(800, 304, "same output,", 13, MUTED) + t(800, 322, "different bucket", 13, TEXT, "700")
    return svg(960, 380, "The input/output lens defines the task, but doesn't decide the bucket", b)


# ------------------------------------------------------------------ hard inputs
def hard_inputs():
    b = DEFS
    tiles = [
        "Scan or phone photo", "Same vendor, many names", "Rules that keep growing",
        "Messy Excel export", "Layout changed", "Duplicates and locked files",
    ]
    for k, name in enumerate(tiles):
        x = 20 + (k % 3) * 313
        y = 20 + (k // 3) * 250
        b += f'<rect x="{x}" y="{y}" width="297" height="234" rx="12" fill="{AMBER}14" stroke="{AMBER}" stroke-width="2"/>\n'
        b += t(x + 14, y + 26, name, 15, AMBER, "700")
    # 1 scan
    x, y = 20, 20
    b += paper(x + 30, y + 50, 110, 150)
    b += t(x + 38, y + 68, "STATEMENT", 8, INK, "700") + lines(x + 38, y + 78, 94, 11)
    b += t(x + 85, y + 220, "Text PDF", 11, MUTED, anchor="middle")
    b += paper(x + 165, y + 55, 105, 140, rot=-7, fill="#ddd6c7")
    b += f'<rect x="{x + 165}" y="{y + 55}" width="105" height="140" fill="url(#none)" opacity="0"/>\n'
    for k in range(11):
        b += f'<line x1="{x + 175}" y1="{y + 80 + k * 10}" x2="{x + 245 - (k * 7) % 25}" y2="{y + 72 + k * 10}" stroke="#a49c8c" stroke-width="3"/>\n'
    b += f'<circle cx="{x + 240}" cy="{y + 170}" r="10" fill="#b8a98a88"/>\n'
    b += t(x + 218, y + 220, "Tilted scan", 11, MUTED, anchor="middle")
    # 2 vendor names
    x, y = 333, 20
    b += paper(x + 25, y + 45, 245, 160)
    rows = [("03/02", "AMAZON.COM*2X4LK9", "38.12"), ("03/05", "AMZN Mktp US*RT5", "12.99"),
            ("03/09", "Amazon", "64.00"), ("03/11", "AMZN DIGITAL", "4.99"), ("03/14", "Amazon Web Svcs", "212.40")]
    for k, (d, v, a) in enumerate(rows):
        yy = y + 70 + k * 26
        b += f'<rect x="{x + 30}" y="{yy - 14}" width="235" height="20" fill="#fff1a8{"" if k % 2 == 0 else "88"}"/>\n'
        b += t(x + 35, yy, d, 10, INK, mono=True) + t(x + 75, yy, v, 10, INK, mono=True) + t(x + 260, yy, a, 10, INK, anchor="end", mono=True)
    # 3 rules growing
    x, y = 646, 20
    b += paper(x + 25, y + 45, 245, 175)
    rules = ['if "AMZN" in memo: Supplies', 'if "AMAZON" in memo: Supplies', 'if "Web Svcs" in memo: Software',
             'if "UBER" in memo: Travel', 'if "UBER EATS" in memo: Meals', 'if "SQ *" in memo: ???',
             'if "TST*" in memo: Meals?', "... 412 more rules"]
    for k, r in enumerate(rules):
        b += t(x + 33, y + 66 + k * 18, r, 9.5, AI if "?" in r or "..." in r else INK, mono=True)
    # 4 messy excel
    x, y = 20, 270
    hl = {}
    b += grid(x + 25, y + 46, 5, 8, 49, 18, highlight={(4, c): "#ffe2b8" for c in range(5)})
    b += f'<rect x="{x + 25}" y="{y + 46}" width="245" height="18" fill="#d9e2ec"/>\n'
    b += t(x + 147, y + 59, "ACME HOLDINGS – GL DETAIL (merged)", 9, INK, "700", "middle")
    b += f'<rect x="{x + 25}" y="{y + 64}" width="245" height="18" fill="#e8edf2"/>\n'
    for c, s in enumerate(["Date", "Acct", "Desc", "Dr", "Cr"]):
        b += t(x + 29 + c * 49, y + 77, s, 9, INK, "700")
    b += t(x + 29, y + 131, "Subtotal Q1", 9, INK, "700")
    b += t(x + 147, y + 210, "Merged title, two header rows, totals mid-table", 10, MUTED, anchor="middle")
    # 5 layout changed
    x, y = 333, 270
    for k, (lab, ty) in enumerate([("2025 layout", 160), ("2026 layout", 72)]):
        px = x + 25 + k * 135
        b += paper(px, y + 45, 110, 155)
        b += t(px + 8, y + 62, "INVOICE", 9, INK, "700") + lines(px + 8, y + 72 + (0 if k == 0 else 30), 94, 6)
        b += f'<rect x="{px + 50}" y="{y + ty}" width="54" height="16" fill="#ffd8d3"/>\n'
        b += t(px + 100, y + ty + 12, "Total", 9, INK, "700", "end")
        b += t(px + 55, y + 220, lab, 11, MUTED, anchor="middle")
    b += arrow(x + 138, y + 120, x + 158, y + 120)
    # 6 duplicates and locked
    x, y = 646, 270
    for k in range(2):
        b += paper(x + 30 + k * 16, y + 50 + k * 12, 90, 120)
        b += lines(x + 38 + k * 16, y + 66 + k * 12, 72, 9)
    b += t(x + 85, y + 210, "invoice_0412.pdf", 10, MUTED, anchor="middle")
    b += t(x + 85, y + 225, "invoice_0412 (1).pdf", 10, MUTED, anchor="middle")
    b += paper(x + 170, y + 55, 100, 130, fill="#d8d3c8")
    b += f'<rect x="{x + 200}" y="{y + 115}" width="40" height="32" rx="4" fill="{AMBER}"/>\n'
    b += f'<path d="M{x + 207},{y + 115} v-10 a13,13 0 0 1 26,0 v10" fill="none" stroke="{AMBER}" stroke-width="5"/>\n'
    b += t(x + 220, y + 210, "Password-protected", 10, MUTED, anchor="middle")
    return svg(960, 540, "Hard inputs that are easy to overlook", b)


# ------------------------------------------------------------ demo: tokens
def demo_tokens():
    b = DEFS
    b += t(20, 34, "Lines sent to the LLM each month", 17, TEXT, "700")
    groups = [
        ("Example 1: match bank lines to the ledger", [("All AI", "every line, every month", 30, AI),
                                                        ("All script", "none: the script does all of it", 0, SCRIPT)]),
        ("Example 2: categorize credit card lines", [("All AI", "every line, every month", 40, AI),
                                                      ("Hybrid", "only the 9 lines no rule matched", 9, HYBRID)]),
    ]
    scale = 15
    y = 62
    for title, rows in groups:
        b += t(20, y + 4, title, 14, MUTED, "700")
        y += 16
        for name, note, n, color in rows:
            b += t(20, y + 30, name, 16, color, "700")
            b += f'<rect x="160" y="{y + 8}" width="{40 * scale}" height="30" rx="6" fill="#21262d"/>\n'
            if n:
                b += f'<rect x="160" y="{y + 8}" width="{n * scale}" height="30" rx="6" fill="{color}"/>\n'
            b += t(160 + n * scale + 12, y + 29, str(n), 16, TEXT, "700")
            b += t(160, y + 56, note, 12, MUTED)
            y += 66
        y += 14
    b += t(20, y + 6, "Building the script uses tokens once. After that, only the AI-in-the-loop part uses tokens on every run.", 13, TEXT)
    return svg(960, y + 24, "Demo: lines sent to the LLM each month, two examples", b)

# ------------------------------------------------- cost-volume chart (growth)
def cost_volume():
    """Laid out like a cost-volume (break-even) chart: fixed vs. variable cost."""
    b = DEFS
    x0, y0, w, h = 110, 70, 560, 330          # plot area
    X = lambda v: x0 + v / 100 * w            # volume 0..100
    Y = lambda c: y0 + h - c / 100 * h        # cost 0..100
    b += t(480, 34, "How cost grows with volume", 18, TEXT, "700", "middle")
    b += t(480, 54, "Illustrative shapes, not to scale", 12, MUTED, anchor="middle")
    for k in range(6):                         # gridlines, like an Excel chart
        gy = y0 + k * h / 5
        b += f'<line x1="{x0}" y1="{gy}" x2="{x0 + w}" y2="{gy}" stroke="#30363d"/>\n'
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + h}" stroke="{MUTED}" stroke-width="2"/>\n'
    b += f'<line x1="{x0}" y1="{y0 + h}" x2="{x0 + w}" y2="{y0 + h}" stroke="{MUTED}" stroke-width="2"/>\n'
    b += (f'<text x="34" y="{y0 + h / 2}" font-size="17" fill="{TEXT}" font-weight="700" text-anchor="middle" '
          f'transform="rotate(-90 34 {y0 + h / 2})">Tokens and $$$</text>\n')
    b += t(x0 + w / 2, y0 + h + 34, "Volume: documents or rows processed, run after run", 14, TEXT, "700", "middle")
    b += t(x0, y0 + h + 16, "0", 11, MUTED, anchor="middle") + t(x0 + w, y0 + h + 16, "more", 11, MUTED, anchor="end")

    build = 22
    script = lambda v: build
    hybrid = lambda v: build + 0.15 * v
    ai = lambda v: 0.9 * v
    pairs = lambda v: 0.012 * v * v

    def line(fn, color, width=3.5, dash=""):
        pts = []
        for i in range(0, 1001):
            v = i / 10
            c = fn(v)
            if c > 100:
                break
            pts.append(f"{X(v):.1f},{Y(c):.1f}")
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}"{d}/>\n'

    b += line(pairs, AMBER, dash="7 5") + line(ai, AI) + line(hybrid, HYBRID) + line(script, SCRIPT)

    # Fixed cost bracket on the axis
    b += f'<line x1="{x0 - 10}" y1="{Y(0)}" x2="{x0 - 10}" y2="{Y(build)}" stroke="{SCRIPT}" stroke-width="2"/>\n'
    b += f'<line x1="{x0 - 15}" y1="{Y(build)}" x2="{x0 - 5}" y2="{Y(build)}" stroke="{SCRIPT}" stroke-width="2"/>\n'
    b += t(X(40), Y(build) + 19, "Fixed cost: tokens to build the script, once (treated as fixed)", 12, SCRIPT)

    # Break-even: where AI in the loop passes the script's build cost
    be = build / 0.9
    b += f'<line x1="{X(be)}" y1="{Y(build)}" x2="{X(be)}" y2="{y0 + h}" stroke="{TEXT}" stroke-dasharray="3 4"/>\n'
    b += f'<circle cx="{X(be)}" cy="{Y(build)}" r="6" fill="{BG}" stroke="{TEXT}" stroke-width="2.5"/>\n'
    b += t(X(be) + 12, Y(8), "Break-even:", 12, TEXT, "700")
    b += t(X(be) + 12, Y(8) + 15, "the script has paid for itself", 12, TEXT)

    # Direct labels at the right, in the order the lines end
    lx = x0 + w + 14
    px = X(84)
    b += t(px, y0 + 6, "AI compares every item", 13, AMBER, "700", "end")
    b += t(px, y0 + 23, "with every other item:", 13, AMBER, "700", "end")
    b += t(px, y0 + 39, "cost grows with the square", 12, MUTED, anchor="end")
    b += t(lx, Y(ai(100)) + 2, "AI in the loop", 13, AI, "700")
    b += t(lx, Y(ai(100)) + 19, "variable cost: every item,", 12, MUTED)
    b += t(lx, Y(ai(100)) + 34, "every run", 12, MUTED)
    b += t(lx, Y(hybrid(100)) - 4, "Hybrid", 13, HYBRID, "700")
    b += t(lx, Y(hybrid(100)) + 13, "fixed cost + a small variable cost", 12, MUTED)
    b += t(lx, Y(build) + 12, "Scripting", 13, SCRIPT, "700")
    b += t(lx, Y(build) + 29, "fixed cost only: flat", 12, MUTED)
    return svg(960, 450, "Cost-volume chart: how tokens and dollars grow with volume", b)


# ------------------------------------------- return on converting (4 panels)
def return_panels():
    """Four plausible workflows: today's token line vs. the line after converting."""
    b = DEFS
    b += t(20, 30, "Is it worth converting? Four plausible workflows", 17, TEXT, "700")
    # legend
    b += f'<line x1="20" y1="52" x2="50" y2="52" stroke="{AI}" stroke-width="3.5"/>\n' + t(56, 56, "Today: AI does all of it", 12, TEXT)
    b += f'<line x1="230" y1="52" x2="260" y2="52" stroke="{HYBRID}" stroke-width="3.5"/>\n' + t(266, 56, "After converting (hybrid or script)", 12, TEXT)
    b += f'<line x1="510" y1="44" x2="510" y2="60" stroke="{TEXT}" stroke-width="2" stroke-dasharray="3 3"/>\n' + t(518, 56, "Your volume", 12, TEXT)
    b += t(940, 56, "Illustrative shapes, not to scale", 11, MUTED, anchor="end")

    panels = [
        dict(title="Categorize credit card lines", vol="about 3,000 lines a month",
             today=lambda v: 0.9 * v, after=lambda v: 18 + 0.12 * v, you=80,
             verdict="Return: large", color=GREEN,
             why=["Rules catch most lines.", "AI sees only the leftovers."]),
        dict(title="Find duplicate vendor payments", vol="about 5,000 payments a year",
             today=lambda v: 0.011 * v * v, after=lambda v: 15 + 0.1 * v, you=80,
             verdict="Return: largest", color=GREEN,
             why=["Today's line curves upward.", "A script finds the exact", "matches. AI checks only", "the near-matches."]),
        dict(title="Pull amounts from W-2s", vol="about 15 forms a year",
             today=lambda v: 0.9 * v, after=lambda v: 45, you=15, breakeven=50,
             verdict="Return: not yet", color=AMBER,
             why=["Your volume is below", "break-even. Revisit if", "the volume grows."]),
        dict(title="Answer client questions", vol="about 30 emails a month",
             today=lambda v: 0.8 * v, after=lambda v: 6 + 0.8 * v, you=60,
             verdict="Return: none", color=MUTED,
             why=["Every email needs reading", "and writing. Converting", "doesn't change the line."]),
    ]
    for k, p in enumerate(panels):
        px = 20 + (k % 2) * 470
        py = 76 + (k // 2) * 262
        b += f'<rect x="{px}" y="{py}" width="450" height="248" rx="12" fill="#1c2128" stroke="#30363d"/>\n'
        b += t(px + 14, py + 24, p["title"], 15, TEXT, "700")
        b += t(px + 14, py + 42, p["vol"], 12, MUTED)
        x0, y0, w, h = px + 44, py + 58, 230, 150
        X = lambda v: x0 + v / 100 * w
        Y = lambda c: y0 + h - c / 100 * h
        b += f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + h}" stroke="{MUTED}" stroke-width="1.5"/>\n'
        b += f'<line x1="{x0}" y1="{y0 + h}" x2="{x0 + w}" y2="{y0 + h}" stroke="{MUTED}" stroke-width="1.5"/>\n'
        b += (f'<text x="{px + 22}" y="{y0 + h / 2}" font-size="11" fill="{MUTED}" text-anchor="middle" '
              f'transform="rotate(-90 {px + 22} {y0 + h / 2})">Tokens and $$$ in a year</text>\n')
        b += t(x0 + w / 2, y0 + h + 28, "Records in a year", 11, MUTED, anchor="middle")
        for fn_, color in ((p["today"], AI), (p["after"], HYBRID)):
            pts = []
            for i in range(0, 1001):
                v = i / 10
                c = fn_(v)
                if c > 100:
                    break
                pts.append(f"{X(v):.1f},{Y(c):.1f}")
            b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="3"/>\n'
        you = p["you"]
        ct, ca = p["today"](you), p["after"](you)
        b += f'<line x1="{X(you)}" y1="{y0}" x2="{X(you)}" y2="{y0 + h}" stroke="{TEXT}" stroke-width="1.5" stroke-dasharray="3 3"/>\n'
        b += t(X(you), y0 + h + 13, "you", 11, TEXT, "700", "middle")
        # the gap at your volume
        if abs(ct - ca) > 8:
            gap_color = GREEN if ct > ca else AMBER
            b += f'<line x1="{X(you) + 7}" y1="{Y(ct)}" x2="{X(you) + 7}" y2="{Y(ca)}" stroke="{gap_color}" stroke-width="4"/>\n'
            label = "saved" if ct > ca else "costs more"
            b += t(X(you) + 14, (Y(ct) + Y(ca)) / 2 + 4, label, 11, gap_color, "700")
        if "breakeven" in p:
            be = p["breakeven"]
            b += f'<circle cx="{X(be)}" cy="{Y(p["after"](be))}" r="5" fill="{BG}" stroke="{TEXT}" stroke-width="2"/>\n'
            b += t(X(be) + 4, Y(p["after"](be)) + 18, "break-even", 11, TEXT)
        # verdict and reason
        tx = px + 292
        b += f'<rect x="{tx}" y="{py + 70}" width="146" height="28" rx="14" fill="{p["color"]}33" stroke="{p["color"]}" stroke-width="2"/>\n'
        b += t(tx + 73, py + 89, p["verdict"], 13, p["color"] if p["color"] != MUTED else TEXT, "700", "middle")
        for i, line_ in enumerate(p["why"]):
            b += t(tx, py + 124 + i * 17, line_, 12, TEXT)
    return svg(960, 610, "Is it worth converting? Today's token line and the line after converting, for four workflows", b)


def main():
    for name, fn in [("data-types.svg", data_types), ("script-cant.svg", script_cant),
                     ("io-lens.svg", io_lens), ("hard-inputs.svg", hard_inputs), ("demo-tokens.svg", demo_tokens), ("cost-volume.svg", cost_volume), ("return-panels.svg", return_panels)]:
        (OUT / name).write_text(fn(), encoding="utf-8")
        print("wrote", name)


if __name__ == "__main__":
    main()
