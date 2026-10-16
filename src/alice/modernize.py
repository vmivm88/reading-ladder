import json, re
chs = json.load(open("chapters.json"))
# (pattern, replacement, old label, new label, expected) — prose only; poems are kept as written
RULES = [
 (r"\bPresently\b", "Soon", "presently", "soon", 2),
 (r"\bshan’t\b", "won’t", "shan’t", "won’t", 5),
 (r"\bShan’t\b", "Won’t", "shan’t", "won’t", 1),
 (r"\bqueer-looking\b", "strange-looking", "queer", "strange", 1),
 (r"\bqueer-shaped\b", "strange-shaped", "queer", "strange", 1),
 (r"\bqueerest\b", "strangest", "queerest", "strangest", 1),
 (r"\bqueer\b", "strange", "queer", "strange", 10),
 (r"in great fear lest she should meet", "in great fear that she would meet", "lest she should", "that she would", 1),
 (r"—Nay, I won’t!", "—No, I won’t!", "nay", "no", 1),
 (r"thank ye;", "thank you;", "ye", "you", 1),
 (r"; whereupon the puppy", "; and then the puppy", "whereupon", "and then", 1),
 (r"“Pray don’t", "“Please don’t", "pray", "please", 1),
 (r"\bto-day\b", "today", "to-day", "today", 3),
 (r"\bto-night\b", "tonight", "to-night", "tonight", 1),
 (r"\bGood-bye\b", "Goodbye", "good-bye", "goodbye", 1),
 (r"\bcurtseying\b", "curtsying", "curtseying", "curtsying", 1),
 (r"\bcurtsey\b", "curtsy", "curtsey", "curtsy", 1),
 (r"one a-piece", "one each", "a-piece", "each", 1),
 (r"doesn’t signify", "doesn’t matter", "signify", "matter", 1),
 (r"\bdraggled\b", "bedraggled", "draggled", "bedraggled", 1),
 (r"I’m a deal too flustered", "I’m much too flustered", "a deal too", "much too", 1),
 (r"go round a deal faster", "go round a great deal faster", "a deal", "a great deal", 1),
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
json.dump(out, open("modern.json", "w"), ensure_ascii=False)
print("total replacements:", sum(c["n_changes"] for c in out))
