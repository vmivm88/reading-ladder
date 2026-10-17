import os, re, sys, html, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib
CFG = {
 "aladdin": dict(text="aladdin_modern", wb="aladdin_wb2", level="Level 1 (B1)", meetings=2, per="Parts 1–6, then Parts 7–9"),
 "alibaba": dict(text="alibaba_modern", wb="alibaba_wb", level="Level 1 (B1)", meetings=1, per="all 6 parts"),
}
SLUG = sys.argv[1]
_c = CFG[SLUG]
_t = importlib.import_module(_c["text"]); _w = importlib.import_module(_c["wb"])
TITLE, SOURCE, PARTS = _t.TITLE, _t.SOURCE, _t.PARTS
WB, OLD, IDIOMS, NOTES, FINAL_DISCUSSION = _w.WB, _w.OLD, _w.IDIOMS, _w.NOTES, _w.FINAL_DISCUSSION
WPM = 100
def mins(n): return max(1, round(n / WPM))
def hm(m):
    h, r = divmod(int(round(m / 5.0) * 5), 60)
    return (f"{h} hr " if h else "") + (f"{r} min" if r else "").strip()
from playwright.sync_api import sync_playwright

REPO = os.path.dirname(os.path.dirname(HERE))
SCR = os.environ.get("BUILD_TMP", os.path.join(REPO, ".build")); os.makedirs(os.path.join(SCR, "prev"), exist_ok=True)
CSS = open(os.path.join(REPO, "src", "animal-farm", "style.css"), encoding="utf-8").read()
e = html.escape
stem = lambda w: w.lower()[:max(3, len(w) - 2)]

# ---------- validation ----------
probs = []
for i, ((text, changes), wb) in enumerate(zip(PARTS, WB), 1):
    bold = [b.lower() for b in re.findall(r"\*\*(.+?)\*\*", text)]
    words = [v[0] for v in wb["vocab"]]
    for w in words:
        if not any(b.startswith(stem(w)) for b in bold): probs.append(f"p{i}: vocab '{w}' not marked in text")
    for k in re.findall(r"\{\{(.+?)\}\}", text):
        if k.capitalize() not in {o.capitalize() for o in OLD}: probs.append(f"p{i}: no note for old word {k}")
    for k in re.findall(r"\[\[(.+?)\]\]", text):
        if k not in IDIOMS: probs.append(f"p{i}: no note for idiom {k}")
    for s, a, d in wb["quiz"]:
        if s.count("___") != 1 or a in d or len(set(d)) != 3: probs.append(f"p{i}: quiz issue {a}")
    used = {w for w in words for s, a, d in wb["quiz"] if a.lower().startswith(stem(w))}
    if set(words) - used: probs.append(f"p{i}: untested {set(words) - used}")
print("\n".join(probs) or "validation OK")
words_total = sum(len(re.sub(r"\*\*|\{\{|\}\}|\[\[|\]\]", "", t).split()) for t, _ in PARTS)
print("words:", words_total)

EXTRA = """
.reader p { font-family: 'Noto Serif CJK KR', Georgia, serif; font-size: 12pt; line-height: 1.72; margin: 0 0 9px; text-align: left; }
b.v { background: linear-gradient(transparent 62%, #f6e7a6 62%); font-weight: 700; }
span.old { border-bottom: 2px dotted #8a5a2b; }
span.old sup, span.idi sup { font-size: 7pt; color: #8a5a2b; margin-left: 1px; }
span.idi { border-bottom: 2px solid #6f93c9; }
span.idi sup { color: #3f6aa8; }
.legend { display: grid; gap: 6px; margin-top: 8px; }
.legend div { font-size: 10.5pt; }
.wc { font-size: 9pt; color: #a08a5a; margin-bottom: 12px; letter-spacing: 1px; }
.credit { font-size: 9pt; color: #6b5d45; margin: 50px auto 0; width: 135mm; line-height: 1.6; }
table.ch { width: 100%; border-collapse: collapse; font-size: 10pt; margin-top: 4px; }
table.ch td { border-bottom: 1px solid #e6dfcf; padding: 3px 6px; vertical-align: top; }
table.ch td.o { color: #8a5a2b; text-decoration: line-through; width: 45%; }
.note-box { border: 1px solid #e0d6bf; border-radius: 6px; padding: 8px 12px; margin-bottom: 8px; page-break-inside: avoid; }
.note-box .h { font-weight: 700; color: #3d3220; }
.note-box .ko { color: #8a5a2b; margin-left: 6px; }
.note-box .m { font-size: 10pt; margin-top: 2px; }
.reading-note { background: #f8f5ee; border-left: 4px solid #c9b78f; padding: 8px 12px; font-size: 10pt; margin: 8px 0; }
"""

def mark(text):
    out = []
    for p in [x.strip() for x in text.strip().split("\n\n") if x.strip()]:
        p = e(p)
        p = re.sub(r"\*\*(.+?)\*\*", r"<b class='v'>\1</b>", p)
        p = re.sub(r"\{\{(.+?)\}\}", r"<span class='old'>\1<sup>†</sup></span>", p)
        p = re.sub(r"\[\[(.+?)\]\]", r"<span class='idi'>\1<sup>※</sup></span>", p)
        out.append(f"<p>{p}</p>")
    return "".join(out)

def cover(sub, note):
    return f"""<div class='page cover'><div class='series'>ENGLISH BOOK CLUB · CLASSICS IN TODAY'S WORDS</div>
<h1 style='font-size:30pt'>{e(TITLE)}</h1><div class='author'>{e(sub)}</div>
<div class='note'>{note}</div>
<div class='credit'>Text: {e(SOURCE)}, public domain. Every sentence and event is kept; only words no longer in everyday use were replaced with today's words. Part divisions were added for reading.<br>Workbook, part divisions, notes, markings and exercises © 2026 Fine pearls (파인펄스) · Reading Ladder, licensed under CC BY-NC 4.0 (creativecommons.org/licenses/by-nc/4.0): free to share and adapt for non-commercial use with credit.</div></div>"""

LEGEND = """<div class='legend'>
<div><b class='v'>highlighted</b> — a word studied in the workbook</div>
<div><span class='old'>dotted<sup>†</sup></span> — an old word kept because there is no good modern replacement (see the workbook)</div>
<div><span class='idi'>blue line<sup>※</sup></span> — an old expression that people no longer use (see the workbook)</div></div>"""

def reader(path):
    p = [f"<html><head><meta charset='utf-8'><style>{CSS}{EXTRA}</style></head><body class='reader'>"]
    p.append(cover("Andrew Lang's 1889 text in today's words", f"{len(PARTS)} parts · {words_total:,} words · {_c['level']}<br>Reading time: about {hm(words_total / WPM)} · with the workbook: about {hm(2 * words_total / WPM)} · {_c["meetings"]} book club meeting{"s" if _c["meetings"] > 1 else ""} ({_c['per']})."))
    p.append("<div class='page'><h2>How to Read This Book</h2><div>The original story is not changed. Only old words like <i>bade</i>, <i>thou</i> and <i>whence</i> were replaced with the words we use today. Three kinds of marks help you:</div>" + LEGEND +
             "<h3>READING TIME</h3><div>Most English learners read about 100 words a minute (1,000 words ≈ 10 minutes). With the workbook, plan about twice as long. Our book club reads about 4,300 words per meeting.</div>"
             "<h3>PARTS</h3><table class='chars'>" + "".join(f"<tr><td class='n'>Part {i}</td><td>{len(re.sub(r'\\*\\*|\\{\\{|\\}\\}|\\[\\[|\\]\\]', '', t).split())} words · about {mins(len(re.sub(r'\\*\\*|\\{\\{|\\}\\}|\\[\\[|\\]\\]', '', t).split()))} min</td></tr>" for i, (t, _) in enumerate(PARTS, 1)) + "</table></div>")
    for i, (t, _) in enumerate(PARTS, 1):
        wc = len(re.sub(r"\*\*|\{\{|\}\}|\[\[|\]\]", "", t).split())
        p.append(f"<div class='page'><div class='chlabel'>PART {i}</div><h2>Part {i}</h2><div class='wc'>{wc} WORDS · ABOUT {mins(wc)} MIN</div>{mark(t)}</div>")
    p.append("</body></html>")
    open(path, "w", encoding="utf-8").write("".join(p))

def workbook(path):
    random.seed(1889)
    p = [f"<html><head><meta charset='utf-8'><style>{CSS}{EXTRA}</style></head><body>"]
    p.append(cover("Workbook", "Use with the reader. For each part: 10 word cards, 10 fill-in-the-blank questions, notes on old words and old expressions, and questions to talk about."))
    p.append("<div class='page'><h2>How to Use This Workbook</h2><div>1. Read one part in the reader.<br>2. Study the 10 word cards.<br>3. Do the 10 practice questions without looking back.<br>"
             "4. Read the notes on old words (†) and old expressions (※).<br>5. Check the table of updated words to see how the 1889 English was changed.<br>6. Choose a question to talk about at the meeting.</div>" + LEGEND + "</div>")
    for i, ((text, changes), wb) in enumerate(zip(PARTS, WB), 1):
        lab = f"<div class='chlabel'>PART {i}</div>"
        for half in (0, 5):
            p.append(f"<div class='page'>{lab}<h2>{'Vocabulary' if half == 0 else 'Vocabulary (continued)'}</h2>")
            for n, (w, pos, st, ipa, ko, col, ex1, ex2) in enumerate(wb["vocab"][half:half + 5], half + 1):
                p.append(f"""<div class='card'><div><span class='num'>{n:02d}</span><span class='w'>{e(w)}</span><span class='pos'>{e(pos)}</span>
<span class='pron'>{e(st)} · {e(ipa)}</span><span class='ko'>({e(ko)})</span></div>
<div class='col'><span class='lbl'>COLLOCATIONS</span>{e(col)}</div><ul><li>{e(ex1)}</li><li>{e(ex2)}</li></ul></div>""")
            p.append("</div>")
        key = []
        p.append(f"<div class='page'>{lab}<h2>Practice &amp; Talk</h2><p>Choose the best word. Watch the form of the word (-ed, -s, -ly).</p>")
        for n, (s, a, d) in enumerate(wb["quiz"], 1):
            opts = [a] + d; random.shuffle(opts)
            key.append(f"{n}. ({'abcd'[opts.index(a)]}) {a}")
            os_ = "".join(f"<span>({l}) {e(o)}</span>" for l, o in zip("abcd", opts))
            p.append(f"<div class='q'><b>{n}.</b> {e(s).replace('___', '__________')}<div class='opts'>{os_}</div></div>")
        p.append("<h3>LET'S TALK</h3><ol class='disc'>" + "".join(f"<li>{e(d)}<div class='lines'></div></li>" for d in wb["discussion"]) + "</ol>")
        p.append("<h3>ANSWER KEY</h3><div class='key'>" + "<br>".join(e(k) for k in key) + "</div></div>")
        # old words & expressions page
        olds = list(dict.fromkeys(re.findall(r"\{\{(.+?)\}\}", text)))
        idis = list(dict.fromkeys(re.findall(r"\[\[(.+?)\]\]", text)))
        p.append(f"<div class='page'>{lab}<h2>Old Words &amp; Expressions</h2>")
        if i in NOTES:
            p.append(f"<div class='reading-note'><b>Reading note.</b> {e(NOTES[i])}</div>")
        if olds:
            p.append("<h3>OLD WORDS KEPT †</h3>")
            for k in olds:
                key_ = next(o for o in OLD if o.lower() == k.lower())
                pos, ko, m = OLD[key_]
                p.append(f"<div class='note-box'><span class='h'>{e(k)}</span> <span class='pos'>{e(pos)}</span><span class='ko'>({e(ko)})</span><div class='m'>{e(m)}</div></div>")
        if idis:
            p.append("<h3>OLD EXPRESSIONS ※</h3>")
            for k in idis:
                ko, mod, ex = IDIOMS[k]
                p.append(f"<div class='note-box'><span class='h'>{e(k)}</span><span class='ko'>({e(ko)})</span><div class='m'><b>Today:</b> {e(mod)}</div><div class='m' style='color:#666'>{e(ex)}</div></div>")
        if not olds and not idis:
            p.append("<p>This part has no kept old words or old expressions.</p>")
        p.append("<h3>WORDS WE UPDATED</h3><table class='ch'><tr><td><b>1889</b></td><td><b>Today</b></td></tr>" +
                 "".join(f"<tr><td class='o'>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in changes) + "</table></div>")
    p.append("<div class='page'><h2>After the Whole Story</h2><ol class='disc'>" +
             "".join(f"<li>{e(d)}<div class='lines'></div><div class='lines'></div><div class='lines'></div></li>" for d in FINAL_DISCUSSION) + "</ol></div></body></html>")
    open(path, "w", encoding="utf-8").write("".join(p))

if __name__ == "__main__":
    out = os.path.join(REPO, "workbooks")
    reader(os.path.join(SCR, f"{SLUG}_reader.html")); workbook(os.path.join(SCR, f"{SLUG}_wb.html"))
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page()
        for src, pdf in [(f"{SLUG}_reader.html", f"{SLUG}-reader.pdf"), (f"{SLUG}_wb.html", f"{SLUG}-workbook.pdf")]:
            pg.goto("file://" + os.path.join(SCR, src))
            pg.pdf(path=os.path.join(out, pdf), format="A4", print_background=True, prefer_css_page_size=True)
        b.close()
    import pypdfium2 as pd
    for pdf, pages in [(f"{SLUG}-reader.pdf", [0, 1, 2]), (f"{SLUG}-workbook.pdf", [5])]:
        d = pd.PdfDocument(os.path.join(out, pdf)); print(pdf, len(d), "pages")
        for k in pages:
            if k < len(d): d[k].render(scale=0.6).to_pil().save(os.path.join(SCR, "prev", f"{pdf[:-4]}_{k}.png"))
