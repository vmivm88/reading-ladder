import json, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
chs = json.load(open("chapters.json", encoding="utf-8"))
# (pattern, replacement, old label, new label, expected count) — prose only; songs, the poem, the schedule and lists are kept.
# Fitzgerald's English is modern. Only words whose everyday meaning has changed are replaced.
RULES = [
 (r"knew that presently dinner", "knew that soon dinner", "presently", "soon", 1),
 (r"\bPresently Tom\b", "Soon Tom", "presently", "soon", 1),
 (r"he said presently", "he said after a moment", "presently", "after a moment", 1),
 (r"and presently a lovely", "and soon a lovely", "presently", "soon", 1),
 (r"I ejaculated an unrestrained", "I let out an unrestrained", "ejaculated (= cried out)", "let out", 1),
 (r"had done gay, exciting things", "had done fun, exciting things", "gay (= merry)", "fun", 1),
 (r"there were gay, exciting things", "there were fun, exciting things", "gay (= merry)", "fun", 1),
 (r"Having a gay time now", "Having a good time now", "gay (= merry)", "good", 1),
 (r"she was gay again, gay as ever", "she was cheerful again, cheerful as ever", "gay (= merry)", "cheerful", 1),
 (r"in the course of gay parties", "in the course of lively parties", "gay (= merry)", "lively", 1),
 (r"of gay and radiant activities", "of lively and radiant activities", "gay (= merry)", "lively", 1),
 (r"more mysterious and gay than", "more mysterious and lively than", "gay (= merry)", "lively", 1),
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
