# Anne of Green Gables workbook, chapters 17–24. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
17: dict(vocab=[
 ("beckon", "beckoning", "v.", "BECK-on", "/ˈbekən/", "손짓하여 부르다", "beckon to someone · beckon someone over", "The waiter beckoned us to a table by the window.", "She beckoned me over with one finger."),
 ("relent", "relented", "v.", "re-LENT", "/rɪˈlent/", "(마음이) 누그러지다, 결국 허락하다", "finally relent · refuse to relent", "Mom finally relented and let us have a puppy.", "The rain didn't relent all day."),
 ("tearfully", "tearfully", "adv.", "TEAR-ful-ly", "/ˈtɪrfəli/", "울먹이며", "say tearfully · smile tearfully", "\"I'll miss you,\" she said tearfully.", "He tearfully thanked the doctors."),
 ("devotedly", "devotedly", "adv.", "de-VOT-ed-ly", "/dɪˈvoʊtɪdli/", "헌신적으로, 깊이", "love devotedly · serve devotedly", "She cared for her mother devotedly.", "The dog followed him devotedly."),
 ("console", "consoled", "v.", "con-SOLE", "/kənˈsoʊl/", "위로하다", "console someone · be consoled by", "I tried to console her after the exam.", "He was consoled by his friends' letters."),
 ("ruthlessly", "ruthlessly", "adv.", "RUTH-less-ly", "/ˈruːθləsli/", "무자비하게, 가차 없이", "ruthlessly cut · ruthlessly honest", "The editor ruthlessly cut my long essay.", "The weeds were ruthlessly pulled out."),
 ("smuggle", "smuggled", "v.", "SMUG-gle", "/ˈsmʌɡl/", "몰래 가져가다(주다); 밀수하다", "smuggle something in · smuggle drugs", "We smuggled snacks into the movie theater.", "He was caught smuggling cigarettes."),
 ("ostentatiously", "ostentatiously", "adv.", "os-ten-TA-tious-ly", "/ˌɑːstenˈteɪʃəsli/", "보란 듯이, 과시하듯", "ostentatiously ignore · dress ostentatiously", "She ostentatiously checked her watch while he talked.", "He ostentatiously showed off his new car."),
 ("embitter", "embittered", "v.", "em-BIT-ter", "/ɪmˈbɪtər/", "씁쓸하게 만들다, 기분을 망치다", "embittered by · an embittered man", "Years of failure embittered him.", "The fight embittered the whole holiday."),
 ("tenacity", "tenacity", "n.", "te-NAC-i-ty", "/təˈnæsəti/", "끈질김, 집요함", "with tenacity · great tenacity", "Her tenacity helped her finish the marathon.", "He showed real tenacity in learning Korean."),
], quiz=[
 ("Anne looked out and saw Diana down by the Dryad's Bubble, ___ mysteriously.", "beckoning", ["breaking", "begging", "blinking"]),
 ("\"Your mother hasn't ___?\" Anne gasped when she saw Diana's sad face.", "relented", ["resented", "related", "repeated"]),
 ("\"Ten minutes isn't very long to say an eternal farewell in,\" said Anne ___.", "tearfully", ["tactfully", "thankfully", "tirelessly"]),
 ("\"I love you ___, Anne,\" said Diana, \"and I always will.\"", "devotedly", ["decidedly", "delicately", "distantly"]),
 ("After the romantic parting, Anne went home, quite ___ for the time being.", "consoled", ["concealed", "controlled", "consulted"]),
 ("Anne said school was all she had left now that her friend had been ___ torn from her.", "ruthlessly", ["restlessly", "rightfully", "rarely"]),
 ("On her first day back, Ruby Gillis ___ three blue plums over to Anne during testament reading.", "smuggled", ["snuggled", "struggled", "smothered"]),
 ("When she learned the apple came from the Blythe orchard, Anne dropped it and ___ wiped her fingers.", "ostentatiously", ["obediently", "occasionally", "outrageously"]),
 ("Diana did not smile at her even once, and that ___ Anne's little triumph in spelling.", "embittered", ["embraced", "embodied", "embroidered"]),
 ("Anne had an unpraiseworthy ___ for holding grudges, so she stayed cold to Gilbert.", "tenacity", ["capacity", "vivacity", "audacity"]),
], discussion=[
 "Anne and Diana say goodbye with a lock of hair and words from old stories. Why do you think Anne makes even sad moments so romantic?",
 "Anne refuses an apple just because it came from Gilbert's orchard. Have you ever stayed angry at someone for a long time? What helped you let go?",
]),
18: dict(vocab=[
 ("wistful", "wistful", "adj.", "WIST-ful", "/ˈwɪstfəl/", "아쉬워하는, 그리워하는", "a wistful smile · wistful glances", "She gave a wistful smile as the train left.", "He looked wistful when he talked about his hometown."),
 ("soothingly", "soothingly", "adv.", "SOOTH-ing-ly", "/ˈsuːðɪŋli/", "달래듯이", "speak soothingly · say soothingly", "The nurse spoke soothingly to the child.", "\"It's okay,\" he said soothingly."),
 ("comprehend", "comprehend", "v.", "com-pre-HEND", "/ˌkɑːmprɪˈhend/", "(완전히) 이해하다", "fail to comprehend · hard to comprehend", "I can't comprehend why he left.", "The size of the universe is hard to comprehend."),
 ("sincerely", "sincerely", "adv.", "sin-CERE-ly", "/sɪnˈsɪrli/", "진심으로", "sincerely hope · sincerely apologize", "I sincerely hope you feel better.", "We sincerely apologize for the delay."),
 ("estranged", "estranged", "adj.", "es-TRANGED", "/ɪˈstreɪndʒd/", "사이가 멀어진, 소원해진", "estranged from · an estranged wife", "He has been estranged from his brother for years.", "They met again after being estranged for a decade."),
 ("feverish", "feverish", "adj.", "FE-ver-ish", "/ˈfiːvərɪʃ/", "열이 나는; 몹시 흥분한", "feel feverish · feverish activity", "The baby felt feverish all night.", "There was feverish activity before the wedding."),
 ("incapable", "incapable", "adj.", "in-CA-pa-ble", "/ɪnˈkeɪpəbl/", "~할 수 없는, 무능한", "incapable of · totally incapable", "He is incapable of telling a lie.", "She seemed incapable of sitting still."),
 ("relieve", "relieve", "v.", "re-LIEVE", "/rɪˈliːv/", "(고통·감정을) 덜다, 완화하다", "relieve pain · relieve stress", "This medicine will relieve your headache.", "A walk helps me relieve stress."),
 ("indulgently", "indulgently", "adv.", "in-DUL-gent-ly", "/ɪnˈdʌldʒəntli/", "너그럽게, 오냐오냐하며", "smile indulgently · laugh indulgently", "Grandpa smiled indulgently at the noisy kids.", "She indulgently let him stay up late."),
 ("pledge", "pledged", "v./n.", "PLEDGE", "/pledʒ/", "맹세하다, 약속하다; 서약", "pledge to do · make a pledge", "They pledged to stay friends forever.", "He made a pledge to stop smoking."),
], quiz=[
 ("Anne studied hard, despite many ___ glances at the new book on the clock shelf.", "wistful", ["powerful", "wonderful", "wasteful"]),
 ("When Anne called herself a dunce at geometry, Matthew said ___, \"I guess you're all right at anything.\"", "soothingly", ["suddenly", "sternly", "stubbornly"]),
 ("\"Well now, I dunno as I ___ them all myself,\" Matthew admitted about the world's puzzles.", "comprehend", ["compare", "complain", "compete"]),
 ("Anne was ___ sorry for Minnie May, but she also enjoyed the romance of the situation.", "sincerely", ["severely", "secretly", "securely"]),
 ("Running through the snow with her bosom friend, who had been so long ___, felt delightful.", "estranged", ["arranged", "exchanged", "strangled"]),
 ("Minnie May lay on the kitchen sofa, ___ and restless, with hoarse breathing.", "feverish", ["famous", "foolish", "faithful"]),
 ("Young Mary Joe was helpless and bewildered, quite ___ of thinking what to do.", "incapable", ["incredible", "inevitable", "inexpensive"]),
 ("Anne quietly said a sad line to herself, just to ___ her feelings.", "relieve", ["receive", "relive", "retrieve"]),
 ("When Anne begged to go to Diana's at once, Marilla said ___, \"Yes, yes, run along.\"", "indulgently", ["indignantly", "intelligently", "independently"]),
 ("Diana and Anne ___ a solemn vow never to reveal the new crochet stitch to anyone.", "pledged", ["pleaded", "plunged", "plucked"]),
], discussion=[
 "Anne saved Minnie May because she had looked after twins before. Has a hard experience in your past ever helped you later?",
 "Matthew always takes Anne's side. Who was \"your Matthew\" when you were young?",
]),
19: dict(vocab=[
 ("traipse", "traipsing", "v.", "TRAIPSE", "/treɪps/", "(괜히) 쏘다니다", "traipse around · traipse about", "I don't want to traipse around the mall all day.", "We traipsed through the rain to find the hotel."),
 ("emphatically", "emphatically", "adv.", "em-PHAT-i-cal-ly", "/ɪmˈfætɪkli/", "단호하게, 힘주어", "emphatically deny · say emphatically", "He emphatically denied the rumor.", "\"No,\" she said emphatically."),
 ("stipulated", "stipulated", "adj.", "STIP-u-lat-ed", "/ˈstɪpjəleɪtɪd/", "정해진, 규정된", "the stipulated time · stipulated in the contract", "Please pay within the stipulated time.", "The price was stipulated in the contract."),
 ("interfere", "interfere", "v.", "in-ter-FERE", "/ˌɪntərˈfɪr/", "간섭하다; 방해하다", "interfere in · interfere with", "Don't interfere in their argument.", "Noise can interfere with your sleep."),
 ("tartly", "tartly", "adv.", "TART-ly", "/ˈtɑːrtli/", "쏘아붙이듯, 퉁명스럽게", "reply tartly · say tartly", "\"Do it yourself,\" she replied tartly.", "He answered tartly that he was busy."),
 ("repentantly", "repentantly", "adv.", "re-PENT-ant-ly", "/rɪˈpentəntli/", "뉘우치며", "say repentantly · look repentantly", "\"I broke it,\" the boy said repentantly.", "She looked at me repentantly."),
 ("furtive", "furtive", "adj.", "FUR-tive", "/ˈfɜːrtɪv/", "남몰래 하는, 은밀한", "a furtive glance · furtive smiles", "He took a furtive look at her phone.", "They exchanged furtive smiles during the meeting."),
 ("apprehensive", "apprehensive", "adj.", "ap-pre-HEN-sive", "/ˌæprɪˈhensɪv/", "걱정하는, 불안해하는", "apprehensive about · an apprehensive look", "I'm a little apprehensive about the interview.", "She gave an apprehensive glance at the door."),
 ("exultation", "exultation", "n.", "ex-ul-TA-tion", "/ˌeɡzʌlˈteɪʃən/", "의기양양, 크게 기뻐함", "a shout of exultation · in exultation", "The fans cried out in exultation.", "There was exultation in his voice."),
 ("arduous", "arduous", "adj.", "AR-du-ous", "/ˈɑːrdʒuəs/", "고된, 몹시 힘든", "an arduous journey · arduous work", "The climb was long and arduous.", "Moving house is an arduous task."),
], quiz=[
 ("\"I don't see what you want to be ___ about after dark for,\" Marilla said to Anne.", "traipsing", ["trading", "training", "trapping"]),
 ("When Anne said the candle signals were her idea, Marilla said ___, \"I'll warrant you it was.\"", "emphatically", ["emotionally", "economically", "energetically"]),
 ("Anne came back from Diana's within the ___ ten minutes.", "stipulated", ["stimulated", "speculated", "simulated"]),
 ("\"Who's bringing this child up, you or me?\" Marilla asked Matthew. \"Don't ___ then.\"", "interfere", ["interpret", "inspire", "insert"]),
 ("Marilla finally gave in and said ___, \"Very well, she can go.\"", "tartly", ["tenderly", "tightly", "tastefully"]),
 ("\"Oh, I know I'm a great trial to you, Marilla,\" said Anne ___.", "repentantly", ["resentfully", "repeatedly", "reportedly"]),
 ("At breakfast Diana and Anne exchanged ___ smiles of guilty amusement.", "furtive", ["festive", "fertile", "futile"]),
 ("Diana answered, stifling a giggle, with an ___ glance at the closed sitting-room door.", "apprehensive", ["appreciative", "comprehensive", "expensive"]),
 ("\"I knew it!\" said Mrs. Lynde, with the ___ of a correct guesser.", "exultation", ["exhibition", "expectation", "exhalation"]),
 ("Aunt Josephine complained about being woken after a long and ___ journey.", "arduous", ["ardent", "anxious", "ambitious"]),
], discussion=[
 "Anne and Diana jumped onto the spare-room bed—and landed on Aunt Josephine! What is the funniest accident you remember from your childhood?",
 "Matthew didn't argue loudly. He just kept saying, \"I think you ought to let Anne go.\" Is quiet persistence a good way to win an argument?",
]),
20: dict(vocab=[
 ("capricious", "capricious", "adj.", "ca-PRI-cious", "/kəˈprɪʃəs/", "변덕스러운", "capricious weather · a capricious boss", "Spring weather here is very capricious.", "Her capricious moods are hard to follow."),
 ("troublesome", "troublesome", "adj.", "TROU-ble-some", "/ˈtrʌblsəm/", "골치 아픈, 말썽 많은", "a troublesome child · troublesome questions", "My old car has been troublesome lately.", "That's a troublesome question to answer."),
 ("penitently", "penitently", "adv.", "PEN-i-tent-ly", "/ˈpenɪtəntli/", "뉘우치며", "say penitently · bow penitently", "\"I forgot again,\" he said penitently.", "She penitently returned the book."),
 ("instinctively", "instinctively", "adv.", "in-STINC-tive-ly", "/ɪnˈstɪŋktɪvli/", "본능적으로", "know instinctively · react instinctively", "I instinctively knew something was wrong.", "She instinctively covered her face."),
 ("harrowing", "harrowing", "adj.", "HAR-row-ing", "/ˈhæroʊɪŋ/", "끔찍한, 괴로운", "a harrowing experience · harrowing stories", "Their escape was a harrowing experience.", "The film shows harrowing scenes of war."),
 ("shudder", "shudder", "n./v.", "SHUD-der", "/ˈʃʌdər/", "몸서리(치다), 전율", "give someone a shudder · shudder at", "The cold wind gave me a shudder.", "I shudder to think what could have happened."),
 ("inexorable", "inexorable", "adj.", "in-EX-o-ra-ble", "/ɪnˈeksərəbl/", "냉혹한, 굽히지 않는; 막을 수 없는", "inexorable rise · remain inexorable", "The teacher was inexorable about the deadline.", "Nothing could stop the inexorable rise in prices."),
 ("perspiration", "perspiration", "n.", "per-spi-RA-tion", "/ˌpɜːrspəˈreɪʃən/", "땀", "beads of perspiration · drip with perspiration", "Beads of perspiration formed on his forehead.", "Her shirt was wet with perspiration."),
 ("unearthly", "unearthly", "adj.", "un-EARTH-ly", "/ʌnˈɜːrθli/", "이 세상 것 같지 않은, 기이한", "an unearthly sound · an unearthly glow", "We heard an unearthly cry in the night.", "The lake had an unearthly blue color."),
 ("unsympathetically", "unsympathetically", "adv.", "un-sym-pa-THET-i-cal-ly", "/ˌʌnsɪmpəˈθetɪkli/", "냉담하게, 동정심 없이", "say unsympathetically · look unsympathetically", "\"That's your problem,\" he said unsympathetically.", "The guard looked at us unsympathetically."),
], quiz=[
 ("Spring came to Green Gables once more—the beautiful, ___, reluctant Canadian spring.", "capricious", ["delicious", "precious", "spacious"]),
 ("Anne said there were so many different Annes in her that she was a ___ person.", "troublesome", ["wholesome", "handsome", "lonesome"]),
 ("\"Oh, I'm so sorry,\" said Anne ___ when Marilla mentioned the burned pie.", "penitently", ["patiently", "pleasantly", "politely"]),
 ("Anne said she had felt ___ that something was missing on the dinner table.", "instinctively", ["intentionally", "internationally", "incredibly"]),
 ("Anne and Diana had imagined the most ___ things about the spruce grove: a white lady, a headless man, skeletons.", "harrowing", ["harmonious", "borrowing", "narrowing"]),
 ("Anne said the ghost of a little murdered child gave her a ___ just to think of it.", "shudder", ["shoulder", "shutter", "shadow"]),
 ("Anne cried and pleaded, but Marilla was ___ and sent her through the grove.", "inexorable", ["inexpensive", "inexperienced", "incredible"]),
 ("The wail of two old boughs rubbing together brought out ___ in beads on Anne's forehead.", "perspiration", ["inspiration", "aspiration", "preparation"]),
 ("The bats swooping in the dark seemed like the wings of ___ creatures.", "unearthly", ["unhealthy", "untidy", "unlucky"]),
 ("\"Well, so nothing caught you?\" said Marilla ___ when Anne got back.", "unsympathetically", ["unselfishly", "unsuccessfully", "unexpectedly"]),
], discussion=[
 "Anne's imagination made the Haunted Wood truly frightening for her. Have you ever scared yourself with your own imagination?",
 "Marilla made Anne walk through the wood to cure her of her fears. Was this a good way to teach a lesson? Why or why not?",
]),
21: dict(vocab=[
 ("plaintively", "plaintively", "adv.", "PLAIN-tive-ly", "/ˈpleɪntɪvli/", "구슬프게, 애처롭게", "say plaintively · cry plaintively", "The kitten mewed plaintively at the door.", "\"Can't we stay?\" the kids asked plaintively."),
 ("heartrending", "heartrending", "adj.", "HEART-rend-ing", "/ˈhɑːrtrendɪŋ/", "가슴이 찢어지는 듯한", "a heartrending story · heartrending cries", "The movie's ending was heartrending.", "We heard heartrending stories from the survivors."),
 ("remorseful", "remorseful", "adj.", "re-MORSE-ful", "/rɪˈmɔːrsfəl/", "후회하는, 뉘우치는", "feel remorseful · a remorseful look", "He felt remorseful about shouting at her.", "The remorseful boy wrote an apology."),
 ("sojourn", "sojourn", "n.", "SO-journ", "/ˈsoʊdʒɜːrn/", "(일시적인) 체류, 머무름", "a brief sojourn · during his sojourn", "During her sojourn in Paris she learned French.", "We enjoyed a short sojourn by the sea."),
 ("resign", "resigned", "v.", "re-SIGN", "/rɪˈzaɪn/", "사임하다, 그만두다", "resign from · resign as", "The manager resigned after the scandal.", "She resigned from her job to travel."),
 ("undignified", "undignified", "adj.", "un-DIG-ni-fied", "/ʌnˈdɪɡnɪfaɪd/", "품위 없는, 체면이 서지 않는", "undignified behavior · look undignified", "Crawling under the table felt undignified.", "It was an undignified end to his career."),
 ("exquisite", "exquisite", "adj.", "ex-QUIS-ite", "/ɪkˈskwɪzɪt/", "매우 아름다운, 정교한", "exquisite taste · an exquisite view", "The hotel has an exquisite view of the lake.", "She has exquisite taste in clothes."),
 ("prudent", "prudent", "adj.", "PRU-dent", "/ˈpruːdənt/", "신중한, 현명한", "a prudent decision · it is prudent to", "It is prudent to save some money each month.", "That was a prudent choice."),
 ("culinary", "culinary", "adj.", "CU-li-nar-y", "/ˈkʌlɪneri/", "요리의", "culinary skills · culinary school", "He went to culinary school in Italy.", "Her culinary skills are amazing."),
 ("anguish", "anguish", "n.", "AN-guish", "/ˈæŋɡwɪʃ/", "극심한 괴로움, 비통", "in anguish · cry out in anguish", "She cried out in anguish.", "He could see the anguish on her face."),
], quiz=[
 ("\"There is nothing but meetings and partings in this world,\" Anne said ___ on the last day of June.", "plaintively", ["playfully", "plainly", "politely"]),
 ("Everyone cried at Mr. Phillips's goodbye speech; Anne said it was ___.", "heartrending", ["heartwarming", "hardworking", "heartless"]),
 ("Anne felt sorry and ___ for all the times she had drawn pictures of Mr. Phillips on her slate.", "remorseful", ["resourceful", "respectful", "restful"]),
 ("Gossip married the old minister to someone new every year of his ___ in Avonlea.", "sojourn", ["journal", "sermon", "season"]),
 ("In February the old minister had ___ and left, and Avonlea heard many new candidates preach.", "resigned", ["designed", "resided", "reminded"]),
 ("Anne said one candidate told too many funny stories in church; he was ___.", "undignified", ["unidentified", "unqualified", "unsatisfied"]),
 ("Anne admired Mrs. Allan's lovely smile and her ___ dimples.", "exquisite", ["exclusive", "expensive", "explicit"]),
 ("After the Haunted Wood trouble, Diana did not think it ___ to believe even in harmless dryads.", "prudent", ["proud", "prominent", "prudish"]),
 ("Anne had a bad cold, but nothing short of pneumonia could stop her interest in ___ matters that morning.", "culinary", ["cultural", "ordinary", "military"]),
 ("When Marilla tasted the cake, Anne cried with a look of ___, \"Oh, isn't it all right?\"", "anguish", ["language", "English", "languish"]),
], discussion=[
 "Anne flavored the cake with liniment instead of vanilla, but Mrs. Allan was kind about it. How do you react when a guest makes a mistake—or when you do?",
 "Anne thinks a minister should not tell too many funny stories. What makes a good teacher or leader: humor or seriousness?",
]),
22: dict(vocab=[
 ("cherish", "cherish", "v.", "CHER-ish", "/ˈtʃerɪʃ/", "소중히 여기다", "cherish memories · cherish a gift", "I will cherish this letter forever.", "We cherish the time we spend together."),
 ("treble", "trebled", "v./adj.", "TREB-le", "/ˈtrebl/", "세 배가 되다; 세 배의", "treble in size · treble the price", "The price of houses has trebled.", "Our sales trebled last year."),
 ("intensity", "intensity", "n.", "in-TEN-si-ty", "/ɪnˈtensəti/", "강렬함, 세기", "great intensity · the intensity of", "The storm grew in intensity.", "She feels everything with great intensity."),
 ("compensate", "compensate", "v.", "COM-pen-sate", "/ˈkɑːmpənseɪt/", "보상하다, 메우다", "compensate for · fully compensate", "Nothing can compensate for lost time.", "The company compensated us for the delay."),
 ("tranquil", "tranquil", "adj.", "TRAN-quil", "/ˈtræŋkwɪl/", "고요한, 평온한", "a tranquil lake · a tranquil life", "We stayed in a tranquil village by the sea.", "He wants a tranquil life after retirement."),
 ("exalt", "exalted", "v.", "ex-ALT", "/ɪɡˈzɔːlt/", "의기양양하게 하다; 높이다", "feel exalted · exalted position", "Winning the prize left her exalted for days.", "He holds an exalted position in the company."),
 ("deportment", "deportment", "n.", "de-PORT-ment", "/dɪˈpɔːrtmənt/", "몸가짐, 행실", "good deportment · lessons in deportment", "Girls once took lessons in deportment.", "His deportment was calm and polite."),
 ("prophecy", "prophecy", "n.", "PROPH-e-cy", "/ˈprɑːfəsi/", "예언", "a prophecy of · fulfill a prophecy", "The dark clouds were a prophecy of rain.", "The story begins with an old prophecy."),
 ("enchanting", "enchanting", "adj.", "en-CHANT-ing", "/ɪnˈtʃæntɪŋ/", "매혹적인, 황홀한", "an enchanting smile · enchanting music", "The old town is enchanting at night.", "She has an enchanting smile."),
 ("etiquette", "etiquette", "n.", "ET-i-quette", "/ˈetɪkət/", "예절, 에티켓", "table etiquette · a breach of etiquette", "In Korea, drinking etiquette is important.", "Using your phone at dinner is bad etiquette."),
], quiz=[
 ("Anne said she would ___ Mrs. Allan's invitation forever among her choicest treasures.", "cherish", ["perish", "cheer", "polish"]),
 ("The pleasures and pains of life came to Anne three times stronger—with ___ intensity.", "trebled", ["troubled", "tumbled", "trembled"]),
 ("Anne felt everything with great ___, so small things made her very happy or very sad.", "intensity", ["intention", "integrity", "identity"]),
 ("Marilla did not see that Anne's great capacity for delight might more than ___ for her sorrows.", "compensate", ["complicate", "concentrate", "contemplate"]),
 ("Marilla tried to drill Anne into a calm, ___ way of being, which was impossible for her.", "tranquil", ["tropical", "tribal", "tearful"]),
 ("When a dear plan came true, it ___ Anne to dizzy realms of delight.", "exalted", ["exhausted", "exploded", "exhaled"]),
 ("Marilla dreamed of a model little girl with demure manners and prim ___.", "deportment", ["department", "apartment", "development"]),
 ("The roar of the gulf sounded like a ___ of storm to a girl who wanted a fine day.", "prophecy", ["privacy", "policy", "pharmacy"]),
 ("Coming home, Anne felt the wind, stars and fireflies were tangled into something sweet and ___.", "enchanting", ["enhancing", "entering", "endangering"]),
 ("Anne got through her visit without any serious breach of ___.", "etiquette", ["etymology", "ethics", "estate"]),
], discussion=[
 "Anne loves Mrs. Allan because Mrs. Allan treats her like a real person. Did you have an adult like that when you were a child?",
 "Anne's feelings are always very strong—very high highs and very low lows. Are you more like Anne or more like Marilla?",
]),
23: dict(vocab=[
 ("elapse", "elapsed", "v.", "e-LAPSE", "/ɪˈlæps/", "(시간이) 지나다, 흐르다", "time elapsed · weeks elapsed", "Ten minutes elapsed before the bus came.", "A year had elapsed since we last met."),
 ("untoward", "untoward", "adj.", "un-TO-ward", "/ʌnˈtɔːrd/", "뜻밖의, 곤란한", "nothing untoward · untoward events", "Nothing untoward happened during the trip.", "Call me if anything untoward happens."),
 ("discomfiture", "discomfiture", "n.", "dis-COM-fi-ture", "/dɪsˈkʌmfɪtʃər/", "당황, 낭패", "to someone's discomfiture · obvious discomfiture", "To his discomfiture, everyone laughed.", "She enjoyed her rival's discomfiture."),
 ("precarious", "precarious", "adj.", "pre-CAR-i-ous", "/prɪˈkeriəs/", "불안정한, 위태로운", "a precarious position · precarious footing", "The ladder looked precarious.", "Many workers have precarious jobs."),
 ("stagger", "staggered", "v.", "STAG-ger", "/ˈstæɡər/", "비틀거리다", "stagger to your feet · stagger home", "He staggered out of the bar.", "She staggered under the heavy box."),
 ("frantically", "frantically", "adv.", "FRAN-ti-cal-ly", "/ˈfræntɪkli/", "미친 듯이, 허둥지둥", "search frantically · wave frantically", "I searched frantically for my passport.", "She waved frantically at the taxi."),
 ("revelation", "revelation", "n.", "rev-e-LA-tion", "/ˌrevəˈleɪʃən/", "(갑작스러운) 깨달음; 폭로", "have a revelation · a shocking revelation", "Living abroad was a revelation for me.", "The revelation shocked the whole country."),
 ("sprain", "sprained", "v.", "SPRAIN", "/spreɪn/", "(발목 등을) 삐다", "sprain your ankle · a sprained wrist", "I sprained my ankle playing soccer.", "She has a sprained wrist."),
 ("plaintive", "plaintive", "adj.", "PLAIN-tive", "/ˈpleɪntɪv/", "애처로운, 구슬픈", "a plaintive voice · a plaintive cry", "We heard the plaintive cry of a bird.", "\"Can I come?\" she asked in a plaintive voice."),
 ("absurdity", "absurdity", "n.", "ab-SURD-i-ty", "/əbˈsɜːrdəti/", "터무니없음, 어리석음", "the absurdity of · sheer absurdity", "We laughed at the absurdity of the situation.", "The absurdity of the rule was clear to everyone."),
], quiz=[
 ("Almost a month had ___ since the liniment cake, so it was time for Anne to get into fresh trouble.", "elapsed", ["collapsed", "relapsed", "eclipsed"]),
 ("Nothing ___ happened at Diana's party until after tea, when the girls began daring each other.", "untoward", ["upward", "toward", "untold"]),
 ("Ruby Gillis climbed the willow tree, to the ___ of Carrie Sloane, who had dared her.", "discomfiture", ["discovery", "furniture", "departure"]),
 ("Anne balanced herself on that ___ footing and started to walk along the ridgepole.", "precarious", ["previous", "precious", "curious"]),
 ("Anne swayed, lost her balance, stumbled, ___, and fell.", "staggered", ["stuttered", "scattered", "swaggered"]),
 ("Diana and the other girls rushed ___ around the house to find her.", "frantically", ["fantastically", "romantically", "frankly"]),
 ("When she saw Matthew carrying Anne, Marilla had a ___: she realized what Anne had come to mean to her.", "revelation", ["revolution", "reservation", "relaxation"]),
 ("\"I expect I have ___ my ankle,\" Anne said, but the doctor found it was broken.", "sprained", ["sprayed", "sprinkled", "spread"]),
 ("That night a ___ voice from the bed asked, \"Aren't you very sorry for me, Marilla?\"", "plaintive", ["primitive", "positive", "festive"]),
 ("\"I'd have stayed on good firm ground and let them dare away. Such ___!\" said Marilla.", "absurdity", ["obscurity", "maturity", "security"]),
], discussion=[
 "Anne walked the ridgepole because Josie Pye dared her. Have you ever done something risky because of a dare or pressure from friends?",
 "Marilla only realized how much she loved Anne when Anne got hurt. Why do we sometimes notice our feelings only in a crisis?",
]),
24: dict(vocab=[
 ("inspire", "inspired", "v.", "in-SPIRE", "/ɪnˈspaɪər/", "영감을 주다, 북돋우다", "inspire someone to · be inspired by", "Her speech inspired me to try again.", "The song was inspired by a true story."),
 ("meditatively", "meditatively", "adv.", "MED-i-ta-tive-ly", "/ˈmedɪteɪtɪvli/", "생각에 잠겨", "say meditatively · gaze meditatively", "He stirred his coffee meditatively.", "\"Maybe,\" she said meditatively."),
 ("humbling", "humbling", "adj.", "HUM-bling", "/ˈhʌmblɪŋ/", "겸손하게 만드는, 자존심이 꺾이는", "a humbling experience · find it humbling", "Losing to a child at chess was humbling.", "It's humbling to see how much I don't know."),
 ("laudable", "laudable", "adj.", "LAUD-a-ble", "/ˈlɔːdəbl/", "칭찬할 만한", "a laudable goal · laudable efforts", "Raising money for the hospital is a laudable goal.", "His efforts were laudable but not enough."),
 ("hamper", "hampered", "v.", "HAM-per", "/ˈhæmpər/", "방해하다", "be hampered by · hamper progress", "The rescue was hampered by bad weather.", "A lack of money hampered the project."),
 ("disapproval", "disapproval", "n.", "dis-ap-PROV-al", "/ˌdɪsəˈpruːvəl/", "반대, 못마땅함", "show disapproval · shake your head in disapproval", "She shook her head in disapproval.", "His parents' disapproval didn't stop him."),
 ("grumble", "grumbled", "v.", "GRUM-ble", "/ˈɡrʌmbl/", "투덜거리다", "grumble about · grumble at", "He always grumbles about the weather.", "\"Not again,\" she grumbled."),
 ("appreciative", "appreciative", "adj.", "ap-PRE-cia-tive", "/əˈpriːʃətɪv/", "고마워하는; 잘 알아주는", "an appreciative audience · appreciative of", "The audience was warm and appreciative.", "I'm very appreciative of your help."),
 ("vivacious", "vivacious", "adj.", "vi-VA-cious", "/vɪˈveɪʃəs/", "쾌활한, 생기 넘치는", "a vivacious girl · vivacious personality", "She is a vivacious woman who loves to dance.", "His vivacious personality made him popular."),
 ("conscientious", "conscientious", "adj.", "con-sci-EN-tious", "/ˌkɑːnʃiˈenʃəs/", "성실한, 양심적인", "a conscientious worker · conscientious about", "He is a conscientious student who never misses class.", "She is conscientious about recycling."),
], quiz=[
 ("The crisp autumn air ___ the hearts of the little girls hurrying to school.", "inspired", ["inspected", "inquired", "insisted"]),
 ("\"Of course I will,\" said Anne ___, thinking about reciting for Matthew in the barn.", "meditatively", ["immediately", "mechanically", "moderately"]),
 ("Anne said being such a dunce at geometry was a ___ thought.", "humbling", ["rumbling", "tumbling", "crumbling"]),
 ("Miss Stacy's concert had the ___ purpose of paying for a schoolhouse flag.", "laudable", ["laughable", "audible", "lovable"]),
 ("Anne threw herself into the concert heart and soul, ___ as she was by Marilla.", "hampered", ["hammered", "pampered", "happened"]),
 ("Marilla showed her ___ of the concert; she thought it was all rank foolishness.", "disapproval", ["disappearance", "disposal", "disappointment"]),
 ("\"It's just filling your heads up with nonsense,\" Marilla ___.", "grumbled", ["rumbled", "crumbled", "stumbled"]),
 ("Anne talked the concert over with Matthew, sure of an ___ and sympathetic listener.", "appreciative", ["apprehensive", "approximate", "appropriate"]),
 ("Matthew smiled down into Anne's eager, ___ little face.", "vivacious", ["vicious", "various", "voracious"]),
 ("A little appreciation sometimes does as much good as all the ___ \"bringing up\" in the world.", "conscientious", ["conscious", "contentious", "convenient"]),
], discussion=[
 "Miss Stacy takes her pupils outside for lessons and lets them choose their own writing topics. What made your favorite teacher different?",
 "Matthew \"spoils\" Anne with praise, while Marilla \"brings her up\" with rules. Which do children need more—praise or rules?",
]),
}

OLD = {
 "wilt": ("조동사", "(옛) ~하겠느냐 (= will, thou와 함께)", "\"Wilt thou give me…?\" = \"Will you give me…?\" Anne uses Bible-style English to make her goodbye romantic."),
 "thy": ("한정사", "(옛) 너의 (= your)", "\"Thy memory\" = \"your memory\". Anne talks like the heroine of an old story, so these words are kept."),
 "thenceforth": ("부사", "(옛) 그때부터 (= from then on)", "\"She got on very well with Mr. Phillips thenceforth\" = from that time on."),
 "tis": ("축약", "(옛) = it is", "Anne repeats a dramatic line from a book: \"I fear 'tis a vain one\" = \"I fear it is a useless hope.\""),
}
IDIOMS = {
 "In a trice": ("눈 깜짝할 사이에", "in a moment / in no time", "Today: \"In no time, Anne was out of the house.\""),
 "Fare thee well": ("잘 있어요, 안녕히", "goodbye / farewell", "A very old, poetic way to say goodbye. Anne uses it to sound like a heroine."),
 "heaping coals of fire": ("(친절로 갚아) 상대를 부끄럽게 만들다", "making someone feel ashamed by being kind to them", "From the Bible. Mrs. Barry treated Anne badly, so Anne's kindness should make Mrs. Barry feel ashamed."),
 "I’ll warrant you": ("틀림없이 그렇겠지", "I'm sure / I bet", "Marilla means \"I bet it was your idea!\" Today: \"I bet it was.\""),
 "last shot in her locker": ("마지막 남은 수단", "her last chance / last argument", "Originally a sailors' phrase: the last shot a ship has left. Today: \"her last card to play\"."),
}
OLD_MARKS = {17: ["thy", "wilt", "thenceforth"], 18: ["tis"]}
IDIOM_MARKS = {17: ["In a trice", "Fare thee well"], 18: ["heaping coals of fire"], 19: ["I’ll warrant you", "last shot in her locker"]}

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
