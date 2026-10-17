# The Secret Garden workbook, chapters 22–27. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
22: dict(vocab=[
 ("support", "supported", "v.", "sup-PORT", "/səˈpɔːrt/", "지탱하다, 받치다; 지지하다", "support yourself · support a family", "He supported himself against the wall.", "Her parents supported her decision."),
 ("testily", "testily", "adv.", "TEST-i-ly", "/ˈtestɪli/", "성마르게, 짜증스럽게", "reply testily · say testily", "\"I heard you,\" he replied testily.", "She spoke testily after the long day."),
 ("thinness", "thinness", "n.", "THIN-ness", "/ˈθɪnnəs/", "마름, 가늘음", "the thinness of · alarming thinness", "We worried about the thinness of his arms.", "The thinness of the ice was dangerous."),
 ("exultation", "exultation", "n.", "ex-ul-TA-tion", "/ˌeɡzʌlˈteɪʃən/", "기쁨에 찬 승리감", "with exultation · a cry of exultation", "He raised his arms in exultation.", "There was exultation in her voice."),
 ("tenderness", "tenderness", "n.", "TEN-der-ness", "/ˈtendərnəs/", "다정함, 애정", "with tenderness · a moment of tenderness", "She looked at the baby with tenderness.", "There was tenderness behind his rough words."),
 ("grumpy", "grumpy", "adj.", "GRUM-py", "/ˈɡrʌmpi/", "심통 난, 툴툴거리는", "a grumpy old man · feel grumpy", "I'm always grumpy before coffee.", "The grumpy neighbor shouted at the kids."),
 ("obstinacy", "obstinacy", "n.", "OB-sti-na-cy", "/ˈɑːbstɪnəsi/", "고집, 완고함", "sheer obstinacy · out of obstinacy", "He refused out of sheer obstinacy.", "Her obstinacy helped her succeed."),
 ("persevere", "persevered", "v.", "per-se-VERE", "/ˌpɜːrsəˈvɪr/", "끈기 있게 계속하다", "persevere with · persevere in", "She persevered and finally passed the test.", "If you persevere, you'll improve."),
 ("deepen", "deepened", "v.", "DEEP-en", "/ˈdiːpən/", "깊게 하다, 깊어지다", "deepen a hole · deepen understanding", "They deepened the well.", "Travel deepened her love of languages."),
 ("hobble", "hobbled", "v.", "HOB-ble", "/ˈhɑːbl/", "절뚝거리며 걷다", "hobble along · hobble over", "He hobbled to the door with his bad knee.", "The old man hobbled across the road."),
], quiz=[
 ("Colin stood against the tree trunk, and it was not too plain that he ___ himself against it.", "supported", ["supposed", "suppressed", "surprised"]),
 ("\"What art sayin'?\" Ben asked Mary rather ___, not wanting to look away from Colin.", "testily", ["tastily", "tenderly", "tightly"]),
 ("Mary felt Colin looked quite beautiful in spite of his ___.", "thinness", ["thickness", "thirstiness", "tininess"]),
 ("\"Tha' die!\" Ben said with dry ___. \"Nowt o' th' sort!\"", "exultation", ["exhaustion", "exaggeration", "expectation"]),
 ("There was a strange mixture of crabbed ___ and shrewd understanding in Ben's manner.", "tenderness", ["tidiness", "toughness", "tiredness"]),
 ("\"But I come,\" Ben said with ___ obstinacy. \"Over th' wall I come.\"", "grumpy", ["grubby", "bumpy", "lumpy"]),
 ("Ben kept coming to tend the roses with grumpy ___, though no one was allowed in.", "obstinacy", ["intimacy", "delicacy", "democracy"]),
 ("Colin ___ with his trowel until he had turned over the soil.", "persevered", ["preserved", "perceived", "persuaded"]),
 ("When Dickon had ___ the hole, Colin went on turning the soft earth.", "deepened", ["depended", "dampened", "deafened"]),
 ("Ben ___ over the grass as fast as he could with the rose in its pot.", "hobbled", ["hobnobbed", "bobbled", "hiccuped"]),
], discussion=[
 "Colin plants a rose himself before the sun goes down. Why is planting something so meaningful for him?",
 "Ben secretly climbed over the wall for years to care for the roses. Why? What does this tell you about him?",
]),
23: dict(vocab=[
 ("peculiarity", "peculiarities", "n.", "pe-cu-li-AR-i-ty", "/pɪˌkjuːliˈærəti/", "특이한 점, 별난 버릇", "a strange peculiarity · peculiarities of", "One of his peculiarities is talking to plants.", "Every language has its peculiarities."),
 ("prejudice", "prejudice", "n.", "PREJ-u-dice", "/ˈpredʒədɪs/", "편견", "without prejudice · racial prejudice", "We should judge people without prejudice.", "Prejudice is often based on fear."),
 ("impartially", "impartially", "adv.", "im-PAR-tial-ly", "/ɪmˈpɑːrʃəli/", "공정하게, 치우침 없이", "judge impartially · act impartially", "A referee must act impartially.", "She listened impartially to both sides."),
 ("crevice", "crevices", "n.", "CREV-ice", "/ˈkrevɪs/", "갈라진 틈", "a crevice in the rock · cracks and crevices", "Small plants grew in the crevices of the wall.", "The lizard hid in a crevice."),
 ("imposing", "imposing", "adj.", "im-POS-ing", "/ɪmˈpoʊzɪŋ/", "인상적인, 위엄 있는", "an imposing building · an imposing figure", "The bank is an imposing stone building.", "He was tall and imposing."),
 ("orator", "orator", "n.", "OR-a-tor", "/ˈɔːrətər/", "연설가, 웅변가", "a great orator · a gifted orator", "Martin Luther King was a great orator.", "The orator spoke for an hour."),
 ("majestic", "majestic", "adj.", "ma-JES-tic", "/məˈdʒestɪk/", "장엄한, 위엄 있는", "a majestic view · majestic mountains", "We saw majestic mountains from the plane.", "The lion looked majestic."),
 ("entranced", "entranced", "adj.", "en-TRANCED", "/ɪnˈtrænst/", "넋을 잃은, 매료된", "listen entranced · be entranced by", "The children watched entranced.", "She was entranced by the music."),
 ("disrespectful", "disrespectful", "adj.", "dis-re-SPECT-ful", "/ˌdɪsrɪˈspektfəl/", "무례한, 실례되는", "disrespectful to · a disrespectful remark", "It's disrespectful to talk during the anthem.", "He was disrespectful to his teacher."),
 ("stimulate", "stimulated", "v.", "STIM-u-late", "/ˈstɪmjəleɪt/", "자극하다, 격려하다", "stimulate interest · stimulate growth", "Good teachers stimulate curiosity.", "The news stimulated him to work harder."),
], quiz=[
 ("One of Colin's chief ___ was that he did not know what a rude little brute he was.", "peculiarities", ["particularities", "popularities", "possibilities"]),
 ("Mary thought the thing out quite without ___: nobody dared to slap Colin.", "prejudice", ["precedence", "privilege", "practice"]),
 ("\"You needn't be cross,\" Mary added ___, \"because so am I strange.\"", "impartially", ["imperially", "impractically", "importantly"]),
 ("Green things pushed through the earth, the grass, the beds and even the ___ of the walls.", "crevices", ["devices", "services", "novices"]),
 ("Colin's talk about Magic, electricity and steam sounded so ___ that Ben became excited.", "imposing", ["imploring", "importing", "opposing"]),
 ("\"When Mary found this garden it looked quite dead,\" the ___ proceeded.", "orator", ["operator", "creator", "senator"]),
 ("Sitting down in their circle for the Magic seemed most ___ and mysterious.", "majestic", ["magnetic", "domestic", "drastic"]),
 ("Mary listened ___ as Colin chanted, \"Magic is in me!\"", "entranced", ["entrenched", "enhanced", "entrusted"]),
 ("\"Weatherstaff,\" said Colin sternly, \"that is ___.\"", "disrespectful", ["distrustful", "disappointed", "disinfected"]),
 ("The thought that most ___ Colin was imagining his father's face when he saw him strong.", "stimulated", ["simulated", "estimated", "stipulated"]),
], discussion=[
 "Colin calls the power that makes things grow \"Magic.\" What do you think Burnett means by Magic? Do you believe in something like it?",
 "Mary says she and Colin and Ben are all \"strange.\" Is it a good or bad thing to be strange?",
]),
24: dict(vocab=[
 ("domain", "domain", "n.", "do-MAIN", "/doʊˈmeɪn/", "영역, 영토", "a private domain · in the public domain", "The kitchen is my mother's domain.", "This book is now in the public domain."),
 ("incident", "incident", "n.", "IN-ci-dent", "/ˈɪnsɪdənt/", "사건, 일", "a strange incident · without incident", "There was a small incident at school.", "The trip passed without incident."),
 ("suspicion", "suspicion", "n.", "sus-PI-cion", "/səˈspɪʃən/", "의심", "under suspicion · arouse suspicion", "His strange behavior aroused suspicion.", "She looked at me with suspicion."),
 ("unconsciously", "unconsciously", "adv.", "un-CON-scious-ly", "/ʌnˈkɑːnʃəsli/", "무의식적으로", "unconsciously copy · act unconsciously", "Children unconsciously copy their parents.", "He unconsciously touched his hair."),
 ("annoyance", "annoyance", "n.", "an-NOY-ance", "/əˈnɔɪəns/", "짜증, 성가심", "to someone's annoyance · show annoyance", "To my annoyance, the bus was late.", "She couldn't hide her annoyance."),
 ("abnormal", "abnormal", "adj.", "ab-NOR-mal", "/æbˈnɔːrml/", "비정상적인, 이례적인", "abnormal behavior · abnormally high", "The test showed nothing abnormal.", "It's abnormal to be this hot in April."),
 ("regretfully", "regretfully", "adv.", "re-GRET-ful-ly", "/rɪˈɡretfəli/", "유감스럽게, 아쉬워하며", "say regretfully · smile regretfully", "\"I have to go,\" she said regretfully.", "He regretfully turned down the offer."),
 ("desperation", "desperation", "n.", "des-per-A-tion", "/ˌdespəˈreɪʃən/", "절박함, 필사적임", "in desperation · a sense of desperation", "In desperation, he called his mother.", "There was desperation in her eyes."),
 ("copious", "copious", "adj.", "CO-pi-ous", "/ˈkoʊpiəs/", "풍부한, 많은", "copious notes · copious amounts", "She took copious notes in class.", "He drank copious amounts of water."),
 ("repress", "repress", "v.", "re-PRESS", "/rɪˈpres/", "(감정·웃음을) 억누르다", "repress a smile · repress feelings", "I tried to repress a laugh.", "Don't repress your feelings."),
], quiz=[
 ("Dickon told his mother everything, including Colin's introduction to the hidden ___.", "domain", ["domino", "dome", "remain"]),
 ("He told her about the ___ of Ben's angry face peering over the wall.", "incident", ["accident", "insistent", "incentive"]),
 ("Protecting themselves from ___ became one of Colin and Mary's favorite games.", "suspicion", ["supervision", "superstition", "suspension"]),
 ("The idea of hiding Colin's health had been ___ suggested by the nurse and Dr. Craven.", "unconsciously", ["unconditionally", "unanimously", "unconvincingly"]),
 ("Dr. Craven asked many questions, to Colin's great ___.", "annoyance", ["announcement", "allowance", "ignorance"]),
 ("Dr. Craven said Colin's improvement seemed almost ___.", "abnormal", ["abominable", "abdominal", "nominal"]),
 ("\"I may be obliged to have a tantrum,\" said Colin ___.", "regretfully", ["respectfully", "resourcefully", "remorselessly"]),
 ("Seeing the delicious breakfast they were supposed to refuse, they looked at each other in ___.", "desperation", ["dedication", "decoration", "deceleration"]),
 ("Colin stuffed himself with buns and drank milk from the pail in ___ draughts.", "copious", ["curious", "copied", "cautious"]),
 ("Mary made a strange sound which she tried so hard to ___ that she almost choked.", "repress", ["reprise", "regress", "repaint"]),
], discussion=[
 "Colin and Mary pretend to be ill so his father can be surprised. Is this kind of secret OK? Why or why not?",
 "Mrs. Sowerby sends milk and buns so the children won't be hungry. How does she help them without ever coming to the house?",
]),
25: dict(vocab=[
 ("watchful", "watchful", "adj.", "WATCH-ful", "/ˈwɑːtʃfəl/", "경계하는, 주의 깊은", "a watchful eye · under the watchful eye of", "The children played under the watchful eye of their mother.", "Stay watchful in crowded places."),
 ("convey", "conveyed", "v.", "con-VEY", "/kənˈveɪ/", "전하다, 전달하다", "convey a message · convey feelings", "Music can convey feelings words can't.", "Please convey my thanks to your family."),
 ("gibberish", "gibberish", "n.", "GIB-ber-ish", "/ˈdʒɪbərɪʃ/", "알아들을 수 없는 말", "talk gibberish · sound like gibberish", "The baby was talking gibberish.", "This contract sounds like gibberish to me."),
 ("disconcerting", "disconcerting", "adj.", "dis-con-CERT-ing", "/ˌdɪskənˈsɜːrtɪŋ/", "당황스러운, 불안하게 하는", "a disconcerting silence · find something disconcerting", "His long stare was disconcerting.", "It's disconcerting to hear your own voice."),
 ("injurious", "injurious", "adj.", "in-JU-ri-ous", "/ɪnˈdʒʊriəs/", "해로운", "injurious to health", "Smoking is injurious to health.", "Too much stress is injurious."),
 ("fluently", "fluently", "adv.", "FLU-ent-ly", "/ˈfluːəntli/", "유창하게", "speak fluently · read fluently", "She speaks English fluently.", "He reads Chinese fluently."),
 ("atrophied", "atrophied", "adj.", "AT-ro-phied", "/ˈætrəfid/", "(근육 등이) 위축된, 약해진", "atrophied muscles · become atrophied", "After months in bed his muscles were atrophied.", "Unused skills can become atrophied."),
 ("restive", "restive", "adj.", "RES-tive", "/ˈrestɪv/", "안달하는, 가만있지 못하는", "grow restive · a restive crowd", "The children grew restive in the car.", "The restive horse kicked the fence."),
 ("inordinately", "inordinately", "adv.", "in-OR-di-nate-ly", "/ɪnˈɔːrdɪnətli/", "지나치게, 엄청나게", "inordinately proud · inordinately long", "He is inordinately proud of his car.", "She giggled inordinately."),
 ("fixedly", "fixedly", "adv.", "FIX-ed-ly", "/ˈfɪksɪdli/", "뚫어지게, 꼼짝 않고", "stare fixedly · look fixedly", "He stared fixedly at the screen.", "She looked fixedly at the door."),
], quiz=[
 ("At first the mother robin was nervous and the robin himself was indignantly ___.", "watchful", ["wasteful", "wishful", "woeful"]),
 ("Dickon seemed to have ___ to the robins that the children were just like themselves.", "conveyed", ["convened", "conveyor", "converted"]),
 ("Dickon spoke robin, so the strange ___ he used with humans did not matter to the robin.", "gibberish", ["giblets", "lavish", "radish"]),
 ("The boy would lie down and then get up again in a ___ manner.", "disconcerting", ["disconnecting", "discontinuing", "disconnected"]),
 ("The robin stopped talking about it, afraid the mother's terror might be ___ to the Eggs.", "injurious", ["industrious", "luxurious", "envious"]),
 ("The boy who could speak robin so ___ was doing the exercises with them.", "fluently", ["frequently", "fluidly", "fruitfully"]),
 ("If you fly about for every meal, your muscles do not become ___.", "atrophied", ["attracted", "attached", "atomized"]),
 ("On a rainy morning Colin began to feel a little ___ on his sofa.", "restive", ["restful", "festive", "resistive"]),
 ("Mary giggled ___ at the idea of Colin shouting out of bed.", "inordinately", ["inadequately", "immediately", "ordinarily"]),
 ("Mary sat and looked ___ at the picture over the mantel.", "fixedly", ["fixably", "foxily", "flexibly"]),
], discussion=[
 "This chapter tells the story from the robin's point of view. Why do you think Burnett did that? How does it change the story?",
 "Colin uncovers his mother's picture and is no longer angry at her. What has changed in him?",
]),
26: dict(vocab=[
 ("abiding", "abiding", "adj.", "a-BID-ing", "/əˈbaɪdɪŋ/", "변치 않는, 오래 지속되는", "an abiding love · abiding interest", "She has an abiding love of nature.", "His abiding memory is of his grandmother's garden."),
 ("incantation", "incantations", "n.", "in-can-TA-tion", "/ˌɪnkænˈteɪʃən/", "주문(을 욈)", "chant an incantation · magic incantations", "The witch muttered an incantation.", "The children repeated their incantations."),
 ("devouring", "devouring", "adj./v.", "de-VOUR-ing", "/dɪˈvaʊərɪŋ/", "탐하는 듯한; 게걸스럽게 먹다", "devouring eyes · devour a book", "He fixed devouring eyes on the cake.", "She devoured the novel in one day."),
 ("rapturous", "rapturous", "adj.", "RAP-tur-ous", "/ˈræptʃərəs/", "열광적인, 황홀한", "rapturous applause · a rapturous welcome", "The singer got rapturous applause.", "They gave us a rapturous welcome."),
 ("reverence", "reverence", "n.", "REV-er-ence", "/ˈrevərəns/", "존경, 경외", "with reverence · deep reverence", "They spoke of their teacher with reverence.", "He has a reverence for nature."),
 ("unaffected", "unaffected", "adj.", "un-af-FECT-ed", "/ˌʌnəˈfektɪd/", "꾸밈없는, 자연스러운; 영향받지 않은", "simple and unaffected · unaffected by", "She has a warm, unaffected smile.", "The town was unaffected by the storm."),
 ("raspingly", "raspingly", "adv.", "RASP-ing-ly", "/ˈræspɪŋli/", "거칠게 긁는 소리로", "cough raspingly · speak raspingly", "The old man cleared his throat raspingly.", "\"Come in,\" he said raspingly."),
 ("intruder", "intruder", "n.", "in-TRU-der", "/ɪnˈtruːdər/", "침입자, 불청객", "an unwelcome intruder · feel like an intruder", "The dog barked at the intruder.", "I felt like an intruder at their party."),
 ("gloat", "gloating", "v.", "GLOAT", "/ɡloʊt/", "흐뭇해하다; 고소해하다", "gloat over · gloat about", "Don't gloat over your brother's mistake.", "She was gloating over her win."),
 ("adoration", "adoration", "n.", "ad-o-RA-tion", "/ˌædəˈreɪʃən/", "흠모, 깊은 사랑", "with adoration · look of adoration", "The puppy looked at him with adoration.", "Fans screamed in adoration."),
], quiz=[
 ("Their belief in the Magic was an ___ thing.", "abiding", ["abounding", "abetting", "abolishing"]),
 ("After the morning's ___, Colin sometimes gave them Magic lectures.", "incantations", ["incarnations", "invitations", "inclinations"]),
 ("When Colin spoke, old Ben fixed ___ eyes on him and kept them there.", "devouring", ["devoting", "detouring", "devolving"]),
 ("Something rushed through Colin—a sort of ___ belief that he would live.", "rapturous", ["ruptured", "rapacious", "raucous"]),
 ("Ben suggested singing the Doxology, though not with any particular ___.", "reverence", ["reference", "relevance", "severance"]),
 ("Dickon was quite simple and ___ about singing the Doxology.", "unaffected", ["unaffordable", "unattended", "unaffectionate"]),
 ("At the second line Ben ___ cleared his throat, and then he joined in.", "raspingly", ["raptly", "rapidly", "rashly"]),
 ("When Mrs. Sowerby appeared, no one felt that she was an ___ at all.", "intruder", ["instructor", "introducer", "interpreter"]),
 ("Mrs. Sowerby watched them eat, laughing and quite ___ over their appetites.", "gloating", ["floating", "bloating", "glowering"]),
 ("Colin looked at Susan Sowerby with a kind of bewildered ___.", "adoration", ["adaptation", "adornment", "adoption"]),
], discussion=[
 "Colin wishes Mrs. Sowerby were his mother. What makes her such a good mother to everyone?",
 "Mrs. Sowerby says the Magic and the \"Big Good Thing\" are the same. What do you think she means?",
]),
27: dict(vocab=[
 ("astounding", "astounding", "adj.", "a-STOUND-ing", "/əˈstaʊndɪŋ/", "놀라운, 믿기 어려운", "an astounding success · astounding news", "The results were astounding.", "She has an astounding memory."),
 ("detestation", "detestation", "n.", "de-tes-TA-tion", "/ˌdiːteˈsteɪʃən/", "혐오", "a detestation of · deep detestation", "He has a detestation of liars.", "Her detestation of cold weather is well known."),
 ("hypochondriac", "hypochondriac", "n.", "hy-po-CHON-dri-ac", "/ˌhaɪpəˈkɑːndriæk/", "건강염려증 환자", "a real hypochondriac", "My uncle is a hypochondriac; he thinks every cough is serious.", "Don't be such a hypochondriac."),
 ("stagnant", "stagnant", "adj.", "STAG-nant", "/ˈstæɡnənt/", "고여 있는, 정체된", "stagnant water · a stagnant economy", "Mosquitoes breed in stagnant water.", "His career felt stagnant."),
 ("reposeful", "reposeful", "adj.", "re-POSE-ful", "/rɪˈpoʊzfəl/", "평온한, 편안한", "a reposeful sleep · reposeful atmosphere", "The garden had a reposeful feeling.", "He fell into a reposeful sleep."),
 ("startlingly", "startlingly", "adv.", "START-ling-ly", "/ˈstɑːrtlɪŋli/", "깜짝 놀랄 만큼", "startlingly beautiful · startlingly bright", "Her eyes were startlingly blue.", "The answer was startlingly simple."),
 ("flustered", "flustered", "adj.", "FLUS-tered", "/ˈflʌstərd/", "허둥대는, 당황한", "get flustered · look flustered", "She got flustered when the boss walked in.", "He looked hot and flustered."),
 ("uncontrollable", "uncontrollable", "adj.", "un-con-TROL-la-ble", "/ˌʌnkənˈtroʊləbl/", "억누를 수 없는", "uncontrollable laughter · uncontrollable anger", "We burst into uncontrollable laughter.", "The fire was uncontrollable."),
 ("shrewdly", "shrewdly", "adv.", "SHREWD-ly", "/ˈʃruːdli/", "약삭빠르게, 영리하게", "shrewdly guess · smile shrewdly", "She shrewdly guessed what he wanted.", "He invested his money shrewdly."),
 ("forsake", "forsaken", "v.", "for-SAKE", "/fərˈseɪk/", "버리다, 저버리다", "forsake a place · forsaken by friends", "He felt forsaken by his friends.", "They forsook the city for the countryside."),
], quiz=[
 ("In this new century, hundreds of things still more ___ will be brought to light.", "astounding", ["astonished", "abounding", "astringent"]),
 ("Colin used to think only of his fears and his ___ of people who looked at him.", "detestation", ["destination", "devastation", "determination"]),
 ("Colin had been a hysterical half-crazy little ___ who knew nothing of the sunshine.", "hypochondriac", ["hypocrite", "hippopotamus", "hydrangea"]),
 ("It was as if a sweet clear spring had begun to rise in a ___ pool.", "stagnant", ["pregnant", "stagy", "stringent"]),
 ("After that magical day in the garden, Colin slept a new ___ sleep.", "reposeful", ["respectful", "resourceful", "remorseful"]),
 ("Mr. Craven looked at the sleeping face, the black lashes rimming ___ the closed eyes.", "startlingly", ["sparklingly", "sternly", "stiflingly"]),
 ("Mrs. Medlock came to Mr. Craven somewhat excited and curious and ___.", "flustered", ["clustered", "fostered", "plastered"]),
 ("Mr. Craven heard the ___ laughter of children trying not to be heard.", "uncontrollable", ["uncomfortable", "unconquerable", "unconvincing"]),
 ("\"Aye, that I did,\" Ben answered with a ___ significant air.", "shrewdly", ["shrewishly", "shrilly", "crudely"]),
 ("Mr. Craven felt drawn back to the place he had so long ___.", "forsaken", ["foreseen", "forbidden", "forgiven"]),
], discussion=[
 "Mr. Craven hears his wife's voice in a dream saying \"In the garden.\" Why do you think the ending happens in the garden?",
 "Both Colin and his father were \"sick\" from sadness and fear. What heals them? What heals people in real life?",
]),
}

# keep vocab and quiz in story order
_M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "modern.json"), encoding="utf-8"))
for _n, _d in WB.items():
    _t = " ".join(p["t"] for p in _M[_n - 1]["paras"] if not p["poem"])
    _pos = {v[0]: re.search(rf"\b{re.escape(v[1])}\b", _t).start() for v in _d["vocab"]}
    _d["vocab"].sort(key=lambda v: _pos[v[0]])
    _stem = lambda w: w.lower()[:max(3, len(w) - 2)]
    def _qpos(q, _d=_d, _pos=_pos):
        for v in _d["vocab"]:
            if q[1].lower().startswith(_stem(v[0])) or q[1].lower() == v[1].lower(): return _pos[v[0]]
        return 10**9
    _d["quiz"].sort(key=_qpos)
