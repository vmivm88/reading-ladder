# Anne of Green Gables workbook, chapters 25–32. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
25: dict(vocab=[
 ("animated", "animated", "adj.", "AN-i-mat-ed", "/ˈænɪmeɪtɪd/", "활기찬, 생기 있는; 만화 영화의", "an animated discussion · animated film", "We had an animated discussion about the movie.", "Her face became animated when she talked about music."),
 ("inscrutable", "inscrutable", "adj.", "in-SCRU-ta-ble", "/ɪnˈskruːtəbl/", "헤아릴 수 없는, 수수께끼 같은", "an inscrutable smile · inscrutable reasons", "The cat gave me an inscrutable look.", "For some inscrutable reason, he quit the team."),
 ("recourse", "recourse", "n.", "RE-course", "/ˈriːkɔːrs/", "의지(하는 것), 의존", "have recourse to · without recourse to", "When he couldn't sleep, he had recourse to warm milk.", "We solved it without recourse to violence."),
 ("ingratiatingly", "ingratiatingly", "adv.", "in-GRA-ti-at-ing-ly", "/ɪnˈɡreɪʃieɪtɪŋli/", "환심을 사려는 듯이", "smile ingratiatingly · speak ingratiatingly", "The salesman smiled ingratiatingly.", "She spoke ingratiatingly to the boss."),
 ("harassed", "harassed", "adj.", "ha-RASSED", "/həˈræst/", "몹시 시달린, 지친", "a harassed mother · look harassed", "A harassed waiter ran between the tables.", "She looked tired and harassed after work."),
 ("humility", "humility", "n.", "hu-MIL-i-ty", "/hjuːˈmɪləti/", "겸손", "with humility · a lesson in humility", "He accepted the prize with humility.", "Losing taught her humility."),
 ("diplomatic", "diplomatic", "adj.", "dip-lo-MAT-ic", "/ˌdɪpləˈmætɪk/", "외교적인; 요령 있는", "a diplomatic answer · diplomatic relations", "She gave a diplomatic answer to avoid a fight.", "The two countries have diplomatic relations."),
 ("tolerantly", "tolerantly", "adv.", "TOL-er-ant-ly", "/ˈtɑːlərəntli/", "너그럽게, 참아 주며", "smile tolerantly · listen tolerantly", "The teacher smiled tolerantly at the noisy kids.", "He listened tolerantly to her long story."),
 ("extravagance", "extravagance", "n.", "ex-TRAV-a-gance", "/ɪkˈstrævəɡəns/", "낭비, 사치", "sheer extravagance · a little extravagance", "Buying a second car would be sheer extravagance.", "Flowers every week are my one extravagance."),
 ("feign", "feigned", "v.", "FEIGN", "/feɪn/", "~인 척하다", "feign illness · feign interest", "He feigned illness to stay home.", "She feigned interest in his stamp collection."),
], quiz=[
 ("Anne stood among the other girls, bright-eyed and ___ as they were.", "animated", ["animal", "anxious", "annoyed"]),
 ("Matthew thought Marilla must have some wise, ___ reason for dressing Anne so plainly.", "inscrutable", ["incredible", "indestructible", "invisible"]),
 ("Matthew had ___ to his pipe that evening to help him think it out, much to Marilla's disgust.", "recourse", ["resource", "remorse", "discourse"]),
 ("\"What can I do for you this evening, Mr. Cuthbert?\" Miss Harris asked briskly and ___.", "ingratiatingly", ["indignantly", "ignorantly", "impatiently"]),
 ("Mrs. Lynde promptly took the matter out of the ___ man's hands.", "harassed", ["harvested", "hardened", "harnessed"]),
 ("Mrs. Lynde thought Marilla was trying to teach Anne ___ by dressing her so plainly.", "humility", ["humanity", "humidity", "hostility"]),
 ("Marilla did not quite trust Mrs. Lynde's ___ explanation of why she had made the dress.", "diplomatic", ["dramatic", "democratic", "domestic"]),
 ("\"So this is what Matthew has been grinning about,\" Marilla said, a little stiffly but ___.", "tolerantly", ["tenderly", "tirelessly", "terribly"]),
 ("Marilla said Anne had three good dresses already, so anything more was sheer ___.", "extravagance", ["elegance", "relevance", "ignorance"]),
 ("Marilla ___ to be busy filling the teapot, but she watched the scene out of the corner of her eye.", "feigned", ["feared", "failed", "fainted"]),
], discussion=[
 "Matthew was too shy to buy a dress, so he came home with garden rakes and hayseed instead! Have you ever been too nervous to ask for what you really wanted?",
 "Mrs. Lynde says plain clothes are more likely to make Anne feel envy than humility. Do you agree? Do clothes change how children feel about themselves?",
]),
26: dict(vocab=[
 ("humdrum", "humdrum", "adj.", "HUM-drum", "/ˈhʌmdrʌm/", "단조로운, 평범한", "a humdrum life · humdrum routine", "I needed a holiday from my humdrum routine.", "It was just another humdrum day at the office."),
 ("novelty", "novelty", "n.", "NOV-el-ty", "/ˈnɑːvəlti/", "새로움, 신기함", "the novelty wears off · a novelty item", "The novelty of the new phone soon wore off.", "Snow is a novelty for people from hot countries."),
 ("complacent", "complacent", "adj.", "com-PLA-cent", "/kəmˈpleɪsənt/", "자기만족에 빠진, 안주하는", "become complacent · a complacent smile", "Don't get complacent just because you won once.", "He gave a complacent smile."),
 ("dubiously", "dubiously", "adv.", "DU-bi-ous-ly", "/ˈduːbiəsli/", "미심쩍은 듯이", "look dubiously · say dubiously", "She looked dubiously at the strange-colored soup.", "\"Are you sure?\" he asked dubiously."),
 ("masterpiece", "masterpiece", "n.", "MAS-ter-piece", "/ˈmæstərpiːs/", "걸작", "a true masterpiece · a literary masterpiece", "The Mona Lisa is a masterpiece.", "This cake is my masterpiece!"),
 ("turbulent", "turbulent", "adj.", "TUR-bu-lent", "/ˈtɜːrbjələnt/", "거센, 격동의", "turbulent water · a turbulent time", "The boat crossed the turbulent river.", "The 1960s were a turbulent time."),
 ("retribution", "retribution", "n.", "ret-ri-BU-tion", "/ˌretrɪˈbjuːʃən/", "응징, (마땅한) 벌", "divine retribution · fear retribution", "The villain finally faced retribution.", "Witnesses were afraid of retribution."),
 ("sentimental", "sentimental", "adj.", "sen-ti-MEN-tal", "/ˌsentɪˈmentl/", "감상적인", "sentimental value · get sentimental", "This old ring has great sentimental value.", "He gets sentimental when he hears that song."),
 ("scoff", "scoffed", "v.", "SCOFF", "/skɑːf/", "비웃다, 코웃음 치다", "scoff at · scoff at the idea", "People scoffed at his idea at first.", "\"You? A singer?\" she scoffed."),
 ("mischievous", "mischievous", "adj.", "MIS-chie-vous", "/ˈmɪstʃɪvəs/", "장난기 많은, 짓궂은", "a mischievous smile · mischievous kids", "He gave me a mischievous smile.", "The mischievous puppy chewed my shoes."),
], quiz=[
 ("After the concert, Avonlea found it hard to settle down to a ___ life again.", "humdrum", ["humble", "humid", "hundred"]),
 ("Anne told Diana that being thirteen was still such a ___ to her.", "novelty", ["novel", "royalty", "penalty"]),
 ("Anne tried hard not to look virtuously ___ about her finished composition, and failed.", "complacent", ["compliant", "complicated", "competent"]),
 ("\"I never saw anybody with purple eyes,\" said Diana ___.", "dubiously", ["deliciously", "deviously", "dutifully"]),
 ("Anne rewrote Geraldine's long speech five times and called it her ___.", "masterpiece", ["masterplan", "mouthpiece", "centerpiece"]),
 ("Cordelia pushed Geraldine off a bridge into a rushing, ___ stream.", "turbulent", ["truculent", "tolerant", "transparent"]),
 ("Cordelia went mad with remorse, which Anne thought was a poetic ___ for her crime.", "retribution", ["contribution", "distribution", "attribution"]),
 ("Anne said Ruby Gillis's stories were rather ___, with too much romance in them.", "sentimental", ["sensational", "elemental", "fundamental"]),
 ("\"I think this story-writing business is the foolishest yet,\" ___ Marilla.", "scoffed", ["scuffed", "coughed", "sniffed"]),
 ("Anne felt encouraged to hear that Mrs. Allan had been ___ as a girl.", "mischievous", ["miserable", "marvelous", "nervous"]),
], discussion=[
 "Anne's stories always end with someone dying. Why do you think young writers love dramatic and tragic endings?",
 "Anne feels encouraged when she hears that adults were naughty as children. Does it help you to know that others have made the same mistakes?",
]),
27: dict(vocab=[
 ("subjective", "subjective", "adj.", "sub-JEC-tive", "/səbˈdʒektɪv/", "주관적인", "a subjective opinion · highly subjective", "Taste in music is very subjective.", "That's just your subjective opinion."),
 ("irritated", "irritated", "adj.", "IR-ri-tat-ed", "/ˈɪrɪteɪtɪd/", "짜증 난", "irritated by · get irritated", "I get irritated when people are late.", "She was irritated by the noise."),
 ("tomfoolery", "tomfoolery", "n.", "tom-FOOL-er-y", "/ˌtɑːmˈfuːləri/", "바보짓, 허튼짓", "stop this tomfoolery · silly tomfoolery", "Stop this tomfoolery and do your homework!", "Grandpa had no patience for tomfoolery."),
 ("desirous", "desirous", "adj.", "de-SIR-ous", "/dɪˈzaɪərəs/", "(격식) 몹시 바라는", "desirous of · desirous to", "He was desirous of making a good impression.", "She seemed desirous to leave early."),
 ("mystified", "mystified", "adj.", "MYS-ti-fied", "/ˈmɪstɪfaɪd/", "어리둥절한", "be mystified by · a mystified look", "I was mystified by his strange message.", "She gave me a mystified look."),
 ("scrutinizingly", "scrutinizingly", "adv.", "SCRU-ti-niz-ing-ly", "/ˈskruːtənaɪzɪŋli/", "자세히 살피며", "look scrutinizingly · gaze scrutinizingly", "The officer looked scrutinizingly at my passport.", "She studied the painting scrutinizingly."),
 ("grotesque", "grotesque", "adj.", "gro-TESQUE", "/ɡroʊˈtesk/", "기괴한, 괴상한", "a grotesque mask · grotesque shapes", "The old trees had grotesque shapes in the fog.", "He wore a grotesque mask on Halloween."),
 ("dejectedly", "dejectedly", "adv.", "de-JECT-ed-ly", "/dɪˈdʒektɪdli/", "풀이 죽어, 낙담하여", "sit dejectedly · walk dejectedly", "He sat dejectedly after losing the game.", "\"I failed again,\" she said dejectedly."),
 ("veracity", "veracity", "n.", "ve-RAC-i-ty", "/vəˈræsəti/", "진실성", "question the veracity of · doubt someone's veracity", "Police questioned the veracity of his story.", "No one doubted her veracity."),
 ("implicitly", "implicitly", "adv.", "im-PLIC-it-ly", "/ɪmˈplɪsɪtli/", "절대적으로, 무조건; 암묵적으로", "trust implicitly · believe implicitly", "I trust my sister implicitly.", "The children believed his stories implicitly."),
], quiz=[
 ("Marilla was not given to ___ analysis of her own thoughts and feelings.", "subjective", ["objective", "subtractive", "selective"]),
 ("Finding the fire out and no tea ready, Marilla felt disappointed and ___.", "irritated", ["imitated", "irrigated", "invited"]),
 ("Marilla guessed Anne was off with Diana, practicing dialogues or some such ___.", "tomfoolery", ["foolproof", "jewelry", "tomorrow"]),
 ("Anne hid deeper in her pillows, as if ___ of hiding herself forever.", "desirous", ["disastrous", "delicious", "devious"]),
 ("\"Did anyone ever hear the like?\" the ___ Marilla wanted to know.", "mystified", ["modified", "magnified", "mortified"]),
 ("Marilla lifted her candle and looked ___ at Anne's hair.", "scrutinizingly", ["surprisingly", "sympathizingly", "satisfyingly"]),
 ("Never in her life had Marilla seen anything so ___ as Anne's green hair.", "grotesque", ["gorgeous", "picturesque", "generous"]),
 ("\"But I didn't mean to dye it green, Marilla,\" protested Anne ___.", "dejectedly", ["directly", "delightedly", "defiantly"]),
 ("The peddler said the dye wouldn't wash off, and that was true, whatever his ___ in other matters.", "veracity", ["velocity", "voracity", "vivacity"]),
 ("Anne said she had believed every word the peddler said ___.", "implicitly", ["explicitly", "impolitely", "implausibly"]),
], discussion=[
 "Anne dyed her hair because she believed the peddler. Have you ever bought something because a salesperson promised too much?",
 "Anne says she dyed her hair out of vanity. Do people today worry too much about their looks? What do you think Anne learns from the green hair?",
]),
28: dict(vocab=[
 ("concede", "conceded", "v.", "con-CEDE", "/kənˈsiːd/", "(마지못해) 인정하다", "concede that · concede defeat", "He conceded that he was wrong.", "The team conceded defeat."),
 ("prescribe", "prescribed", "v.", "pre-SCRIBE", "/prɪˈskraɪb/", "처방하다; 규정하다", "prescribe medicine · prescribed by law", "The doctor prescribed some pills.", "The school prescribes three novels each year."),
 ("procure", "procured", "v.", "pro-CURE", "/proʊˈkjʊr/", "(애써) 구하다, 입수하다", "procure supplies · difficult to procure", "We procured tickets for the sold-out show.", "The hospital procured new equipment."),
 ("abominably", "abominably", "adv.", "a-BOM-i-na-bly", "/əˈbɑːmɪnəbli/", "지독하게, 끔찍하게", "behave abominably · abominably rude", "He behaved abominably at the party.", "The service was abominably slow."),
 ("substitute", "substitute", "n./v.", "SUB-sti-tute", "/ˈsʌbstɪtuːt/", "대체물, 대신하는 것; 대신하다", "a substitute for · substitute A for B", "Honey is a good substitute for sugar.", "We had a substitute teacher today."),
 ("frigidly", "frigidly", "adv.", "FRIG-id-ly", "/ˈfrɪdʒɪdli/", "냉랭하게, 쌀쌀맞게", "reply frigidly · smile frigidly", "\"No, thank you,\" she said frigidly.", "He nodded frigidly and walked away."),
 ("obligingly", "obligingly", "adv.", "o-BLIG-ing-ly", "/əˈblaɪdʒɪŋli/", "친절하게, 기꺼이 도와주며", "move obligingly · obligingly agree", "The driver obligingly waited for us.", "She obligingly moved her bag."),
 ("outraged", "outraged", "adj.", "out-RAGED", "/ˈaʊtreɪdʒd/", "격분한", "outraged by · outraged dignity", "Citizens were outraged by the decision.", "He was outraged at the high price."),
 ("grievance", "grievance", "n.", "GRIEV-ance", "/ˈɡriːvəns/", "불만, 원한", "an old grievance · hold a grievance", "She still holds a grievance against her old boss.", "Workers listed their grievances."),
 ("skeptically", "skeptically", "adv.", "SKEP-ti-cal-ly", "/ˈskeptɪkli/", "회의적으로, 의심스럽게", "look skeptically · say skeptically", "He looked skeptically at the cheap watch.", "\"Really?\" she asked skeptically."),
], quiz=[
 ("\"Of course it would be romantic,\" ___ Jane Andrews, \"but I know I couldn't keep still.\"", "conceded", ["conceited", "concealed", "concerned"]),
 ("Tennyson's poem had been ___ for the English course in Prince Edward Island schools.", "prescribed", ["described", "subscribed", "proscribed"]),
 ("Once the old black shawl had been ___, Anne spread it over the flat and lay down.", "procured", ["provoked", "produced", "protected"]),
 ("Ruby worried, because Mrs. Lynde says all play-acting is ___ wicked.", "abominably", ["admirably", "affectionately", "absentmindedly"]),
 ("There was no cloth of gold, but an old yellow piano scarf was an excellent ___.", "substitute", ["institute", "statute", "prostitute"]),
 ("\"We were playing Elaine,\" Anne explained ___, without even looking at her rescuer.", "frigidly", ["frankly", "fearfully", "fondly"]),
 ("Gilbert ___ rowed to the landing, and Anne sprang on shore without his help.", "obligingly", ["obviously", "obliquely", "obnoxiously"]),
 ("Under her ___ dignity, Anne felt that Gilbert's shy, eager look was very good to see.", "outraged", ["outdated", "outlined", "outgrown"]),
 ("But the bitterness of her old ___ made Anne refuse to be friends.", "grievance", ["guidance", "allowance", "grievous"]),
 ("\"I'm sure I hope so,\" said Marilla ___ when Anne promised to be less romantic.", "skeptically", ["sympathetically", "systematically", "specifically"]),
], discussion=[
 "Anne refused Gilbert's friendship, and later she felt she had made a mistake. Have you ever said \"no\" too fast and then regretted it?",
 "Anne says the Elaine adventure has cured her of being too romantic. Is being romantic a bad thing? When is it good?",
]),
29: dict(vocab=[
 ("exult", "exulting", "v.", "ex-ULT", "/ɪɡˈzʌlt/", "크게 기뻐하다, 의기양양해하다", "exult in · exult over", "The fans exulted in their team's victory.", "She exulted over her perfect score."),
 ("merriment", "merriment", "n.", "MER-ri-ment", "/ˈmerimənt/", "흥겨움, 유쾌함", "eyes full of merriment · sounds of merriment", "Her eyes were full of merriment.", "We heard sounds of merriment from the party."),
 ("seclusion", "seclusion", "n.", "se-CLU-sion", "/sɪˈkluːʒən/", "외딴 곳, 은둔", "in seclusion · live in seclusion", "The actor lives in seclusion now.", "The cabin stood in the seclusion of the forest."),
 ("radiantly", "radiantly", "adv.", "RA-di-ant-ly", "/ˈreɪdiəntli/", "환하게, 빛나게", "smile radiantly · radiantly happy", "The bride smiled radiantly.", "She looked radiantly happy."),
 ("magnificence", "magnificence", "n.", "mag-NIF-i-cence", "/mæɡˈnɪfɪsəns/", "웅장함, 화려함", "great magnificence · the magnificence of", "We admired the magnificence of the palace.", "The view had a quiet magnificence."),
 ("insignificant", "insignificant", "adj.", "in-sig-NIF-i-cant", "/ˌɪnsɪɡˈnɪfɪkənt/", "하찮은, 사소한", "feel insignificant · an insignificant amount", "Looking at the stars makes me feel insignificant.", "The difference is insignificant."),
 ("abomination", "abomination", "n.", "a-bom-i-NA-tion", "/əˌbɑːmɪˈneɪʃən/", "혐오스러운 것", "an abomination · regard as an abomination", "That ugly building is an abomination.", "She thinks pineapple pizza is an abomination."),
 ("prosaic", "prosaic", "adj.", "pro-SA-ic", "/proʊˈzeɪɪk/", "평범한, 낭만 없는", "a prosaic explanation · prosaic details", "There was a prosaic reason for the delay: traffic.", "Let's talk about the prosaic details, like money."),
 ("transparent", "transparent", "adj.", "trans-PAR-ent", "/trænsˈpærənt/", "투명한; (감정이) 그대로 드러나는", "transparent glass · transparent emotions", "Her lies were transparent.", "The box is made of transparent plastic."),
 ("appetizing", "appetizing", "adj.", "AP-pe-tiz-ing", "/ˈæpɪtaɪzɪŋ/", "식욕을 돋우는, 맛있어 보이는", "look appetizing · an appetizing smell", "The bread smelled very appetizing.", "The food looked appetizing on the plate."),
], quiz=[
 ("Anne walked behind the cows, reciting a battle poem and ___ in its rushing lines.", "exulting", ["exiting", "existing", "exhausting"]),
 ("Diana shook her head, her black eyes dancing with ___.", "merriment", ["argument", "sentiment", "settlement"]),
 ("Miss Barry's fine old mansion stood back from the street in a ___ of elms and beeches.", "seclusion", ["conclusion", "confusion", "collision"]),
 ("\"Indeed I didn't,\" said Anne ___ when Miss Barry said she was better-looking now.", "radiantly", ["randomly", "rapidly", "rationally"]),
 ("Anne told Marilla that Miss Barry's house was furnished with \"great ___.\"", "magnificence", ["magnitude", "munificence", "significance"]),
 ("There were thousands of people at the Exhibition, and it made Anne feel dreadfully ___.", "insignificant", ["indignant", "insufficient", "intelligent"]),
 ("Mrs. Lynde would not go to the horse races; she said horse racing was an ___.", "abomination", ["abbreviation", "admiration", "accommodation"]),
 ("Going for ice cream sounded so ___ to Anne, but it really did help.", "prosaic", ["poetic", "mosaic", "romantic"]),
 ("Miss Barry thought less about Anne's quaint speeches than about her ___ emotions and winning ways.", "transparent", ["apparent", "transferred", "transient"]),
 ("Marilla cooked a broiled chicken because Anne would need something real ___ after the drive.", "appetizing", ["apologizing", "appreciating", "appealing"]),
], discussion=[
 "After the excitement of town, Anne says the best part was coming home. Do you feel the same after a trip? What do you miss most about home?",
 "Miss Barry lives in a grand house in town, yet she enjoys Anne's visit enormously. Can money buy happiness? Why or why not?",
]),
30: dict(vocab=[
 ("enthralling", "enthralling", "adj.", "en-THRALL-ing", "/ɪnˈθrɔːlɪŋ/", "매혹적인, 마음을 사로잡는", "an enthralling story · find something enthralling", "The book was so enthralling I read it in one night.", "The show was enthralling from start to end."),
 ("tenderness", "tenderness", "n.", "TEN-der-ness", "/ˈtendərnəs/", "다정함, 애정", "with tenderness · show tenderness", "She held the baby with great tenderness.", "There was tenderness in his voice."),
 ("appalling", "appalling", "adj.", "ap-PALL-ing", "/əˈpɔːlɪŋ/", "끔찍한, 기막힌", "appalling conditions · an appalling mistake", "The living conditions were appalling.", "His spelling is appalling."),
 ("deceitful", "deceitful", "adj.", "de-CEIT-ful", "/dɪˈsiːtfəl/", "속이는, 기만적인", "deceitful behavior · a deceitful person", "It was deceitful to hide the truth.", "I don't trust deceitful people."),
 ("diligent", "diligent", "adj.", "DIL-i-gent", "/ˈdɪlɪdʒənt/", "부지런한, 성실한", "a diligent student · diligent work", "She is a diligent worker.", "Diligent practice makes you better."),
 ("calamity", "calamity", "n.", "ca-LAM-i-ty", "/kəˈlæməti/", "재앙, 큰 불행", "a terrible calamity · natural calamity", "The flood was a terrible calamity.", "Missing the train felt like a calamity."),
 ("tacitly", "tacitly", "adv.", "TAC-it-ly", "/ˈtæsɪtli/", "암묵적으로, 말없이", "tacitly agree · tacitly accept", "Everyone tacitly agreed not to talk about it.", "He tacitly accepted the new rules."),
 ("superiority", "superiority", "n.", "su-pe-ri-OR-i-ty", "/suːˌpɪriˈɔːrəti/", "우월(성)", "a sense of superiority · superiority over", "He has an annoying sense of superiority.", "The team showed clear superiority."),
 ("snub", "snubbed", "v.", "SNUB", "/snʌb/", "무시하다, 냉대하다", "snub someone · feel snubbed", "She snubbed me at the party.", "He felt snubbed when no one invited him."),
 ("vitality", "vitality", "n.", "vi-TAL-i-ty", "/vaɪˈtæləti/", "활력, 생명력", "full of vitality · health and vitality", "My grandmother is still full of vitality.", "Exercise gives you vitality."),
], quiz=[
 ("Anne daydreamed of adventures, wonderful and ___, that always ended happily.", "enthralling", ["enrolling", "appalling", "enduring"]),
 ("Marilla looked at Anne with a ___ she would never show in clearer light.", "tenderness", ["tidiness", "toughness", "tiredness"]),
 ("\"It's perfectly ___ to think of being twenty, Marilla,\" said Anne. \"It sounds so old.\"", "appalling", ["appealing", "applauding", "enthralling"]),
 ("Anne had not realized that reading a storybook behind her history book was ___.", "deceitful", ["delightful", "doubtful", "dutiful"]),
 ("Marilla told Anne that Miss Stacy said she was bright and ___.", "diligent", ["delicate", "elegant", "indulgent"]),
 ("Diana was not going to Queen's, which seemed nothing short of a ___ to Anne.", "calamity", ["comedy", "capacity", "celebrity"]),
 ("The rest of the class ___ accepted that Anne and Gilbert were the best and did not compete.", "tacitly", ["tactfully", "tastily", "totally"]),
 ("The others acknowledged Anne's and Gilbert's ___ and never tried to compete with them.", "superiority", ["seniority", "security", "sincerity"]),
 ("Gilbert's only comfort was that Anne ___ Charlie Sloane even more than him.", "snubbed", ["stubbed", "scrubbed", "stunned"]),
 ("Miss Stacy told her class to lay in a good stock of health and ___ for the next year.", "vitality", ["validity", "vanity", "vicinity"]),
], discussion=[
 "Anne and Gilbert are now rivals, and both work hard to be first. Is competition good for learning? Why or why not?",
 "Marilla and Matthew decide to send Anne to the Queen's class so she can become a teacher. How did your family influence your own studies or career?",
]),
31: dict(vocab=[
 ("wholeheartedly", "wholeheartedly", "adv.", "whole-HEART-ed-ly", "/ˌhoʊlˈhɑːrtɪdli/", "진심으로, 전적으로", "agree wholeheartedly · support wholeheartedly", "I wholeheartedly agree with you.", "She threw herself wholeheartedly into the project."),
 ("afford", "afforded", "v.", "af-FORD", "/əˈfɔːrd/", "(여유가) 있다; (격식) 제공하다", "afford to · afford a view", "The window affords a beautiful view of the sea.", "I can't afford a new car."),
 ("scrupulously", "scrupulously", "adv.", "SCRU-pu-lous-ly", "/ˈskruːpjələsli/", "철저하게, 꼼꼼하게", "scrupulously clean · scrupulously honest", "The kitchen was scrupulously clean.", "He followed the rules scrupulously."),
 ("scandalous", "scandalous", "adj.", "SCAN-dal-ous", "/ˈskændələs/", "수치스러운, 충격적인", "a scandalous waste · scandalous behavior", "The price of the tickets is scandalous.", "People called her behavior scandalous."),
 ("irresistibly", "irresistibly", "adv.", "ir-re-SIS-ti-bly", "/ˌɪrɪˈzɪstəbli/", "참을 수 없을 만큼, 저항할 수 없이", "irresistibly drawn · irresistibly funny", "I was irresistibly drawn to the smell of bread.", "The puppy was irresistibly cute."),
 ("perplex", "perplex", "v.", "per-PLEX", "/pərˈpleks/", "당황하게 하다, 어리둥절하게 하다", "perplex someone · be perplexed by", "His strange question perplexed me.", "Scientists are perplexed by the results."),
 ("tactful", "tactful", "adj.", "TACT-ful", "/ˈtæktfəl/", "요령 있는, 눈치 있는", "a tactful reply · be tactful about", "She was tactful about my bad haircut.", "Try to be tactful when you give feedback."),
 ("innovation", "innovations", "n.", "in-no-VA-tion", "/ˌɪnəˈveɪʃən/", "혁신, 새로운 방법", "technological innovation · new innovations", "Smartphones were a huge innovation.", "The company is famous for innovation."),
 ("unbelievingly", "unbelievingly", "adv.", "un-be-LIEV-ing-ly", "/ˌʌnbɪˈliːvɪŋli/", "믿을 수 없다는 듯이", "stare unbelievingly · say unbelievingly", "He stared unbelievingly at the lottery ticket.", "\"You won?\" she asked unbelievingly."),
 ("unconcernedly", "unconcernedly", "adv.", "un-con-CERN-ed-ly", "/ˌʌnkənˈsɜːrnɪdli/", "아무렇지 않게, 태연하게", "say unconcernedly · shrug unconcernedly", "\"Who cares?\" he said unconcernedly.", "She walked past the dog unconcernedly."),
], quiz=[
 ("Anne had her \"good\" summer and enjoyed it ___.", "wholeheartedly", ["halfheartedly", "lightheartedly", "wholesomely"]),
 ("Anne and Diana enjoyed all the delights that Lover's Lane and Willowmere ___.", "afforded", ["afflicted", "affected", "accorded"]),
 ("Marilla feared Anne would get sick unless the doctor's advice was ___ obeyed.", "scrupulously", ["scarcely", "scornfully", "spontaneously"]),
 ("When Anne asked why women can't be ministers, Mrs. Lynde said it would be a ___ thing.", "scandalous", ["scholarly", "fabulous", "ridiculous"]),
 ("With Mrs. Lynde, Anne feels ___ tempted to do the very thing she is told not to do.", "irresistibly", ["irresponsibly", "irreversibly", "irregularly"]),
 ("Anne said new things to worry about keep coming up all the time—things to ___ you.", "perplex", ["perfect", "protect", "reflect"]),
 ("Much of Anne's growth was due to Miss Stacy's ___, careful, broadminded guidance.", "tactful", ["tasteful", "tearful", "thankful"]),
 ("Mrs. Lynde and the school trustees viewed all ___ in teaching methods rather dubiously.", "innovations", ["invitations", "inventions", "renovations"]),
 ("\"Why, Anne, how you've grown!\" Marilla said, almost ___.", "unbelievingly", ["unbearably", "unwillingly", "unknowingly"]),
 ("\"Why, go to school next year and try again,\" said Marilla ___ when Anne worried about failing.", "unconcernedly", ["unconditionally", "unconsciously", "unconvincingly"]),
], discussion=[
 "Anne asks why women can't be ministers, and Mrs. Lynde is shocked. What jobs were closed to women when your grandparents were young? What has changed?",
 "Anne talks much less now and says she likes to keep her thoughts to herself. How did you change between age 12 and 16?",
]),
32: dict(vocab=[
 ("testimony", "testimony", "n.", "TES-ti-mo-ny", "/ˈtestɪmoʊni/", "증언; 증거", "give testimony · testimony to", "Her success is testimony to her hard work.", "The witness gave testimony in court."),
 ("imploringly", "imploringly", "adv.", "im-PLOR-ing-ly", "/ɪmˈplɔːrɪŋli/", "애원하듯이", "look imploringly · say imploringly", "The child looked at me imploringly.", "\"Please help,\" she said imploringly."),
 ("superstitious", "superstitious", "adj.", "su-per-STI-tious", "/ˌsuːpərˈstɪʃəs/", "미신을 믿는", "superstitious about · a superstitious belief", "Some people are superstitious about the number four.", "He's too superstitious to walk under a ladder."),
 ("cram", "crammed", "v.", "CRAM", "/kræm/", "벼락치기 공부하다; 쑤셔 넣다", "cram for an exam · cram into", "I crammed all night for the test.", "We crammed our clothes into one bag."),
 ("distractedly", "distractedly", "adv.", "dis-TRACT-ed-ly", "/dɪˈstræktɪdli/", "정신이 딴 데 팔려, 심란하게", "wander distractedly · answer distractedly", "He nodded distractedly while reading his phone.", "She walked distractedly around the room."),
 ("chastened", "chastened", "adj.", "CHAS-tened", "/ˈtʃeɪsənd/", "(실수·어려움 끝에) 겸손해진, 차분해진", "feel chastened · a chastened mood", "After the defeat, the team looked chastened.", "He returned home, chastened and quiet."),
 ("fervently", "fervently", "adv.", "FER-vent-ly", "/ˈfɜːrvəntli/", "열렬히, 간절히", "hope fervently · pray fervently", "I fervently hope you get the job.", "They prayed fervently for rain."),
 ("unimaginative", "unimaginative", "adj.", "un-i-MAG-i-na-tive", "/ˌʌnɪˈmædʒɪnətɪv/", "상상력이 없는, 재미없는", "an unimaginative design · dull and unimaginative", "The movie's ending was unimaginative.", "He gave an unimaginative answer."),
 ("languish", "languished", "v.", "LAN-guish", "/ˈlæŋɡwɪʃ/", "시들해지다, 약해지다", "languish in · interest languished", "The project languished for years without money.", "Her interest in piano languished."),
 ("presumptuous", "presumptuous", "adj.", "pre-SUMP-tu-ous", "/prɪˈzʌmptʃuəs/", "주제넘은, 건방진", "it is presumptuous to · a presumptuous question", "It would be presumptuous to expect first prize.", "Sorry if this is presumptuous, but can I join you?"),
], quiz=[
 ("Red eyes and damp handkerchiefs bore convincing ___ that Miss Stacy's farewell had been touching.", "testimony", ["ceremony", "harmony", "matrimony"]),
 ("\"If you would stop crying I could,\" said Anne ___ to Diana.", "imploringly", ["imperfectly", "importantly", "impolitely"]),
 ("Anne's exam number was thirteen; she said she was not ___, but she still wished it wasn't thirteen.", "superstitious", ["suspicious", "supernatural", "superficial"]),
 ("Prissy Andrews said she sat up half the night every night and ___ for her exams.", "crammed", ["cramped", "crashed", "cried"]),
 ("Anne met Moody Spurgeon wandering ___ around, sure he had failed history.", "distractedly", ["distinctly", "dramatically", "disgracefully"]),
 ("Anne came home tired but with an air of ___ triumph about her.", "chastened", ["chased", "cheated", "chattered"]),
 ("Anne hoped ___ to be in the first ten, so that Matthew's eyes would shine with pride.", "fervently", ["frequently", "faithfully", "fearfully"]),
 ("Her reward would make up for all her patient work among ___ equations and conjugations.", "unimaginative", ["unimaginable", "unforgettable", "unbelievable"]),
 ("While she waited for the pass list, Anne's appetite failed and her interest in Avonlea ___.", "languished", ["launched", "laughed", "lingered"]),
 ("Anne had once let herself dream of coming first, though it seemed so vain and ___.", "presumptuous", ["presentable", "prosperous", "precious"]),
], discussion=[
 "Anne and Gilbert tie for first place on the whole Island. How do you feel when you share a success with a rival?",
 "Anne wants to do well mostly to make Matthew proud. Who did you want to make proud when you were studying?",
]),
}

OLD = {
 "lovemaking": ("명사", "(옛 의미) 구애, 사랑 고백 (= romantic talk, courting)", "In 1908 \"lovemaking\" meant romantic talk and courting—saying sweet things and proposing. It did NOT mean sex as it does today. Ruby just writes too many romantic scenes."),
 "complected": ("형용사", "(방언) 피부색이 ~한 (= complexioned)", "\"A dark-complected man\" = a man with dark skin and hair. Today we say \"dark-skinned\" or \"dark-haired\"."),
}
IDIOMS = {
 "bounden duty": ("반드시 해야 할 의무", "a strong duty / something you must do", "Still heard in formal English: \"It is my bounden duty to help.\" Today usually just \"my duty\"."),
 "castles in Spain": ("공상, 헛된 꿈", "daydreams / impossible dreams", "Today we say \"castles in the air\": She builds castles in the air about becoming a star."),
 "foeman worthy of her steel": ("호적수, 맞수", "a rival as good as she is", "\"Steel\" means a sword. Today: \"Gilbert was a worthy rival.\""),
 "as of yore": ("예전처럼", "as in the past / as before", "\"Yore\" means long ago. Today: \"as before\" or \"like in the old days\"."),
}
OLD_MARKS = {26: ["lovemaking"], 29: ["complected"]}
IDIOM_MARKS = {29: ["bounden duty"], 30: ["castles in Spain", "foeman worthy of her steel"], 31: ["as of yore"]}

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
