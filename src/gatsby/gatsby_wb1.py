# The Great Gatsby workbook, chapters 1–3. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
1: dict(vocab=[
 ("vulnerable", "vulnerable", "adj.", "VUL-ner-a-ble", "/ˈvʌlnərəbl/", "상처받기 쉬운, 취약한", "vulnerable to · feel vulnerable", "Young children are vulnerable to illness.", "I felt vulnerable after telling her my secret."),
 ("privileged", "privileged", "adj.", "PRIV-i-leged", "/ˈprɪvəlɪdʒd/", "특권을 가진, 특별히 허락된", "a privileged background · feel privileged", "He grew up in a privileged family.", "I feel privileged to work with such people."),
 ("supercilious", "supercilious", "adj.", "su-per-CIL-i-ous", "/ˌsuːpərˈsɪliəs/", "거만한, 남을 깔보는", "a supercilious smile · supercilious manner", "The waiter gave us a supercilious look.", "She spoke in a supercilious tone."),
 ("arrogant", "arrogant", "adj.", "AR-ro-gant", "/ˈærəɡənt/", "오만한", "an arrogant attitude · arrogant behavior", "He's arrogant about his success.", "Don't be so arrogant—listen to others."),
 ("wistfulness", "wistfulness", "n.", "WIST-ful-ness", "/ˈwɪstfəlnəs/", "아쉬움, 그리움이 섞인 마음", "a touch of wistfulness · with wistfulness", "She spoke of her childhood with wistfulness.", "There was wistfulness in his smile."),
 ("compulsion", "compulsion", "n.", "com-PUL-sion", "/kəmˈpʌlʃən/", "강박, 끌어당기는 힘; 강요", "feel a compulsion to · under compulsion", "I felt a compulsion to check my phone.", "Nobody is under any compulsion to come."),
 ("complacency", "complacency", "n.", "com-PLA-cen-cy", "/kəmˈpleɪsənsi/", "자기만족, 안주", "a mood of complacency · no room for complacency", "Success led to complacency.", "There is no room for complacency."),
 ("sophisticated", "sophisticated", "adj.", "so-PHIS-ti-cat-ed", "/səˈfɪstɪkeɪtɪd/", "세련된, 세상 물정에 밝은; 정교한", "a sophisticated woman · sophisticated technology", "She looked elegant and sophisticated.", "This is a very sophisticated system."),
 ("cynical", "cynical", "adj.", "CYN-i-cal", "/ˈsɪnɪkl/", "냉소적인", "cynical about · a cynical view", "He's cynical about politicians.", "Don't be so cynical—people can be kind."),
 ("peremptorily", "peremptorily", "adv.", "pe-REMP-to-ri-ly", "/pəˈremptərəli/", "단호하게, 명령하듯", "call peremptorily · order peremptorily", "\"Sit down,\" she said peremptorily.", "He peremptorily ended the meeting."),
], quiz=[
 ("\"In my younger and more ___ years my father gave me some advice,\" Nick begins.", "vulnerable", ["valuable", "venerable", "variable"]),
 ("Nick wanted no more riotous excursions with ___ glimpses into the human heart.", "privileged", ["prevailed", "pickled", "pivoted"]),
 ("At thirty, Tom was a sturdy man with a rather hard mouth and a ___ manner.", "supercilious", ["superstitious", "supernatural", "superficial"]),
 ("Two shining ___ eyes had established dominance over Tom's face.", "arrogant", ["elegant", "abrogated", "ignorant"]),
 ("Nick felt Tom wanted him to like him, with some harsh, defiant ___ of his own.", "wistfulness", ["wastefulness", "watchfulness", "wilfulness"]),
 ("There was an excitement in Daisy's voice: a singing ___, a whispered \"Listen.\"", "compulsion", ["compassion", "completion", "competition"]),
 ("Tom talked about race, as if his ___ was not enough for him any more.", "complacency", ["complexity", "competency", "complicity"]),
 ("\"___—God, I'm sophisticated!\" Daisy said with thrilling scorn.", "Sophisticated", ["Sympathetic", "Suffocated", "Systematic"]),
 ("\"I've had a very bad time, Nick, and I'm pretty ___ about everything,\" Daisy said.", "cynical", ["clinical", "cyclical", "comical"]),
 ("As Nick started his motor, Daisy ___ called: \"Wait!\"", "peremptorily", ["perpetually", "permanently", "periodically"]),
], discussion=[
 "Nick's father tells him: \"Just remember that all the people in this world haven't had the advantages that you've had.\" Is this good advice? How does it shape Nick?",
 "Daisy hopes her daughter will be \"a beautiful little fool.\" What does she mean? What does it say about women's lives in the 1920s?",
]),
2: dict(vocab=[
 ("impenetrable", "impenetrable", "adj.", "im-PEN-e-tra-ble", "/ɪmˈpenɪtrəbl/", "꿰뚫을 수 없는, 짙은; 이해할 수 없는", "impenetrable fog · an impenetrable mystery", "An impenetrable fog covered the city.", "His accent was almost impenetrable."),
 ("anaemic", "anaemic", "adj.", "a-NAE-mic", "/əˈniːmɪk/", "빈혈의, 핏기 없는; 활기 없는", "look anaemic · anaemic growth (US: anemic)", "She looked pale and anaemic.", "The economy showed anaemic growth."),
 ("smoulder", "smouldering", "v.", "SMOUL-der", "/ˈsmoʊldər/", "(불·감정이) 연기만 내며 타다, 들끓다", "smouldering anger · a smouldering fire (US: smolder)", "The fire was still smouldering in the morning.", "She gave him a smouldering look."),
 ("discreetly", "discreetly", "adv.", "dis-CREET-ly", "/dɪˈskriːtli/", "남의 눈에 띄지 않게, 신중하게", "leave discreetly · discreetly ask", "He discreetly left the room.", "She discreetly checked her phone."),
 ("apathetically", "apathetically", "adv.", "ap-a-THET-i-cal-ly", "/ˌæpəˈθetɪkli/", "무관심하게, 무기력하게", "shrug apathetically · sit apathetically", "The students listened apathetically.", "He shrugged apathetically."),
 ("possessively", "possessively", "adv.", "pos-SES-sive-ly", "/pəˈzesɪvli/", "소유욕을 드러내며, 내 것인 양", "hold possessively · look possessively", "He held her arm possessively.", "The dog guarded its bowl possessively."),
 ("hauteur", "hauteur", "n.", "hau-TEUR", "/hoʊˈtɜːr/", "오만함, 도도함", "with hauteur · aristocratic hauteur", "She looked at us with cold hauteur.", "His hauteur made him unpopular."),
 ("disdain", "disdain", "n./v.", "dis-DAIN", "/dɪsˈdeɪn/", "경멸, 업신여김", "with disdain · disdain for", "He looked at the cheap food with disdain.", "She has disdain for liars."),
 ("strident", "strident", "adj.", "STRI-dent", "/ˈstraɪdnt/", "귀에 거슬리는, 시끄럽고 강경한", "a strident voice · strident criticism", "Her strident voice filled the room.", "The plan faced strident opposition."),
 ("inexhaustible", "inexhaustible", "adj.", "in-ex-HAUST-i-ble", "/ˌɪnɪɡˈzɔːstəbl/", "무궁무진한, 끝없는", "an inexhaustible supply · inexhaustible energy", "Children have inexhaustible energy.", "The internet is an inexhaustible source of information."),
], quiz=[
 ("In the valley of ashes, ash-grey men stir up an ___ cloud with their spades.", "impenetrable", ["impeccable", "impenitent", "improbable"]),
 ("George Wilson was a blond, spiritless man, ___, and faintly handsome.", "anaemic", ["academic", "anatomic", "epidemic"]),
 ("Myrtle had a vitality as if the nerves of her body were continually ___.", "smouldering", ["shouldering", "smothering", "soldering"]),
 ("Mrs. Wilson sat ___ in another car on the way to New York.", "discreetly", ["discordantly", "directly", "distinctly"]),
 ("One dog biscuit decomposed ___ in the saucer of milk all afternoon.", "apathetically", ["apologetically", "pathetically", "alphabetically"]),
 ("Myrtle looked around so ___ at the furniture that Nick wondered if she lived there.", "possessively", ["positively", "progressively", "passively"]),
 ("After changing her dress, Myrtle's vitality was converted into impressive ___.", "hauteur", ["hatter", "humor", "hunter"]),
 ("Mrs. Wilson rejected the compliment by raising her eyebrow in ___.", "disdain", ["detain", "domain", "sustain"]),
 ("Each time Nick tried to leave, he was pulled into some wild, ___ argument.", "strident", ["student", "strided", "stringent"]),
 ("Nick was both enchanted and repelled by the ___ variety of life.", "inexhaustible", ["inexplicable", "inexcusable", "inexpressible"]),
], discussion=[
 "The eyes of Doctor T. J. Eckleburg watch over the valley of ashes. What do you think they might stand for?",
 "Nick is \"within and without\"—both enjoying and disliking the party. Have you ever felt like that in a group?",
]),
3: dict(vocab=[
 ("innuendo", "innuendo", "n.", "in-nu-EN-do", "/ˌɪnjuˈendoʊ/", "암시, 빈정대는 넌지시 하는 말", "sexual innuendo · full of innuendo", "The comedian's jokes were full of innuendo.", "She ignored his innuendo."),
 ("vehemently", "vehemently", "adv.", "VE-he-ment-ly", "/ˈviːəməntli/", "격렬하게, 강력히", "deny vehemently · argue vehemently", "He vehemently denied the rumor.", "She vehemently opposed the plan."),
 ("credulity", "credulity", "n.", "cre-DU-li-ty", "/krɪˈduːləti/", "쉽게 믿는 성질, 믿음", "strain credulity · beyond credulity", "The story strains credulity.", "His credulity made him easy to cheat."),
 ("notorious", "notorious", "adj.", "no-TO-ri-ous", "/noʊˈtɔːriəs/", "악명 높은, 유명한(나쁜 쪽으로)", "a notorious criminal · notorious for", "The road is notorious for accidents.", "He was a notorious liar."),
 ("corpulent", "corpulent", "adj.", "COR-pu-lent", "/ˈkɔːrpjələnt/", "뚱뚱한, 비만한", "a corpulent man · corpulent figure", "A corpulent man sat at the bar.", "The king was old and corpulent."),
 ("convivial", "convivial", "adj.", "con-VIV-i-al", "/kənˈvɪviəl/", "흥겨운, 유쾌하게 어울리는", "a convivial atmosphere · convivial evening", "The party had a convivial atmosphere.", "He was a convivial host."),
 ("tantalize", "tantalizing", "v.", "TAN-ta-lize", "/ˈtæntəlaɪz/", "감질나게 하다, 애태우다", "tantalizing smell · tantalize someone", "The tantalizing smell of bread filled the street.", "Stop tantalizing me—just tell me!"),
 ("poignant", "poignant", "adj.", "POIG-nant", "/ˈpɔɪnjənt/", "가슴 아픈, 애잔한", "a poignant moment · poignant memories", "It was a poignant farewell.", "The film has many poignant scenes."),
 ("insolent", "insolent", "adj.", "IN-so-lent", "/ˈɪnsələnt/", "무례한, 건방진", "an insolent smile · insolent behavior", "The insolent boy laughed at the teacher.", "She gave an insolent reply."),
 ("incurably", "incurably", "adv.", "in-CUR-a-bly", "/ɪnˈkjʊrəbli/", "고칠 수 없을 만큼, 구제불능으로", "incurably romantic · incurably ill", "He is incurably optimistic.", "She was incurably curious."),
], quiz=[
 ("The garden is alive with chatter and laughter, and casual ___ and introductions forgotten on the spot.", "innuendo", ["crescendo", "intuition", "inventory"]),
 ("People denied so ___ any knowledge of Gatsby's movements that Nick slunk off.", "vehemently", ["vaguely", "vividly", "virtually"]),
 ("Guests said Gatsby was a German spy, then a war hero, and their ___ switched back and forth.", "credulity", ["cruelty", "curiosity", "credibility"]),
 ("A celebrated tenor sang in Italian, and a ___ contralto sang in jazz.", "notorious", ["nutritious", "numerous", "nervous"]),
 ("Nick had expected Gatsby to be a florid and ___ person in his middle years.", "corpulent", ["corporal", "competent", "opulent"]),
 ("Girls were putting their heads on men's shoulders in a puppyish, ___ way.", "convivial", ["conventional", "convincing", "convertible"]),
 ("\"I swore I wouldn't tell it and here I am ___ you,\" Jordan said.", "tantalizing", ["tranquilizing", "tattooing", "terrorizing"]),
 ("Young clerks in the dusk were wasting the most ___ moments of night and life.", "poignant", ["pregnant", "pungent", "pointed"]),
 ("Jordan kept a cool, ___ smile turned to the world.", "insolent", ["indolent", "insulin", "innocent"]),
 ("Nick realized that Jordan was ___ dishonest.", "incurably", ["incredibly", "invariably", "inaudibly"]),
], discussion=[
 "Many guests come to Gatsby's parties without being invited, and no one seems to know him. What does this tell you about the guests? About Gatsby?",
 "Nick says, \"I am one of the few honest people that I have ever known.\" Do you believe him? Why or why not?",
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
