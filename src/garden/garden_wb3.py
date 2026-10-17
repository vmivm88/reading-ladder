# The Secret Garden workbook, chapters 15–21. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
15: dict(vocab=[
 ("colorless", "colorless", "adj.", "COL-or-less", "/ˈkʌlərləs/", "핏기 없는, 무색의", "a colorless face · colorless liquid", "Her face was pale and colorless.", "Water is a colorless liquid."),
 ("whine", "whining", "v./adj.", "WHINE", "/waɪn/", "징징거리다, 우는소리 하다", "stop whining · a whining voice", "Stop whining and eat your dinner.", "The dog was whining at the door."),
 ("uncertainly", "uncertainly", "adv.", "un-CER-tain-ly", "/ʌnˈsɜːrtnli/", "자신 없게, 머뭇거리며", "smile uncertainly · ask uncertainly", "She smiled uncertainly at the stranger.", "\"Is this right?\" he asked uncertainly."),
 ("quiver", "quivering", "v.", "QUIV-er", "/ˈkwɪvər/", "가볍게 떨다", "quiver with excitement · lips quivering", "Her lips were quivering with fear.", "The leaves quivered in the wind."),
 ("unfurl", "unfurling", "v.", "un-FURL", "/ʌnˈfɜːrl/", "(말린 것이) 펴지다, 펼치다", "unfurl a flag · leaves unfurling", "New leaves were unfurling in the sun.", "They unfurled the flag."),
 ("tousled", "tousled", "adj.", "TOU-sled", "/ˈtaʊzld/", "(머리가) 헝클어진", "tousled hair · look tousled", "He came down with tousled hair.", "The wind left her looking tousled."),
 ("rapture", "rapture", "n.", "RAP-ture", "/ˈræptʃər/", "황홀감, 큰 기쁨", "with rapture · in raptures", "The children listened with rapture.", "She was in raptures over the gift."),
 ("inquiringly", "inquiringly", "adv.", "in-QUIR-ing-ly", "/ɪnˈkwaɪərɪŋli/", "묻는 듯이", "look inquiringly · raise eyebrows inquiringly", "She looked at me inquiringly.", "He raised his eyebrows inquiringly."),
 ("scold", "scolds", "v.", "SCOLD", "/skoʊld/", "꾸짖다, 야단치다", "scold someone for · get scolded", "Mom scolded me for coming home late.", "The teacher never scolds the kids."),
 ("disobey", "disobey", "v.", "dis-o-BEY", "/ˌdɪsəˈbeɪ/", "불복종하다, 거역하다", "disobey orders · disobey your parents", "He disobeyed his parents and went out.", "Soldiers cannot disobey orders."),
], quiz=[
 ("When Colin was interested he hardly looked ill, except that his face was so ___.", "colorless", ["colorful", "careless", "cloudless"]),
 ("Mrs. Medlock said Colin hadn't had a tantrum or a ___ fit since Mary made friends with him.", "whining", ["whirling", "winning", "shining"]),
 ("\"Would you hate it if—if a boy looked at you?\" Mary asked ___.", "uncertainly", ["uncommonly", "unkindly", "unwillingly"]),
 ("Mary sniffed the air until she laughed, remembering Dickon's nose ___ like a rabbit's.", "quivering", ["quarreling", "covering", "delivering"]),
 ("Here and there, glimpses of purple and yellow were ___ among the crocus stems.", "unfurling", ["unfurnished", "unfounded", "unfriendly"]),
 ("Dickon got up, laughing and glowing and ___, his eyes like a bit of the sky.", "tousled", ["tossed", "toasted", "tussled"]),
 ("Mary and Dickon dug and pulled and laughed low with ___.", "rapture", ["rupture", "capture", "raptor"]),
 ("The robin turned his head and looked at Dickon ___, still holding his twig.", "inquiringly", ["increasingly", "injuriously", "ingeniously"]),
 ("\"Ben Weatherstaff ___ him and makes fun of him,\" Mary said about the robin.", "scolds", ["scalds", "scowls", "holds"]),
 ("Mary said no one would dare ___ Colin if he wanted to go out with them.", "disobey", ["dismay", "display", "disarray"]),
], discussion=[
 "Mary tells Colin about Dickon little by little before she brings him. Why do you think she takes it slowly?",
 "The robins are building a nest, and Dickon says we must not stare at them. Why is it important to give others space?",
]),
16: dict(vocab=[
 ("self-sacrificing", "self-sacrificing", "adj.", "self-SAC-ri-fic-ing", "/ˌselfˈsækrɪfaɪsɪŋ/", "자기희생적인", "a self-sacrificing mother", "She is a kind, self-sacrificing nurse.", "He's not the self-sacrificing type."),
 ("doleful", "doleful", "adj.", "DOLE-ful", "/ˈdoʊlfəl/", "시무룩한, 슬픈", "a doleful face · doleful music", "The puppy had a doleful look.", "He sang a doleful song."),
 ("pitifulness", "pitifulness", "n.", "PIT-i-ful-ness", "/ˈpɪtɪfəlnəs/", "가련함, 딱함", "the pitifulness of", "She didn't see the pitifulness of his situation.", "The pitifulness of the old dog moved us."),
 ("condescend", "condescended", "v.", "con-de-SCEND", "/ˌkɑːndɪˈsend/", "(잘난 척) 마지못해 ~해 주다", "condescend to · condescending tone", "He condescended to answer my question.", "Don't condescend to me!"),
 ("sneer", "sneered", "v.", "SNEER", "/snɪr/", "비웃다, 냉소하다", "sneer at · sneer contemptuously", "\"You call that art?\" he sneered.", "She sneered at my old car."),
 ("ferociously", "ferociously", "adv.", "fe-RO-cious-ly", "/fəˈroʊʃəsli/", "사납게, 맹렬하게", "bark ferociously · fight ferociously", "The dog barked ferociously.", "They argued ferociously."),
 ("contradict", "contradicted", "v.", "con-tra-DICT", "/ˌkɑːntrəˈdɪkt/", "반박하다, 모순되다", "contradict someone · contradict yourself", "Don't contradict your father.", "His story contradicts the facts."),
 ("indignation", "indignation", "n.", "in-dig-NA-tion", "/ˌɪndɪɡˈneɪʃən/", "분개, 분노", "with indignation · full of indignation", "She opened her eyes wide with indignation.", "The decision caused indignation."),
 ("sourly", "sourly", "adv.", "SOUR-ly", "/ˈsaʊərli/", "시큰둥하게, 언짢게", "say sourly · look sourly", "\"Fine,\" he said sourly.", "She looked sourly at the rain."),
 ("pampered", "pampered", "adj.", "PAM-pered", "/ˈpæmpərd/", "응석받이로 자란, 애지중지하는", "a pampered child · pampered pets", "The pampered cat eats only fish.", "He was a rich, pampered boy."),
], quiz=[
 ("Mary was not a ___ person, so she ran off to Dickon instead of staying with Colin.", "self-sacrificing", ["self-satisfying", "self-supporting", "self-serving"]),
 ("Martha was waiting in Mary's room with a ___ face.", "doleful", ["dutiful", "delightful", "doubtful"]),
 ("Mary knew nothing about the ___ of people who were ill and nervous.", "pitifulness", ["playfulness", "plentifulness", "powerfulness"]),
 ("Colin frowned and ___ to look at her.", "condescended", ["concentrated", "conducted", "descended"]),
 ("\"A nice angel!\" Colin ___. \"He's a common cottage boy off the moor!\"", "sneered", ["sneezed", "steered", "smeared"]),
 ("Colin sneered ___, angry that Mary had stayed with Dickon.", "ferociously", ["precociously", "graciously", "spaciously"]),
 ("\"You're not!\" ___ Mary when Colin said he was going to die.", "contradicted", ["contracted", "conducted", "constructed"]),
 ("Colin opened his eyes wide with ___. He had never heard such a thing.", "indignation", ["imagination", "indigestion", "inclination"]),
 ("\"I don't believe it!\" said Mary ___. \"You just say that to make people sorry.\"", "sourly", ["surely", "sorely", "softly"]),
 ("The nurse laughed that it was the best thing for the sickly ___ boy to have someone stand up to him.", "pampered", ["papered", "pampas", "tampered"]),
], discussion=[
 "Mary and Colin have a big fight, but the nurse thinks it is good for Colin. Why? Can a fight ever be good for a friendship?",
 "Mary says Dickon is \"better than a common Rajah.\" What does she mean? What makes someone truly valuable?",
]),
17: dict(vocab=[
 ("restrain", "restrain", "v.", "re-STRAIN", "/rɪˈstreɪn/", "제지하다, 억제하다", "restrain yourself · restrain someone", "Two men restrained the angry fan.", "I couldn't restrain my laughter."),
 ("swollen", "swollen", "adj.", "SWOL-len", "/ˈswoʊlən/", "부은, 부어오른", "swollen eyes · a swollen ankle", "Her eyes were swollen from crying.", "He has a swollen ankle."),
 ("writhe", "writhe", "v.", "WRITHE", "/raɪð/", "(고통으로) 몸부림치다", "writhe in pain · writhe on the floor", "He writhed in pain on the floor.", "The snake writhed in the grass."),
 ("heave", "heaving", "v.", "HEAVE", "/hiːv/", "들썩이다; 들어 올리다", "heaving with sobs · heave a sigh", "His shoulders were heaving with sobs.", "She heaved the heavy box onto the table."),
 ("weariness", "weariness", "n.", "WEA-ri-ness", "/ˈwɪrinəs/", "피로", "a feeling of weariness · aches and weariness", "Weariness came over her after the trip.", "He spoke with great weariness."),
 ("ignorant", "ignorant", "adj.", "IG-no-rant", "/ˈɪɡnərənt/", "무지한, 잘 모르는", "ignorant of · an ignorant comment", "Many people are ignorant of the danger.", "That was an ignorant thing to say."),
 ("pathetically", "pathetically", "adv.", "pa-THET-i-cal-ly", "/pəˈθetɪkli/", "애처롭게", "say pathetically · pathetically small", "\"Please help me,\" he said pathetically.", "The puppy looked pathetically thin."),
 ("appealingly", "appealingly", "adv.", "ap-PEAL-ing-ly", "/əˈpiːlɪŋli/", "호소하듯이; 매력적으로", "look appealingly · smile appealingly", "The dog looked at me appealingly.", "She smiled appealingly at her father."),
 ("reluctance", "reluctance", "n.", "re-LUC-tance", "/rɪˈlʌktəns/", "꺼림, 마지못함", "with reluctance · show reluctance", "He agreed with reluctance.", "She showed some reluctance to leave."),
 ("relent", "relented", "v.", "re-LENT", "/rɪˈlent/", "(마음이) 누그러지다", "finally relent · heart relented", "Her parents finally relented and let her go.", "When she saw his tears, her heart relented."),
], quiz=[
 ("No one had ever dared to ___ or contradict this hysterical boy.", "restrain", ["retrain", "restore", "refrain"]),
 ("Colin's face looked dreadful, white and red and ___, and he was choking.", "swollen", ["stolen", "swallowed", "sworn"]),
 ("\"I felt the lump,\" Colin choked, and he began to ___ again and sob.", "writhe", ["write", "wreathe", "wither"]),
 ("Colin was ___ with great breathless sobs.", "heaving", ["heading", "having", "heeding"]),
 ("Colin had thought about his aches and ___ for hours and days and years.", "weariness", ["wariness", "wetness", "wilderness"]),
 ("The house was heavy with the fears of people who were ___ and tired of him.", "ignorant", ["important", "arrogant", "elegant"]),
 ("\"C-could you?\" Colin said ___ when the nurse said there was no lump.", "pathetically", ["poetically", "patiently", "practically"]),
 ("Colin turned his tired eyes on Mary ___: \"Oh, yes! Sing me that song.\"", "appealingly", ["appallingly", "apparently", "approvingly"]),
 ("\"Well,\" said the nurse, with an attempt at ___, and then she left gladly.", "reluctance", ["relevance", "reliance", "resistance"]),
 ("Mary looked at his poor tired face and swollen eyes, and her heart ___.", "relented", ["resented", "rented", "relayed"]),
], discussion=[
 "Mary shouts at Colin to stop his tantrum, and it works. Why does it work when no one else could stop him?",
 "The writer says most of Colin's illness was created by his own fear. Can fear make people sick? Do you have an example?",
]),
18: dict(vocab=[
 ("pitifully", "pitifully", "adv.", "PIT-i-ful-ly", "/ˈpɪtɪfəli/", "애처로울 만큼", "pitifully thin · pitifully small", "The kitten was pitifully thin.", "He was paid pitifully little."),
 ("bearable", "bearable", "adj.", "BEAR-a-ble", "/ˈberəbl/", "견딜 만한", "make life bearable · barely bearable", "Friends made the hard times bearable.", "The pain was barely bearable."),
 ("soak", "soaked", "v.", "SOAK", "/soʊk/", "흠뻑 적시다; 흠뻑 받아들이다", "soaked through · soak up the sun", "We got soaked in the rain.", "Let's soak up the sunshine."),
 ("modify", "modify", "v.", "MOD-i-fy", "/ˈmɑːdɪfaɪ/", "수정하다, 조정하다", "modify a plan · modify your behavior", "We modified the plan a little.", "He modified his accent for the job."),
 ("experienced", "experienced", "adj.", "ex-PE-ri-enced", "/ɪkˈspɪriənst/", "경험 많은, 능숙한", "an experienced teacher · experienced in", "She is an experienced driver.", "We need someone experienced in sales."),
 ("joyously", "joyously", "adv.", "JOY-ous-ly", "/ˈdʒɔɪəsli/", "기쁘게, 즐겁게", "laugh joyously · sing joyously", "The children laughed joyously.", "Bells rang joyously."),
 ("nuzzle", "nuzzling", "v.", "NUZ-zle", "/ˈnʌzl/", "코를 비비다", "nuzzle against · nuzzling nose", "The horse nuzzled my hand.", "The puppy nuzzled against her neck."),
 ("muzzle", "muzzle", "n.", "MUZ-zle", "/ˈmʌzl/", "(동물의) 주둥이; 입마개", "a soft muzzle · a dog muzzle", "The pony touched me with its soft muzzle.", "The dog wore a muzzle."),
 ("affectation", "affectation", "n.", "af-fec-TA-tion", "/ˌæfekˈteɪʃən/", "꾸밈, 가식", "without affectation · an affectation", "She spoke simply, without affectation.", "His British accent is just an affectation."),
 ("detest", "detested", "v.", "de-TEST", "/dɪˈtest/", "몹시 싫어하다", "detest someone · detest doing", "I detest getting up early.", "She detested the noise of the city."),
], quiz=[
 ("Colin was in bed; his face was ___ white and there were dark circles round his eyes.", "pitifully", ["plentifully", "peacefully", "powerfully"]),
 ("It seemed hardly ___ to leave the garden, but Mary told Dickon about Colin.", "bearable", ["bendable", "readable", "breakable"]),
 ("Dickon wanted Colin to be ___ through with sunshine.", "soaked", ["soaped", "sucked", "smoked"]),
 ("At other times Dickon tried to ___ his dialect so that Mary could understand better.", "modify", ["mollify", "magnify", "notify"]),
 ("Colin sniffed like Dickon, though not in such an ___ way.", "experienced", ["experimental", "expensive", "expressed"]),
 ("\"You smell like flowers and fresh things,\" Colin cried out quite ___.", "joyously", ["jealously", "jokingly", "gingerly"]),
 ("Jump was a shaggy moor pony with a pretty face and a ___ velvet nose.", "nuzzling", ["puzzling", "nestling", "guzzling"]),
 ("Jump kissed Mary on the cheek with his velvet ___.", "muzzle", ["puzzle", "muscle", "nozzle"]),
 ("\"Yes,\" Mary answered without any ___, when Colin asked if she had hated people.", "affectation", ["affection", "infection", "application"]),
 ("Mary said she would have ___ Colin if she had met him before the robin and Dickon.", "detested", ["detected", "tested", "detained"]),
], discussion=[
 "Mary admits she used to hate people. What changed her? Can friends change who we are?",
 "Mary loves Dickon's broad Yorkshire and starts to speak it herself. Have you ever picked up a dialect or accent from a friend?",
]),
19: dict(vocab=[
 ("dread", "dreaded", "v.", "DREAD", "/dred/", "몹시 두려워하다", "dread doing · dread the thought", "I dreaded going to the dentist.", "She dreads the long winter."),
 ("irritably", "irritably", "adv.", "IR-ri-ta-bly", "/ˈɪrɪtəbli/", "짜증스럽게", "say irritably · answer irritably", "\"What now?\" he said irritably.", "She waved irritably at the fly."),
 ("hysteria", "hysteria", "n.", "hys-TER-i-a", "/hɪˈstɪriə/", "히스테리, 병적 흥분", "mass hysteria · in hysteria", "The news caused mass hysteria.", "She laughed with near hysteria."),
 ("self-indulgence", "self-indulgence", "n.", "self-in-DUL-gence", "/ˌself ɪnˈdʌldʒəns/", "방종, 제멋대로 함", "a bit of self-indulgence", "Eating the whole cake was pure self-indulgence.", "His self-indulgence annoyed everyone."),
 ("unscrupulous", "unscrupulous", "adj.", "un-SCRU-pu-lous", "/ʌnˈskruːpjələs/", "부도덕한, 파렴치한", "an unscrupulous businessman", "An unscrupulous dealer cheated them.", "Be careful of unscrupulous websites."),
 ("volubly", "volubly", "adv.", "VOL-u-bly", "/ˈvɑːljəbli/", "말을 쏟아내듯 유창하게", "talk volubly", "She talked volubly about her trip.", "He apologized volubly."),
 ("recluse", "recluse", "n.", "REC-luse", "/ˈrekluːs/", "은둔자", "live like a recluse · a famous recluse", "The writer lived as a recluse for years.", "After retiring, he became a recluse."),
 ("austerely", "austerely", "adv.", "aus-TERE-ly", "/ɔːˈstɪrli/", "엄격하게, 근엄하게", "say austerely · austerely furnished", "\"That is not allowed,\" she said austerely.", "The room was austerely furnished."),
 ("overwhelmed", "overwhelmed", "adj.", "o-ver-WHELMED", "/ˌoʊvərˈwelmd/", "압도된, 벅찬", "feel overwhelmed · overwhelmed by", "I felt overwhelmed by all the work.", "She was overwhelmed with joy."),
 ("ravenous", "ravenous", "adj.", "RAV-en-ous", "/ˈrævənəs/", "몹시 배고픈, 게걸스러운", "a ravenous appetite · feel ravenous", "After the hike we were ravenous.", "The baby had a ravenous appetite."),
], quiz=[
 ("Dr. Craven ___ and detested the difficulties of visiting Colin.", "dreaded", ["dreamed", "threaded", "dredged"]),
 ("\"How is he?\" Dr. Craven asked Mrs. Medlock rather ___.", "irritably", ["inevitably", "invisibly", "incredibly"]),
 ("Dr. Craven said the boy was half insane with ___ and self-indulgence.", "hysteria", ["history", "mystery", "hostility"]),
 ("Dr. Craven said the boy was half insane with hysteria and ___.", "self-indulgence", ["self-confidence", "self-defense", "self-reliance"]),
 ("Dr. Craven could inherit the Manor if Colin died, but he was not an ___ man.", "unscrupulous", ["unscrewed", "unsuspicious", "unsurprised"]),
 ("Mrs. Medlock talked quite ___ about Susan Sowerby's wise words.", "volubly", ["voluntarily", "valuably", "vulnerably"]),
 ("The servants joked that the unpopular young ___ had \"found his master.\"", "recluse", ["recruit", "refuse", "excuse"]),
 ("\"I told you he was a charmer,\" said Colin ___. \"Charmers' animals never bite.\"", "austerely", ["absurdly", "actually", "annually"]),
 ("Colin was so ___ by his own pleasure that he did not even think of speaking.", "overwhelmed", ["overheard", "overflowed", "overthrown"]),
 ("The little lamb sucked the bottle with ___ ecstasy.", "ravenous", ["ravishing", "rigorous", "nervous"]),
], discussion=[
 "Colin cannot believe that spring has really come. What signs of spring do you love most where you live?",
 "Mrs. Sowerby says \"th' whole orange\" belongs to nobody alone—everyone gets a piece. What do you think she means?",
]),
20: dict(vocab=[
 ("absorbing", "absorbing", "adj.", "ab-SORB-ing", "/əbˈzɔːrbɪŋ/", "몰입하게 하는, 흥미진진한", "an absorbing book · find something absorbing", "The puzzle was absorbing.", "It's an absorbing story."),
 ("secrecy", "secrecy", "n.", "SE-cre-cy", "/ˈsiːkrəsi/", "비밀 유지", "in secrecy · great secrecy", "The plan was made in secrecy.", "Why all the secrecy?"),
 ("rational", "rational", "adj.", "RA-tion-al", "/ˈræʃənl/", "이성적인, 합리적인", "a rational decision · rational thinking", "Let's make a rational choice.", "His fear was not rational."),
 ("exaggerated", "exaggerated", "adj.", "ex-AG-ger-at-ed", "/ɪɡˈzædʒəreɪtɪd/", "과장된", "exaggerated stories · greatly exaggerated", "The reports were exaggerated.", "He told an exaggerated story about the fish."),
 ("uncanny", "uncanny", "adj.", "un-CAN-ny", "/ʌnˈkæni/", "묘한, 이상한", "an uncanny feeling · uncanny resemblance", "She has an uncanny ability to guess.", "There's an uncanny silence here."),
 ("fanciful", "fanciful", "adj.", "FAN-ci-ful", "/ˈfænsɪfəl/", "공상적인, 터무니없는", "a fanciful idea · fanciful stories", "His fanciful ideas made us laugh.", "That seems a little fanciful."),
 ("menagerie", "menagerie", "n.", "me-NAG-er-ie", "/məˈnædʒəri/", "동물 무리, (작은) 동물원", "a menagerie of pets", "Their house is a menagerie of cats and dogs.", "The castle once had a royal menagerie."),
 ("leniently", "leniently", "adv.", "LE-ni-ent-ly", "/ˈliːniəntli/", "너그럽게, 관대하게", "treat leniently · smile leniently", "The judge treated him leniently.", "She smiled leniently at the mistake."),
 ("attentively", "attentively", "adv.", "at-TEN-tive-ly", "/əˈtentɪvli/", "주의 깊게", "listen attentively · watch attentively", "The students listened attentively.", "The cat watched the bird attentively."),
 ("morbid", "morbid", "adj.", "MOR-bid", "/ˈmɔːrbɪd/", "병적인, 음울한", "a morbid interest · morbid thoughts", "He has a morbid interest in death.", "Don't be so morbid!"),
], quiz=[
 ("The most ___ thing was preparing to get Colin to the garden secretly.", "absorbing", ["absolving", "adoring", "absurd"]),
 ("Colin had to be taken to the garden with sufficient ___.", "secrecy", ["secretary", "security", "accuracy"]),
 ("Looking at the flower-beds would seem such a ___ thing to do that no one would wonder.", "rational", ["national", "rationed", "rotational"]),
 ("Mr. Roach had heard a dozen ___ stories about Colin's looks and tempers.", "exaggerated", ["excavated", "exasperated", "exhilarated"]),
 ("People told stories about Colin's ___ looks and ways and his insane tempers.", "uncanny", ["uncanned", "unclean", "unlucky"]),
 ("There had been ___ descriptions of a humped back given by people who had never seen him.", "fanciful", ["fearful", "forceful", "fruitful"]),
 ("Mrs. Medlock warned Mr. Roach he might find himself in the middle of a ___.", "menagerie", ["manager", "marriage", "massage"]),
 ("When Mr. Roach heard Dickon's name, he smiled quite ___.", "leniently", ["lengthily", "lazily", "loudly"]),
 ("A squirrel sat on Dickon's back, ___ nibbling a nut.", "attentively", ["attractively", "alternatively", "accidentally"]),
 ("Shut in and ___ as his life had been, Colin had a great imagination.", "morbid", ["mobile", "moral", "rabid"]),
], discussion=[
 "Colin plans the trip to the garden like a general. How do you feel before a big day you've planned carefully?",
 "When Colin enters the garden he says, \"I shall live forever!\" What do you think he feels at that moment?",
]),
21: dict(vocab=[
 ("radiantly", "radiantly", "adv.", "RA-di-ant-ly", "/ˈreɪdiəntli/", "눈부시게, 환하게", "radiantly beautiful · smile radiantly", "The bride looked radiantly happy.", "The sun shone radiantly."),
 ("reign", "reigned", "v.", "REIGN", "/reɪn/", "지배하다, 가득하다", "peace reigned · reign over", "Silence reigned in the room.", "The queen reigned for fifty years."),
 ("threateningly", "threateningly", "adv.", "THREAT-en-ing-ly", "/ˈθretnɪŋli/", "위협적으로", "growl threateningly · move threateningly", "The dog growled threateningly.", "He raised his fist threateningly."),
 ("harangue", "harangued", "v.", "ha-RANGUE", "/həˈræŋ/", "장황하게 호통치다", "harangue a crowd · harangue someone", "The coach harangued the players.", "He harangued us about being late."),
 ("outraged", "outraged", "adj.", "OUT-raged", "/ˈaʊtreɪdʒd/", "격분한", "outraged by · outraged citizens", "She was outraged by the unfair decision.", "Outraged fans booed the referee."),
 ("spellbound", "spellbound", "adj.", "SPELL-bound", "/ˈspelbaʊnd/", "넋을 잃은, 홀린 듯한", "hold someone spellbound · listen spellbound", "The story held the children spellbound.", "We watched spellbound."),
 ("imperiously", "imperiously", "adv.", "im-PE-ri-ous-ly", "/ɪmˈpɪriəsli/", "오만하게, 명령하듯이", "beckon imperiously · speak imperiously", "She waved imperiously for the waiter.", "\"Bring it here,\" he said imperiously."),
 ("gnarled", "gnarled", "adj.", "GNARLED", "/nɑːrld/", "(손·나무가) 울퉁불퉁 마디진", "gnarled hands · a gnarled tree", "Grandpa's gnarled hands held the cup.", "A gnarled old oak stood by the river."),
 ("tactless", "tactless", "adj.", "TACT-less", "/ˈtæktləs/", "눈치 없는, 무신경한", "a tactless remark · tactless question", "It was tactless to ask her age.", "He's honest but tactless."),
 ("wraith", "wraith", "n.", "WRAITH", "/reɪθ/", "유령, 망령", "as pale as a wraith · a wraith-like figure", "She looked as white as a wraith.", "A wraith-like figure appeared in the fog."),
], quiz=[
 ("That afternoon the whole world seemed perfect and ___ beautiful for one boy.", "radiantly", ["randomly", "rapidly", "rationally"]),
 ("\"Tha'rt shapin' first-rate,\" Mary said to Colin, and delight ___.", "reigned", ["rained", "resigned", "reined"]),
 ("Ben mounted another step ___ as if he meant to jump down and deal with Mary.", "threateningly", ["thrillingly", "thoroughly", "thoughtfully"]),
 ("\"I never thowt much o' thee!\" Ben ___ from the top of his ladder.", "harangued", ["hanged", "hammered", "harmonized"]),
 ("When Mary blamed the robin, Ben was so ___ that he nearly climbed down.", "outraged", ["outrun", "outgrown", "outdated"]),
 ("At first Colin sat up and listened as if he were ___.", "spellbound", ["homebound", "spellchecked", "spelled"]),
 ("Then Colin recovered and beckoned ___ to Dickon: \"Wheel me over there!\"", "imperiously", ["imperfectly", "impressively", "impartially"]),
 ("Ben put his ___ hand up and passed it over his eyes.", "gnarled", ["snarled", "gnawed", "garbled"]),
 ("Ben was an ignorant and ___ old man who could only repeat what he had heard.", "tactless", ["tasteless", "tireless", "faultless"]),
 ("\"Tha'rt as thin as a lath an' as white as a ___, but there's not a knob on thee,\" said Ben.", "wraith", ["wreath", "wrath", "raft"]),
], discussion=[
 "Colin stands up on his own legs to prove Ben wrong. What gave him the strength? Have you ever done something just to prove people wrong?",
 "Ben cries when he sees Colin standing. Why is it so emotional for him?",
]),
}

OLD = {
 "carven": ("형용사", "(옛) 조각된 (= carved)", "\"the carven four-posted bed\" = the carved bed. An old poetic form."),
 "hearken": ("동사", "(옛) 귀 기울이다 (= listen)", "Dickon says \"hearken at 'em callin'\" = listen to them calling."),
}
IDIOMS = {
 "as thin as a lath": ("비쩍 마른", "very thin / as thin as a rail", "A lath is a thin strip of wood. Today: \"as thin as a stick\" or \"skinny\"."),
}
DIALECT = {
 "jography": ("geography", "지리(책)", "Mrs. Sowerby's spelling of how she says \"geography\"."),
 "ses": ("says / said", "말한다, 말했다", "\"I ses to 'em all\" = I said to them all."),
 "impidint": ("impudent, cheeky", "뻔뻔한, 건방진", "Ben's way of saying \"impudent\"."),
 "seed": ("saw / seen", "보았다", "\"I never seed one as graidely\" = I never saw such a fine one.", "never seed"),
 "graidelest": ("finest, best", "가장 멋진", "Mary makes \"graidely\" into \"graidelest\" (the most graidely). She is enjoying Yorkshire talk!"),
 "happen": ("perhaps, maybe", "아마, 어쩌면", "In Yorkshire \"happen\" can mean \"perhaps\": \"as happen it was made\" = that perhaps it was made.", "as happen"),
 "mon": ("man", "남자, 사나이", "\"Tha'lt make a mon yet\" = you'll grow up to be a man yet."),
}
OLD_MARKS = {15: ["carven"], 18: ["hearken"]}
IDIOM_MARKS = {21: ["as thin as a lath"]}

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
