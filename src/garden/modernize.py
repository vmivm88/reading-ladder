import json, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
chs = json.load(open("chapters.json", encoding="utf-8"))
# (pattern, replacement, old label, new label, expected count) — prose only; poems and the hymn are kept.
# Yorkshire dialect (tha’, thee, mun, nowt, th’ ...) is kept as written and explained in the workbook.
RULES = [
 (r"\bqueer\b", "strange", "queer", "strange", 57),
 (r"\bqueerer\b", "stranger", "queerer", "stranger", 1),
 (r"\bqueerest\b", "strangest", "queerest", "strangest", 2),
 (r"\bqueerly\b", "strangely", "queerly", "strangely", 1),
 (r"I shall make you tell me about Rajahs presently", "I shall make you tell me about Rajahs later", "presently", "later", 1),
 (r"\bPresently\b", "Soon", "presently", "soon", 6),
 (r"\bpresently\b", "soon", "presently", "soon", 3),
 (r"\bbeheld\b", "saw", "beheld", "saw", 2),
 (r"lest his robin should start away", "in case his robin should start away", "lest", "in case", 1),
 (r"amuse herself with gay people", "amuse herself with lively people", "gay (= merry)", "lively", 1),
 (r"her gay, lovely eyes", "her merry, lovely eyes", "gay (= merry)", "merry", 1),
 (r"\bshan’t\b", "won’t", "shan’t", "won’t", 3),
 (r"\bmayn’t\b", "might not", "mayn’t", "might not", 4),
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
