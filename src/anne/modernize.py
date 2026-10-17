import json, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
chs = json.load(open("chapters.json", encoding="utf-8"))
# (pattern, replacement, old label, new label, expected count) — prose only; poems, prayers and Anne's deliberate "thou/thee" are kept
RULES = [
 (r"\bPresently\b", "Soon", "presently", "soon", 5),
 (r"\bpresently\b", "soon", "presently", "soon", 9),
 (r"\bqueer\b", "strange", "queer", "strange", 14),
 (r"\bhastened\b", "hurried", "hastened", "hurried", 6),
 (r"as she bade them good-bye", "as she said goodbye to them", "bade ... good-bye", "said goodbye to", 1),
 (r"\bgood-bye\b", "goodbye", "good-bye", "goodbye", 4),
 (r"\bbeheld\b", "saw", "beheld", "saw", 5),
 (r"it was to behold Diana", "it was to see Diana", "behold", "see", 1),
 (r"Please, mayn’t I go", "Please, can’t I go", "mayn’t", "can’t", 1),
 (r"\bmayn’t\b", "may not", "mayn’t", "may not", 3),
 (r"did any one ever see", "did anyone ever see", "any one", "anyone", 1),
 (r"to any one for a spell", "to anyone for a spell", "any one", "anyone", 1),
 (r"\bsome one\b", "someone", "some one", "someone", 2),
 (r"lest Marilla return prematurely", "in case Marilla returned prematurely", "lest ... return", "in case ... returned", 1),
 (r"lest Marilla should suspect", "in case Marilla suspected", "lest ... should suspect", "in case ... suspected", 1),
 (r"lest it should keep on raining", "in case it kept on raining", "lest it should keep", "in case it kept", 1),
 (r"were wont to tell", "used to tell", "were wont to", "used to", 1),
 (r"she was wont to run", "she used to run", "was wont to", "used to", 1),
 (r"the east one, whence you got", "the east one, from which you got", "whence", "from which", 1),
 (r"to hills whence a far sweep", "to hills from which a far sweep", "whence", "from which", 1),
 (r"\bThereupon Anne\b", "Then Anne", "thereupon", "then", 1),
 (r"were thereupon tied", "were then tied", "thereupon", "then", 1),
 (r"do as I bid you", "do as I tell you", "bid", "tell", 1),
 (r"Do as I bid you", "Do as I tell you", "bid", "tell", 1),
 (r", whereupon she always", ", and then she always", "whereupon", "and then", 1),
 (r"Whereupon Anne arose", "At this Anne arose", "whereupon", "at this", 1),
 (r"side of politics; hence on the night", "side of politics; so on the night", "hence", "so", 1),
 (r"\bHence, while Marilla", "So, while Marilla", "hence", "so", 1),
 (r"triumph on the morrow", "triumph the next day", "on the morrow", "the next day", 1),
 (r"liked Anne—nay, that", "liked Anne—no, that", "nay", "no", 1),
 (r"\bshan’t\b", "won’t", "shan’t", "won’t", 1),
 (r"\bsha’n’t\b", "won’t", "sha’n’t", "won’t", 1),
]
out = []; totals = {}
for c in chs:
    changes = []; newp = []
    for p in c["paras"]:
        t = p["t"]
        if not p["poem"]:
            for pat, rep, o, n, _ in RULES:
                k = len(re.findall(pat, t))
                if k:
                    t = re.sub(pat, rep, t); totals[pat] = totals.get(pat, 0) + k; changes += [(o, n)] * k
        newp.append({"t": t, "poem": p["poem"]})
    seen = []; [seen.append(x) for x in changes if x not in seen]
    out.append({"title": c["title"], "paras": newp, "changes": seen, "n_changes": len(changes)})
for pat, rep, o, n, exp in RULES:
    if exp is not None and totals.get(pat, 0) != exp: print("COUNT MISMATCH", pat, totals.get(pat, 0), exp)
json.dump(out, open("modern.json", "w", encoding="utf-8"), ensure_ascii=False)
print("total replacements:", sum(c["n_changes"] for c in out))
