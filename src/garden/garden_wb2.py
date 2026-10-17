# The Secret Garden workbook, chapters 8–14. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
8: dict(vocab=[
 ("consult", "consult", "v.", "con-SULT", "/kənˈsʌlt/", "상의하다, 의견을 구하다", "consult a doctor · consult with", "You should consult a doctor.", "She never consults anyone before deciding."),
 ("mysteriously", "mysteriously", "adv.", "mys-TE-ri-ous-ly", "/mɪˈstɪriəsli/", "이상하게, 신비롭게", "disappear mysteriously · smile mysteriously", "My keys mysteriously disappeared.", "She smiled mysteriously and said nothing."),
 ("baffling", "baffling", "adj.", "BAF-fling", "/ˈbæflɪŋ/", "도무지 이해할 수 없는", "a baffling problem · find something baffling", "The instructions were baffling.", "His sudden anger was baffling."),
 ("contrariness", "contrariness", "n.", "con-TRAR-i-ness", "/kənˈtrerinəs/", "청개구리 심보, 심술", "pure contrariness · out of contrariness", "He said no out of pure contrariness.", "Her contrariness made everyone tired."),
 ("exhibit", "exhibited", "v.", "ex-HIB-it", "/ɪɡˈzɪbɪt/", "보여 주다, 전시하다", "exhibit paintings · exhibit signs of", "She proudly exhibited her new bag.", "The museum exhibits old coins."),
 ("impudence", "impudence", "n.", "IM-pu-dence", "/ˈɪmpjədəns/", "건방짐, 뻔뻔함", "the impudence to · sheer impudence", "He had the impudence to laugh at me.", "What impudence!"),
 ("adorably", "adorably", "adv.", "a-DOR-a-bly", "/əˈdɔːrəbli/", "사랑스럽게", "adorably cute · smile adorably", "The puppy was adorably clumsy.", "She looked adorably sleepy."),
 ("untrimmed", "untrimmed", "adj.", "un-TRIMMED", "/ʌnˈtrɪmd/", "다듬지 않은, 손질하지 않은", "an untrimmed hedge · untrimmed hair", "The garden was full of untrimmed bushes.", "His untrimmed beard looked messy."),
 ("trail", "trails", "n./v.", "TRAIL", "/treɪl/", "늘어진 줄기; 오솔길; 끌리다", "ivy trails · a hiking trail", "Long trails of ivy hung from the wall.", "We followed the trail through the forest."),
 ("keyhole", "keyhole", "n.", "KEY-hole", "/ˈkiːhoʊl/", "열쇠 구멍", "look through the keyhole · fit the keyhole", "He peeked through the keyhole.", "The key didn't fit the keyhole."),
], quiz=[
 ("Mary had never been trained to ask permission or ___ her elders about things.", "consult", ["insult", "result", "convert"]),
 ("Living in a house with a hundred ___ closed rooms set Mary's brain to work.", "mysteriously", ["miserably", "marvelously", "mischievously"]),
 ("The ivy was the ___ thing: Mary could see nothing but thick green leaves.", "baffling", ["babbling", "bubbling", "bustling"]),
 ("Something of her old ___ came back to Mary as she paced the walk.", "contrariness", ["contrast", "carelessness", "correctness"]),
 ("Martha brought out the skipping-rope from under her apron and ___ it proudly.", "exhibited", ["inhibited", "inhabited", "exhaled"]),
 ("The old portraits seemed to wonder what this cottager had the ___ to be doing there.", "impudence", ["prudence", "imprudence", "impotence"]),
 ("Nothing in the world is quite as ___ lovely as a robin when he shows off.", "adorably", ["arguably", "agreeably", "adorable"]),
 ("A gust of wind swayed the trailing sprays of ___ ivy hanging from the wall.", "untrimmed", ["untried", "untamed", "untied"]),
 ("The wind swung aside some loose ivy ___, and Mary saw a round knob.", "trails", ["trials", "tails", "trays"]),
 ("Mary drew the key from her pocket and found it fitted the ___.", "keyhole", ["keyboard", "keystone", "pothole"]),
], discussion=[
 "Mary skips 100 times with her new rope and feels proud. What simple activity gave you that feeling as a child?",
 "Mary decides not to ask anyone before opening the door. Is it ever right to keep a secret from adults? When?",
]),
9: dict(vocab=[
 ("leafless", "leafless", "adj.", "LEAF-less", "/ˈliːfləs/", "잎이 없는", "leafless trees · leafless branches", "In winter the trees are leafless.", "Birds sat on the leafless branches."),
 ("matted", "matted", "adj.", "MAT-ted", "/ˈmætɪd/", "엉킨, 뒤엉킨", "matted hair · matted together", "The dog's fur was matted and dirty.", "The roots were matted together."),
 ("tendril", "tendrils", "n.", "TEN-dril", "/ˈtendrəl/", "덩굴손; 곱슬한 머리카락", "tendrils of ivy · curly tendrils", "Tendrils of ivy climbed the wall.", "A tendril of hair fell over her eyes."),
 ("mantle", "mantle", "n.", "MAN-tle", "/ˈmæntl/", "망토; 덮개, 덮인 것", "a mantle of snow · take on the mantle", "The hills lay under a mantle of snow.", "She took on the mantle of leadership."),
 ("fastening", "fastenings", "n.", "FAS-ten-ing", "/ˈfæsənɪŋ/", "고정 장치, 잠금 장치", "door fastenings · come loose from its fastenings", "The sign fell from its fastenings.", "Check the fastenings on your bag."),
 ("smother", "smothering", "v.", "SMOTH-er", "/ˈsmʌðər/", "숨 막히게 하다, 뒤덮다", "smothered by weeds · smother a fire", "Weeds were smothering the young plants.", "He smothered the fire with a blanket."),
 ("weed", "weeded", "v./n.", "WEED", "/wiːd/", "잡초를 뽑다; 잡초", "weed the garden · pull weeds", "We weeded the garden all afternoon.", "The path was full of weeds."),
 ("ponder", "pondered", "v.", "PON-der", "/ˈpɑːndər/", "곰곰이 생각하다", "ponder a question · ponder over", "She pondered the offer for days.", "He pondered what to say."),
 ("dictate", "dictated", "v.", "DIC-tate", "/ˈdɪkteɪt/", "받아쓰게 하다; 지시하다", "dictate a letter · dictate terms", "The boss dictated a letter to his assistant.", "You can't dictate what I wear."),
 ("envelope", "envelope", "n.", "EN-ve-lope", "/ˈenvəloʊp/", "봉투", "seal an envelope · a stamped envelope", "She put the card in an envelope.", "Write the address on the envelope."),
], quiz=[
 ("The high walls were covered with the ___ stems of climbing roses.", "leafless", ["lawless", "lifeless", "listless"]),
 ("The rose stems were so thick that they were ___ together.", "matted", ["mated", "mattered", "melted"]),
 ("Climbing roses had swung down long ___ which made light swaying curtains.", "tendrils", ["tendons", "tunnels", "trends"]),
 ("The gray and brown branches looked like a sort of hazy ___ spreading over everything.", "mantle", ["mental", "mantra", "metal"]),
 ("Some branches had fallen from their ___ and run along the ground.", "fastenings", ["fashions", "feelings", "foundations"]),
 ("Grass and weeds had been ___ the tiny pale green points.", "smothering", ["mothering", "smoothing", "slithering"]),
 ("Mary dug and ___ out the grass until she made little clear places around the green points.", "weeded", ["wedded", "needed", "weighed"]),
 ("When Martha asked why she wanted a spade, Mary looked at the fire and ___ a little.", "pondered", ["pounded", "powdered", "plundered"]),
 ("Martha ___ a letter to Dickon, and Mary printed it.", "dictated", ["dedicated", "predicted", "delicated"]),
 ("Martha said they would put the money in the ___ and send it with the butcher boy.", "envelope", ["develop", "antelope", "enclosure"]),
], discussion=[
 "Mary calls the garden her \"secret kingdom.\" Did you have a secret place as a child? What made it special?",
 "Mary asks for garden tools and seeds instead of toys. Why do you think working in the garden makes her happier than toys?",
]),
10: dict(vocab=[
 ("sprout", "sprouting", "v.", "SPROUT", "/spraʊt/", "싹이 트다", "sprout from · begin to sprout", "The seeds started sprouting after a week.", "New leaves are sprouting on the tree."),
 ("flattered", "flattered", "adj.", "FLAT-tered", "/ˈflætərd/", "(칭찬·관심에) 우쭐한, 기분 좋은", "feel flattered · be flattered by", "I was flattered by her invitation.", "He felt flattered that she remembered him."),
 ("engagingly", "engagingly", "adv.", "en-GAG-ing-ly", "/ɪnˈɡeɪdʒɪŋli/", "애교 있게, 매력적으로", "smile engagingly · talk engagingly", "The child smiled engagingly at the guests.", "She writes engagingly about her travels."),
 ("scowl", "scowled", "v.", "SCOWL", "/skaʊl/", "얼굴을 찌푸리다", "scowl at · scowl angrily", "He scowled at the noisy children.", "She scowled when she saw the bill."),
 ("crossness", "crossness", "n.", "CROSS-ness", "/ˈkrɔːsnəs/", "짜증, 언짢음", "in spite of his crossness", "Her crossness disappeared after lunch.", "I forgave his crossness because he was tired."),
 ("pheasant", "pheasant", "n.", "PHEAS-ant", "/ˈfezənt/", "꿩", "a cock pheasant · pheasant feathers", "A pheasant ran across the field.", "The hat had a pheasant feather in it."),
 ("stoop", "stooped", "v.", "STOOP", "/stuːp/", "몸을 굽히다", "stoop down · stoop to pick up", "She stooped to pick up a coin.", "He had to stoop to get through the door."),
 ("sidle", "sidled", "v.", "SI-dle", "/ˈsaɪdl/", "옆걸음질하다, 슬그머니 다가가다", "sidle up to · sidle away", "The cat sidled up to me for food.", "He sidled toward the door."),
 ("good-humoredly", "good-humoredly", "adv.", "good-HU-mored-ly", "/ˌɡʊdˈhjuːmərdli/", "기분 좋게, 너그럽게", "laugh good-humoredly · answer good-humoredly", "He took the joke good-humoredly.", "She answered good-humoredly."),
 ("defiantly", "defiantly", "adv.", "de-FI-ant-ly", "/dɪˈfaɪəntli/", "반항적으로, 도전적으로", "say defiantly · stare defiantly", "\"I won't go,\" she said defiantly.", "He stared defiantly at the teacher."),
], quiz=[
 ("Mary found many more of the ___ pale green points than she had hoped.", "sprouting", ["spouting", "spotting", "shouting"]),
 ("Perhaps Ben was secretly rather ___ by Mary's wish for his company.", "flattered", ["flattened", "fluttered", "battered"]),
 ("The robin hopped closer and looked at Ben Weatherstaff more and more ___.", "engagingly", ["enormously", "endlessly", "enviously"]),
 ("Ben dragged out another weed and ___ at it: \"That were as much as ten year' ago.\"", "scowled", ["scolded", "scored", "howled"]),
 ("Mary liked old Ben Weatherstaff in spite of his ___.", "crossness", ["crossing", "closeness", "coarseness"]),
 ("From behind a bush, a cock ___ stretched his neck to peep at Dickon.", "pheasant", ["peasant", "pleasant", "pageant"]),
 ("Dickon ___ to pick up the garden tools lying beside him.", "stooped", ["stopped", "stomped", "swooped"]),
 ("The robin ___ and twittered and tilted as he hopped on his bush.", "sidled", ["sizzled", "saddled", "settled"]),
 ("Dickon looked puzzled, but he answered quite ___: \"I'm keepin' secrets all th' time.\"", "good-humoredly", ["bad-temperedly", "half-heartedly", "hot-headedly"]),
 ("Inside the garden, Mary waved her hand round ___: \"It's a secret garden.\"", "defiantly", ["definitely", "deftly", "delightedly"]),
], discussion=[
 "Dickon can charm animals and people. What makes someone easy to trust? Do you know anyone like Dickon?",
 "Mary is afraid Dickon will tell her secret, and she gets fierce. Why is the garden so important to her?",
]),
11: dict(vocab=[
 ("lichen", "lichen", "n.", "LI-chen", "/ˈlaɪkən/", "이끼(지의류)", "covered in lichen · gray lichen", "The old stones were covered in lichen.", "Lichen grows on trees in clean air."),
 ("thrive", "thrived", "v.", "THRIVE", "/θraɪv/", "잘 자라다, 번성하다", "thrive on · plants thrive", "These plants thrive in the sun.", "She thrives on hard work."),
 ("lifeless", "lifeless", "adj.", "LIFE-less", "/ˈlaɪfləs/", "생명이 없는, 죽은 듯한", "lifeless body · lifeless eyes", "The branch looked lifeless.", "The town was lifeless on Sunday."),
 ("unpromising", "unpromising", "adj.", "un-PROM-is-ing", "/ʌnˈprɑːmɪsɪŋ/", "가망 없어 보이는", "an unpromising start · look unpromising", "The project had an unpromising start.", "The weather looked unpromising."),
 ("industriously", "industriously", "adv.", "in-DUS-tri-ous-ly", "/ɪnˈdʌstriəsli/", "부지런히", "work industriously", "The ants worked industriously all day.", "She studied industriously for the exam."),
 ("clearing", "clearings", "n.", "CLEAR-ing", "/ˈklɪrɪŋ/", "(숲 등의) 빈터, 치운 자리", "a clearing in the woods", "We had a picnic in a clearing.", "Deer came out into the clearing."),
 ("wonderingly", "wonderingly", "adv.", "WON-der-ing-ly", "/ˈwʌndərɪŋli/", "신기한 듯이, 놀라워하며", "gaze wonderingly · ask wonderingly", "The child gazed wonderingly at the stars.", "\"Is it real?\" she asked wonderingly."),
 ("spiteful", "spiteful", "adj.", "SPITE-ful", "/ˈspaɪtfəl/", "앙심을 품은, 심술궂은", "a spiteful remark · spiteful gossip", "That was a spiteful thing to say.", "She gave a spiteful laugh."),
 ("stifle", "stifle", "v.", "STI-fle", "/ˈstaɪfl/", "(웃음·하품을) 참다, 억누르다", "stifle a laugh · stifle a yawn", "I tried to stifle a yawn.", "He stifled a laugh during the speech."),
 ("encouragingly", "encouragingly", "adv.", "en-COUR-ag-ing-ly", "/ɪnˈkɜːrɪdʒɪŋli/", "격려하듯이", "smile encouragingly · nod encouragingly", "The teacher nodded encouragingly.", "She smiled encouragingly at the nervous boy."),
], quiz=[
 ("Dickon stepped over to an old tree with gray ___ all over its bark.", "lichen", ["kitchen", "linen", "lantern"]),
 ("Dickon said the strongest rose bushes had fair ___ on being left wild.", "thrived", ["thrown", "thirsted", "thrilled"]),
 ("Dickon knelt and cut through a ___-looking branch to show it was still alive.", "lifeless", ["lifelong", "lifelike", "leafy"]),
 ("Dickon could tell when an ___ bough still had green life in it.", "unpromising", ["unpronounced", "uncompromising", "unpredictable"]),
 ("Mary and Dickon were working ___ round a big rose when he saw something.", "industriously", ["industrially", "indirectly", "indifferently"]),
 ("Dickon was surprised to see one of Mary's own little ___ round the green points.", "clearings", ["clippings", "cleanings", "clothings"]),
 ("\"Do you never catch cold?\" asked Mary, gazing at him ___.", "wonderingly", ["wanderingly", "wrongly", "worriedly"]),
 ("Remembering the rhyme, Mary gave her trowel a rather ___ dig into the earth.", "spiteful", ["spoonful", "splendid", "spacious"]),
 ("Dickon laughed so hard he had to ___ the sound with his arm over his mouth.", "stifle", ["stiffen", "shuffle", "stumble"]),
 ("His cheeks were full of bread and bacon, but he managed to smile ___.", "encouragingly", ["courageously", "enormously", "embarrassingly"]),
], discussion=[
 "Dickon shows Mary that the \"dead-looking\" roses are still \"wick.\" Can a person who seems cold also be \"wick\" inside? Think of Mary.",
 "Mary asks Dickon, \"Do you like me?\" Why is this question so important for her?",
]),
12: dict(vocab=[
 ("ruffled", "ruffled", "adj.", "RUF-fled", "/ˈrʌfld/", "(머리가) 헝클어진; 동요한", "ruffled hair · ruffled feathers", "Her hair was ruffled by the wind.", "He looked a little ruffled by the question."),
 ("beam", "beamed", "v.", "BEAM", "/biːm/", "환하게 웃다; 빛나다", "beam with pride · beam at someone", "She beamed with pride at her son.", "The sun beamed down on us."),
 ("hesitate", "hesitating", "v.", "HES-i-tate", "/ˈhezɪteɪt/", "망설이다", "hesitate to · without hesitating", "Don't hesitate to ask.", "He answered without hesitating."),
 ("absent-mindedly", "absent-mindedly", "adv.", "ab-sent-MIND-ed-ly", "/ˌæbsəntˈmaɪndɪdli/", "멍하니, 딴생각하며", "nod absent-mindedly · say absent-mindedly", "He absent-mindedly put salt in his coffee.", "She nodded absent-mindedly."),
 ("fret", "fretted", "v.", "FRET", "/fret/", "애태우다, 초조하게 하다", "fret about · fret over", "Don't fret about the test.", "The noise fretted him all night."),
 ("tremulously", "tremulously", "adv.", "TREM-u-lous-ly", "/ˈtremjələsli/", "떨리는 목소리로, 떨며", "say tremulously · smile tremulously", "\"Will you come back?\" she asked tremulously.", "He smiled tremulously."),
 ("quaver", "quavered", "v.", "QUA-ver", "/ˈkweɪvər/", "(목소리가) 떨리다, 떨며 말하다", "a quavering voice · quaver with fear", "\"Is anyone there?\" he quavered.", "Her voice quavered with emotion."),
 ("liberty", "liberty", "n.", "LIB-er-ty", "/ˈlɪbərti/", "자유", "liberty and freedom · at liberty to", "Children need some liberty to play.", "You're at liberty to leave."),
 ("romp", "romping", "v./n.", "ROMP", "/rɑːmp/", "뛰놀다", "romp around · romp in the snow", "The kids were romping in the garden.", "The dogs romped on the beach."),
 ("woefully", "woefully", "adv.", "WOE-ful-ly", "/ˈwoʊfəli/", "슬프게; 한심할 만큼", "say woefully · woefully inadequate", "\"It's gone,\" he said woefully.", "The plan was woefully unprepared."),
], quiz=[
 ("Mary ran home so fast that her hair was ___ on her forehead and her cheeks were pink.", "ruffled", ["rippled", "rumbled", "rattled"]),
 ("When Mary praised Dickon's blue eyes, Martha ___ with satisfaction.", "beamed", ["boomed", "blamed", "bent"]),
 ("\"I haven't asked anybody yet,\" said Mary, ___.", "hesitating", ["heating", "hastening", "heaving"]),
 ("Mr. Craven looked as if the sight of Mary worried and ___ him.", "fretted", ["fitted", "freed", "fronted"]),
 ("\"That was what the Sowerby woman said,\" Mr. Craven muttered ___.", "absent-mindedly", ["single-mindedly", "open-mindedly", "narrow-mindedly"]),
 ("\"May I?\" Mary said ___, afraid he would see the lump in her throat.", "tremulously", ["tremendously", "tirelessly", "tunefully"]),
 ("\"Might I,\" ___ Mary, \"might I have a bit of earth?\"", "quavered", ["quarreled", "covered", "quartered"]),
 ("Mr. Craven said Mary needed ___ and fresh air and romping about.", "liberty", ["library", "loyalty", "luxury"]),
 ("Mr. Craven said the child needed fresh air and ___ about outside.", "romping", ["ramping", "rumbling", "rotting"]),
 ("Back in the garden, Mary found it empty and said ___, \"He's gone.\"", "woefully", ["wilfully", "wonderfully", "watchfully"]),
], discussion=[
 "Mary asks her uncle for \"a bit of earth\" instead of toys. If you could ask for one thing that would make your life better, what would it be?",
 "Mr. Craven seems sad and distant, but he gives Mary freedom. What do you think of him as a guardian?",
]),
13: dict(vocab=[
 ("rebellious", "rebellious", "adj.", "re-BEL-lious", "/rɪˈbeljəs/", "반항적인", "a rebellious teenager · rebellious mood", "He was rebellious as a teenager.", "She was in a rebellious mood today."),
 ("glimmer", "glimmer", "n./v.", "GLIM-mer", "/ˈɡlɪmər/", "희미한 빛; 깜빡이다", "a glimmer of light · a glimmer of hope", "We saw a glimmer of light under the door.", "There's still a glimmer of hope."),
 ("ancient", "ancient", "adj.", "AN-cient", "/ˈeɪnʃənt/", "아주 오래된, 고대의", "ancient furniture · ancient history", "The castle has ancient walls.", "We studied ancient Rome."),
 ("indifferently", "indifferently", "adv.", "in-DIF-fer-ent-ly", "/ɪnˈdɪfrəntli/", "무관심하게", "shrug indifferently · answer indifferently", "\"I don't care,\" he said indifferently.", "She looked at the menu indifferently."),
 ("coolly", "coolly", "adv.", "COOL-ly", "/ˈkuːlli/", "냉정하게, 태연하게", "reply coolly · coolly calm", "She coolly answered the hard question.", "He coolly walked past the guards."),
 ("persistently", "persistently", "adv.", "per-SIST-ent-ly", "/pərˈsɪstəntli/", "끈질기게, 집요하게", "ask persistently · persistently high", "He persistently asked for more money.", "The phone rang persistently."),
 ("clamber", "clambered", "v.", "CLAM-ber", "/ˈklæmbər/", "(기어) 오르다", "clamber over · clamber up", "The kids clambered over the rocks.", "Ivy clambered up the wall."),
 ("complainingly", "complainingly", "adv.", "com-PLAIN-ing-ly", "/kəmˈpleɪnɪŋli/", "불평하듯이", "say complainingly · whine complainingly", "\"It's too hot,\" he said complainingly.", "She spoke complainingly about her job."),
 ("grumble", "grumbled", "v.", "GRUM-ble", "/ˈɡrʌmbl/", "투덜거리다", "grumble about · grumble at", "He grumbled about the long wait.", "\"Fine,\" she grumbled."),
 ("chant", "chanting", "v./n.", "CHANT", "/tʃænt/", "단조로운 노래(를 부르다), 구호", "chant a song · a low chant", "The crowd was chanting his name.", "Monks were chanting in the temple."),
], quiz=[
 ("Perhaps her ___ mood made Mary bold enough to follow the crying.", "rebellious", ["religious", "rebuilding", "ridiculous"]),
 ("Mary could see a ___ of light coming from beneath the door.", "glimmer", ["glamour", "grimmer", "hammer"]),
 ("It was a big room with ___, handsome furniture in it.", "ancient", ["anxious", "agent", "accent"]),
 ("\"Everyone is obliged to do what pleases me,\" Colin said ___.", "indifferently", ["independently", "indignantly", "ingeniously"]),
 ("Mary was amazed at how ___ Colin spoke about not living.", "coolly", ["cozily", "cruelly", "cheaply"]),
 ("\"I do,\" Colin went on ___. \"I want to see that garden.\"", "persistently", ["presently", "patiently", "pleasantly"]),
 ("Mary told Colin the roses might have ___ from tree to tree.", "clambered", ["clamored", "climaxed", "cluttered"]),
 ("\"She is my mother,\" said Colin ___. \"I don't see why she died.\"", "complainingly", ["compellingly", "convincingly", "confidingly"]),
 ("\"If she had lived I believe I should not have been ill always,\" he ___.", "grumbled", ["gambled", "grabbed", "grinned"]),
 ("Mary stroked Colin's hand and sang a very low little ___ song in Hindustani.", "chanting", ["charming", "changing", "chatting"]),
], discussion=[
 "Colin says, \"Everyone is obliged to do what pleases me.\" How is Colin like the old Mary? How is he different?",
 "Colin keeps a curtain over his mother's picture. Why do you think he does that?",
]),
14: dict(vocab=[
 ("rouse", "roused", "v.", "ROUSE", "/raʊz/", "깨우다; 불러일으키다", "rouse someone from sleep · rouse anger", "The noise roused the whole house.", "His speech roused the crowd."),
 ("agitated", "agitated", "adj.", "AG-i-tat-ed", "/ˈædʒɪteɪtɪd/", "불안해하는, 동요한", "become agitated · look agitated", "She became agitated when she lost her bag.", "He paced up and down, agitated."),
 ("raging", "raging", "n./adj.", "RAG-ing", "/ˈreɪdʒɪŋ/", "격노; 맹렬한", "a raging storm · raging anger", "A raging storm hit the coast.", "There was shouting and raging in the house."),
 ("downright", "downright", "adv./adj.", "DOWN-right", "/ˈdaʊnraɪt/", "완전히, 정말로", "downright rude · downright dangerous", "That was downright rude.", "The road is downright dangerous at night."),
 ("brocaded", "brocaded", "adj.", "bro-CAD-ed", "/broʊˈkeɪdɪd/", "무늬를 넣어 짠 (비단)", "a brocaded cushion · brocaded silk", "She sat on a brocaded sofa.", "The queen wore a brocaded gown."),
 ("superb", "superb", "adj.", "su-PERB", "/suːˈpɜːrb/", "최고의, 훌륭한", "a superb view · superb quality", "The food was superb.", "She gave a superb performance."),
 ("hideous", "hideous", "adj.", "HID-e-ous", "/ˈhɪdiəs/", "흉측한, 끔찍한", "a hideous building · hideous noise", "That sweater is hideous!", "The monster had a hideous face."),
 ("resentful", "resentful", "adj.", "re-SENT-ful", "/rɪˈzentfəl/", "분해하는, 억울해하는", "feel resentful · resentful of", "He felt resentful about the unfair rule.", "She was resentful of her sister's success."),
 ("boast", "boasted", "v.", "BOAST", "/boʊst/", "자랑하다, 뽐내다", "boast about · boast of", "He boasted about his new car.", "She never boasts about her success."),
 ("unloving", "unloving", "adj.", "un-LOV-ing", "/ʌnˈlʌvɪŋ/", "애정이 없는, 차가운", "an unloving parent · cold and unloving", "She grew up in an unloving home.", "He seemed cold and unloving."),
], quiz=[
 ("Martha said that normally Colin would have thrown a tantrum and ___ the whole house.", "roused", ["roasted", "rounded", "refused"]),
 ("\"I don't know what to do!\" cried ___ Martha.", "agitated", ["agile", "aggravated", "activated"]),
 ("Martha's mother said there was enough trouble and ___ in the house to set any child wrong.", "raging", ["ranging", "racing", "ragging"]),
 ("Colin fretted so much about wearing a brace that he became ___ ill.", "downright", ["downhill", "upright", "daylight"]),
 ("Colin sat in a velvet dressing-gown against a big ___ cushion.", "brocaded", ["barricaded", "bracketed", "broadcasted"]),
 ("Colin's book had ___ colored illustrations, including a snake-charmer.", "superb", ["suburb", "superior", "proverb"]),
 ("Mary said she had driven over the moor in the dark and thought it was ___.", "hideous", ["hidden", "tedious", "hilarious"]),
 ("\"I couldn't go on the moor,\" Colin said in a ___ tone.", "resentful", ["restful", "respectful", "resourceful"]),
 ("Mary felt as if Colin almost ___ about dying.", "boasted", ["boosted", "bloated", "toasted"]),
 ("Soon they were laughing like ordinary children, not a hard, ___ girl and a sickly boy.", "unloving", ["unlovely", "unmoving", "unlucky"]),
], discussion=[
 "Mary tells Colin about Dickon and the moor, and Colin forgets to talk about dying. Why does talking about nature help him?",
 "Colin and Mary laugh together for the first time. Can laughter change how we feel about our problems?",
]),
}

OLD = {
 "howsoever": ("부사", "(옛) 아무리 ~해도 (= however)", "\"Howsoever carefully she looked\" = however carefully she looked."),
}
OLD_MARKS = {8: ["Howsoever"]}

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
