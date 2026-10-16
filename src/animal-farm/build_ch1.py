import random, html, subprocess, sys

OUT_HTML = sys.argv[1]
OUT_PDF = sys.argv[2]

SUMMARY = (
    "One night, after the drunken farmer Mr. Jones goes to bed, the animals of Manor Farm gather in the big barn "
    "to hear Old Major, a respected old boar. He tells them their lives are short, hard and miserable because humans "
    "take everything they produce, and he urges them to prepare for a Rebellion that will one day set them free. "
    "He teaches them a song, 'Beasts of England', and the excited singing wakes Mr. Jones, who fires his gun and breaks up the meeting."
)

CHARACTERS = [
    ("Mr. Jones", "the owner of Manor Farm; careless and often drunk"),
    ("Old Major", "a wise, respected old boar who shares his dream of freedom"),
    ("Boxer", "a huge, strong cart-horse; not clever but hard-working and trusted"),
    ("Clover", "a gentle, motherly mare who protects the weak"),
    ("Benjamin", "an old, grumpy donkey who rarely speaks or laughs"),
    ("Mollie", "a pretty, vain white mare who loves sugar and ribbons"),
    ("Moses", "Mr. Jones's tame raven"),
]

# word, pos, stress, ipa, korean, collocations, in the story, example1, example2
VOCAB = [
    ("lurch", "v.", "LURCH", "/lɜːrtʃ/", "비틀거리며 가다, 휘청하다",
     "lurch forward · lurch across the room · lurch to a stop",
     "Mr. Jones is so drunk that he cannot walk straight across the yard.",
     "The bus lurched forward, and everyone grabbed the handles.",
     "After the long flight, I lurched off the plane half asleep."),
    ("stir", "n. / v.", "STIR", "/stɜːr/", "움직임, 동요 / 움직이다, 불러일으키다",
     "cause a stir · stir up trouble · stir emotions",
     "As soon as the farmhouse light goes out, the animals begin to move about.",
     "The news of the new teacher caused quite a stir at school.",
     "Her speech stirred strong feelings in the audience."),
    ("regard", "v.", "re-GARD", "/rɪˈɡɑːrd/", "여기다, 존경하다",
     "be highly regarded · regard A as B · with regard to",
     "Old Major is so respected that everyone gives up sleep to hear him.",
     "She is highly regarded as one of the best doctors in the city.",
     "Many people regard this novel as a classic."),
    ("ensconced", "adj.", "en-SCONCED", "/ɪnˈskɑːnst/", "(편안하게) 자리 잡은",
     "be ensconced in a chair · comfortably ensconced",
     "Major is already settled on his straw bed before the others arrive.",
     "By the time we arrived, Grandpa was ensconced in his favorite armchair.",
     "The cat was comfortably ensconced on the warm laptop."),
    ("stout", "adj.", "STOUT", "/staʊt/", "통통한, 튼튼한",
     "a stout man · stout boots · grow stout",
     "Major has become rather heavy in his old age.",
     "A stout old man opened the door and smiled at us.",
     "You will need stout shoes for the mountain trail."),
    ("majestic", "adj.", "ma-JES-tic", "/məˈdʒestɪk/", "위엄 있는, 장엄한",
     "a majestic view · majestic mountains · look majestic",
     "Even at twelve, Major still looks grand and dignified.",
     "We stood in silence before the majestic mountains.",
     "The lion walked slowly, looking calm and majestic."),
    ("benevolent", "adj.", "be-NEV-o-lent", "/bəˈnevələnt/", "자비로운, 인자한",
     "a benevolent smile · a benevolent ruler · benevolent fund",
     "Major has a wise and kind face, even with his long tusks.",
     "The old teacher gave the nervous student a benevolent smile.",
     "People hoped the new king would be a benevolent ruler."),
    ("conceal", "v.", "con-CEAL", "/kənˈsiːl/", "숨기다, 감추다",
     "conceal the truth · conceal one's feelings · be concealed in",
     "The horses step carefully in case a small animal is hidden in the straw.",
     "He tried to conceal his disappointment, but his face showed it.",
     "The key was concealed under a flowerpot."),
    ("cynical", "adj.", "CYN-i-cal", "/ˈsɪnɪkəl/", "냉소적인",
     "a cynical remark · cynical about politics · grow cynical",
     "Benjamin seldom talks, and when he does, his comments are bitter.",
     "After years of broken promises, she became cynical about politicians.",
     "\"Nothing ever changes,\" he said in a cynical voice."),
    ("devoted", "adj.", "de-VO-ted", "/dɪˈvoʊtɪd/", "헌신적인, 애정이 깊은",
     "devoted to (someone/something) · a devoted fan · devoted parents",
     "Benjamin never says so, but he cares deeply about Boxer.",
     "She is devoted to her children and her work.",
     "He is a devoted fan who has never missed a game."),
    ("contentedly", "adv.", "con-TENT-ed-ly", "/kənˈtentɪdli/", "만족스럽게",
     "smile contentedly · sigh contentedly · purr contentedly",
     "The cat purrs happily between the horses without listening at all.",
     "The baby fell asleep contentedly after her bottle.",
     "He leaned back and sighed contentedly after dinner."),
    ("laborious", "adj.", "la-BOR-i-ous", "/ləˈbɔːriəs/", "고된, 힘든",
     "a laborious task · a laborious process · laborious work",
     "Major says the animals' lives are miserable, hard-working and short.",
     "Copying the whole book by hand was a laborious task.",
     "Learning a new language can be a slow and laborious process."),
    ("slaughter", "v. / n.", "SLAUGH-ter", "/ˈslɔːtər/", "도살하다 / 도살, 대학살",
     "be slaughtered · slaughter animals · the slaughter of",
     "Major warns that animals are killed as soon as they are no longer useful.",
     "The farmer refused to slaughter his old horse.",
     "The war ended with the slaughter of thousands of soldiers."),
    ("abundance", "n.", "a-BUN-dance", "/əˈbʌndəns/", "풍부함, 넉넉함",
     "in abundance · an abundance of · food in abundance",
     "Major claims England's soil could feed far more animals than it does now.",
     "Fruit grows in abundance on this island.",
     "The city offers an abundance of cafes and parks."),
    ("abolish", "v.", "a-BOL-ish", "/əˈbɑːlɪʃ/", "폐지하다, 없애다",
     "abolish slavery · abolish a law · abolish the system",
     "If humans are removed, Major says, hunger and overwork will end forever.",
     "Many countries have abolished the death penalty.",
     "The school abolished its strict uniform rules last year."),
    ("tyranny", "n.", "TYR-an-ny", "/ˈtɪrəni/", "폭정, 압제",
     "fight against tyranny · the tyranny of · live under tyranny",
     "Major blames all the animals' suffering on the cruel rule of humans.",
     "The people finally rose up against years of tyranny.",
     "Some people feel trapped by the tyranny of the clock."),
    ("rebellion", "n.", "re-BEL-lion", "/rɪˈbeljən/", "반란, 저항",
     "lead a rebellion · crush a rebellion · an act of rebellion",
     "Major's main message is that the animals must prepare for an uprising.",
     "The army quickly crushed the rebellion.",
     "Dyeing her hair green was her small act of rebellion."),
    ("falter", "v.", "FAL-ter", "/ˈfɔːltər/", "흔들리다, 머뭇거리다",
     "never falter · voice falters · courage falters",
     "Major tells the animals their determination must stay strong.",
     "Her voice faltered as she began to speak about her father.",
     "Even when the plan failed, his courage never faltered."),
    ("overwhelming", "adj.", "o-ver-WHELM-ing", "/ˌoʊvərˈwelmɪŋ/", "압도적인",
     "an overwhelming majority · overwhelming evidence · overwhelming feeling",
     "Almost everyone votes that the rats should be treated as comrades.",
     "The plan was approved by an overwhelming majority.",
     "She felt an overwhelming sense of relief."),
    ("vice", "n.", "VICE", "/vaɪs/", "악덕, 나쁜 습관",
     "virtue and vice · a minor vice · give up one's vices",
     "Major warns the animals not to copy humans' bad habits once they win.",
     "Chocolate is my only vice.",
     "The story shows how greed can become a dangerous vice."),
]

# Quiz: sentence (with ___), answer, distractors. All sentences retell Chapter 1 in new wording.
QUIZ = [
    ("Mr. Jones was so drunk that he ___ across the yard with his lantern.", "lurched", ["marched", "galloped", "tiptoed"]),
    ("When the bedroom light went out, a ___ spread through the farm buildings.", "stir", ["silence", "vice", "slaughter"]),
    ("Old Major was so highly ___ that the animals gladly lost an hour of sleep.", "regarded", ["ignored", "concealed", "abolished"]),
    ("Major was already ___ on his bed of straw under the lantern.", "ensconced", ["abandoned", "concealed", "lurched"]),
    ("Old Major had grown rather ___, but he still looked grand.", "stout", ["slender", "cynical", "devoted"]),
    ("At twelve years old, Major was still a ___-looking pig.", "majestic", ["miserable", "laborious", "cynical"]),
    ("Even with his uncut tusks, Major had a wise and ___ appearance.", "benevolent", ["hostile", "laborious", "overwhelming"]),
    ("Boxer and Clover walked slowly in case a small animal was ___ in the straw.", "concealed", ["displayed", "abolished", "slaughtered"]),
    ("Benjamin rarely spoke, and his remarks were usually ___.", "cynical", ["cheerful", "benevolent", "majestic"]),
    ("Without openly admitting it, Benjamin was ___ to Boxer.", "devoted", ["hostile", "indifferent", "stout"]),
    ("The cat purred ___ throughout the speech without listening to a word.", "contentedly", ["anxiously", "laboriously", "angrily"]),
    ("Major said that the animals' lives were miserable, ___, and short.", "laborious", ["leisurely", "majestic", "abundant"]),
    ("According to Major, animals are ___ as soon as they are no longer useful.", "slaughtered", ["rewarded", "regarded", "ensconced"]),
    ("Major claimed English soil could produce food in ___ for many more animals.", "abundance", ["shortage", "tyranny", "secret"]),
    ("If Man were removed, hunger and overwork would be ___ forever.", "abolished", ["increased", "concealed", "regarded"]),
    ("Major blamed every evil in their lives on the ___ of human beings.", "tyranny", ["kindness", "abundance", "rebellion"]),
    ("Major did not know when the ___ would come, but he was sure it would.", "Rebellion", ["harvest", "vote", "vice"]),
    ("He told the animals that their resolution must never ___.", "falter", ["succeed", "conceal", "abolish"]),
    ("The rats were declared comrades by an ___ majority.", "overwhelming", ["narrow", "cynical", "laborious"]),
    ("Major warned them not to adopt Man's ___, such as drinking or trading.", "vices", ["virtues", "rebellions", "abundances"]),
]

DISCUSSION = [
    "Old Major changed the animals' thinking in a single night. Have you ever heard a speech or talk that changed your mind? What made it powerful?",
    "Which animal are you most like right now: hard-working Boxer, caring Clover, doubtful Benjamin, or Mollie who loves pretty things? Why?",
    "Major says humans \"take without producing.\" Have you ever seen a situation at work, school, or home where one person does the work and another takes the credit?",
    "Major tells the animals never to copy human habits, even after they win. Why do you think people who fight against something sometimes end up becoming like it?",
    "The animals vote on whether the rats are \"comrades.\" In your own groups (family, friends, this book club), how do you decide who belongs?",
]

random.seed(7)
quiz_items, key = [], []
for i, (sent, ans, dis) in enumerate(QUIZ, 1):
    opts = [ans] + dis
    random.shuffle(opts)
    letter = "abcd"[opts.index(ans)]
    key.append(f"{i}. ({letter}) {ans}")
    quiz_items.append((i, sent, opts))

e = html.escape

css = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { font-family: 'Noto Sans CJK KR', 'Noto Sans', sans-serif; color: #2b2b2b; margin: 0; font-size: 10pt; line-height: 1.45; }
.page { padding: 18mm 18mm 16mm; page-break-after: always; }
.page:last-child { page-break-after: auto; }
.cover { height: 296mm; display: block; padding-top: 70mm; text-align: center; background: #f4efe4; }
.cover .series { letter-spacing: 3px; font-size: 10pt; color: #7a6a4f; }
.cover h1 { font-family: 'Noto Serif CJK KR', serif; font-size: 40pt; margin: 18px 0 4px; color: #3d3220; }
.cover .author { font-size: 13pt; color: #5a4c34; }
.cover .ch { margin-top: 40px; font-size: 16pt; color: #3d3220; }
.cover .note { margin: 60px auto 0; width: 120mm; font-size: 9pt; color: #6b5d45; }
h2 { font-family: 'Noto Serif CJK KR', serif; color: #3d3220; border-bottom: 2px solid #c9b78f; padding-bottom: 4px; margin: 0 0 10px; font-size: 17pt; }
h3 { color: #7a6a4f; font-size: 11pt; margin: 14px 0 6px; letter-spacing: 1px; }
.summary { background: #f8f5ee; border-left: 4px solid #c9b78f; padding: 10px 14px; }
table.chars { width: 100%; border-collapse: collapse; margin-top: 6px; }
table.chars td { padding: 5px 6px; border-bottom: 1px solid #e6dfcf; vertical-align: top; }
table.chars td.n { font-weight: bold; width: 28mm; color: #3d3220; }
.card { border: 1px solid #e0d6bf; border-radius: 6px; padding: 7px 11px; margin-bottom: 7px; page-break-inside: avoid; }
.card .top { display: block; }
.card .num { color: #b39c6b; font-weight: bold; margin-right: 6px; }
.card .w { font-size: 13pt; font-weight: bold; color: #3d3220; }
.card .pos { font-style: italic; color: #7a6a4f; margin-left: 4px; }
.card .pron { color: #555; margin-left: 8px; font-size: 9.5pt; }
.card .ko { color: #8a5a2b; margin-left: 8px; }
.card .col { font-size: 9.5pt; color: #4f6b5a; margin-top: 2px; }
.card .ctx { font-size: 9.5pt; color: #666; margin-top: 2px; }
.card ul { margin: 3px 0 0 16px; padding: 0; font-size: 10pt; }
.lbl { font-size: 8pt; font-weight: bold; letter-spacing: 1px; color: #a08a5a; margin-right: 4px; }
.q { margin-bottom: 9px; page-break-inside: avoid; }
.q .opts { margin-left: 18px; color: #444; }
.q .opts span { display: inline-block; width: 38mm; }
.disc li { margin-bottom: 12px; }
.lines { border-bottom: 1px solid #d9d0bb; height: 18px; margin: 4px 0; }
.key { columns: 2; font-size: 10pt; }
.foot { font-size: 8.5pt; color: #999; margin-top: 10px; }
"""

parts = [f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>"]
parts.append(f"""
<div class='page cover'>
  <div class='series'>ENGLISH BOOK CLUB WORKBOOK</div>
  <h1>Animal Farm</h1>
  <div class='author'>George Orwell</div>
  <div class='ch'>Chapter 1 · Old Major's Dream</div>
  <div class='note'>Vocabulary &amp; Usage Workbook — read the chapter in your own copy of the book, then use this workbook to study 20 key words, practise them in context, and prepare for discussion.</div>
</div>""")

parts.append("<div class='page'><h2>Chapter 1 at a Glance</h2>")
parts.append(f"<h3>SUMMARY</h3><div class='summary'>{e(SUMMARY)}</div>")
parts.append("<h3>WHO'S WHO</h3><table class='chars'>")
for n, d in CHARACTERS:
    parts.append(f"<tr><td class='n'>{e(n)}</td><td>{e(d)}</td></tr>")
parts.append("</table>")
parts.append("<h3>HOW TO USE THIS WORKBOOK</h3><div>1. Read Chapter 1 and underline the 20 words when you meet them.<br>"
             "2. Study each word card: pronunciation, meaning, common word partners (collocations), and examples.<br>"
             "3. Complete the 20 fill-in-the-blank questions without looking back.<br>"
             "4. Choose two discussion questions to talk about at the meeting.</div>")
parts.append("</div>")

# vocab pages: 7 cards per page
for start in range(0, len(VOCAB), 7):
    chunk = VOCAB[start:start+7]
    title = "Vocabulary" if start == 0 else "Vocabulary (continued)"
    parts.append(f"<div class='page'><h2>{title}</h2>")
    for i, (w, pos, st, ipa, ko, col, ctx, ex1, ex2) in enumerate(chunk, start+1):
        parts.append(f"""<div class='card'>
<div class='top'><span class='num'>{i:02d}</span><span class='w'>{e(w)}</span><span class='pos'>{e(pos)}</span>
<span class='pron'>{e(st)} · {e(ipa)}</span><span class='ko'>({e(ko)})</span></div>
<div class='col'><span class='lbl'>COLLOCATIONS</span>{e(col)}</div>
<div class='ctx'><span class='lbl'>IN THE STORY</span>{e(ctx)}</div>
<ul><li>{e(ex1)}</li><li>{e(ex2)}</li></ul></div>""")
    parts.append("</div>")

# quiz: 10 per page
for start in range(0, len(quiz_items), 10):
    title = "Practice: Fill in the Blank" if start == 0 else "Practice (continued)"
    parts.append(f"<div class='page'><h2>{title}</h2>")
    if start == 0:
        parts.append("<p>Choose the best word to complete each sentence about Chapter 1. Watch the form of the word (-ed, -s, -ly).</p>")
    for i, sent, opts in quiz_items[start:start+10]:
        os_ = "".join(f"<span>({l}) {e(o)}</span>" for l, o in zip("abcd", opts))
        parts.append(f"<div class='q'><b>{i}.</b> {e(sent).replace("___","__________")}<div class='opts'>{os_}</div></div>")
    parts.append("</div>")

parts.append("<div class='page'><h2>Let's Talk</h2><p>Pick two questions. Try to use at least one word from this chapter in your answer.</p><ol class='disc'>")
for d in DISCUSSION:
    parts.append(f"<li>{e(d)}<div class='lines'></div><div class='lines'></div></li>")
parts.append("</ol>")
parts.append("<h3>ANSWER KEY</h3><div class='key'>" + "<br>".join(e(k) for k in key) + "</div>")
parts.append("<div class='foot'>Summary, examples and practice sentences are original to this workbook.</div></div>")
parts.append("</body></html>")

open(OUT_HTML, "w", encoding="utf-8").write("".join(parts))
subprocess.run(["wkhtmltopdf", "--quiet", "--enable-local-file-access", "--zoom", "1.3", "-s", "A4", "-B", "0", "-T", "0", "-L", "0", "-R", "0",
                OUT_HTML, OUT_PDF], check=False)
print("done")
