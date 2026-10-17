# The Secret Garden — shared notes: Yorkshire guide, dialect glossary, old words kept, old expressions.
WB = {}

GUIDE = """<div class='page'><h2>Yorkshire Talk: A Quick Guide</h2>
<div>Martha, Dickon, Ben Weatherstaff and Mrs. Sowerby speak the <b>Yorkshire dialect</b> of northern England, and later Mary and Colin try it too.
Burnett wrote their words the way they sound, so we kept every word exactly as she wrote it. The first time a Yorkshire word appears, it has a
<span class='dia'>green line<sup>Y</sup></span>, and the workbook explains it. Here are the patterns you will meet most often.</div>
<h3>1. DROPPED LETTERS</h3>
<table class='ch guide'>
<tr><td class='d'>th’ · o’ · an’ · wi’ · i’</td><td>the · of · and · with · in</td></tr>
<tr><td class='d'>goin’ · nothin’ · mornin’</td><td>going · nothing · morning (the final <i>g</i> of <i>-ing</i> is dropped)</td></tr>
<tr><td class='d'>’em · ’un · ’taters</td><td>them · one · potatoes</td></tr>
<tr><td class='d'>mysel’ · thysel’ · hissel’</td><td>myself · yourself · himself</td></tr>
</table>
<h3>2. THA’ AND THEE = YOU</h3>
<table class='ch guide'>
<tr><td class='d'>tha’ · thee</td><td>you (old <i>thou</i>, used with family, friends and children)</td></tr>
<tr><td class='d'>thy</td><td>your</td></tr>
<tr><td class='d'>tha’rt · art tha’?</td><td>you are · are you?</td></tr>
<tr><td class='d'>tha’ll · tha’lt · tha’d · tha’st</td><td>you’ll · you will · you’d · you have</td></tr>
</table>
<h3>3. OTHER WORDS</h3>
<table class='ch guide'>
<tr><td class='d'>aye · nay · eh!</td><td>yes · no · oh! / well!</td></tr>
<tr><td class='d'>mun · munnot</td><td>must · must not</td></tr>
<tr><td class='d'>canna’ · couldna’</td><td>can’t · couldn’t</td></tr>
<tr><td class='d'>nowt · summat</td><td>nothing · something</td></tr>
<tr><td class='d'>lad · lass · wench</td><td>boy · girl · girl</td></tr>
<tr><td class='d'>fair · rare</td><td>really, completely · very</td></tr>
<tr><td class='d'>knowed · growed · seed</td><td>knew · grew · saw (regular <i>-ed</i> on irregular verbs)</td></tr>
</table>
<div class='reading-note'>Tip: read Yorkshire speech aloud. It is much easier to understand when you hear it.</div></div>"""

DIALECT = {
 # key: (standard English, Korean, note, anchor phrase or None) — marked the first time each appears in the book
 "marred": ("spoiled and pettish", "버릇없고 심통 난", "Burnett explains this Yorkshire word herself in the text: \"marred-looking\" = looks spoiled and sulky."),
 "tha’s": ("you have / you are", "너는 ~했다 / 너는 ~이다", "\"Tha’s browt th’ young ’un\" = \"You’ve brought the young one.\""),
 "browt": ("brought", "데려왔다, 가져왔다", "Yorkshire spelling of how \"brought\" sounds."),
 "’un": ("one", "~한 아이(것)", "\"th’ young ’un\" = the young one, the child."),
 "enow": ("enough", "충분히", "\"Well enow\" = well enough."),
 "art": ("are (with tha’)", "~이니?", "\"Art tha’ th’ little wench from India?\" = \"Are you the little girl from India?\"", "Art tha’"),
 "wench": ("girl, young woman", "아가씨, 여자아이", "Friendly in old Yorkshire talk. In modern standard English \"wench\" sounds rude or old-fashioned, so don't use it."),
 "fair": ("really, completely", "정말, 아주", "\"It’s fair lovely\" = it’s really lovely.", "fair lovely"),
 "knowed": ("known / knew", "알았다", "Yorkshire speakers add -ed to irregular verbs: knowed, growed, throwed, ketched."),
 "t’other": ("the other", "다른 쪽", "\"on t’other side\" = on the other side."),
 "mester": ("Mr. / master", "~씨, 주인 나리", "\"Mester Craven\" = Mr. Craven."),
 "hissel’": ("himself", "그 자신", "Also mysel’ (myself), hersel’ (herself), himsel’ (himself)."),
 "yeller": ("yellow", "노란", "Martha says Mary is \"so yeller\"—her skin was yellow from illness in India."),
 "wutherin’": ("(wind) roaring and blowing wildly", "(바람이) 휘몰아치는", "A Yorkshire word for a loud, wild wind—the same word as in Emily Brontë's novel Wuthering Heights."),
 "moithered": ("confused, worn out", "정신없는, 지친", "\"She gets fair moithered\" = she gets really tired and confused."),
 "soart": ("sort", "종류", "\"Nowt o’ th’ soart!\" = \"Nothing of the sort!\" (No, not at all!)"),
 "nowt": ("nothing", "아무것도 (없다)", "\"Nowt o’ th’ soart\" = nothing of the sort."),
 "daffydowndillys": ("daffodils", "수선화", "A children's and country name for daffodils."),
 "nay": ("no", "아니", "Still heard in Yorkshire today."),
 "lass": ("girl", "소녀, 아가씨", "Still common in northern England and Scotland."),
 "’taters": ("potatoes", "감자", "Short for potatoes. British people still say \"taters\" casually."),
 "bachelder": ("bachelor", "독신 남자", "\"I’m bachelder\" = I’m not married."),
 "rare": ("very, really", "아주, 굉장히", "\"Birds is rare choosers\" = birds are very choosy.", "rare choosers"),
 "ketched": ("caught", "(감기에) 걸렸다, 잡았다", "\"I never ketched cold\" = I never caught a cold."),
 "growed": ("grown / grew", "자랐다", "Like knowed: -ed added to an irregular verb."),
 "wick": ("alive, lively", "살아 있는", "Dickon says a rose bush is \"as wick as you or me\"—it is still alive."),
 "throwed": ("thrown / threw", "던졌다", "\"He’d have throwed himself into one of his tantrums\" = he would have thrown a tantrum."),
 "ha’": ("have", "~했을", "\"Who would ha’ thought it!\" = who would have thought it!"),
 "clemmin’": ("starving, very hungry", "굶주린", "\"half dead wi’ cold an’ clemmin’\" = half dead from cold and hunger."),
 "besom": ("a cheeky, troublesome girl", "말괄량이", "Literally a broom made of twigs. Ben calls Mary a \"young besom\" half as an insult, half with affection."),
 "allus": ("always", "늘, 항상", "\"allus askin’ questions\" = always asking questions."),
 "thowt": ("thought", "생각했다", "\"I never thowt much o’ thee\" = I never thought much of you."),
 "’ere": ("here", "여기(의)", "\"this ’ere\" = this one here."),
 "for’ard": ("forward", "앞으로", "\"backward an’ for’ard\" = back and forth."),
 "kep’": ("kept", "계속 ~하게 되다", "\"he’ll be kep’ so busy\" = he’ll be kept so busy."),
 "agen’": ("against", "~에 반대하는", "\"agen’ prayer-meetin’s\" = against prayer meetings."),
 "theirselves": ("themselves", "그들 자신", "Common in country speech."),
 "feared": ("afraid", "두려운", "\"I’m feared\" = I’m afraid (I think).", "I’m feared"),
 "graidely": ("fine, good, proper", "멋진, 훌륭한", "A warm Yorkshire word of praise: \"a graidely one\" = a fine one."),
 "mun": ("must", "~해야 한다", "\"Tha’ mun\" = you must."),
 "munnot": ("must not", "~하면 안 된다", "\"Tha’ munnot waste no time\" = you mustn't waste any time."),
 "nesh": ("weak, easily cold", "허약한, 추위를 타는", "Still used in northern England for someone who feels the cold easily."),
 "canna’": ("can't", "~할 수 없다", "Also couldna’ = couldn't."),
}

OLD = {
 "ayah": ("명사", "(영국 식민지 시대 인도의) 유모, 하녀", "A Hindi word for a nanny who looked after the children of British families in India."),
 "mem sahib": ("명사", "(식민지 인도에서) 마님", "What Indian servants called a European married woman. It shows the colonial world Mary grew up in."),
 "rajah": ("명사", "(인도의) 왕, 군주", "An Indian king or prince. Mary says Colin acts \"like a young Rajah\" because he gives orders to everyone."),
 "victuals": ("명사", "(옛) 음식", "Pronounced \"vittles\". Today: food."),
 "abide": ("동사", "(옛) 참다, 견디다", "\"I can’t abide\" = I can’t stand / I hate. Still heard, but old-fashioned."),
}
IDIOMS = {
 "lo and behold": ("이게 웬일이야, 놀랍게도", "and surprisingly / and guess what", "Still used today, often jokingly: \"I looked in my bag, and lo and behold, there were my keys!\""),
}
OLD_MARKS = {1: ["Ayah", "Mem Sahib"], 4: ["abide", "victuals"], 14: ["Rajah"]}
IDIOM_MARKS = {8: ["lo and behold"]}
