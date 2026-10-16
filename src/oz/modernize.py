import json, re
chs = json.load(open("chapters.json"))
# (pattern, replacement, label old, label new, expected count)  — exact, word-level only
RULES = [
 (r"She bade her friends good-bye", "She said goodbye to her friends", "bade ... good-bye", "said goodbye to", 1),
 (r"when she bade me good-bye", "when she said goodbye to me", "bade ... good-bye", "said goodbye to", 1),
 (r"bade him enter", "told him to enter", "bade", "told ... to", 1),
 (r"bade him good-bye", "said goodbye to him", "bade ... good-bye", "said goodbye to", 1),
 (r"the Witch bade her clean", "the Witch told her to clean", "bade", "told ... to", 1),
 (r"bade them good-bye", "said goodbye to them", "bade ... good-bye", "said goodbye to", 1),
 (r"As Dorothy bade the good-natured Guardian a last farewell", "As Dorothy said a last farewell to the good-natured Guardian", "bade ... farewell", "said farewell to", 1),
 (r"He bade his comrades good-bye", "He said goodbye to his comrades", "bade ... good-bye", "said goodbye to", 1),
 (r"Good-bye", "Goodbye", "good-bye", "goodbye", None),
 (r"good-bye", "goodbye", "good-bye", "goodbye", None),
 (r"\bPresently\b", "Soon", "presently", "soon", None),
 (r"\bpresently\b", "soon", "presently", "soon", None),
 (r"\bvexed\b", "annoyed", "vexed", "annoyed", 3),
 (r"I pray you", "I beg you", "I pray you", "I beg you", 2),
 (r"lest he should run after her", "so that he would not run after her", "lest he should", "so that he would not", 1),
 (r"shan’t", "won’t", "shan’t", "won’t", 1),
 (r"Yonder, among", "Over there, among", "yonder", "over there", 1),
 (r"Thereupon the", "Then the", "thereupon", "then", 1),
 (r", whereupon the", ", and then the", "whereupon", "and then", 1),
 (r"\bamongst\b", "among", "amongst", "among", 1),
 (r"\bdwelt\b", "lived", "dwelt", "lived", 2),
 (r"\bstraightway\b", "immediately", "straightway", "immediately", 1),
 (r"\bStraightway\b", "Immediately", "straightway", "immediately", 1),
 (r"\bqueerest\b", "strangest", "queerest", "strangest", 1),
 (r"\bqueerly\b", "strangely", "queerly", "strangely", 1),
 (r"\bgarret\b", "attic", "garret", "attic", 1),
 (r"\bForthwith\b", "Immediately", "forthwith", "immediately", 1),
 (r"and behold!", "and look!", "behold", "look", 1),
 (r"\bhastened\b", "hurried", "hastened", "hurried", 1),
 (r"\bqueer\b", "strange", "queer", "strange", None),
 (r"\bQueer\b", "Strange", "queer", "strange", None),
 (r"\bfrocks\b", "dresses", "frocks", "dresses", None),
 (r"\bfrock\b", "dress", "frock", "dress", None),
]
out = []; totals = {}
for title, paras in chs:
    changes = []; newp = []
    for p in paras:
        for pat, rep, o, n, _ in RULES:
            k = len(re.findall(pat, p))
            if k:
                p = re.sub(pat, rep, p); totals[pat] = totals.get(pat, 0) + k
                changes += [(o, n)] * k
        newp.append(p)
    # unique change list, keep order
    seen = []; [seen.append(c) for c in changes if c not in seen]
    out.append({"title": title, "paras": newp, "changes": seen, "n_changes": len(changes)})
for pat, rep, o, n, exp in RULES:
    if exp is not None and totals.get(pat, 0) != exp: print("COUNT MISMATCH", pat, totals.get(pat, 0), exp)
json.dump(out, open("modern.json", "w"), ensure_ascii=False)
print("total replacements:", sum(c["n_changes"] for c in out))
