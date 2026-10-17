import os, sys, random, html, re
S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from data_a import CHAPTERS_A
from data_b import CHAPTERS_B

# Load chapter 1 data from the sample builder (data section only)
src = open(os.path.join(S, "build_ch1.py"), encoding="utf-8").read()
src = src.split("random.seed(7)")[0]
ns = {"sys": sys, "__name__": "ch1"}
src = src.replace("OUT_HTML = sys.argv[1]", "").replace("OUT_PDF = sys.argv[2]", "")
exec(src, ns)
CH1 = dict(num=1, title="Old Major's Dream", summary=ns["SUMMARY"], characters=ns["CHARACTERS"],
           vocab=ns["VOCAB"], quiz=ns["QUIZ"], discussion=ns["DISCUSSION"])
CHAPTERS = [CH1] + CHAPTERS_A + CHAPTERS_B

# ---- apply copyright-safe rewrites ----
import patch as P
for ch in CHAPTERS:
    n = ch["num"]
    ch["quiz"] = list(ch["quiz"])
    for q, item in P.QUIZ.get(n, {}).items():
        ch["quiz"][q - 1] = item
    if n in P.SUMMARY:
        ch["summary"] = P.SUMMARY[n]
    ch["discussion"] = list(ch["discussion"])
    for q, text in P.DISCUSSION.get(n, {}).items():
        ch["discussion"][q - 1] = text
    newv = []
    for v in ch["vocab"]:
        c = P.CTX.get(n, {}).get(v[0])
        newv.append(v[:6] + (c,) + v[7:] if c else v)
    ch["vocab"] = newv

# ---- validation ----
seen = {}
problems = []
for ch in CHAPTERS:
    n = ch["num"]
    if len(ch["vocab"]) != 20: problems.append(f"ch{n}: {len(ch['vocab'])} vocab")
    if len(ch["quiz"]) != 20: problems.append(f"ch{n}: {len(ch['quiz'])} quiz")
    for v in ch["vocab"]:
        if len(v) != 9: problems.append(f"ch{n}: bad tuple {v[0]}")
        w = v[0].lower()
        if w in seen: problems.append(f"dup word {w}: ch{seen[w]} & ch{n}")
        seen[w] = n
    words = [v[0].lower() for v in ch["vocab"]]
    used = set()
    for s, a, d in ch["quiz"]:
        if s.count("___") != 1: problems.append(f"ch{n}: blank count in '{s}'")
        if a in d or len(set(d)) != 3: problems.append(f"ch{n}: options issue '{a}'")
        stem = a.lower()[:4]
        match = [w for w in words if w[:min(4,len(w)-1)] == a.lower()[:min(4,len(w)-1)]]
        if not match: problems.append(f"ch{n}: answer '{a}' not from word list")
        used.update(match)
    missing = set(words) - used
    if missing: problems.append(f"ch{n}: words not tested {missing}")
print("\n".join(problems) or "validation OK")

e = html.escape
random.seed(2026)

CSS = open(os.path.join(S, "style.css"), encoding="utf-8").read()

def chapter_html(ch):
    n, out, key = ch["num"], [], []
    out.append(f"<div class='page'><div class='chlabel'>CHAPTER {n}</div><h2>{e(ch['title'])}</h2>")
    out.append(f"<h3>SUMMARY</h3><div class='summary'>{e(ch['summary'])}</div>")
    if ch["characters"]:
        lab = "WHO'S WHO" if n == 1 else "NEW FACES"
        out.append(f"<h3>{lab}</h3><table class='chars'>")
        for a, b in ch["characters"]:
            out.append(f"<tr><td class='n'>{e(a)}</td><td>{e(b)}</td></tr>")
        out.append("</table>")
    out.append("<h3>WORDS IN THIS CHAPTER</h3><div class='wordlist'>" +
               " · ".join(e(v[0]) for v in ch["vocab"]) + "</div>")
    out.append("</div>")
    for start in range(0, 20, 7):
        title = "Vocabulary" if start == 0 else "Vocabulary (continued)"
        out.append(f"<div class='page'><div class='chlabel'>CHAPTER {n}</div><h2>{title}</h2>")
        for i, (w, pos, st, ipa, ko, col, ctx, ex1, ex2) in enumerate(ch["vocab"][start:start+7], start+1):
            out.append(f"""<div class='card'>
<div><span class='num'>{i:02d}</span><span class='w'>{e(w)}</span><span class='pos'>{e(pos)}</span>
<span class='pron'>{e(st)} · {e(ipa)}</span><span class='ko'>({e(ko)})</span></div>
<div class='col'><span class='lbl'>COLLOCATIONS</span>{e(col)}</div>
<div class='ctx'><span class='lbl'>IN THE STORY</span>{e(ctx)}</div>
<ul><li>{e(ex1)}</li><li>{e(ex2)}</li></ul></div>""")
        out.append("</div>")
    items = []
    for i, (s, a, d) in enumerate(ch["quiz"], 1):
        opts = [a] + d
        random.shuffle(opts)
        L = "abcd"[opts.index(a)]
        key.append(f"{i}. ({L}) {a}")
        items.append((i, s, opts))
    for start in (0, 10):
        title = "Practice: Fill in the Blank" if start == 0 else "Practice (continued)"
        out.append(f"<div class='page'><div class='chlabel'>CHAPTER {n}</div><h2>{title}</h2>")
        if start == 0:
            out.append(f"<p>Choose the best word to complete each sentence about Chapter {n}. Watch the form of the word (-ed, -s, -ly).</p>")
        for i, s, opts in items[start:start+10]:
            os_ = "".join(f"<span>({l}) {e(o)}</span>" for l, o in zip("abcd", opts))
            out.append(f"<div class='q'><b>{i}.</b> {e(s).replace('___', '__________')}<div class='opts'>{os_}</div></div>")
        out.append("</div>")
    out.append(f"<div class='page'><div class='chlabel'>CHAPTER {n}</div><h2>Let's Talk</h2>"
               "<p>Pick two questions. Try to use at least one word from this chapter in your answer.</p><ol class='disc'>")
    for d in ch["discussion"]:
        out.append(f"<li>{e(d)}<div class='lines'></div><div class='lines'></div></li>")
    out.append("</ol><h3>ANSWER KEY</h3><div class='key'>" + "<br>".join(e(k) for k in key) + "</div></div>")
    return "".join(out)

SCHEDULE = [("Week 1", "Chapters 1–2", "Old Major's dream and the Rebellion"),
            ("Week 2", "Chapters 3–4", "The first harvest and the Battle of the Cowshed"),
            ("Week 3", "Chapter 5", "Snowball is driven out"),
            ("Week 4", "Chapter 6", "Trade and the fallen windmill"),
            ("Week 5", "Chapter 7", "The confessions"),
            ("Week 6", "Chapter 8", "The Battle of the Windmill"),
            ("Week 7", "Chapters 9–10", "Boxer's fate and the final dinner")]

def build(chs, path_html, cover_sub):
    p = [f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"]
    p.append(f"""<div class='page cover'><div class='series'>ENGLISH BOOK CLUB WORKBOOK</div>
<h1>Animal Farm</h1><div class='author'>George Orwell</div><div class='ch'>{e(cover_sub)}</div>
<div class='note'>Vocabulary &amp; Usage Workbook — read each chapter in your own copy of the book, then use this workbook to study 20 key words per chapter, practise them in context, and prepare for discussion.</div><div class='credit' style='font-size:9pt;color:#6b5d45;margin:50px auto 0;width:135mm;line-height:1.6'>This workbook contains no text from the novel; summaries, examples and questions are original. © 2026 Fine pearls (파인펄스) · Reading Ladder, licensed under CC BY-NC 4.0 (creativecommons.org/licenses/by-nc/4.0): free to share and adapt for non-commercial use with credit.</div></div>""")
    if len(chs) > 1:
        p.append("<div class='page'><h2>How to Use This Workbook</h2>"
                 "<div>1. Read the chapter in your own copy and underline the 20 words when you meet them.<br>"
                 "2. Study each word card: pronunciation, meaning, common word partners (collocations), and examples.<br>"
                 "3. Complete the 20 fill-in-the-blank questions without looking back.<br>"
                 "4. Choose two discussion questions to talk about at the meeting.</div>"
                 "<h3>SEVEN-WEEK READING PLAN (ABOUT 4,300 WORDS A WEEK)</h3><table class='chars'>")
        for a, b, c in SCHEDULE:
            p.append(f"<tr><td class='n'>{a}</td><td><b>{b}</b> — {e(c)}</td></tr>")
        p.append("</table><h3>CONTENTS</h3><table class='chars'>")
        for ch in chs:
            p.append(f"<tr><td class='n'>Chapter {ch['num']}</td><td>{e(ch['title'])}</td></tr>")
        p.append("</table><div class='foot'>Summaries, examples and practice sentences are original to this workbook; no text from the novel is reproduced.</div></div>")
    for ch in chs:
        p.append(chapter_html(ch))
    p.append("</body></html>")
    open(path_html, "w", encoding="utf-8").write("".join(p))

if __name__ == "__main__":
    build(CHAPTERS, os.path.join(S, "full.html"), "Chapters 1–10")
    print("html written")
