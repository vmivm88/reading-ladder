# Anne of Green Gables workbook, chapters 1–8. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
1: dict(vocab=[
 ("decorum", "decorum", "n.", "de-CO-rum", "/dɪˈkɔːrəm/", "예의 바름, 품위", "with decorum · a sense of decorum", "The guests behaved with perfect decorum.", "She has a strong sense of decorum."),
 ("neglect", "neglecting", "v.", "ne-GLECT", "/nɪˈɡlekt/", "소홀히 하다, 방치하다", "neglect your duties · neglect your health", "Don't neglect your health because of work.", "He neglected the garden all summer."),
 ("orchard", "orchard", "n.", "OR-chard", "/ˈɔːrtʃərd/", "과수원", "an apple orchard · in the orchard", "We picked apples in the orchard.", "The orchard is full of blossoms in May."),
 ("placidly", "placidly", "adv.", "PLAC-id-ly", "/ˈplæsɪdli/", "평온하게, 차분하게", "smile placidly · sit placidly", "The cows were grazing placidly in the field.", "She smiled placidly while the children shouted."),
 ("curiosity", "curiosity", "n.", "cu-ri-OS-i-ty", "/ˌkjʊriˈɑːsəti/", "호기심", "out of curiosity · satisfy your curiosity", "I asked out of curiosity.", "The box was too much for his curiosity."),
 ("mystery", "mystery", "n.", "MYS-ter-y", "/ˈmɪstəri/", "수수께끼, 미스터리", "solve a mystery · a complete mystery", "How he got in is still a mystery.", "She loves reading mystery novels."),
 ("distrustful", "distrustful", "adj.", "dis-TRUST-ful", "/dɪsˈtrʌstfəl/", "믿지 않는, 의심하는", "distrustful of · a distrustful look", "He is distrustful of strangers.", "She gave me a distrustful look."),
 ("asylum", "asylum", "n.", "a-SY-lum", "/əˈsaɪləm/", "(옛) 보호 시설, 고아원; 망명", "an orphan asylum · seek asylum", "In the past, orphans often lived in an asylum.", "The family asked for asylum in another country."),
 ("adopt", "adopting", "v.", "a-DOPT", "/əˈdɑːpt/", "입양하다; 채택하다", "adopt a child · adopt a plan", "They adopted a baby girl from Korea.", "The school adopted a new rule."),
 ("pessimism", "pessimism", "n.", "PES-si-mism", "/ˈpesɪmɪzəm/", "비관(주의)", "a mood of pessimism · full of pessimism", "His pessimism made everyone feel worse.", "There is a lot of pessimism about the economy."),
], quiz=[
 ("Even the little brook seemed to flow past Mrs. Rachel's door with proper ___.", "decorum", ["pessimism", "curiosity", "mystery"]),
 ("Some people mind their neighbors' business by ___ their own, but Mrs. Rachel managed both.", "neglecting", ["adopting", "driving", "knitting"]),
 ("From her window, Mrs. Rachel could see the ___ on the slope, full of white blossoms.", "orchard", ["asylum", "mystery", "decorum"]),
 ("On a busy afternoon, Matthew Cuthbert was ___ driving over the hill in his best suit.", "placidly", ["distrustfully", "foolishly", "angrily"]),
 ("Not knowing where Matthew was going was too much for Mrs. Rachel's ___.", "curiosity", ["pessimism", "decorum", "asylum"]),
 ("Mrs. Rachel felt dizzy with this unusual ___ about quiet Green Gables.", "mystery", ["orchard", "decorum", "pessimism"]),
 ("Marilla usually sat in the kitchen, always slightly ___ of sunshine.", "distrustful", ["placid", "adopted", "neglected"]),
 ("Marilla explained that they were getting a boy from an orphan ___ in Nova Scotia.", "asylum", ["orchard", "mystery", "kitchen"]),
 ("Mrs. Rachel could hardly believe that Marilla and Matthew were ___ a boy.", "adopting", ["neglecting", "driving", "visiting"]),
 ("Marilla's doubts came back under the influence of Mrs. Rachel's ___.", "pessimism", ["curiosity", "decorum", "mystery"]),
], discussion=[
 "Mrs. Rachel knows everyone's business. Do you know someone like her? Is it good or bad to have such a neighbor?",
 "Mrs. Rachel tells frightening stories about adopted children. Why do you think Marilla still goes ahead with the plan?",
]),

2: dict(vocab=[
 ("freckled", "freckled", "adj.", "FRECK-led", "/ˈfrekld/", "주근깨가 있는", "a freckled face · freckled arms", "The boy had a freckled nose.", "Her freckled face turned red in the sun."),
 ("extraordinary", "extraordinary", "adj.", "ex-TRAOR-di-nar-y", "/ɪkˈstrɔːrdəneri/", "보통이 아닌, 비범한", "an extraordinary person · quite extraordinary", "She has an extraordinary talent for music.", "It was an extraordinary day."),
 ("commonplace", "commonplace", "adj.", "COM-mon-place", "/ˈkɑːmənpleɪs/", "평범한, 흔한", "a commonplace event · commonplace ideas", "Smartphones are now commonplace.", "It was a commonplace story with no surprises."),
 ("awkwardly", "awkwardly", "adv.", "AWK-ward-ly", "/ˈɔːkwərdli/", "어색하게, 서투르게", "smile awkwardly · move awkwardly", "He smiled awkwardly at the camera.", "She held the baby awkwardly."),
 ("ashamed", "ashamed", "adj.", "a-SHAMED", "/əˈʃeɪmd/", "부끄러운", "ashamed of · feel ashamed", "He felt ashamed of his old shoes.", "There's nothing to be ashamed of."),
 ("imagination", "imagination", "n.", "i-mag-i-NA-tion", "/ɪˌmædʒɪˈneɪʃən/", "상상력", "use your imagination · scope for imagination", "Children have wonderful imaginations.", "Use your imagination and draw anything you like."),
 ("fragrant", "fragrant", "adj.", "FRA-grant", "/ˈfreɪɡrənt/", "향기로운", "fragrant flowers · fragrant tea", "The room was full of fragrant roses.", "She made a pot of fragrant jasmine tea."),
 ("glimpse", "glimpse", "n.", "GLIMPSE", "/ɡlɪmps/", "얼핏 봄", "catch a glimpse of · a brief glimpse", "We caught a glimpse of the sea through the trees.", "I only got a quick glimpse of him."),
 ("ingenuously", "ingenuously", "adv.", "in-GEN-u-ous-ly", "/ɪnˈdʒenjuəsli/", "순진하게, 솔직하게", "smile ingenuously · admit ingenuously", "The child ingenuously told the guest she was fat.", "He ingenuously admitted he had never read the book."),
 ("breathlessly", "breathlessly", "adv.", "BREATH-less-ly", "/ˈbreθləsli/", "숨을 헐떡이며, 숨죽이고", "wait breathlessly · say breathlessly", "We waited breathlessly for the results.", "\"I won!\" she said breathlessly."),
], quiz=[
 ("Anne's face was small, white, thin and much ___.", "freckled", ["fragrant", "commonplace", "extraordinary"]),
 ("An ___ observer might have seen that this was no ordinary child.", "extraordinary", ["commonplace", "freckled", "fragrant"]),
 ("No ___ soul lived inside the body of this stray little girl.", "commonplace", ["fragrant", "ashamed", "freckled"]),
 ("Matthew took the girl's thin little hand ___ in his.", "awkwardly", ["breathlessly", "ingenuously", "mournfully"]),
 ("Anne waited outside the station because there was \"more scope for ___\" there.", "imagination", ["curiosity", "freckles", "fragrance"]),
 ("Anne felt ___ of the horrid old dress she had to wear from the asylum.", "ashamed", ["freckled", "fragrant", "commonplace"]),
 ("When Anne asked if he had ever imagined being divinely beautiful, Matthew ___ admitted he hadn't.", "ingenuously", ["breathlessly", "mournfully", "angrily"]),
 ("On the Avenue, the apple trees made a long roof of snowy, ___ blossoms.", "fragrant", ["freckled", "commonplace", "awkward"]),
 ("Far ahead, a ___ of painted sunset sky shone through the trees.", "glimpse", ["freckle", "scope", "asylum"]),
 ("\"Oh, don't tell me,\" Anne interrupted ___, wanting to guess which house was Green Gables.", "breathlessly", ["awkwardly", "ingenuously", "placidly"]),
], discussion=[
 "Anne talks all the way home, and shy Matthew enjoys it. Why do you think they get along so well?",
 "Anne gives places new names, like \"the White Way of Delight.\" Why do you think she does this?",
]),

3: dict(vocab=[
 ("wretchedly", "wretchedly", "adv.", "WRETCH-ed-ly", "/ˈretʃɪdli/", "비참하게, 괴로워하며", "feel wretchedly · say wretchedly", "\"I lost it,\" he said wretchedly.", "She slept wretchedly after the bad news."),
 ("tragical", "tragical", "adj.", "TRAG-i-cal", "/ˈtrædʒɪkəl/", "(옛·과장) 비극적인 (= tragic)", "a tragical story", "Anne loves tragical stories with sad endings.", "Today we would say \"tragic\", not \"tragical\"."),
 ("despair", "despair", "n.", "de-SPAIR", "/dɪˈsper/", "절망", "in despair · the depths of despair", "He gave up in despair.", "She was in the depths of despair after the exam."),
 ("reluctantly", "reluctantly", "adv.", "re-LUC-tant-ly", "/rɪˈlʌktəntli/", "마지못해", "reluctantly agree · reluctantly admit", "He reluctantly agreed to help.", "She reluctantly left the party early."),
 ("sensible", "sensible", "adj.", "SEN-si-ble", "/ˈsensəbəl/", "분별 있는, 실용적인", "a sensible choice · sensible shoes", "That's a sensible idea.", "Wear sensible shoes for the hike."),
 ("stammer", "stammered", "v.", "STAM-mer", "/ˈstæmər/", "말을 더듬다", "stammer an apology · stammer nervously", "He stammered an apology.", "She stammered when the teacher called her name."),
 ("astonishment", "astonishment", "n.", "as-TON-ish-ment", "/əˈstɑːnɪʃmənt/", "깜짝 놀람", "in astonishment · to my astonishment", "She stared at him in astonishment.", "To my astonishment, he said yes."),
 ("bewitch", "bewitched", "v.", "be-WITCH", "/bɪˈwɪtʃ/", "마법을 걸다; 홀리다", "be bewitched by · bewitch someone", "He was bewitched by her smile.", "The village believed the cat had been bewitched."),
 ("wistfully", "wistfully", "adv.", "WIST-ful-ly", "/ˈwɪstfəli/", "아쉬운 듯이, 그리운 듯이", "look wistfully at · smile wistfully", "She looked wistfully at the cakes in the window.", "He smiled wistfully, remembering his childhood."),
 ("whitewashed", "whitewashed", "adj.", "WHITE-washed", "/ˈwaɪtwɑːʃt/", "흰 회칠을 한", "whitewashed walls · a whitewashed cottage", "The village had whitewashed houses.", "Sunlight bounced off the whitewashed walls."),
], quiz=[
 ("\"There wasn't any boy,\" Matthew said ___. \"There was only her.\"", "wretchedly", ["wistfully", "reluctantly", "gravely"]),
 ("Anne cried that this was the most ___ thing that had ever happened to her.", "tragical", ["sensible", "whitewashed", "bewitched"]),
 ("Anne said she couldn't eat, because she was in the depths of ___.", "despair", ["astonishment", "imagination", "curiosity"]),
 ("Anne ___ admitted that her real name was Anne Shirley, not Cordelia.", "reluctantly", ["wistfully", "wretchedly", "breathlessly"]),
 ("Marilla said that Anne was a good, plain, ___ name.", "sensible", ["tragical", "bewitched", "whitewashed"]),
 ("When Marilla questioned him, Matthew ___, \"Well, now, no, I suppose not—not exactly.\"", "stammered", ["bewitched", "despaired", "whitewashed"]),
 ("Marilla's ___ could not have been greater when Matthew hinted they might keep the girl.", "astonishment", ["despair", "curiosity", "consolation"]),
 ("\"I believe that child has ___ you!\" Marilla told Matthew.", "bewitched", ["stammered", "reluctant", "whitewashed"]),
 ("Left alone in the bare room, Anne looked around her ___.", "wistfully", ["placidly", "breathlessly", "awkwardly"]),
 ("The ___ walls of the little room were painfully bare.", "whitewashed", ["tragical", "sensible", "bewitched"]),
], discussion=[
 "Marilla wants to send Anne back because they asked for a boy. Do you think that is fair?",
 "Anne wants to be called Cordelia. If you could choose a different name, what would it be and why?",
]),

4: dict(vocab=[
 ("fragrance", "fragrance", "n.", "FRA-grance", "/ˈfreɪɡrəns/", "향기", "a sweet fragrance · the fragrance of", "The fragrance of roses filled the room.", "This soap has a fresh fragrance."),
 ("affliction", "affliction", "n.", "af-FLIC-tion", "/əˈflɪkʃən/", "고통, 고난", "bear an affliction · a terrible affliction", "She bore her affliction bravely.", "Poverty was the greatest affliction of the village."),
 ("ridiculous", "ridiculous", "adj.", "ri-DIC-u-lous", "/rɪˈdɪkjələs/", "말도 안 되는, 터무니없는", "look ridiculous · a ridiculous idea", "That hat looks ridiculous!", "It's ridiculous to pay that much for coffee."),
 ("sympathetic", "sympathetic", "adj.", "sym-pa-THET-ic", "/ˌsɪmpəˈθetɪk/", "공감하는, 동정적인", "a sympathetic listener · sympathetic to", "She was very sympathetic when I lost my job.", "He's a sympathetic listener."),
 ("kindred", "kindred", "adj.", "KIN-dred", "/ˈkɪndrəd/", "비슷한, 같은 성향의 (kindred spirit: 마음이 통하는 사람)", "a kindred spirit · kindred souls", "I knew at once that she was a kindred spirit.", "The two artists were kindred souls."),
 ("reverie", "reverie", "n.", "REV-er-ie", "/ˈrevəri/", "공상, 몽상", "lost in reverie · break someone's reverie", "She was lost in a pleasant reverie.", "The phone rang and broke his reverie."),
 ("relapse", "relapsed", "v.", "re-LAPSE", "/rɪˈlæps/", "(이전 상태로) 다시 빠지다", "relapse into silence · relapse into old habits", "After a short talk, he relapsed into silence.", "She relapsed into her old habit of biting her nails."),
 ("obediently", "obediently", "adv.", "o-BE-di-ent-ly", "/oʊˈbiːdiəntli/", "고분고분하게, 순종적으로", "follow obediently · sit obediently", "The dog sat obediently by the door.", "The children obediently lined up."),
 ("persistency", "persistency", "n.", "per-SIS-ten-cy", "/pərˈsɪstənsi/", "끈질김 (= persistence)", "with great persistency", "Her persistency finally paid off.", "Today we usually say \"persistence\"."),
 ("aggravating", "aggravating", "adj.", "AG-gra-vat-ing", "/ˈæɡrəveɪtɪŋ/", "짜증 나게 하는", "an aggravating habit · really aggravating", "It's aggravating when the bus is late.", "He has an aggravating habit of interrupting."),
], quiz=[
 ("The sweet ___ of the lilac trees drifted up to Anne's window.", "fragrance", ["affliction", "reverie", "persistency"]),
 ("Anne said it was easier to be cheerful and bear up under ___ on a sunny day.", "affliction", ["fragrance", "reverie", "persistency"]),
 ("Marilla said Matthew was a most ___ man for wanting to keep Anne.", "ridiculous", ["sympathetic", "kindred", "obedient"]),
 ("Anne disagreed and said Matthew was very ___; he didn't mind how much she talked.", "sympathetic", ["aggravating", "ridiculous", "obedient"]),
 ("Anne felt that Matthew was a ___ spirit as soon as she saw him.", "kindred", ["ridiculous", "aggravating", "obedient"]),
 ("After the meal, Anne came out of her ___ and offered to wash the dishes.", "reverie", ["affliction", "fragrance", "persistency"]),
 ("Anne had ___ into dreaming again, with her chin in her hand.", "relapsed", ["admonished", "stammered", "bewitched"]),
 ("When Marilla said she talked too much, Anne held her tongue so ___ that her silence made Marilla nervous.", "obediently", ["placidly", "wistfully", "breathlessly"]),
 ("Matthew clung to his wish with amazing silent ___.", "persistency", ["affliction", "fragrance", "reverie"]),
 ("Marilla thought nothing is more ___ than a man who won't talk back.", "aggravating", ["sympathetic", "kindred", "obedient"]),
], discussion=[
 "On a beautiful morning, Anne forgets her trouble for a while. Does good weather change your mood?",
 "Matthew says little but usually gets his way. Is silence a kind of power?",
]),

5: dict(vocab=[
 ("disgrace", "disgrace", "n.", "dis-GRACE", "/dɪsˈɡreɪs/", "망신, 수치", "a real disgrace · bring disgrace on", "The dirty streets are a disgrace.", "He felt he had brought disgrace on his family."),
 ("mercilessly", "mercilessly", "adv.", "MER-ci-less-ly", "/ˈmɜːrsɪləsli/", "무자비하게, 사정없이", "tease mercilessly · beat mercilessly", "His friends teased him mercilessly.", "The sun beat down mercilessly."),
 ("flush", "flushed", "v.", "FLUSH", "/flʌʃ/", "(얼굴이) 붉어지다", "flush with anger · flush red", "Her cheeks flushed with embarrassment.", "He flushed red when she smiled at him."),
 ("heroine", "heroine", "n.", "HER-o-ine", "/ˈheroʊɪn/", "여주인공, 여걸", "the heroine of the story · a national heroine", "The heroine of the novel is a brave nurse.", "She became a heroine after saving the child."),
 ("homeliest", "homeliest", "adj.", "HOME-li-est", "/ˈhoʊmliəst/", "가장 못생긴 (homely: 美 못생긴; 英 아늑한)", "a homely face", "In American English, \"homely\" can mean plain or not pretty.", "In British English, a \"homely\" room is warm and cozy."),
 ("scrawny", "scrawny", "adj.", "SCRAW-ny", "/ˈskrɔːni/", "비쩍 마른", "a scrawny cat · scrawny arms", "A scrawny cat was looking for food.", "He was a scrawny boy who grew into a strong man."),
 ("rapture", "rapture", "n.", "RAP-ture", "/ˈræptʃər/", "황홀감, 큰 기쁨", "in rapture · go into raptures", "The children listened in rapture.", "She went into raptures over the new dress."),
 ("ponder", "pondered", "v.", "PON-der", "/ˈpɑːndər/", "곰곰이 생각하다", "ponder a question · ponder over", "He pondered the question for a long time.", "She pondered whether to take the job."),
 ("drudgery", "drudgery", "n.", "DRUDG-er-y", "/ˈdrʌdʒəri/", "고되고 단조로운 일", "a life of drudgery · household drudgery", "Washing dishes by hand is pure drudgery.", "Machines took away much of the drudgery of farm work."),
 ("teachable", "teachable", "adj.", "TEACH-a-ble", "/ˈtiːtʃəbəl/", "가르치기 쉬운, 배우려는", "a teachable child · a teachable moment", "She is bright and teachable.", "A mistake can be a teachable moment."),
], quiz=[
 ("Anne said it would be a real ___ to have a father named Jedediah.", "disgrace", ["rapture", "drudgery", "heroine"]),
 ("When Anne asked if red hair could change color, Marilla answered ___ that it was not likely.", "mercilessly", ["ingenuously", "breathlessly", "placidly"]),
 ("Anne loved romantic things and liked to feel like a ___ in a book.", "heroine", ["disgrace", "rapture", "poverty"]),
 ("Mrs. Thomas said Anne was the ___ baby she had ever seen.", "homeliest", ["loveliest", "luckiest", "quietest"]),
 ("As a baby, Anne was so ___ and tiny that she was nothing but eyes.", "scrawny", ["ladylike", "teachable", "fragrant"]),
 ("When Marilla asked if those women had been good to her, Anne's face suddenly ___ scarlet.", "flushed", ["pondered", "relapsed", "stammered"]),
 ("On the shore road, Anne gave herself up to silent ___.", "rapture", ["drudgery", "poverty", "disgrace"]),
 ("Marilla guided the horse absent-mindedly while she ___ deeply.", "pondered", ["flushed", "relapsed", "stammered"]),
 ("Marilla saw that Anne had lived a starved, unloved life of ___ and poverty.", "drudgery", ["rapture", "heroine", "decorum"]),
 ("Marilla thought the child seemed a nice, ___ little thing.", "teachable", ["fractious", "flighty", "tragical"]),
], discussion=[
 "Anne had a hard childhood but still talks about beautiful things. How do you think she stays hopeful?",
 "Marilla begins to feel pity for Anne in this chapter. What changes her feelings?",
]),

6: dict(vocab=[
 ("benevolent", "benevolent", "adj.", "be-NEV-o-lent", "/bəˈnevələnt/", "인자한, 자비로운", "a benevolent smile · benevolent society", "The old man had a benevolent face.", "A benevolent stranger paid for our meal."),
 ("flighty", "flighty", "adj.", "FLIGHT-y", "/ˈflaɪti/", "변덕스러운, 경솔한", "a flighty girl · flighty behavior", "She was too flighty to finish anything.", "He's a bit flighty, so check his work."),
 ("providential", "providential", "adj.", "prov-i-DEN-tial", "/ˌprɑːvɪˈdenʃəl/", "하늘이 도운, 천만다행인", "a providential escape · positively providential", "The rain was providential for the farmers.", "Meeting her that day was providential."),
 ("shrewish", "shrewish", "adj.", "SHREW-ish", "/ˈʃruːɪʃ/", "잔소리 심한, 성질 사나운", "a shrewish wife · shrewish voice", "In old stories, the shrewish wife is always scolding.", "She answered in a sharp, shrewish voice."),
 ("stinginess", "stinginess", "n.", "STIN-gi-ness", "/ˈstɪndʒinəs/", "인색함", "famous for stinginess", "His stinginess annoyed his friends.", "She was known for her stinginess with money."),
 ("fractious", "fractious", "adj.", "FRAC-tious", "/ˈfrækʃəs/", "보채는, 짜증 잘 내는", "a fractious child · fractious mood", "The baby was fractious after the long trip.", "The meeting became fractious and loud."),
 ("fascinated", "fascinated", "adj.", "FAS-ci-nat-ed", "/ˈfæsɪneɪtɪd/", "매료된, (겁에 질려) 눈을 떼지 못하는", "be fascinated by · watch fascinated", "The children were fascinated by the magic show.", "She watched, fascinated, as the snake moved."),
 ("ungraciously", "ungraciously", "adv.", "un-GRA-cious-ly", "/ʌnˈɡreɪʃəsli/", "무뚝뚝하게, 불친절하게", "accept ungraciously · reply ungraciously", "He accepted the gift ungraciously.", "\"Fine,\" she said ungraciously."),
 ("transfigured", "transfigured", "adj.", "trans-FIG-ured", "/trænsˈfɪɡjərd/", "(기쁨으로) 완전히 변한, 빛나는", "transfigured with joy", "Her face was transfigured with joy.", "The old house was transfigured by fresh paint."),
 ("reprove", "reproved", "v.", "re-PROVE", "/rɪˈpruːv/", "꾸짖다, 나무라다", "reprove someone for · gently reprove", "The teacher reproved him for being late.", "She gently reproved her son."),
], quiz=[
 ("Mrs. Spencer came to the door with surprise and welcome on her ___ face.", "benevolent", ["shrewish", "fractious", "flighty"]),
 ("Mrs. Spencer blamed the mistake on Nancy, a terribly ___ girl.", "flighty", ["benevolent", "providential", "transfigured"]),
 ("Mrs. Spencer called Mrs. Blewett's arrival positively ___.", "providential", ["shrewish", "fractious", "ungracious"]),
 ("Marilla knew Mrs. Blewett only as a small, ___-faced woman.", "shrewish", ["benevolent", "transfigured", "providential"]),
 ("Servant girls told terrible tales of Mrs. Blewett's temper and ___.", "stinginess", ["fascination", "providence", "heedlessness"]),
 ("Mrs. Blewett said her baby was awfully ___ and she was worn out.", "fractious", ["benevolent", "providential", "transfigured"]),
 ("Anne stared at Mrs. Blewett as if ___, afraid she would be given to her.", "fascinated", ["reproved", "ungracious", "benevolent"]),
 ("\"I suppose it'll have to,\" said Mrs. Blewett ___.", "ungraciously", ["benevolently", "placidly", "ingenuously"]),
 ("When Marilla hinted they might keep her, Anne's face was quite ___ with hope.", "transfigured", ["reproved", "fascinated", "flighty"]),
 ("Marilla hid a smile, knowing Anne must be ___ for comparing Mrs. Blewett to a gimlet.", "reproved", ["transfigured", "fascinated", "providential"]),
], discussion=[
 "Marilla could easily give Anne to Mrs. Blewett, but she doesn't. Why do you think she changes her mind?",
 "Anne says Mrs. Blewett looks \"like a gimlet\" (a small sharp tool for making holes). What do you think she means?",
]),

7: dict(vocab=[
 ("admonish", "admonished", "v.", "ad-MON-ish", "/ədˈmɑːnɪʃ/", "타이르다, 훈계하다", "admonish someone for · gently admonish", "The teacher admonished the students for talking.", "\"Be careful,\" his mother admonished."),
 ("horrified", "horrified", "adj.", "HOR-ri-fied", "/ˈhɔːrɪfaɪd/", "몹시 놀란, 겁에 질린", "horrified at · a horrified look", "She was horrified at the price.", "He gave me a horrified look."),
 ("heathen", "heathen", "n.", "HEA-then", "/ˈhiːðən/", "(옛) 이교도; 교양 없는 사람", "a little heathen", "In old books, \"heathen\" meant someone with no religion.", "\"You little heathen!\" she laughed when he ate with his hands."),
 ("catechism", "catechism", "n.", "CAT-e-chism", "/ˈkætəkɪzəm/", "교리 문답", "learn the catechism", "The children learned the catechism at Sunday school.", "A catechism teaches religion through questions and answers."),
 ("gravely", "gravely", "adv.", "GRAVE-ly", "/ˈɡreɪvli/", "진지하게, 엄숙하게", "nod gravely · gravely ill", "The doctor nodded gravely.", "He spoke gravely about the danger."),
 ("embarrassed", "embarrassed", "adj.", "em-BAR-rassed", "/ɪmˈbærəst/", "당황한, 쑥스러운", "feel embarrassed · embarrassed about", "I felt embarrassed when I fell in the street.", "Don't be embarrassed to ask questions."),
 ("blessing", "blessings", "n.", "BLESS-ing", "/ˈblesɪŋ/", "축복, 감사할 일", "count your blessings · a mixed blessing", "Good health is a great blessing.", "Count your blessings, not your problems."),
 ("petition", "petition", "n.", "pe-TI-tion", "/pəˈtɪʃən/", "청원; (기도로) 간청", "sign a petition · a humble petition", "Hundreds of people signed the petition.", "Her prayer was a simple petition for help."),
 ("irreverence", "irreverence", "n.", "ir-REV-er-ence", "/ɪˈrevərəns/", "불경, 무례함", "a touch of irreverence · irreverence toward", "His jokes showed irreverence toward the rules.", "The comedian is known for his irreverence."),
 ("luxuriously", "luxuriously", "adv.", "lux-U-ri-ous-ly", "/lʌɡˈʒʊriəsli/", "호사스럽게, 아주 편안하게", "stretch luxuriously · luxuriously furnished", "The cat stretched luxuriously in the sun.", "The hotel room was luxuriously furnished."),
], quiz=[
 ("\"You'll have to remember a little better if you stay here,\" Marilla ___ as Anne folded her clothes.", "admonished", ["relapsed", "pondered", "flushed"]),
 ("When Anne said she never said prayers, Marilla looked at her in ___ astonishment.", "horrified", ["luxurious", "heathen", "grateful"]),
 ("Marilla was relieved to find that Anne wasn't quite a ___ after all.", "heathen", ["catechism", "petition", "blessing"]),
 ("At the asylum Sunday school, Anne had to learn the whole ___.", "catechism", ["petition", "heathen", "irreverence"]),
 ("Anne knelt at Marilla's knee and looked up ___.", "gravely", ["luxuriously", "mercilessly", "ungraciously"]),
 ("Marilla felt more ___ than ever, because she had meant to teach Anne a simple prayer.", "embarrassed", ["grateful", "luxurious", "admonished"]),
 ("Marilla told Anne to thank God for her ___ and humbly ask for the things she wanted.", "blessings", ["catechisms", "heathens", "irreverences"]),
 ("Marilla knew that Anne's strange ___ came from ignorance, not from disrespect.", "petition", ["catechism", "heathen", "blessing"]),
 ("Anne's odd prayer was not ___, but simply spiritual ignorance.", "irreverence", ["blessing", "petition", "catechism"]),
 ("With a clear conscience, Anne cuddled down ___ among her pillows.", "luxuriously", ["mercilessly", "ungraciously", "wretchedly"]),
], discussion=[
 "Anne says she would rather pray alone in a big field than kneel down. Where do you feel most peaceful?",
 "Marilla wants to laugh at Anne's prayer but feels she shouldn't. Why do adults sometimes hide their real reactions?",
]),

8: dict(vocab=[
 ("askance", "askance", "adv.", "a-SKANCE", "/əˈskæns/", "의심스럽게, 못마땅하게 (look askance at)", "look askance at", "Some people looked askance at his new idea.", "The waiter eyed our muddy boots askance."),
 ("intently", "intently", "adv.", "in-TENT-ly", "/ɪnˈtentli/", "골똘히, 열중하여", "listen intently · watch intently", "The students listened intently.", "The cat watched the bird intently."),
 ("reprimand", "reprimand", "n.", "REP-ri-mand", "/ˈreprɪmænd/", "질책, 꾸중", "a sharp reprimand · receive a reprimand", "He got a reprimand from his boss.", "She was let off with a reprimand."),
 ("catastrophe", "catastrophe", "n.", "ca-TAS-tro-phe", "/kəˈtæstrəfi/", "큰 재앙, 대참사", "a total catastrophe · avoid a catastrophe", "The flood was a catastrophe for the town.", "Forgetting the cake was a small catastrophe."),
 ("irresistible", "irresistible", "adj.", "ir-re-SIS-ti-ble", "/ˌɪrɪˈzɪstəbəl/", "거부할 수 없는", "an irresistible urge · irresistible smell", "The smell of fresh bread was irresistible.", "She felt an irresistible urge to laugh."),
 ("discourse", "discourse", "v. / n.", "dis-COURSE", "/dɪsˈkɔːrs/", "(길게) 이야기하다 / 담론", "discourse on · public discourse", "He loves to discourse on politics.", "There is little polite discourse online."),
 ("mooning", "mooning", "n. / v.", "MOON-ing", "/ˈmuːnɪŋ/", "멍하니 공상에 잠기기 (moon about)", "moon about · moon over", "Stop mooning about and help me!", "He spent the day mooning over old photos."),
 ("confide", "confide", "v.", "con-FIDE", "/kənˈfaɪd/", "(비밀을) 털어놓다", "confide in someone · confide a secret", "She confided in her sister.", "He confided his fears to his best friend."),
 ("consolation", "consolation", "n.", "con-so-LA-tion", "/ˌkɑːnsəˈleɪʃən/", "위안, 위로", "a great consolation · a consolation prize", "Her letters were a great consolation to me.", "If it's any consolation, I failed too."),
 ("bewilderment", "bewilderment", "n.", "be-WIL-der-ment", "/bɪˈwɪldərmənt/", "어리둥절함, 당혹", "in bewilderment · a look of bewilderment", "He stared at the map in bewilderment.", "She shook her head in bewilderment."),
], quiz=[
 ("When Marilla said she could stay, Anne began to cry and said, in a tone of ___, \"I can't think why.\"", "bewilderment", ["consolation", "discourse", "catastrophe"]),
 ("Marilla had looked ___ at the flowers Anne put on the table, but said nothing.", "askance", ["luxuriously", "mercilessly", "placidly"]),
 ("Anne studied the prayer card ___ for several silent minutes.", "intently", ["ungraciously", "wretchedly", "mercilessly"]),
 ("Anne would dream until she was called back to earth by a ___ from Marilla.", "reprimand", ["consolation", "discourse", "bewilderment"]),
 ("Anne's daydreams often ended with a scolding or a small ___ in the kitchen.", "catastrophe", ["consolation", "bewilderment", "discourse"]),
 ("Anne said picking the apple blossom was wrong, but the temptation was ___.", "irresistible", ["teachable", "tragical", "sensible"]),
 ("Marilla told Anne to obey at once and not stand still and ___ about it.", "discourse", ["confide", "reprimand", "bewilder"]),
 ("Marilla said Anne must not fall into ___ and imagining in front of pictures.", "mooning", ["admonishing", "stammering", "reproving"]),
 ("Anne longed for a bosom friend to whom she could ___ her inmost soul.", "confide", ["reprimand", "bewitch", "admonish"]),
 ("Katie Maurice, the girl Anne saw in the bookcase glass, was the comfort and ___ of her life.", "consolation", ["catastrophe", "reprimand", "bewilderment"]),
], discussion=[
 "Anne had an imaginary friend, Katie Maurice. Did you have an imaginary friend or a favorite toy as a child?",
 "Anne cries when Marilla says she can stay. Why do people sometimes cry when they are happy?",
]),
}

OLD = {
 "fiddlesticks": ("감탄사", "(옛) 말도 안 돼!, 흥!", "An old-fashioned way to say \"Nonsense!\". Marilla uses it to show she thinks Anne's romantic ideas are silly."),
 "thee": ("대명사", "(옛말) 당신을, 주님을 (= you)", "Old form of \"you\", still used in some prayers. Anne's prayer uses it, so it is kept: \"I thank Thee\" = \"I thank You\"."),
}
IDIOMS = {
 "by dint of": ("~의 힘으로, ~ 덕분에", "by means of / because of", "Today: thanks to, through (She passed by dint of hard work → She passed through hard work)."),
 "bosom friend": ("단짝, 가장 친한 친구", "best friend / close friend", "Anne uses this old-fashioned phrase often. Today we say \"best friend\"."),
}
OLD_MARKS = {3: ["fiddlesticks"], 7: ["Thee"]}
IDIOM_MARKS = {1: ["by dint of"], 8: ["bosom friend"]}

# ---- put word cards and questions in story order ----
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
