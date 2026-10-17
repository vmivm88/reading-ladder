# Anne of Green Gables workbook, chapters 33–38. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
33: dict(vocab=[
 ("inhospitable", "inhospitable", "adj.", "in-hos-PIT-a-ble", "/ˌɪnhɑːˈspɪtəbl/", "쌀쌀맞은, 살기 힘든", "an inhospitable place · inhospitable climate", "The desert is an inhospitable place.", "The hotel staff were cold and inhospitable."),
 ("lament", "lamented", "v.", "la-MENT", "/ləˈment/", "슬퍼하다, 아쉬워하다", "lament the loss of · lament that", "She lamented the loss of her old house.", "Fans lamented the end of the series."),
 ("gratified", "gratified", "adj.", "GRAT-i-fied", "/ˈɡrætɪfaɪd/", "흐뭇한, 만족한", "be gratified by · a gratified smile", "I was gratified by the warm response.", "The teacher looked gratified."),
 ("unenvious", "unenvious", "adj.", "un-EN-vi-ous", "/ʌnˈenviəs/", "질투하지 않는", "unenvious admiration · an unenvious friend", "She praised her sister with unenvious joy.", "A true friend is unenvious of your success."),
 ("scrutinize", "scrutinized", "v.", "SCRU-ti-nize", "/ˈskruːtənaɪz/", "면밀히 살펴보다", "scrutinize closely · be scrutinized", "The officer scrutinized my passport.", "Every word of the contract was scrutinized."),
 ("audibly", "audibly", "adv.", "AU-di-bly", "/ˈɔːdəbli/", "들릴 만큼, 들리게", "sigh audibly · laugh audibly", "He sighed audibly during the speech.", "The crowd gasped audibly."),
 ("languidly", "languidly", "adv.", "LAN-guid-ly", "/ˈlæŋɡwɪdli/", "나른하게, 느긋하게", "move languidly · stretch languidly", "The cat stretched languidly in the sun.", "She waved languidly from the sofa."),
 ("paralyze", "paralyzed", "v.", "PAR-a-lyze", "/ˈpærəlaɪz/", "마비시키다, 꼼짝 못 하게 하다", "paralyzed with fear · paralyze traffic", "I was paralyzed with fear.", "The snow paralyzed the city."),
 ("taunting", "taunting", "adj.", "TAUNT-ing", "/ˈtɔːntɪŋ/", "조롱하는, 약 올리는", "a taunting smile · taunting words", "He gave me a taunting smile.", "The fans shouted taunting songs."),
 ("captivate", "captivated", "v.", "CAP-ti-vate", "/ˈkæptɪveɪt/", "마음을 사로잡다", "captivate an audience · be captivated by", "The singer captivated the audience.", "I was captivated by the view."),
], quiz=[
 ("Four years ago the east gable's bareness had chilled Anne with its ___ feel.", "inhospitable", ["hospitable", "inhabitable", "invisible"]),
 ("Anne never got her velvet carpet, but her dreams had grown with her, and it is not likely she ___ them.", "lamented", ["laminated", "lightened", "limited"]),
 ("Matthew was in the seventh heaven of ___ pride over the honor given to his Anne.", "gratified", ["gratuitous", "granted", "graceful"]),
 ("\"There's something so stylish about you, Anne,\" said Diana, with ___ admiration.", "unenvious", ["unanimous", "unconscious", "unenthusiastic"]),
 ("A stout lady stared at Anne through her eyeglasses until Anne, hating to be so ___, felt she must scream.", "scrutinized", ["sanitized", "summarized", "satirized"]),
 ("A girl in white lace kept talking ___ about the \"country bumpkins\" in the audience.", "audibly", ["audaciously", "awfully", "auditorily"]),
 ("The white-lace girl ___ looked forward to \"such fun\" from the local performers.", "languidly", ["lavishly", "loudly", "lovingly"]),
 ("Anne had stage fright, and the brilliant audience ___ her energies completely.", "paralyzed", ["paraphrased", "parked", "polished"]),
 ("Anne thought Gilbert's smile was triumphant and ___, but he was only enjoying the show.", "taunting", ["tempting", "touching", "trusting"]),
 ("For her encore, Anne gave a funny little piece that ___ the audience even more.", "captivated", ["cultivated", "calculated", "captioned"]),
], discussion=[
 "Anne almost froze with stage fright until she saw Gilbert smiling. Have you ever been saved from nervousness by something unexpected?",
 "On the way home, Anne says she doesn't envy the rich people at the hotel. What does it mean to be rich in Anne's way?",
]),
34: dict(vocab=[
 ("preposterous", "preposterous", "adj.", "pre-POS-ter-ous", "/prɪˈpɑːstərəs/", "터무니없는, 말도 안 되는", "a preposterous idea · simply preposterous", "The price is preposterous.", "It's preposterous to think he stole it."),
 ("agitatedly", "agitatedly", "adv.", "AG-i-tat-ed-ly", "/ˈædʒɪteɪtɪdli/", "불안하게, 초조하게", "pace agitatedly · speak agitatedly", "He paced agitatedly up and down the hall.", "She spoke agitatedly on the phone."),
 ("outwardly", "outwardly", "adv.", "OUT-ward-ly", "/ˈaʊtwərdli/", "겉으로는, 외견상", "outwardly calm · change outwardly", "Outwardly calm, he was nervous inside.", "The house looks the same outwardly."),
 ("tolerably", "tolerably", "adv.", "TOL-er-a-bly", "/ˈtɑːlərəbli/", "그런대로, 꽤", "tolerably well · tolerably good", "I speak French tolerably well.", "The food was tolerably good."),
 ("appall", "appalled", "v.", "ap-PALL", "/əˈpɔːl/", "몹시 놀라게 하다, 질겁하게 하다", "be appalled by · appalled at", "I was appalled by the dirty kitchen.", "She was appalled at his rudeness."),
 ("pessimistically", "pessimistically", "adv.", "pes-si-MIS-ti-cal-ly", "/ˌpesɪˈmɪstɪkli/", "비관적으로", "think pessimistically · say pessimistically", "\"We'll never win,\" he said pessimistically.", "Don't look at things so pessimistically."),
 ("undeniably", "undeniably", "adv.", "un-de-NI-a-bly", "/ˌʌndɪˈnaɪəbli/", "부인할 수 없이, 분명히", "undeniably true · undeniably beautiful", "She is undeniably talented.", "It was undeniably the best day of the trip."),
 ("objectionable", "objectionable", "adj.", "ob-JEC-tion-a-ble", "/əbˈdʒekʃənəbl/", "불쾌한, 못마땅한", "objectionable behavior · find something objectionable", "Some viewers found the joke objectionable.", "He removed the objectionable words."),
 ("homesickness", "homesickness", "n.", "HOME-sick-ness", "/ˈhoʊmsɪknəs/", "향수병", "suffer from homesickness · a wave of homesickness", "Homesickness hit me on my first night abroad.", "Letters from home eased his homesickness."),
 ("broaden", "broadened", "v.", "BROAD-en", "/ˈbrɔːdn/", "넓히다, 넓어지다", "broaden your horizons · broaden your mind", "Travel broadens your horizons.", "The road broadens after the bridge."),
], quiz=[
 ("Marilla remembered the odd, frightened child in her ___ yellowish-brown dress.", "preposterous", ["prosperous", "prestigious", "posterior"]),
 ("Matthew went outside and walked ___ across the yard to the gate.", "agitatedly", ["accurately", "aggressively", "affectionately"]),
 ("\"It won't make a bit of difference how much I change ___,\" Anne said; at heart she would always be the same.", "outwardly", ["outright", "awkwardly", "inwardly"]),
 ("After Anne left, Diana went to a beach picnic and enjoyed herself ___ well.", "tolerably", ["terribly", "tenderly", "totally"]),
 ("That night Marilla wept so wildly that she was ___ when she grew calm and thought about it.", "appalled", ["appealed", "applied", "applauded"]),
 ("Knowing Gilbert the way she did did not help her much, Anne thought ___.", "pessimistically", ["philosophically", "patriotically", "practically"]),
 ("Yet she was ___ glad that she and Gilbert were in the same class.", "undeniably", ["unbearably", "unusually", "unwillingly"]),
 ("Miss Barry said Anne would not meet any ___ people at the boardinghouse.", "objectionable", ["objective", "obtainable", "observable"]),
 ("Anne's narrow little room did nothing to help the first agony of ___ that seized her.", "homesickness", ["homelessness", "hopelessness", "helpfulness"]),
 ("When Josie mentioned the Avery scholarship, the horizons of Anne's ambition shifted and ___.", "broadened", ["brightened", "broken", "bordered"]),
], discussion=[
 "Anne tells Marilla, \"I'm not a bit changed—not really.\" How have you changed since you were a teenager? What part of you has stayed the same?",
 "Anne feels terribly homesick in her first days at Queen's. Have you ever lived away from home? What helped you feel better?",
]),
35: dict(vocab=[
 ("profitably", "profitably", "adv.", "PROF-it-a-bly", "/ˈprɑːfɪtəbli/", "유익하게; 이익이 나게", "use time profitably · run profitably", "Use your free time profitably.", "The shop is now running profitably."),
 ("gravitate", "gravitated", "v.", "GRAV-i-tate", "/ˈɡrævɪteɪt/", "(자연스레) 끌리다, 모이다", "gravitate toward · gravitate to", "At parties, I gravitate toward the kitchen.", "Young people gravitate to big cities."),
 ("individuality", "individuality", "n.", "in-di-vid-u-AL-i-ty", "/ˌɪndɪˌvɪdʒuˈæləti/", "개성", "express your individuality · a strong individuality", "Her clothes show her individuality.", "School uniforms can hide individuality."),
 ("competent", "competent", "adj.", "COM-pe-tent", "/ˈkɑːmpɪtənt/", "유능한, 자격 있는", "a competent driver · competent at", "He is a competent manager.", "She is competent at her job."),
 ("plodding", "plodding", "adj.", "PLOD-ding", "/ˈplɑːdɪŋ/", "꾸준하지만 느린, 터벅터벅 걷는", "a plodding worker · plodding pace", "He's a plodding student, but he never gives up.", "The story moves at a plodding pace."),
 ("preeminence", "preeminence", "n.", "pre-EM-i-nence", "/priˈemɪnəns/", "탁월함, 두드러짐", "achieve preeminence · preeminence in", "The city achieved preeminence in trade.", "Her preeminence in the field is clear."),
 ("insupportable", "insupportable", "adj.", "in-sup-PORT-a-ble", "/ˌɪnsəˈpɔːrtəbl/", "견딜 수 없는", "insupportable pain · find something insupportable", "The heat became insupportable.", "Life without music would be insupportable."),
 ("belittle", "belittling", "v.", "be-LIT-tle", "/bɪˈlɪtl/", "하찮게 여기다, 깎아내리다", "belittle someone's work · stop belittling", "Don't belittle your own achievements.", "He always belittles my ideas."),
 ("philosophically", "philosophically", "adv.", "phil-o-SOPH-i-cal-ly", "/ˌfɪləˈsɑːfɪkli/", "달관하여, 침착하게; 철학적으로", "take it philosophically · accept philosophically", "He took the bad news philosophically.", "She accepted the loss philosophically."),
 ("optimism", "optimism", "n.", "OP-ti-mism", "/ˈɑːptɪmɪzəm/", "낙관(주의)", "cautious optimism · full of optimism", "There is a mood of optimism in the office.", "Her optimism is contagious."),
], quiz=[
 ("Ruby Gillis did not seem the sort of person with whom Gilbert's ambitions could be ___ discussed.", "profitably", ["probably", "properly", "proudly"]),
 ("After Christmas, all the Queen's students had ___ into their own places in the ranks.", "gravitated", ["graduated", "gratified", "aggravated"]),
 ("The classes had settled into distinct shades of ___.", "individuality", ["individual", "inequality", "indignity"]),
 ("Ethel Marr was said by all ___ judges to have the most stylish hairstyles.", "competent", ["compliant", "complacent", "convenient"]),
 ("Jane Andrews—plain, ___, conscientious Jane—won the honors in domestic science.", "plodding", ["plotting", "pleading", "plucking"]),
 ("Even Josie Pye gained a certain ___ as the sharpest-tongued girl at Queen's.", "preeminence", ["permanence", "pertinence", "preference"]),
 ("Anne no longer thought life would be ___ if she did not win.", "insupportable", ["unsupported", "insuperable", "irresistible"]),
 ("Anne, sure of passing, could have her moments of ___ the exams.", "belittling", ["befitting", "believing", "belonging"]),
 ("When your whole future depended on the exams, you could not regard them ___.", "philosophically", ["photographically", "physically", "phonetically"]),
 ("Anne wove dreams of the future from the golden tissue of youth's ___.", "optimism", ["organism", "criticism", "optimum"]),
], discussion=[
 "Anne no longer wants to win just to beat Gilbert, but for a \"well-won victory.\" What is the difference? Which motivates you more?",
 "Jane worries about exams so much that she loses weight, while Anne stays calmer. How do you deal with stress before a big test or deadline?",
]),
36: dict(vocab=[
 ("bulletin", "bulletin", "n.", "BUL-le-tin", "/ˈbʊlətɪn/", "게시, 공지; 뉴스 단신", "a bulletin board · a news bulletin", "The results were posted on the bulletin board.", "We heard the news bulletin on the radio."),
 ("anxiety", "anxiety", "n.", "anx-I-e-ty", "/æŋˈzaɪəti/", "불안, 걱정", "feel anxiety · anxiety about", "She felt anxiety before the interview.", "There is a lot of anxiety about the economy."),
 ("discouragement", "discouragement", "n.", "dis-COUR-age-ment", "/dɪsˈkɜːrɪdʒmənt/", "낙담, 좌절", "feel discouragement · despite discouragement", "Despite discouragement, he kept trying.", "Learning a language has moments of discouragement."),
 ("congratulate", "congratulating", "v.", "con-GRAT-u-late", "/kənˈɡrætʃuleɪt/", "축하하다", "congratulate someone on", "Let me congratulate you on your new job.", "Everyone congratulated her on the baby."),
 ("studious", "studious", "adj.", "STU-di-ous", "/ˈstuːdiəs/", "학구적인, 공부를 열심히 하는", "a studious child · studious habits", "My brother was always studious.", "The library has a quiet, studious feel."),
 ("hesitatingly", "hesitatingly", "adv.", "HES-i-tat-ing-ly", "/ˈhezɪteɪtɪŋli/", "머뭇거리며", "speak hesitatingly · answer hesitatingly", "\"Can I ask something?\" she said hesitatingly.", "He hesitatingly raised his hand."),
 ("nominal", "nominal", "adj.", "NOM-i-nal", "/ˈnɑːmɪnl/", "이름뿐인, 명목상의; 아주 적은", "nominal head · a nominal fee", "The king is only the nominal ruler.", "They charge a nominal fee of one dollar."),
 ("institution", "institution", "n.", "in-sti-TU-tion", "/ˌɪnstɪˈtuːʃən/", "기관, 단체", "a financial institution · educational institutions", "Banks are financial institutions.", "The university is an old institution."),
 ("mistily", "mistily", "adv.", "MIST-i-ly", "/ˈmɪstɪli/", "안개 낀 듯 흐릿하게", "shine mistily · smile mistily", "The lights shone mistily through the fog.", "She smiled mistily, holding back tears."),
 ("sanctify", "sanctifying", "v.", "SANC-ti-fy", "/ˈsæŋktɪfaɪ/", "신성하게 하다, 성스럽게 만들다", "sanctify a place · sanctified by", "The old church was sanctified long ago.", "Their love was sanctified by marriage."),
], quiz=[
 ("The final results were to be posted on the ___ board at Queen's.", "bulletin", ["bullet", "billboard", "button"]),
 ("Ambitions are worth having, but they cost work, self-denial, ___ and discouragement.", "anxiety", ["anatomy", "antiquity", "variety"]),
 ("We pay for every ambition with hard work and moments of ___.", "discouragement", ["encouragement", "disagreement", "disappointment"]),
 ("Anne became the center of a laughing, ___ group of girls.", "congratulating", ["concentrating", "consolidating", "complicating"]),
 ("Back home, Anne told Diana she was tired of being ___ and ambitious.", "studious", ["stupid", "stubborn", "spacious"]),
 ("\"Marilla,\" Anne said ___ when Matthew had gone out, \"is Matthew quite well?\"", "hesitatingly", ["hastily", "heartily", "hopefully"]),
 ("Anne said old Mr. Abbey had only been the ___ head of the bank for many years.", "nominal", ["normal", "noble", "minimal"]),
 ("His nephews were really at the head of the ___.", "institution", ["instruction", "intuition", "constitution"]),
 ("Outside, the Snow Queen cherry tree was ___ white in the moonshine.", "mistily", ["mostly", "mightily", "messily"]),
 ("It was the last night before sorrow touched her life with its cold, ___ touch.", "sanctifying", ["satisfying", "signifying", "terrifying"]),
], discussion=[
 "Anne wins the Avery scholarship, but she worries about Matthew's health. Why does the author put a happy event and a worry so close together?",
 "Anne says she is tired of being \"studious and ambitious\" for a while. Do you ever need a break from your goals? What do you do?",
]),
37: dict(vocab=[
 ("instantaneous", "instantaneous", "adj.", "in-stan-TA-ne-ous", "/ˌɪnstənˈteɪniəs/", "즉각적인", "an instantaneous reaction · instantaneous death", "The effect of the medicine was instantaneous.", "Her reply was almost instantaneous."),
 ("likelihood", "likelihood", "n.", "LIKE-li-hood", "/ˈlaɪklihʊd/", "가능성", "in all likelihood · the likelihood of", "In all likelihood, it will rain tomorrow.", "What is the likelihood of winning?"),
 ("throng", "thronged", "v./n.", "THRONG", "/θrɔːŋ/", "(사람들이) 몰려들다; 군중", "thronged with · a throng of people", "Tourists thronged the square.", "A throng of fans waited outside."),
 ("anguished", "anguished", "adj.", "AN-guished", "/ˈæŋɡwɪʃt/", "몹시 괴로워하는", "an anguished cry · anguished eyes", "We heard an anguished cry from the house.", "She gave me an anguished look."),
 ("tearless", "tearless", "adj.", "TEAR-less", "/ˈtɪrləs/", "눈물 없는", "tearless grief · tearless eyes", "Her grief was silent and tearless.", "He stood by the grave, tearless."),
 ("impassioned", "impassioned", "adj.", "im-PAS-sioned", "/ɪmˈpæʃənd/", "열정적인, 격렬한", "an impassioned speech · impassioned grief", "She made an impassioned speech.", "His impassioned plea moved everyone."),
 ("placidity", "placidity", "n.", "pla-CID-i-ty", "/pləˈsɪdəti/", "평온함", "calm placidity · return to placidity", "The lake returned to its usual placidity.", "I admire her placidity in a crisis."),
 ("disloyalty", "disloyalty", "n.", "dis-LOY-al-ty", "/dɪsˈlɔɪəlti/", "불충, 배신", "an act of disloyalty · accuse of disloyalty", "He saw it as disloyalty to the team.", "She felt guilty, as if it were disloyalty."),
 ("benediction", "benediction", "n.", "ben-e-DIC-tion", "/ˌbenɪˈdɪkʃən/", "축복, 축복 기도", "give a benediction · like a benediction", "The priest gave the benediction.", "The warm sun felt like a benediction."),
 ("absently", "absently", "adv.", "AB-sent-ly", "/ˈæbsəntli/", "멍하니, 무심코", "nod absently · say absently", "He nodded absently, still reading.", "She absently stirred her tea."),
], quiz=[
 ("The doctor said Matthew's death had been ___ and probably painless.", "instantaneous", ["simultaneous", "spontaneous", "miscellaneous"]),
 ("It was caused in all ___ by a sudden shock—the news of the Abbey Bank failure.", "likelihood", ["livelihood", "neighborhood", "falsehood"]),
 ("All day friends and neighbors ___ Green Gables on errands of kindness.", "thronged", ["thanked", "thrilled", "throttled"]),
 ("Anne brought Matthew's favorite flowers, her ___ eyes burning in her white face.", "anguished", ["anticipated", "angled", "distinguished"]),
 ("Anne's grief was ___ at first; she could not cry.", "tearless", ["fearless", "careless", "tireless"]),
 ("Diana could understand Marilla's ___ grief better than Anne's silent pain.", "impassioned", ["impatient", "impressed", "imprisoned"]),
 ("After the funeral, Avonlea settled back to its usual ___.", "placidity", ["popularity", "plasticity", "publicity"]),
 ("Anne felt it was a kind of ___ to Matthew to enjoy beautiful things now that he was gone.", "disloyalty", ["royalty", "disability", "dishonesty"]),
 ("Anne liked the honeysuckle in her hair, like a gentle ___ above her.", "benediction", ["prediction", "contradiction", "addiction"]),
 ("\"What a nice-looking fellow he is,\" said Marilla ___ about Gilbert.", "absently", ["abundantly", "absolutely", "accidentally"]),
], discussion=[
 "Anne couldn't cry at first, but cried at night when she remembered Matthew's words. Why do people grieve in such different ways?",
 "Anne feels guilty for enjoying life after Matthew's death. What would you tell her? What did Mrs. Allan tell her?",
]),
38: dict(vocab=[
 ("heaviness", "heaviness", "n.", "HEAV-i-ness", "/ˈhevinəs/", "무거움; 우울함", "heaviness of heart · a feeling of heaviness", "She went to bed with a heaviness of heart.", "There was a heaviness in the air before the storm."),
 ("courageously", "courageously", "adv.", "cou-RA-geous-ly", "/kəˈreɪdʒəsli/", "용감하게", "act courageously · fight courageously", "She courageously spoke out against the plan.", "He faced his illness courageously."),
 ("prohibition", "prohibition", "n.", "pro-hi-BI-tion", "/ˌproʊəˈbɪʃən/", "금지", "a prohibition on · strict prohibition", "There is a prohibition on smoking here.", "The doctor's prohibition on sweets was hard to follow."),
 ("substantial", "substantial", "adj.", "sub-STAN-tial", "/səbˈstænʃəl/", "상당한; 덩치가 큰, 튼튼한", "a substantial amount · a substantial meal", "We had a substantial breakfast.", "She earns a substantial salary."),
 ("weariness", "weariness", "n.", "WEA-ri-ness", "/ˈwɪrinəs/", "피로, 지침", "a feeling of weariness · weariness and relief", "After the long trip, weariness hit me.", "She sighed with weariness."),
 ("vocation", "vocation", "n.", "vo-CA-tion", "/voʊˈkeɪʃən/", "천직, 소명; 적성", "a vocation for · find your vocation", "Teaching is her true vocation.", "I have no vocation for cooking."),
 ("sacrifice", "sacrificing", "v./n.", "SAC-ri-fice", "/ˈsækrɪfaɪs/", "희생하다; 희생", "sacrifice something for · make sacrifices", "Parents sacrifice a lot for their children.", "He sacrificed his free time to help."),
 ("jubilantly", "jubilantly", "adv.", "JU-bi-lant-ly", "/ˈdʒuːbɪləntli/", "환호하며, 몹시 기뻐하며", "shout jubilantly · celebrate jubilantly", "The fans shouted jubilantly.", "\"We did it!\" she said jubilantly."),
 ("thwart", "thwarted", "v.", "THWART", "/θwɔːrt/", "좌절시키다, 방해하다", "thwart a plan · be thwarted", "The police thwarted the robbery.", "Bad weather thwarted our plans."),
 ("congenial", "congenial", "adj.", "con-GEN-ial", "/kənˈdʒiːniəl/", "마음이 맞는, 쾌적한", "congenial company · a congenial atmosphere", "We spent the evening in congenial company.", "The office has a congenial atmosphere."),
], quiz=[
 ("Anne sat alone at her window in the dark with her tears and her ___ of heart.", "heaviness", ["happiness", "heartiness", "holiness"]),
 ("Anne looked her duty ___ in the face and found it a friend.", "courageously", ["contagiously", "cautiously", "conspicuously"]),
 ("Marilla had tears in her eyes, in spite of the eye doctor's ___ against crying.", "prohibition", ["probation", "production", "provision"]),
 ("Mrs. Rachel sat her ___ body down on the stone bench by the door.", "substantial", ["substitute", "superficial", "sensational"]),
 ("Mrs. Rachel let out a long breath of mixed ___ and relief.", "weariness", ["wariness", "wildness", "wetness"]),
 ("Anne said she had no ___ for fancy work, so she would teach at Carmody instead.", "vocation", ["vacation", "location", "vibration"]),
 ("Mrs. Rachel said it was real kind and self-___ of Gilbert to give up the Avonlea school.", "sacrificing", ["satisfying", "sanctifying", "surprising"]),
 ("\"We are going to be the best of friends,\" said Gilbert ___.", "jubilantly", ["jealously", "jokingly", "judiciously"]),
 ("\"You've ___ destiny enough,\" Gilbert told Anne.", "thwarted", ["thawed", "twisted", "thrown"]),
 ("Anne knew the joy of sincere work and ___ friendship would be hers.", "congenial", ["congenital", "general", "congested"]),
], discussion=[
 "Anne gives up the Avery scholarship to stay with Marilla. Was it the right choice? Have you ever given up an opportunity for someone you love?",
 "Anne says, \"the bend in the road\"—you can't see what's around it, but something good may be there. Has a sudden change in your life led to something good?",
]),
}

OLD = {
 "methinks": ("동사구", "(옛) 내 생각엔 (= I think)", "Priscilla says \"methinks\" as a playful, old-fashioned joke. Today: \"I think I see tears.\""),
 "kerwollowps": ("명사(속어)", "(옛 장난 말) 두근거림", "A made-up, joking word: \"His moustache would give you kerwollowps of the heart\" = it would make your heart flutter. No modern word—just fun slang of 1908 school girls."),
 "mejum": ("형용사(사투리)", "(사투리) = medium, 적당한", "Anne quotes a funny character from a popular book who spells \"medium\" the way she says it. She means she will be moderate."),
}
IDIOMS = {
 "seventh heaven": ("더없이 행복한 상태", "extremely happy", "Still used today: \"She was in seventh heaven when she got the job.\""),
 "carried off the palm": ("1등을 차지했다", "won the prize / was the best", "In ancient times winners got a palm branch. Today: \"She won first place for beauty.\""),
}
OLD_MARKS = {34: ["methinks", "kerwollowps"], 38: ["mejum"]}
IDIOM_MARKS = {33: ["seventh heaven"], 35: ["carried off the palm"]}

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
