import os, re, sys, html, random, json, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from playwright.sync_api import sync_playwright
SCR = "/tmp/claude-0/-home-claude/e588e643-7009-5b40-9d8e-ea66df17ea15/scratchpad"
CSS = open(os.path.join(SCR, "style.css"), encoding="utf-8").read()
e = html.escape
TITLE = "The Wonderful Wizard of Oz"; SOURCE = "L. Frank Baum, The Wonderful Wizard of Oz (1900)"
WPM = 100
def mins(n): return max(1, round(n / WPM))
def hm(m):
    h, r = divmod(int(round(m / 5.0) * 5), 60)
    return ((f"{h} hr " if h else "") + (f"{r} min" if r else "")).strip()
MEETINGS = [(1,3),(4,6),(7,8),(9,10),(11,11),(12,13),(14,15),(16,19),(20,24)]
M = json.load(open(os.path.join(HERE, "modern.json"), encoding="utf-8"))
WB, OLD, IDIOMS, OLD_MARKS, IDIOM_MARKS = {}, {}, {}, {}, {}
for mod in sorted(f[:-3] for f in os.listdir(HERE) if re.match(r"oz_wb\d+\.py$", f)):
    w = importlib.import_module(mod)
    WB.update(w.WB); OLD.update(getattr(w, "OLD", {})); IDIOMS.update(getattr(w, "IDIOMS", {}))
    OLD_MARKS.update(getattr(w, "OLD_MARKS", {})); IDIOM_MARKS.update(getattr(w, "IDIOM_MARKS", {}))
stem = lambda w: w.lower()[:max(3, len(w) - 2)]
def roman_title(t):
    m = re.match(r"Chapter ([IVXLC]+) (.*)", t)
    vals = {"I":1,"V":5,"X":10,"L":50,"C":100}; r = m.group(1); n = 0
    for i, ch in enumerate(r):
        v = vals[ch]; n += -v if i + 1 < len(r) and vals[r[i+1]] > v else v
    return n, m.group(2)
CH = []
probs = []
for idx, c in enumerate(M, 1):
    n, name = roman_title(c["title"])
    text = "\n\n".join(c["paras"])
    def wrap(text, word, a, b):
        m = re.search(rf"(?<![\w*{{\[]){re.escape(word)}(?![\w])", text)
        if not m: probs.append(f"ch{n}: '{word}' not found"); return text
        return text[:m.start()] + a + m.group(0) + b + text[m.end():]
    if n in WB:
        for v in WB[n]["vocab"]: text = wrap(text, v[1], "**", "**")
    for w in OLD_MARKS.get(n, []):
        m = re.search(rf"\b{w}\b", text, re.I)
        if m: text = text[:m.start()] + "{{" + m.group(0) + "}}" + text[m.end():]
        else: probs.append(f"ch{n}: old word {w} not found")
    for w in IDIOM_MARKS.get(n, []): text = wrap(text, w, "[[", "]]")
    CH.append(dict(n=n, name=name, text=text, changes=c["changes"], words=len(" ".join(c["paras"]).split())))
for n, d in WB.items():
    words = [v[0] for v in d["vocab"]]
    for s_, a, ds in d["quiz"]:
        if s_.count("___") != 1 or a in ds or len(set(ds)) != 3: probs.append(f"ch{n}: quiz issue {a}")
    used = {w for w in words for s_, a, ds in d["quiz"] if a.lower().startswith(stem(w))}
    if set(words) - used: probs.append(f"ch{n}: untested {set(words) - used}")
print("\n".join(probs) or "validation OK")
words_total = sum(c["words"] for c in CH)
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
<h1 style='font-size:28pt'>{e(TITLE)}</h1><div class='author'>{e(sub)}</div>
<div class='note'>{note}</div>
<div class='credit'>Text: {e(SOURCE)}, public domain (Project Gutenberg edition). Every sentence and event is kept; only words no longer in everyday use were replaced with today's words. Markings and exercises were added by the English Book Club.</div></div>"""

LEGEND = """<div class='legend'>
<div><b class='v'>highlighted</b> — a word studied in the workbook</div>
<div><span class='old'>dotted<sup>†</sup></span> — an old word (or old meaning) kept on purpose (see the workbook)</div>
<div><span class='idi'>blue line<sup>※</sup></span> — an old expression that people no longer use (see the workbook)</div></div>"""

def meeting_of(n):
    for k, (a, b) in enumerate(MEETINGS, 1):
        if a <= n <= b: return k
def meeting_rows():
    rows = []
    for k, (a, b) in enumerate(MEETINGS, 1):
        w = sum(c["words"] for c in CH if a <= c["n"] <= b)
        chs = f"Chapter {a}" if a == b else f"Chapters {a}–{b}"
        rows.append(f"<tr><td class='n'>Meeting {k}</td><td>{chs} · {w:,} words · about {mins(w)} min</td></tr>")
    return "".join(rows)

def reader(path):
    p = [f"<html><head><meta charset='utf-8'><style>{CSS}{EXTRA}</style></head><body class='reader'>"]
    p.append(cover("L. Frank Baum's 1900 text in today's words", f"24 chapters · {words_total:,} words · Level 2 (B1)<br>Reading time: about {hm(words_total / WPM)} · with the workbook: about {hm(2 * words_total / WPM)} · {len(MEETINGS)} book club meetings (about 4,300 words each)."))
    p.append("<div class='page'><h2>How to Read This Book</h2><div>The original story is not changed. Baum's English is already close to today's, so only about sixty old words like <i>bade</i>, <i>presently</i> and <i>queer</i> were replaced. Three kinds of marks help you:</div>" + LEGEND +
             "<h3>READING TIME</h3><div>Most English learners read about 100 words a minute (1,000 words ≈ 10 minutes). With the workbook, plan about twice as long. Our book club reads about 4,300 words per meeting.</div>"
             "<h3>MEETINGS</h3><table class='chars'>" + meeting_rows() + "</table></div>")
    for c in CH:
        p.append(f"<div class='page'><div class='chlabel'>CHAPTER {c['n']} · MEETING {meeting_of(c['n'])}</div><h2>{e(c['name'])}</h2><div class='wc'>{c['words']} WORDS · ABOUT {mins(c['words'])} MIN</div>{mark(c['text'])}</div>")
    p.append("</body></html>")
    open(path, "w", encoding="utf-8").write("".join(p))

def workbook(path, chapters):
    random.seed(1900)
    p = [f"<html><head><meta charset='utf-8'><style>{CSS}{EXTRA}</style></head><body>"]
    rng = f"Chapters {chapters[0]}–{chapters[-1]}"
    p.append(cover(f"Workbook · {rng}", "Use with the reader. For each chapter: 10 word cards, 10 fill-in-the-blank questions, notes on old words and old expressions, the list of updated words, and questions to talk about."))
    p.append("<div class='page'><h2>How to Use This Workbook</h2><div>1. Read one chapter in the reader.<br>2. Study the 10 word cards.<br>3. Do the 10 practice questions without looking back.<br>"
             "4. Read the notes on old words (†) and old expressions (※).<br>5. Choose a question to talk about at the meeting.</div>" + LEGEND + "<h3>MEETINGS</h3><table class='chars'>" + meeting_rows() + "</table></div>")
    for c in CH:
        n = c["n"]
        if n not in chapters or n not in WB: continue
        wb = WB[n]; lab = f"<div class='chlabel'>CHAPTER {n} · {e(c['name'].upper())}</div>"
        for half in (0, 5):
            p.append(f"<div class='page'>{lab}<h2>{'Vocabulary' if half == 0 else 'Vocabulary (continued)'}</h2>")
            for k, (w, surf, pos, st, ipa, ko, col, ex1, ex2) in enumerate(wb["vocab"][half:half + 5], half + 1):
                p.append(f"""<div class='card'><div><span class='num'>{k:02d}</span><span class='w'>{e(w)}</span><span class='pos'>{e(pos)}</span>
<span class='pron'>{e(st)} · {e(ipa)}</span><span class='ko'>({e(ko)})</span></div>
<div class='col'><span class='lbl'>COLLOCATIONS</span>{e(col)}</div><ul><li>{e(ex1)}</li><li>{e(ex2)}</li></ul></div>""")
            p.append("</div>")
        key = []
        p.append(f"<div class='page'>{lab}<h2>Practice &amp; Talk</h2><p>Choose the best word. Watch the form of the word (-ed, -s, -ly).</p>")
        for k, (s_, a, d) in enumerate(wb["quiz"], 1):
            opts = [a] + d; random.shuffle(opts)
            key.append(f"{k}. ({'abcd'[opts.index(a)]}) {a}")
            os_ = "".join(f"<span>({l}) {e(o)}</span>" for l, o in zip("abcd", opts))
            p.append(f"<div class='q'><b>{k}.</b> {e(s_).replace('___', '__________')}<div class='opts'>{os_}</div></div>")
        p.append("<h3>LET'S TALK</h3><ol class='disc'>" + "".join(f"<li>{e(d)}<div class='lines'></div></li>" for d in wb["discussion"]) + "</ol>")
        p.append("<h3>ANSWER KEY</h3><div class='key'>" + "<br>".join(e(k) for k in key) + "</div></div>")
        olds = list(dict.fromkeys(re.findall(r"\{\{(.+?)\}\}", c["text"])))
        idis = list(dict.fromkeys(re.findall(r"\[\[(.+?)\]\]", c["text"])))
        if olds or idis or c["changes"]:
            p.append(f"<div class='page'>{lab}<h2>Old Words &amp; Expressions</h2>")
            if olds:
                p.append("<h3>OLD WORDS KEPT †</h3>")
                for k_ in olds:
                    pos, ko, m_ = OLD[k_.lower()]
                    p.append(f"<div class='note-box'><span class='h'>{e(k_)}</span> <span class='pos'>{e(pos)}</span><span class='ko'>({e(ko)})</span><div class='m'>{e(m_)}</div></div>")
            if idis:
                p.append("<h3>OLD EXPRESSIONS ※</h3>")
                for k_ in idis:
                    ko, mod, ex = IDIOMS[k_]
                    p.append(f"<div class='note-box'><span class='h'>{e(k_)}</span><span class='ko'>({e(ko)})</span><div class='m'><b>Today:</b> {e(mod)}</div><div class='m' style='color:#666'>{e(ex)}</div></div>")
            if c["changes"]:
                p.append("<h3>WORDS WE UPDATED</h3><table class='ch'><tr><td><b>1900</b></td><td><b>Today</b></td></tr>" + "".join(f"<tr><td class='o'>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in c["changes"]) + "</table>")
            p.append("</div>")
    p.append("</body></html>")
    open(path, "w", encoding="utf-8").write("".join(p))

if __name__ == "__main__":
    out = "/home/claude/reading-ladder-site/workbooks"
    chapters = sorted(WB)
    reader(os.path.join(SCR, "oz_reader.html")); workbook(os.path.join(SCR, "oz_wb.html"), chapters)
    name_wb = f"oz-workbook-ch{chapters[0]}-{chapters[-1]}.pdf"
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page()
        for src, pdf in [("oz_reader.html", "oz-reader.pdf"), ("oz_wb.html", name_wb)]:
            pg.goto("file://" + os.path.join(SCR, src)); pg.pdf(path=os.path.join(out, pdf), format="A4", print_background=True, prefer_css_page_size=True)
        b.close()
    import pypdfium2 as pd
    for pdf in ["oz-reader.pdf", name_wb]:
        d = pd.PdfDocument(os.path.join(out, pdf)); print(pdf, len(d), "pages")
        for k in [1, 2, 4]:
            d[k].render(scale=0.6).to_pil().save(os.path.join(SCR, "prev", f"oz_{pdf[3:9]}_{k}.png"))
