import os, re, sys, html, random, json, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from playwright.sync_api import sync_playwright
REPO = os.path.dirname(HERE)
SCR = os.environ.get("BUILD_TMP", os.path.join(REPO, ".build")); os.makedirs(os.path.join(SCR, "prev"), exist_ok=True)
CSS = open(os.path.join(HERE, "animal-farm", "style.css"), encoding="utf-8").read()
e = html.escape
BOOK = sys.argv[1]
CFG = {
 "oz": dict(dir=os.path.join(HERE, "oz"), title="The Wonderful Wizard of Oz", source="L. Frank Baum, The Wonderful Wizard of Oz (1900)", year="1900", sub="L. Frank Baum's 1900 text in today's words", level="Level 2 (B1)",
            meetings=[(1,3),(4,6),(7,8),(9,10),(11,11),(12,13),(14,15),(16,19),(20,24)], slug="oz", unit="Chapter",
            intro="Baum's English is already close to today's, so only about sixty old words like <i>bade</i>, <i>presently</i> and <i>queer</i> were replaced."),
 "alice": dict(dir=os.path.join(HERE, "alice"), title="Alice's Adventures in Wonderland", source="Lewis Carroll, Alice's Adventures in Wonderland (1865)", year="1865", sub="Lewis Carroll's 1865 text in today's words", level="Level 3 (B1–B2)",
            meetings=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)], slug="alice", unit="Chapter",
            intro="Carroll's prose is close to today's English, so only about forty old words like <i>queer</i>, <i>shan't</i> and <i>to-day</i> were replaced. The poems are kept exactly as written, because changing a word would break the rhyme."),
 "anne": dict(dir=os.path.join(HERE, "anne"), title="Anne of Green Gables", source="L. M. Montgomery, Anne of Green Gables (1908)", year="1908", sub="L. M. Montgomery's 1908 text in today's words", level="Level 3 (B1–B2)",
            meetings=[(1,1),(2,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,15),(16,16),(17,18),(19,19),(20,21),(22,23),(24,25),(26,27),(28,28),(29,29),(30,30),(31,32),(33,33),(34,35),(36,37),(38,38)], slug="anne", unit="Chapter",
            intro="Montgomery's English is close to today's, so only about seventy old words like <i>presently</i>, <i>queer</i> and <i>beheld</i> were replaced. Anne's own old-fashioned words, such as <i>thou</i> and <i>thee</i> when she is being romantic, are kept on purpose, because they show her character. Prayers and poems are also kept as written."),
 "jungle": dict(dir=os.path.join(HERE, "jungle"), title="The Jungle Book", source="Rudyard Kipling, The Jungle Book (1894)", year="1894", sub="Rudyard Kipling's 1894 text in today's words", level="Level 3 (B2)",
            meetings=[(1,2,2),(3,4,2),(5,6,2),(7,8,2),(9,10,1),(11,12,2),(13,14,1)], slug="jungle", unit="Section",
            intro="Kipling's animals speak in old English: <i>thou art</i>, <i>hast thou</i>, <i>ye</i>. In the stories these were changed to today's English (<i>you are</i>, <i>have you</i>, <i>you</i>), about 300 changes in all. The songs are kept exactly as written, because changing a word would break the rhyme. The Jungle's Master Word, <i>We be of one blood, ye and I</i>, is also kept as Kipling wrote it.",
            wb_cover="Use with the reader. For each story: 20 word cards, 20 fill-in-the-blank questions, notes on old words and old expressions, the list of updated words, and questions to talk about. For each song: notes on the old words and one question.",
            wb_howto="1. Read the story in the reader. Most stories take two meetings: words 1–10 come from the first half, words 11–20 from the second half.<br>2. Study the word cards for your meeting.<br>3. Do the practice questions without looking back (questions follow the story in order).<br>4. Read the notes on old words (†) and old expressions (※), and the list of words we updated.<br>5. Read the song after each story and choose a question to talk about at the meeting."),
}[BOOK]
TITLE, SOURCE = CFG["title"], CFG["source"]
WPM = 100
def mins(n): return max(1, round(n / WPM))
def hm(m):
    h, r = divmod(int(round(m / 5.0) * 5), 60)
    return ((f"{h} hr " if h else "") + (f"{r} min" if r else "")).strip()
MEETINGS = CFG["meetings"]
M = json.load(open(os.path.join(CFG["dir"], "modern.json"), encoding="utf-8"))
sys.path.insert(0, CFG["dir"])
WB, OLD, IDIOMS, OLD_MARKS, IDIOM_MARKS = {}, {}, {}, {}, {}
for mod in sorted(f[:-3] for f in os.listdir(CFG["dir"]) if re.match(CFG["slug"] + r"_wb\d+\.py$", f)):
    w = importlib.import_module(mod)
    WB.update(w.WB); OLD.update(getattr(w, "OLD", {})); IDIOMS.update(getattr(w, "IDIOMS", {}))
    OLD_MARKS.update(getattr(w, "OLD_MARKS", {})); IDIOM_MARKS.update(getattr(w, "IDIOM_MARKS", {}))
stem = lambda w: w.lower()[:max(3, len(w) - 2)]
def roman_title(t, idx=None):
    m = re.match(r"(?i)Chapter ([IVXLC]+)\.? (.*)", t)
    if not m: return idx, t
    vals = {"I":1,"V":5,"X":10,"L":50,"C":100}; r = m.group(1); n = 0
    for i, ch in enumerate(r):
        v = vals[ch]; n += -v if i + 1 < len(r) and vals[r[i+1]] > v else v
    return n, m.group(2)
CH = []
probs = []
for idx, c in enumerate(M, 1):
    n, name = roman_title(c["title"], idx)
    paras = [p if isinstance(p, dict) else {"t": p, "poem": False} for p in c["paras"]]
    blocks = [("@@POEM@@" + p["t"].replace("\n\n", "\n@@STANZA@@\n")) if p["poem"] else p["t"] for p in paras]
    for g in MEETINGS:
        if len(g) > 2 and g[2] == 2 and g[0] == n:
            prose = [i for i, p in enumerate(paras) if not p["poem"]]
            tot = sum(len(paras[i]["t"].split()) for i in prose); acc = 0; best = None
            for i in prose:
                if best is None or abs(acc - tot / 2) < abs(best[1] - tot / 2): best = (i, acc)
                acc += len(paras[i]["t"].split())
            k2 = sum((gg[2] if len(gg) > 2 else 1) for gg in MEETINGS[:MEETINGS.index(g)]) + 2
            blocks.insert(best[0], f"@@BREAK@@{k2}")
    text = "\n\n".join(blocks)
    def wrap(text, word, a, b):
        m = re.search(rf"(?<![\w*{{\[]){re.escape(word)}(?![\w])", text)
        if not m: probs.append(f"ch{n}: '{word}' not found"); return text
        return text[:m.start()] + a + m.group(0) + b + text[m.end():]
    if n in WB:
        for v in WB[n]["vocab"]: text = wrap(text, v[1], "**", "**")
    for w in OLD_MARKS.get(n, []):
        m = re.search(rf"\b{w}\b(?![’'])", text) if w[:1].isupper() else re.search(rf"\b{w}\b", text, re.I)
        if m: text = text[:m.start()] + "{{" + m.group(0) + "}}" + text[m.end():]
        else: probs.append(f"ch{n}: old word {w} not found")
    for w in IDIOM_MARKS.get(n, []): text = wrap(text, w, "[[", "]]")
    CH.append(dict(n=n, name=name, text=text, changes=c["changes"], words=len(" ".join(p["t"] for p in paras).split())))
for n, d in WB.items():
    words = [v[0] for v in d["vocab"]]
    for s_, a, ds in d["quiz"]:
        if s_.count("___") != 1 or a in ds or len(set(ds)) != 3: probs.append(f"ch{n}: quiz issue {a}")
    used = {v[0] for v in d["vocab"] for s_, a, ds in d["quiz"] if a.lower().startswith(stem(v[0])) or a.lower() == v[1].lower()}
    if set(words) - used: probs.append(f"ch{n}: untested {set(words) - used}")
print("\n".join(probs) or "validation OK")
words_total = sum(c["words"] for c in CH)
print("words:", words_total)

EXTRA = """
.mbreak { margin: 18px 0; padding: 6px 0; border-top: 2px dashed #c9b78f; border-bottom: 2px dashed #c9b78f; text-align: center; font-size: 9pt; letter-spacing: 3px; color: #8a5a2b; font-weight: 700; }
.reader p.poem { font-style: italic; margin: 6px 0 10px 28px; line-height: 1.55; }
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
        if p.startswith("@@BREAK@@"):
            out.append(f"<div class='mbreak'>MEETING {p[9:]} STARTS HERE</div>"); continue
        if p.startswith("@@POEM@@"):
            p = p[8:].replace("\n@@STANZA@@\n", "</p><p class='poem'>").replace("\n", "<br>")
            out.append(f"<p class='poem'>{p}</p>")
        else:
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

def _groups():
    k = 1; out = []
    for g in MEETINGS:
        a, b = g[0], g[1]; cnt = g[2] if len(g) > 2 else 1
        out.append((a, b, k, k + cnt - 1)); k += cnt
    return out
def meeting_of(n):
    for a, b, k1, k2 in _groups():
        if a <= n <= b: return str(k1) if k1 == k2 else f"{k1}–{k2}"
def n_meetings(): return _groups()[-1][3]
def meeting_rows():
    rows = []
    for a, b, k1, k2 in _groups():
        w = sum(c["words"] for c in CH if a <= c["n"] <= b)
        chs = (f"{CFG['unit']} {a}" if a == b else f"{CFG['unit']}s {a}–{b}") + (" · " + " / ".join(c["name"] for c in CH if a <= c["n"] <= b) if CFG["unit"] == "Section" else "")
        lab = f"Meeting {k1}" if k1 == k2 else f"Meetings {k1}–{k2}"
        rows.append(f"<tr><td class='n'>{lab}</td><td>{e(chs)} · {w:,} words · about {mins(w)} min</td></tr>")
    return "".join(rows)

def reader(path):
    p = [f"<html><head><meta charset='utf-8'><style>{CSS}{EXTRA}</style></head><body class='reader'>"]
    p.append(cover(CFG["sub"], f"{len(CH)} {CFG['unit'].lower()}s · {words_total:,} words · {CFG['level']}<br>Reading time: about {hm(words_total / WPM)} · with the workbook: about {hm(2 * words_total / WPM)} · {n_meetings()} book club meetings (about 4,300 words each)."))
    p.append("<div class='page'><h2>How to Read This Book</h2><div>The original story is not changed. " + CFG["intro"] + " Three kinds of marks help you:</div>" + LEGEND +
             "<h3>READING TIME</h3><div>Most English learners read about 100 words a minute (1,000 words ≈ 10 minutes). With the workbook, plan about twice as long. Our book club reads about 4,300 words per meeting.</div>"
             "<h3>MEETINGS</h3><table class='chars'>" + meeting_rows() + "</table></div>")
    for c in CH:
        p.append(f"<div class='page'><div class='chlabel'>{CFG['unit'].upper()} {c['n']} · MEETING {meeting_of(c['n'])}</div><h2>{e(c['name'])}</h2><div class='wc'>{c['words']} WORDS · ABOUT {mins(c['words'])} MIN</div>{mark(c['text'])}</div>")
    p.append("</body></html>")
    open(path, "w", encoding="utf-8").write("".join(p))

def meeting_label(n, i=0, total=10):
    for a, b, k1, k2 in _groups():
        if a <= n <= b:
            if k1 == k2 or total <= 10 or i is None: return f"MEETING {k1}" if k1 == k2 else f"MEETINGS {k1}–{k2}"
            return f"MEETING {k1 if i < total / 2 else k2}"
    return ""

def workbook(path, chapters):
    random.seed(int(CFG["year"]))
    p = [f"<html><head><meta charset='utf-8'><style>{CSS}{EXTRA}</style></head><body>"]
    unit = CFG["unit"]
    rng = f"{unit}s {chapters[0]}–{chapters[-1]}"
    p.append(cover(f"Workbook · {rng}", CFG.get("wb_cover", "Use with the reader. For each chapter: 10 word cards, 10 fill-in-the-blank questions, notes on old words and old expressions, the list of updated words, and questions to talk about.")))
    p.append("<div class='page'><h2>How to Use This Workbook</h2><div>" + CFG.get("wb_howto", "1. Read one chapter in the reader.<br>2. Study the 10 word cards.<br>3. Do the 10 practice questions without looking back.<br>"
             "4. Read the notes on old words (†) and old expressions (※).<br>5. Choose a question to talk about at the meeting.") + "</div>" + LEGEND + "<h3>MEETINGS</h3><table class='chars'>" + meeting_rows() + "</table></div>")
    for c in CH:
        n = c["n"]
        if n not in chapters or n not in WB: continue
        wb = WB[n]; nv = len(wb["vocab"])
        lab = lambda i=None: f"<div class='chlabel'>{unit.upper()} {n} · {e(c['name'].upper())}" + (f" · {meeting_label(n, i, nv)}" if nv > 10 or CFG['slug'] == 'jungle' else "") + "</div>"
        for half in range(0, nv, 5):
            p.append(f"<div class='page'>{lab(half)}<h2>{'Vocabulary' if half == 0 else 'Vocabulary (continued)'}</h2>")
            for k, (w, surf, pos, st, ipa, ko, col, ex1, ex2) in enumerate(wb["vocab"][half:half + 5], half + 1):
                p.append(f"""<div class='card'><div><span class='num'>{k:02d}</span><span class='w'>{e(w)}</span><span class='pos'>{e(pos)}</span>
<span class='pron'>{e(st)} · {e(ipa)}</span><span class='ko'>({e(ko)})</span></div>
<div class='col'><span class='lbl'>COLLOCATIONS</span>{e(col)}</div><ul><li>{e(ex1)}</li><li>{e(ex2)}</li></ul></div>""")
            p.append("</div>")
        if wb["quiz"]:
            key = []; qs = list(enumerate(wb["quiz"], 1))
            for start in range(0, len(qs), 10):
                first = start == 0; last = start + 10 >= len(qs)
                p.append(f"<div class='page'>{lab(start)}<h2>{'Practice &amp; Talk' if first and last else ('Practice' if first else 'Practice (continued)')}</h2>")
                if first: p.append("<p>Choose the best word. Watch the form of the word (-ed, -s, -ly).</p>")
                for k, (s_, a, d) in qs[start:start + 10]:
                    opts = [a] + d; random.shuffle(opts)
                    key.append(f"{k}. ({'abcd'[opts.index(a)]}) {a}")
                    os_ = "".join(f"<span>({l}) {e(o)}</span>" for l, o in zip("abcd", opts))
                    p.append(f"<div class='q'><b>{k}.</b> {e(s_).replace('___', '__________')}<div class='opts'>{os_}</div></div>")
                if last:
                    p.append("<h3>LET'S TALK</h3><ol class='disc'>" + "".join(f"<li>{e(d)}<div class='lines'></div></li>" for d in wb["discussion"]) + "</ol>")
                    p.append("<h3>ANSWER KEY</h3><div class='key'>" + "<br>".join(e(k) for k in key) + "</div>")
                p.append("</div>")
        olds = list(dict.fromkeys(re.findall(r"\{\{(.+?)\}\}", c["text"])))
        idis = list(dict.fromkeys(re.findall(r"\[\[(.+?)\]\]", c["text"])))
        talk_here = not wb["quiz"] and wb.get("discussion")
        if olds or idis or c["changes"] or talk_here:
            p.append(f"<div class='page'>{lab()}<h2>{'Song Notes' if not nv else 'Old Words &amp; Expressions'}</h2>")
            if not nv: p.append("<p>The songs are kept exactly as Kipling wrote them. These notes explain the old words.</p>" if CFG["slug"] == "jungle" else "")
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
                p.append(f"<h3>WORDS WE UPDATED</h3><table class='ch'><tr><td><b>{CFG['year']}</b></td><td><b>Today</b></td></tr>" + "".join(f"<tr><td class='o'>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in c["changes"]) + "</table>")
            if talk_here:
                p.append("<h3>LET'S TALK</h3><ol class='disc'>" + "".join(f"<li>{e(d)}<div class='lines'></div><div class='lines'></div></li>" for d in wb["discussion"]) + "</ol>")
            p.append("</div>")
    p.append("</body></html>")
    open(path, "w", encoding="utf-8").write("".join(p))

if __name__ == "__main__":
    out = os.path.join(REPO, "workbooks"); sl = CFG["slug"]
    chapters = sorted(WB)
    reader(os.path.join(SCR, f"{sl}_reader.html"))
    jobs = [(f"{sl}_reader.html", f"{sl}-reader.pdf")]
    if chapters:
        workbook(os.path.join(SCR, f"{sl}_wb.html"), chapters)
        jobs.append((f"{sl}_wb.html", f"{sl}-workbook.pdf"))
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page()
        for src, pdf in jobs:
            pg.goto("file://" + os.path.join(SCR, src)); pg.pdf(path=os.path.join(out, pdf), format="A4", print_background=True, prefer_css_page_size=True)
        b.close()
    import pypdfium2 as pd
    for _, pdf in jobs:
        d = pd.PdfDocument(os.path.join(out, pdf)); print(pdf, len(d), "pages")
        for k in [1, 2, 4]:
            d[k].render(scale=0.6).to_pil().save(os.path.join(SCR, "prev", f"{pdf[:-4]}_{k}.png"))
