import json, re
chs = json.load(open("chapters.json"))
R = []  # (pattern, replacement, old, new)
def r(p, rep, o=None, n=None): R.append((p, rep, o or p.replace("\\b", ""), n or rep))
# special phrases first
r(r"Go thou down", "You go down", "Go thou", "You go")
r(r"do thou or", "you or", "do thou", "you")
r(r"whither went they", "where did they go", "whither went they", "where did they go")
r(r"\bforsooth\b", "indeed")
r(r"and wilt not face", "and will not face", "wilt", "will")
r(r"lest a swinging bough should sweep him", "so that a swinging bough would not sweep him", "lest ... should", "so that ... would not")
r(r"bade me come again", "told me to come again", "bade", "told ... to")
r(r"He bade me tell you", "He told me to tell you", "bade", "told ... to")
r(r"\bget hence\b", "get away", "hence", "away"); r(r"\bgo hence\b", "go away", "hence", "away"); r(r"\bGet hence\b", "Get away", "hence", "away")
r(r"“Haste! O haste!", "“Hurry! O hurry!", "haste", "hurry"); r(r"I haste!", "I hurry!", "haste", "hurry")
# questions: verb + thou
for a, b in [("Art", "Are"), ("Hast", "Have"), ("Dost", "Do"), ("Didst", "Did"), ("Wilt", "Will"), ("Canst", "Can")]:
    r(rf"\b{a} thou\b", f"{b} you", f"{a.lower()} thou", f"{b.lower()} you")
    r(rf"\b{a.lower()} thou\b", f"{b.lower()} you", f"{a.lower()} thou", f"{b.lower()} you")
# thou + verb
VERBS = [("art", "are"), ("hast", "have"), ("wilt", "will"), ("wast", "were"), ("mayest", "may"), ("shouldst", "should"),
         ("wouldst", "would"), ("canst", "can"), ("knowest", "know"), ("goest", "go"), ("camest", "came"), ("dost", "do"),
         ("didst", "did"), ("owest", "owe"), ("shalt", "will"), ("smellest", "smell")]
for a, b in VERBS:
    r(rf"\bThou {a}\b", f"You {b}", f"thou {a}", f"you {b}")
    r(rf"\bthou {a}\b", f"you {b}", f"thou {a}", f"you {b}")
r(r"\bThou\b", "You", "thou", "you"); r(r"\bthou\b", "you", "thou", "you")
r(r"\bThee\b", "You", "thee", "you"); r(r"\bthee\b", "you", "thee", "you")
r(r"\bThy\b", "Your", "thy", "your"); r(r"\bthy\b", "your", "thy", "your")
r(r"\bthine\b", "yours", "thine", "yours")
r(r"\bYe\b", "You", "ye", "you"); r(r"\bye\b", "you", "ye", "you")
r(r"“Ay,", "“Yes,", "ay", "yes"); r(r"“Ay!", "“Yes!", "ay", "yes"); r(r"“Nay,", "“No,", "nay", "no")
r(r"\bPresently\b", "Soon", "presently", "soon"); r(r"\bpresently\b", "soon", "presently", "soon")
r(r"\bshan’t\b", "won’t", "shan’t", "won’t")
r(r"\bTo-morrow\b", "Tomorrow", "to-morrow", "tomorrow"); r(r"\bto-morrow\b", "tomorrow", "to-morrow", "tomorrow")
r(r"\bTo-night\b", "Tonight", "to-night", "tonight"); r(r"\bto-night\b", "tonight", "to-night", "tonight")
r(r"\bTo-day\b", "Today", "to-day", "today"); r(r"\bto-day\b", "today", "to-day", "today")
r(r"\bGood-night\b", "Goodnight", "good-night", "goodnight"); r(r"\bgood-night\b", "goodnight", "good-night", "goodnight")
r(r"\bGood-bye\b", "Goodbye", "good-bye", "goodbye"); r(r"\bgood-bye\b", "goodbye", "good-bye", "goodbye")
out = []; total = 0
for c in chs:
    changes = []; newp = []
    for p in c["paras"]:
        t = p["t"]
        if not p["poem"]:
            keep = re.findall(r"We be (?:of )?one blood, (?:ye|thou) and I", t)
            for k_i, k in enumerate(keep): t = t.replace(k, f"KEEP{k_i}KEEP", 1)
            for pat, rep, o, n in R:
                k = len(re.findall(pat, t))
                if k: t = re.sub(pat, rep, t); changes += [(o, n)] * k
        if not p["poem"]:
            for k_i, k in enumerate(keep): t = t.replace(f"KEEP{k_i}KEEP", k)
        newp.append({"t": t, "poem": p["poem"]})
    seen = []; [seen.append(x) for x in changes if x not in seen]
    total += len(changes)
    out.append({"title": c["title"], "paras": newp, "changes": seen, "n_changes": len(changes)})
json.dump(out, open("modern.json", "w"), ensure_ascii=False)
print("total replacements:", total)
t = "\n".join(p["t"] for c in out for p in c["paras"] if not p["poem"])
left = re.findall(r"\b(thou|thee|thy|thine|ye|art|hast|wilt|canst|dost|didst|wast|hath|doth|haste|hence|bade|lest|whither|betwixt|\w+eth)\b", t, re.I)
import collections; print("leftovers:", collections.Counter(w.lower() for w in left).most_common())
