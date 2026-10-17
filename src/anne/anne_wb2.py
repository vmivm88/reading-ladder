# Anne of Green Gables workbook, chapters 9–16. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
9: dict(vocab=[
 ("dumbfounded", "dumbfounded", "adj.", "dumb-FOUND-ed", "/ˌdʌmˈfaʊndɪd/", "너무 놀라 말문이 막힌", "be dumbfounded · a dumbfounded look", "I was dumbfounded when she quit her job.", "He stood there, dumbfounded, holding the letter."),
 ("indignation", "indignation", "n.", "in-dig-NA-tion", "/ˌɪndɪɡˈneɪʃən/", "분개, 분노", "full of indignation · in indignation", "She refused the offer with indignation.", "The new tax caused public indignation."),
 ("consternation", "consternation", "n.", "con-ster-NA-tion", "/ˌkɑːnstərˈneɪʃən/", "깜짝 놀람, 당황", "in consternation · cause consternation", "To my consternation, the door was locked.", "The news caused consternation in the office."),
 ("outspoken", "outspoken", "adj.", "out-SPO-ken", "/aʊtˈspoʊkən/", "거침없이 말하는", "an outspoken critic · outspoken about", "She is outspoken about women's rights.", "My grandmother was always outspoken."),
 ("humiliation", "humiliation", "n.", "hu-mil-i-A-tion", "/hjuːˌmɪliˈeɪʃən/", "굴욕, 창피", "feel humiliation · a public humiliation", "Losing 10–0 was a real humiliation.", "He could not hide his humiliation."),
 ("defiant", "defiant", "adj.", "de-FI-ant", "/dɪˈfaɪənt/", "반항적인", "a defiant look · remain defiant", "The boy gave his teacher a defiant look.", "She stayed defiant even after the warning."),
 ("impolite", "impolite", "adj.", "im-po-LITE", "/ˌɪmpəˈlaɪt/", "무례한", "impolite to · an impolite question", "It's impolite to talk with your mouth full.", "Asking someone's salary can be impolite."),
 ("abashed", "abashed", "adj.", "a-BASHED", "/əˈbæʃt/", "당황한, 부끄러워하는", "look abashed · feel abashed", "He looked abashed when we caught him.", "She felt abashed by all the praise."),
 ("emphatic", "emphatic", "adj.", "em-PHAT-ic", "/ɪmˈfætɪk/", "단호한, 강하게 말하는", "an emphatic no · emphatic about", "Her answer was an emphatic \"No!\"", "He was emphatic that he had told the truth."),
 ("gloomily", "gloomily", "adv.", "GLOOM-i-ly", "/ˈɡluːmɪli/", "우울하게, 침울하게", "say gloomily · stare gloomily", "\"It's going to rain again,\" he said gloomily.", "She stared gloomily out of the window."),
], quiz=[
 ("Anne ran in from the orchard, but she was ___ to find a stranger there and stopped inside the door.", "abashed", ["amused", "defiant", "outspoken"]),
 ("\"Well, they didn't pick you for your looks,\" was Mrs. Rachel's ___ comment.", "emphatic", ["empty", "elastic", "energetic"]),
 ("Anne stood up to Mrs. Rachel with blazing eyes, full of passionate ___.", "indignation", ["humiliation", "consternation", "decoration"]),
 ("Anne called Mrs. Rachel a rude, ___, unfeeling woman.", "impolite", ["impatient", "important", "imperfect"]),
 ("\"Anne, go to your room!\" Marilla exclaimed in ___.", "consternation", ["conversation", "constellation", "concentration"]),
 ("Looking at Mrs. Rachel's ___ face, Marilla felt a strange desire to laugh.", "dumbfounded", ["delighted", "defiant", "dignified"]),
 ("Mrs. Rachel said ___ that bringing up a child is hard when you've never had any experience.", "gloomily", ["greedily", "gladly", "gracefully"]),
 ("Marilla felt more ___ over Anne's behavior than sorrow about her bad temper.", "humiliation", ["hesitation", "imagination", "admiration"]),
 ("\"She hadn't any right to call me ugly and redheaded,\" Anne answered in a ___ way.", "defiant", ["delicate", "distant", "decent"]),
 ("Marilla privately thought that Rachel is too ___ and says too much.", "outspoken", ["outgoing", "outdated", "outlined"]),
], discussion=[
 "Mrs. Rachel said Anne was skinny and her hair was \"as red as carrots.\" Was Anne right to get so angry? How would you have reacted?",
 "Marilla thinks Mrs. Rachel is too outspoken. Do you know someone who always says what they think? Is that a good or a bad thing?",
]),
10: dict(vocab=[
 ("penitent", "penitent", "n./adj.", "PEN-i-tent", "/ˈpenɪtənt/", "뉘우치는 (사람)", "a penitent sinner · look penitent", "The boy looked penitent after breaking the window.", "She came back to us like a penitent."),
 ("obdurate", "obdurate", "adj.", "OB-du-rate", "/ˈɑːbdərət/", "고집 센, 완고한", "remain obdurate · an obdurate refusal", "He remained obdurate and would not change his mind.", "The manager was obdurate about the rules."),
 ("humiliating", "humiliating", "adj.", "hu-MIL-i-at-ing", "/hjuːˈmɪlieɪtɪŋ/", "굴욕적인, 창피한", "a humiliating defeat · find it humiliating", "It was humiliating to fall on stage.", "He found it humiliating to ask for money."),
 ("dejected", "dejected", "adj.", "de-JECT-ed", "/dɪˈdʒektɪd/", "낙담한, 풀 죽은", "look dejected · feel dejected", "The team looked dejected after the game.", "She walked home, tired and dejected."),
 ("beseechingly", "beseechingly", "adv.", "be-SEECH-ing-ly", "/bɪˈsiːtʃɪŋli/", "애원하듯이", "look beseechingly · say beseechingly", "The dog looked at me beseechingly.", "\"Just one more time,\" she said beseechingly."),
 ("resentment", "resentment", "n.", "re-SENT-ment", "/rɪˈzentmənt/", "분함, 억울함", "feel resentment · deep resentment", "He felt resentment toward his boss.", "Years of resentment came out at once."),
 ("officious", "officious", "adj.", "of-FI-cious", "/əˈfɪʃəs/", "참견하기 좋아하는, 오지랖 넓은", "an officious neighbor · officious behavior", "An officious man told us where to park.", "Don't be so officious—let them decide."),
 ("benefactor", "benefactor", "n.", "BEN-e-fac-tor", "/ˈbenɪfæktər/", "은인, 후원자", "a generous benefactor · an anonymous benefactor", "A rich benefactor paid for the new library.", "She thanked her benefactor in a letter."),
 ("exhilaration", "exhilaration", "n.", "ex-hil-a-RA-tion", "/ɪɡˌzɪləˈreɪʃən/", "들뜬 기분, 아주 신남", "a feeling of exhilaration · sheer exhilaration", "I felt pure exhilaration at the top of the mountain.", "The exhilaration of winning lasted all week."),
 ("meddlesome", "meddlesome", "adj.", "MED-dle-some", "/ˈmedlsəm/", "남의 일에 참견하는", "a meddlesome neighbor · meddlesome relatives", "Our meddlesome neighbor reads our mail.", "I don't want to seem meddlesome, but…"),
], quiz=[
 ("Anne still remained ___ and would not say sorry, so meals at Green Gables were very silent.", "obdurate", ["obedient", "obvious", "absolute"]),
 ("Anne told Matthew she could not apologize because it would be so ___.", "humiliating", ["interesting", "frightening", "astonishing"]),
 ("Marilla and Anne walked down the lane, Marilla triumphant and Anne drooping and ___.", "dejected", ["delighted", "devoted", "detected"]),
 ("Halfway there, Marilla saw that Anne did not look like a meek ___ at all.", "penitent", ["patient", "pendant", "president"]),
 ("Anne knelt before Mrs. Rachel and held out her hands ___.", "beseechingly", ["beautifully", "bravely", "boastfully"]),
 ("After Anne's thorough apology, all of Mrs. Rachel's ___ vanished.", "resentment", ["refreshment", "retirement", "requirement"]),
 ("Mrs. Rachel had a kindly, if somewhat ___, heart—she liked managing other people's business.", "officious", ["official", "obvious", "delicious"]),
 ("Mrs. Rachel said Anne's red hair might turn auburn, and Anne told her, \"I shall always feel that you are a ___.\"", "benefactor", ["manufacturer", "character", "beneficiary"]),
 ("On the way home Anne walked lightly, with an air of quiet ___ about her.", "exhilaration", ["exhaustion", "exaggeration", "examination"]),
 ("Matthew thought it was good that Rachel Lynde got a calling down, because she's a ___ old gossip.", "meddlesome", ["handsome", "wholesome", "lonesome"]),
], discussion=[
 "Anne's apology was very dramatic, and she even enjoyed making it. Is it still a real apology if you enjoy saying sorry?",
 "Matthew asked Anne to \"smooth things over\" with Mrs. Rachel. Have you ever said sorry just to keep the peace? How did you feel?",
]),
11: dict(vocab=[
 ("serviceable", "serviceable", "adj.", "SER-vice-a-ble", "/ˈsɜːrvɪsəbl/", "실용적인, 쓸 만한", "serviceable shoes · in serviceable condition", "These old boots are still serviceable.", "She bought a plain but serviceable coat."),
 ("furbelows", "furbelows", "n.", "FUR-be-lows", "/ˈfɜːrbɪloʊz/", "(옷의) 화려한 장식, 주름 장식", "frills and furbelows", "Her wedding dress had no frills or furbelows.", "He hates furbelows and likes simple clothes."),
 ("soberly", "soberly", "adv.", "SO-ber-ly", "/ˈsoʊbərli/", "진지하게, 차분하게", "speak soberly · dress soberly", "\"We need to talk,\" she said soberly.", "He was soberly dressed in a gray suit."),
 ("plainness", "plainness", "n.", "PLAIN-ness", "/ˈpleɪnnəs/", "수수함, 꾸밈없음", "the plainness of · simple plainness", "I like the plainness of the room.", "The plainness of her words surprised us."),
 ("irreproachable", "irreproachable", "adj.", "ir-re-PROACH-a-ble", "/ˌɪrɪˈproʊtʃəbl/", "나무랄 데 없는", "irreproachable manners · an irreproachable record", "His manners were irreproachable.", "She has an irreproachable work record."),
 ("garland", "garlanded", "v.", "GAR-land", "/ˈɡɑːrlənd/", "화환으로 장식하다; 화환", "garlanded with flowers · a garland of roses", "The streets were garlanded with lights.", "The winners were garlanded with flowers."),
 ("adornment", "adornment", "n.", "a-DORN-ment", "/əˈdɔːrnmənt/", "장식(품)", "personal adornment · without adornment", "The walls were white, without any adornment.", "Gold rings were a popular adornment."),
 ("rebukingly", "rebukingly", "adv.", "re-BUKE-ing-ly", "/rɪˈbjuːkɪŋli/", "꾸짖듯이", "say rebukingly · look rebukingly", "\"That's enough,\" his father said rebukingly.", "The teacher looked at us rebukingly."),
 ("melancholy", "melancholy", "adj./n.", "MEL-an-chol-y", "/ˈmelənkɑːli/", "우울한, 구슬픈; 우울", "a melancholy song · a feeling of melancholy", "Autumn always makes me a little melancholy.", "She sang a melancholy song about the sea."),
 ("disconsolately", "disconsolately", "adv.", "dis-CON-so-late-ly", "/dɪsˈkɑːnsələtli/", "쓸쓸하게, 침울하게", "sit disconsolately · say disconsolately", "He sat disconsolately on the steps.", "\"I lost again,\" she said disconsolately."),
], quiz=[
 ("Marilla bought one dress fabric from a peddler because it looked so ___.", "serviceable", ["comfortable", "valuable", "fashionable"]),
 ("Marilla said the dresses were sensible, without any frills or ___.", "furbelows", ["fellows", "pillows", "elbows"]),
 ("\"I'll imagine that I like them,\" Anne said ___, looking at the plain dresses.", "soberly", ["solely", "smoothly", "suddenly"]),
 ("The extreme ___ of her new sailor hat disappointed Anne, who had dreamed of ribbons and flowers.", "plainness", ["politeness", "happiness", "sadness"]),
 ("Anne started off for church ___, in a stiff black-and-white dress that no one could criticize.", "irreproachable", ["irreplaceable", "irresistible", "unbearable"]),
 ("On the way, Anne ___ her hat with a heavy wreath of buttercups and wild roses.", "garlanded", ["guarded", "gathered", "gargled"]),
 ("The girls on the church porch stared at the stranger's extraordinary head ___.", "adornment", ["adjustment", "appointment", "amendment"]),
 ("When Anne said Sunday-school was horrid, Marilla said \"Anne Shirley!\" ___.", "rebukingly", ["rapidly", "romantically", "reluctantly"]),
 ("Anne liked the poem she had to learn because it was so sad and ___.", "melancholy", ["melodious", "merciful", "mellow"]),
 ("Anne felt lonely among the other girls with puffed sleeves and whispered ___ to herself.", "disconsolately", ["considerately", "confidently", "consistently"]),
], discussion=[
 "Anne was disappointed with her plain dresses, but she decided to imagine she liked them. Do you ever use your imagination to feel better about something?",
 "Anne put flowers on her hat, and other people laughed. Is it brave or silly to look different from everyone else?",
]),
12: dict(vocab=[
 ("resolute", "resolute", "adj.", "RES-o-lute", "/ˈrezəluːt/", "단호한, 결연한", "a resolute leader · resolute action", "She was resolute in her decision.", "He gave a resolute answer."),
 ("cordially", "cordially", "adv.", "COR-dial-ly", "/ˈkɔːrdʒəli/", "다정하게, 진심으로 반갑게", "cordially invited · greet cordially", "You are cordially invited to our wedding.", "The host greeted us cordially."),
 ("destiny", "destiny", "n.", "DES-ti-ny", "/ˈdestəni/", "운명", "control your destiny · a sense of destiny", "She believed it was her destiny to be a doctor.", "We can shape our own destiny."),
 ("bashfully", "bashfully", "adv.", "BASH-ful-ly", "/ˈbæʃfəli/", "수줍게", "smile bashfully · look bashfully", "The little boy smiled bashfully at the guests.", "She bashfully asked for his autograph."),
 ("tremulous", "tremulous", "adj.", "TREM-u-lous", "/ˈtremjələs/", "(긴장·흥분으로) 떨리는", "a tremulous voice · tremulous hands", "She answered in a tremulous voice.", "His tremulous hands dropped the cup."),
 ("solemnly", "solemnly", "adv.", "SOL-emn-ly", "/ˈsɑːləmli/", "엄숙하게", "promise solemnly · nod solemnly", "He solemnly promised to tell the truth.", "The judge spoke solemnly."),
 ("blissfully", "blissfully", "adv.", "BLISS-ful-ly", "/ˈblɪsfəli/", "더없이 행복하게; (모르고) 태평하게", "blissfully happy · blissfully unaware", "They were blissfully happy on their honeymoon.", "He was blissfully unaware of the danger."),
 ("sarcasm", "sarcasm", "n.", "SAR-casm", "/ˈsɑːrkæzəm/", "비꼼, 빈정거림", "a hint of sarcasm · with sarcasm", "\"Great job,\" he said with sarcasm.", "I couldn't tell if she was using sarcasm."),
 ("dubious", "dubious", "adj.", "DU-bi-ous", "/ˈduːbiəs/", "의심스러운, 애매한", "dubious about · a dubious claim", "I'm dubious about his story.", "The website made some dubious claims."),
 ("sheepishly", "sheepishly", "adv.", "SHEEP-ish-ly", "/ˈʃiːpɪʃli/", "쑥스러워하며, 멋쩍게", "grin sheepishly · admit sheepishly", "He grinned sheepishly when he got caught.", "She sheepishly admitted she had forgotten."),
], quiz=[
 ("Mrs. Barry was a tall black-eyed woman with a very ___ mouth, and she was strict with her children.", "resolute", ["ridiculous", "restless", "rosy"]),
 ("\"How do you do, Marilla?\" Mrs. Barry said ___. \"Come in.\"", "cordially", ["cruelly", "carelessly", "coldly"]),
 ("The Barry garden would have delighted Anne at any time less full of ___.", "destiny", ["density", "dentistry", "distance"]),
 ("Anne and Diana stood in the garden, gazing ___ at each other over the tiger lilies.", "bashfully", ["boldly", "busily", "bitterly"]),
 ("Anne was ___ and excited, but she wanted no misunderstanding: would Diana be her bosom friend?", "tremulous", ["tremendous", "treacherous", "tedious"]),
 ("Anne explained that an oath means vowing and promising ___.", "solemnly", ["solidly", "suddenly", "sorely"]),
 ("Anne sighed happily, ___ unaware that Marilla was teasing her.", "blissfully", ["boastfully", "bashfully", "bitterly"]),
 ("Marilla's words had a little ___ in them, but Anne did not notice.", "sarcasm", ["criticism", "enthusiasm", "symbolism"]),
 ("Marilla preferred safe, concrete facts and would not follow Anne into ___ paths of the abstract.", "dubious", ["delicious", "devious", "various"]),
 ("Matthew ___ took a small parcel of chocolate sweets from his pocket and gave it to Anne.", "sheepishly", ["selfishly", "sharply", "sleepily"]),
], discussion=[
 "Anne and Diana promised to be friends forever. Did you have a \"bosom friend\" as a child? Are you still friends today?",
 "Marilla told Anne to share Matthew's chocolates with Diana. Why do you think Anne was so happy to share?",
]),
13: dict(vocab=[
 ("rapturously", "rapturously", "adv.", "RAP-tur-ous-ly", "/ˈræptʃərəsli/", "황홀하게, 열광적으로", "applaud rapturously · smile rapturously", "The audience applauded rapturously.", "She rapturously hugged her new puppy."),
 ("impulsive", "impulsive", "adj.", "im-PUL-sive", "/ɪmˈpʌlsɪv/", "충동적인", "an impulsive decision · impulsive buying", "Buying the car was an impulsive decision.", "Children are often impulsive."),
 ("brusquely", "brusquely", "adv.", "BRUSQUE-ly", "/ˈbrʌskli/", "퉁명스럽게", "answer brusquely · speak brusquely", "\"I'm busy,\" he said brusquely.", "The nurse spoke brusquely but kindly."),
 ("featherbrained", "featherbrained", "adj.", "FEATH-er-brained", "/ˈfeðərbreɪnd/", "생각 없는, 덜렁대는", "a featherbrained idea · featherbrained girl", "Don't be featherbrained—check the stove before leaving.", "That was a featherbrained plan."),
 ("dolefully", "dolefully", "adv.", "DOLE-ful-ly", "/ˈdoʊlfəli/", "슬프게, 시무룩하게", "say dolefully · look dolefully", "\"No dessert tonight?\" he asked dolefully.", "The puppy looked at me dolefully."),
 ("enraptured", "enraptured", "adj.", "en-RAP-tured", "/ɪnˈræptʃərd/", "황홀해하는, 매료된", "be enraptured by · an enraptured audience", "The children were enraptured by the show.", "She listened, enraptured, to the music."),
 ("tribulations", "tribulations", "n.", "trib-u-LA-tions", "/ˌtrɪbjuˈleɪʃənz/", "시련, 고난", "trials and tribulations", "They shared the trials and tribulations of starting a business.", "The book tells of her many tribulations."),
 ("infatuated", "infatuated", "adj.", "in-FAT-u-at-ed", "/ɪnˈfætʃueɪtɪd/", "홀딱 반한, 푹 빠진", "infatuated with · become infatuated", "He became infatuated with his classmate.", "She is infatuated with that singer."),
 ("bequeath", "bequeathed", "v.", "be-QUEATH", "/bɪˈkwiːð/", "(유언으로) 물려주다", "bequeath something to someone", "She bequeathed her house to her niece.", "He bequeathed his books to the school."),
 ("sacrilegious", "sacrilegious", "adj.", "sac-ri-LE-gious", "/ˌsækrəˈlɪdʒəs/", "신성 모독적인; (농담) 감히 그럴 수 없는", "a sacrilegious act · seem sacrilegious", "Eating pizza with a fork seems sacrilegious to him.", "Some people found the painting sacrilegious."),
], quiz=[
 ("When Marilla said she would teach her to cook, Anne threw herself into her arms and ___ kissed her cheek.", "rapturously", ["respectfully", "regretfully", "reluctantly"]),
 ("Marilla was secretly pleased by Anne's ___ hug.", "impulsive", ["impressive", "expensive", "offensive"]),
 ("To hide her pleasure, Marilla said ___, \"There, there, never mind your kissing nonsense.\"", "brusquely", ["bravely", "brightly", "briefly"]),
 ("Marilla said she hadn't taught Anne to cook yet because Anne was so ___.", "featherbrained", ["warmhearted", "openminded", "strongwilled"]),
 ("\"I do not like patchwork,\" said Anne ___, sitting down to her sewing with a sigh.", "dolefully", ["doubtfully", "dutifully", "delightfully"]),
 ("Anne invented the name \"Idlewild\" for the playhouse, and Diana was ___ when she heard it.", "enraptured", ["enraged", "endangered", "enlarged"]),
 ("The heroine of Diana's book had five lovers and went through great ___.", "tribulations", ["celebrations", "translations", "regulations"]),
 ("Marilla complained that Matthew listened to Anne like a perfect ninny: \"I never saw such an ___ man.\"", "infatuated", ["intimidated", "irritated", "isolated"]),
 ("The amethyst brooch had been given to Marilla's mother, who later ___ it to Marilla.", "bequeathed", ["bewildered", "betrayed", "breathed"]),
 ("Marilla wore the brooch every Sunday; leaving it off would seem almost ___ to her.", "sacrilegious", ["sacrificial", "religious", "ridiculous"]),
], discussion=[
 "Anne is so excited about the picnic that she can't sleep. Do you enjoy looking forward to something as much as the thing itself?",
 "Marilla is happy when Anne kisses her, but she speaks brusquely. Why do some people hide their warm feelings?",
]),
14: dict(vocab=[
 ("falsehood", "falsehood", "n.", "FALSE-hood", "/ˈfɔːlshʊd/", "거짓말, 허위", "tell a falsehood · truth and falsehood", "He was punished for telling a falsehood.", "It's hard to separate truth from falsehood online."),
 ("defiance", "defiance", "n.", "de-FI-ance", "/dɪˈfaɪəns/", "반항, 무시", "an act of defiance · in defiance of", "She stayed out late in defiance of her parents.", "He raised his fist in defiance."),
 ("forlornly", "forlornly", "adv.", "for-LORN-ly", "/fərˈlɔːrnli/", "쓸쓸하게, 처량하게", "stare forlornly · ask forlornly", "The puppy waited forlornly by the door.", "He looked forlornly at the empty plate."),
 ("confession", "confession", "n.", "con-FES-sion", "/kənˈfeʃən/", "고백, 자백", "make a confession · a full confession", "I have a confession to make: I ate your cake.", "The thief made a full confession."),
 ("remorse", "remorse", "n.", "re-MORSE", "/rɪˈmɔːrs/", "후회, 양심의 가책", "feel remorse · full of remorse", "He showed no remorse for what he did.", "She was filled with remorse after the fight."),
 ("compunction", "compunction", "n.", "com-PUNC-tion", "/kəmˈpʌŋkʃən/", "양심의 가책, 거리낌", "without compunction · have no compunction", "He lied without compunction.", "She had no compunction about taking the last piece."),
 ("repentance", "repentance", "n.", "re-PENT-ance", "/rɪˈpentəns/", "뉘우침, 회개", "show repentance · sincere repentance", "His tears were a sign of repentance.", "The story is about sin and repentance."),
 ("candidly", "candidly", "adv.", "CAN-did-ly", "/ˈkændɪdli/", "솔직하게", "speak candidly · candidly admit", "Candidly, I don't like the plan.", "She spoke candidly about her mistakes."),
 ("rigmarole", "rigmarole", "n.", "RIG-ma-role", "/ˈrɪɡmərəʊl/", "장황하고 앞뒤 안 맞는 이야기; 번거로운 절차", "a long rigmarole · go through the rigmarole", "Getting a visa was a real rigmarole.", "I didn't believe his long rigmarole."),
 ("clutch", "clutched", "v.", "CLUTCH", "/klʌtʃ/", "꽉 움켜잡다", "clutch someone's hand · clutch a bag", "She clutched her bag on the crowded train.", "The child clutched his mother's hand."),
], quiz=[
 ("When Anne said she hadn't taken the brooch, Marilla said, \"I believe you are telling me a ___, Anne.\"", "falsehood", ["likelihood", "neighborhood", "childhood"]),
 ("Anne's strong words were only meant to insist she was telling the truth, but Marilla saw them as ___.", "defiance", ["distance", "reliance", "guidance"]),
 ("Matthew ___ asked about Anne, feeling secretly thankful that Marilla, not he, had to deal with her.", "forlornly", ["formally", "fondly", "fortunately"]),
 ("Anne said she had thought out a ___ the night before and made it as interesting as she could.", "confession", ["profession", "conclusion", "condition"]),
 ("Anne told Marilla, \"You'll feel ___ of conscience someday for breaking your promise.\"", "remorse", ["reward", "resource", "remark"]),
 ("Anne calmly described losing the brooch without the least ___ or regret.", "compunction", ["conjunction", "construction", "consumption"]),
 ("Marilla expected tears and ___, but Anne seemed perfectly calm.", "repentance", ["repetition", "resistance", "residence"]),
 ("\"I was very wicked,\" Anne finished ___, \"but I've learned a lesson.\"", "candidly", ["carelessly", "cheerfully", "cautiously"]),
 ("After finding the brooch on her shawl, Marilla asked what that ___ Anne had told her that morning meant.", "rigmarole", ["casserole", "camisole", "protocol"]),
 ("Anne sprang to her feet and ___ Marilla's hand, begging to go to the picnic.", "clutched", ["clashed", "clicked", "crushed"]),
], discussion=[
 "Anne confessed to something she didn't do, just so she could go to the picnic. What would you have done in her place?",
 "In the end Marilla said sorry to Anne. Is it hard for adults to apologize to children? Why?",
]),
15: dict(vocab=[
 ("blithely", "blithely", "adv.", "BLITHE-ly", "/ˈblaɪðli/", "즐겁게; 태평하게", "blithely ignore · walk blithely", "The kids ran blithely through the park.", "He blithely ignored the warning signs."),
 ("giggle", "giggled", "v.", "GIG-gle", "/ˈɡɪɡl/", "키득거리다", "giggle at · start giggling", "The girls giggled at the joke.", "Stop giggling and listen!"),
 ("commotion", "commotion", "n.", "com-MO-tion", "/kəˈmoʊʃən/", "소동, 소란", "cause a commotion · what's the commotion?", "There was a commotion outside the store.", "The dog caused a commotion in the kitchen."),
 ("contritely", "contritely", "adv.", "con-TRITE-ly", "/kənˈtraɪtli/", "뉘우치며, 미안해하며", "apologize contritely · say contritely", "\"I'm so sorry,\" he said contritely.", "She contritely admitted her mistake."),
 ("dignity", "dignity", "n.", "DIG-ni-ty", "/ˈdɪɡnəti/", "위엄, 품위; 존엄", "with dignity · lose your dignity", "She accepted the defeat with dignity.", "Every person deserves dignity."),
 ("disheveled", "disheveled", "adj.", "di-SHEV-eled", "/dɪˈʃevəld/", "(머리·옷이) 헝클어진", "disheveled hair · look disheveled", "He arrived late, looking disheveled.", "Her hair was disheveled from the wind."),
 ("haughtily", "haughtily", "adv.", "HAUGH-ti-ly", "/ˈhɔːtɪli/", "거만하게, 도도하게", "look haughtily · say haughtily", "She looked at us haughtily.", "\"I don't need your help,\" he said haughtily."),
 ("disdainfully", "disdainfully", "adv.", "dis-DAIN-ful-ly", "/dɪsˈdeɪnfəli/", "경멸하듯", "look disdainfully · sniff disdainfully", "The cat looked disdainfully at the cheap food.", "He laughed disdainfully at the idea."),
 ("appease", "appease", "v.", "ap-PEASE", "/əˈpiːz/", "달래다, 진정시키다", "appease someone · try to appease", "He bought flowers to appease his angry wife.", "Nothing could appease the crowd."),
 ("bitterness", "bitterness", "n.", "BIT-ter-ness", "/ˈbɪtərnəs/", "비통함; 원한; 쓴맛", "with bitterness · feel bitterness", "She spoke about her divorce with bitterness.", "The coffee had a slight bitterness."),
], quiz=[
 ("On a crisp September morning Anne and Diana were tripping ___ down the Birch Path.", "blithely", ["blindly", "briefly", "bitterly"]),
 ("Diana said Prissy Andrews blushed red as a beet and ___ when she read the master's slate.", "giggled", ["gargled", "juggled", "wiggled"]),
 ("Ruby Gillis shrieked when her hair was pinned, but Gilbert studied his history until the ___ died down.", "commotion", ["promotion", "emotion", "motion"]),
 ("After calling her \"Carrots,\" Gilbert whispered ___ that he was sorry.", "contritely", ["constantly", "completely", "correctly"]),
 ("Diana said Gilbert called her a crow, but Anne answered with ___ that \"carrots\" was much worse.", "dignity", ["divinity", "density", "destiny"]),
 ("Anne rushed in late with a lily wreath hanging over one ear, looking ___.", "disheveled", ["delivered", "dissolved", "devoted"]),
 ("Mr. Phillips made her sit with Gilbert, so Anne rose ___, crossed the aisle, and buried her face in her arms.", "haughtily", ["heartily", "hungrily", "happily"]),
 ("Anne swept past Gilbert ___, as if she could not hear him at all.", "disdainfully", ["delightfully", "dreadfully", "doubtfully"]),
 ("Gilbert clearly wanted to ___ Anne, but she met him with icy contempt.", "appease", ["appear", "applaud", "approve"]),
 ("Imagining that Diana would marry and leave her someday, Anne cried with increasing ___.", "bitterness", ["brightness", "sweetness", "boldness"]),
], discussion=[
 "Gilbert apologized, but Anne would not forgive him. Was Anne right? Is there something you once found hard to forgive?",
 "Many pupils were late, but Mr. Phillips punished only Anne. Have you ever been treated unfairly at school or at work?",
]),
16: dict(vocab=[
 ("addlepated", "addlepated", "adj.", "AD-dle-pat-ed", "/ˈædlpeɪtɪd/", "(옛) 머리가 멍한, 덜렁대는", "an addlepated idea · addlepated girl", "Grandma called me addlepated when I lost my keys again.", "That addlepated plan will never work."),
 ("ecstatically", "ecstatically", "adv.", "ec-STAT-i-cal-ly", "/ɪkˈstætɪkli/", "황홀하게, 너무나 기쁘게", "ecstatically happy · cheer ecstatically", "The fans cheered ecstatically.", "She was ecstatically happy with the news."),
 ("entreat", "entreated", "v.", "en-TREAT", "/ɪnˈtriːt/", "간청하다", "entreat someone to do", "She entreated him to stay a little longer.", "They entreated the king for mercy."),
 ("dignified", "dignified", "adj.", "DIG-ni-fied", "/ˈdɪɡnɪfaɪd/", "위엄 있는, 점잖은", "a dignified manner · look dignified", "The old man walked in a dignified way.", "She gave a calm, dignified speech."),
 ("mortification", "mortification", "n.", "mor-ti-fi-CA-tion", "/ˌmɔːrtɪfɪˈkeɪʃən/", "굴욕감, 몹시 창피함", "to my mortification · deep mortification", "To my mortification, I fell on the dance floor.", "He blushed with mortification."),
 ("hospitable", "hospitable", "adj.", "hos-PIT-a-ble", "/hɑːˈspɪtəbl/", "손님을 잘 대접하는, 환대하는", "hospitable to guests · a hospitable family", "The villagers were very hospitable to us.", "She is the most hospitable host I know."),
 ("intoxicate", "intoxicate", "v.", "in-TOX-i-cate", "/ɪnˈtɑːksɪkeɪt/", "취하게 하다; 들뜨게 하다", "intoxicated by success · get intoxicated", "Two glasses of wine were enough to intoxicate him.", "She was intoxicated by her sudden fame."),
 ("distracted", "distracted", "adj.", "dis-TRACT-ed", "/dɪˈstræktɪd/", "정신이 산만한; 심란한", "get distracted · look distracted", "He seemed distracted during the meeting.", "Don't get distracted by your phone."),
 ("implore", "implored", "v.", "im-PLORE", "/ɪmˈplɔːr/", "애원하다", "implore someone to do", "\"Please don't go,\" she implored.", "He implored them to listen."),
 ("obstinate", "obstinate", "adj.", "OB-sti-nate", "/ˈɑːbstɪnət/", "고집 센, 완강한", "an obstinate child · obstinate refusal", "My grandfather is too obstinate to see a doctor.", "The stain was obstinate and wouldn't come out."),
], quiz=[
 ("Marilla let Diana come to tea, though she worried it might make Anne more ___ than ever.", "addlepated", ["addicted", "adapted", "agitated"]),
 ("Anne shut her eyes ___ and imagined herself pouring tea at the head of the table.", "ecstatically", ["erratically", "energetically", "eccentrically"]),
 ("Diana drank a second glassful and, being ___ by Anne, did not refuse a third.", "entreated", ["entertained", "entered", "entrusted"]),
 ("Anne tried to act like a grown-up hostess, but she forgot to be ___ and jumped up quickly.", "dignified", ["delighted", "divided", "disguised"]),
 ("Anne remembered the mouse in the pudding sauce and how she nearly sank through the floor with ___ in front of Mrs. Chester Ross.", "mortification", ["modification", "motivation", "multiplication"]),
 ("\"I meant to be so—so—___,\" Anne cried after giving Diana currant wine by mistake.", "hospitable", ["horrible", "honorable", "hostile"]),
 ("\"I did not mean to ___ Diana,\" Anne said to Mrs. Barry.", "intoxicate", ["intimidate", "indicate", "invite"]),
 ("Marilla went into the kitchen, leaving a very ___ little girl in the porch.", "distracted", ["attracted", "subtracted", "detected"]),
 ("\"Oh, Mrs. Barry, please forgive me,\" ___ Anne.", "implored", ["explored", "ignored", "improved"]),
 ("Anne said not even God could do much with such an ___ person as Mrs. Barry.", "obstinate", ["fortunate", "obedient", "passionate"]),
], discussion=[
 "Anne made an honest mistake, but Mrs. Barry would not believe it was an accident. Have you ever been blamed for something you didn't mean to do?",
 "Marilla's face twitched with laughter when she heard the story, even though it was serious. Why do you think she wanted to laugh?",
]),
}

OLD = {
 "behooved": ("동사", "(옛) ~하는 것이 마땅했다 (= was right / should)", "\"Such as it behooved her to take\" means \"the kind of girl she should take.\" Today we say \"it was right for her to…\" or \"she should…\"."),
 "behold": ("동사", "(옛) 보라!, 보다 (= look! / see)", "The writer uses \"behold\" like \"Look!\" to show a funny little scene. It is kept here because it is the author's playful style."),
}
IDIOMS = {
 "Lawful heart": ("세상에!, 맙소사!", "Good heavens! / Oh my goodness!", "An old exclamation of surprise that Mrs. Rachel uses. Today: \"Oh my goodness, look at those freckles!\""),
 "nineteen to the dozen": ("쉴 새 없이 (빠르게 말하다)", "very fast and without stopping", "\"Talking nineteen to the dozen\" = talking nonstop. Today: \"She talks a mile a minute.\""),
 "no whit": ("조금도 ~않다", "not at all / not even a little", "\"Her contempt was no whit thawed\" = her coldness did not soften at all. Today: \"not one bit\"."),
}
OLD_MARKS = {10: ["behooved", "behold"]}
IDIOM_MARKS = {9: ["Lawful heart"], 13: ["nineteen to the dozen"], 15: ["no whit"]}

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
