# The Great Gatsby workbook, chapters 7–9. Chapter 7 takes two meetings: words 1–10 come from the first half, 11–20 from the second half.
import json, os, re

WB = {
7: dict(vocab=[
 ("caravansary", "caravansary", "n.", "car-a-VAN-sa-ry", "/ˌkærəˈvænsəri/", "대상 숙소; 북적이는 큰 집(비유)", "a desert caravansary", "Travelers rested at a caravansary on the Silk Road.", "Their house was a caravansary of guests every weekend."),
 ("simmering", "simmering", "adj.", "SIM-mer-ing", "/ˈsɪmərɪŋ/", "부글부글 끓는; 끓어오르기 직전의", "a simmering pot · simmering anger", "Leave the soup simmering for an hour.", "There was simmering tension in the room."),
 ("despairingly", "despairingly", "adv.", "de-SPAIR-ing-ly", "/dɪˈsperɪŋli/", "절망적으로", "sigh despairingly · look despairingly", "She looked despairingly at the long queue.", "\"It's hopeless,\" he said despairingly."),
 ("affront", "affront", "n.", "af-FRONT", "/əˈfrʌnt/", "모욕, 무례", "an affront to · a personal affront", "His remark was an affront to her family.", "She took the criticism as a personal affront."),
 ("relinquish", "relinquished", "v.", "re-LIN-quish", "/rɪˈlɪŋkwɪʃ/", "(쥐고 있던 것을) 내주다, 포기하다", "relinquish control · relinquish a position", "He relinquished control of the company.", "She relinquished her seat to an old man."),
 ("genially", "genially", "adv.", "GEN-ial-ly", "/ˈdʒiːniəli/", "상냥하게, 다정하게", "smile genially · say genially", "The host greeted us genially.", "He laughed genially at the joke."),
 ("indiscreet", "indiscreet", "adj.", "in-dis-CREET", "/ˌɪndɪˈskriːt/", "경솔한, 입이 가벼운", "an indiscreet remark · indiscreet behavior", "It was indiscreet of him to mention her salary.", "She made an indiscreet comment."),
 ("oppressive", "oppressive", "adj.", "op-PRES-sive", "/əˈpresɪv/", "숨 막히는; 억압적인", "oppressive heat · an oppressive government", "The heat was oppressive.", "People rose up against the oppressive regime."),
 ("disquieting", "disquieting", "adj.", "dis-QUI-et-ing", "/dɪsˈkwaɪətɪŋ/", "불안하게 하는", "a disquieting silence · disquieting news", "There was a disquieting silence.", "We received some disquieting news."),
 ("portentous", "portentous", "adj.", "por-TEN-tous", "/pɔːrˈtentəs/", "불길한, 심상치 않은; 거창한", "a portentous sign · portentous music", "Dark clouds gave the day a portentous feel.", "He spoke in a portentous voice."),
 ("sneer", "sneering", "v.", "SNEER", "/snɪr/", "비웃다, 냉소하다", "sneer at · a sneering tone", "He sneered at my old car.", "Stop sneering at other people's ideas."),
 ("vicariously", "vicariously", "adv.", "vi-CAR-i-ous-ly", "/vaɪˈkeriəsli/", "대리로, 남을 통해 간접적으로", "live vicariously · enjoy vicariously", "She lives vicariously through her children.", "I travel vicariously by watching travel videos."),
 ("libertine", "libertine", "n.", "LIB-er-tine", "/ˈlɪbərtiːn/", "방탕한 사람, 난봉꾼", "a notorious libertine", "The novel's hero is a charming libertine.", "He was known as a libertine in his youth."),
 ("rancour", "rancour", "n.", "RAN-cour", "/ˈræŋkər/", "원한, 앙심 (US: rancor)", "without rancour · bitter rancour", "They parted without rancour.", "There was rancour in her voice."),
 ("magnanimous", "magnanimous", "adj.", "mag-NAN-i-mous", "/mæɡˈnænɪməs/", "너그러운, 관대한 (척하는)", "magnanimous in victory · a magnanimous gesture", "He was magnanimous in victory.", "It was a magnanimous offer."),
 ("menacing", "menacing", "adj.", "MEN-ac-ing", "/ˈmenɪsɪŋ/", "위협적인", "a menacing look · menacing clouds", "The dog gave a menacing growl.", "Menacing clouds gathered in the west."),
 ("formidable", "formidable", "adj.", "FOR-mi-da-ble", "/ˈfɔːrmɪdəbl/", "가공할, 만만치 않은", "a formidable opponent · formidable task", "She is a formidable opponent.", "Climbing the mountain was a formidable task."),
 ("truculent", "truculent", "adj.", "TRUC-u-lent", "/ˈtrʌkjələnt/", "싸울 듯한, 공격적인", "a truculent attitude · truculent eyes", "The truculent player argued with the referee.", "He gave me a truculent stare."),
 ("brutality", "brutality", "n.", "bru-TAL-i-ty", "/bruːˈtæləti/", "잔인함, 폭력", "police brutality · the brutality of war", "The film shows the brutality of war.", "They protested against police brutality."),
 ("despicable", "despicable", "adj.", "de-SPIC-a-ble", "/dɪˈspɪkəbl/", "비열한, 경멸할 만한", "a despicable act · despicable behavior", "Cheating old people is despicable.", "That was a despicable thing to do."),
], quiz=[
 ("Gatsby had fired all his servants, so the whole ___ had fallen in like a card house.", "caravansary", ["sanctuary", "carousel", "commissary"]),
 ("Only the hot whistles of the National Biscuit Company broke the ___ hush at noon.", "simmering", ["shimmering", "stammering", "summering"]),
 ("The woman on the train lapsed ___ into deep heat with a desolate cry.", "despairingly", ["disparagingly", "despicably", "dispassionately"]),
 ("In this heat every extra gesture was an ___ to the common store of life.", "affront", ["effort", "afford", "upfront"]),
 ("The child, ___ by the nurse, rushed across the room to her mother.", "relinquished", ["replenished", "relished", "refurbished"]),
 ("\"I read somewhere that the sun's getting hotter every year,\" said Tom ___.", "genially", ["genuinely", "generally", "genetically"]),
 ("\"She's got an ___ voice,\" Nick remarked. \"Her voice is full of money,\" said Gatsby.", "indiscreet", ["indistinct", "indirect", "indignant"]),
 ("Tom pushed the unfamiliar gears, and they shot off into the ___ heat.", "oppressive", ["impressive", "obsessive", "aggressive"]),
 ("That locality near Wilson's garage was always vaguely ___, even in the afternoon.", "disquieting", ["disqualifying", "distinguishing", "discouraged"]),
 ("They heard the ___ chords of Mendelssohn's Wedding March from the ballroom below.", "portentous", ["pretentious", "potent", "portable"]),
 ("Tom complained that people begin by ___ at family life and family institutions.", "sneering", ["sneezing", "steering", "searing"]),
 ("Jordan and Nick were made to stay, as if it were a privilege to partake ___ of their emotions.", "vicariously", ["variously", "viciously", "vigorously"]),
 ("Nick was tempted to laugh: Tom's change from ___ to prig was so complete.", "libertine", ["libretto", "liberal", "limousine"]),
 ("Daisy's voice was cold, but the ___ was gone from it.", "rancour", ["anchor", "rapport", "candour"]),
 ("Tom sent Daisy home in Gatsby's car with ___ scorn.", "magnanimous", ["unanimous", "anonymous", "magnetic"]),
 ("Before Nick stretched the portentous, ___ road of a new decade: he was thirty.", "menacing", ["mending", "mincing", "managing"]),
 ("The ___ stroke of thirty died away with the reassuring pressure of Jordan's hand.", "formidable", ["formable", "forgivable", "fordable"]),
 ("The policeman caught something in Tom's tone and looked over with ___ eyes.", "truculent", ["translucent", "succulent", "turbulent"]),
 ("Gatsby said Daisy would signal with the light if Tom tried any ___.", "brutality", ["banality", "brevity", "frugality"]),
 ("Somehow, standing there watching the house seemed a ___ occupation to Nick.", "despicable", ["despondent", "dispensable", "applicable"]),
], discussion=[
 "Gatsby says Daisy's voice \"is full of money.\" What does he mean? What does Daisy really love—Gatsby or the life money gives her?",
 "Daisy says she loved Tom once, too. Why can't Gatsby accept this? What do you think about the choice Daisy makes at the end of the chapter?",
]),
8: dict(vocab=[
 ("dejection", "dejection", "n.", "de-JEC-tion", "/dɪˈdʒekʃən/", "낙담, 실의", "in dejection · a look of dejection", "He sat in dejection after the loss.", "Her face showed deep dejection."),
 ("redolent", "redolent", "adj.", "RED-o-lent", "/ˈredələnt/", "(~의) 냄새가 나는; ~을 생각나게 하는", "redolent of · redolent with", "The kitchen was redolent of garlic.", "The town is redolent of the past."),
 ("ravenously", "ravenously", "adv.", "RAV-en-ous-ly", "/ˈrævənəsli/", "게걸스럽게, 탐욕스럽게", "eat ravenously · ravenously hungry", "The children ate ravenously.", "He read ravenously as a teenager."),
 ("unscrupulously", "unscrupulously", "adv.", "un-SCRU-pu-lous-ly", "/ʌnˈskruːpjələsli/", "부도덕하게, 거리낌 없이", "act unscrupulously", "The company acted unscrupulously.", "He unscrupulously used his friends."),
 ("despise", "despised", "v.", "de-SPISE", "/dɪˈspaɪz/", "경멸하다", "despise yourself · despise someone for", "She despised liars.", "He despised himself for being weak."),
 ("pervade", "pervaded", "v.", "per-VADE", "/pərˈveɪd/", "(곳곳에) 스며들다, 가득 퍼지다", "pervade the air · a pervading sense of", "A smell of coffee pervaded the house.", "Sadness pervaded the town."),
 ("corroborate", "corroborate", "v.", "cor-ROB-o-rate", "/kəˈrɑːbəreɪt/", "확증하다, 뒷받침하다", "corroborate a story · corroborating evidence", "A witness corroborated his story.", "Can anyone corroborate this?"),
 ("garrulous", "garrulous", "adj.", "GAR-ru-lous", "/ˈɡærələs/", "수다스러운", "a garrulous old man · garrulous neighbor", "Our garrulous neighbor talked for an hour.", "He gets garrulous after a drink."),
 ("forlorn", "forlorn", "adj.", "for-LORN", "/fərˈlɔːrn/", "가망 없는; 쓸쓸한", "a forlorn hope · look forlorn", "It was a forlorn hope that they would win.", "The dog looked forlorn in the rain."),
 ("amorphous", "amorphous", "adj.", "a-MOR-phous", "/əˈmɔːrfəs/", "형체가 없는, 무정형의", "an amorphous mass · amorphous shapes", "The fog was an amorphous gray mass.", "The plan is still amorphous."),
], quiz=[
 ("Nick found Gatsby leaning against a table in the hall, heavy with ___ or sleep.", "dejection", ["detection", "rejection", "deduction"]),
 ("Daisy's house hinted at romances fresh and breathing and ___ of this year's shining motorcars.", "redolent", ["indolent", "redundant", "resident"]),
 ("Gatsby took what he could get, ___ and unscrupulously.", "ravenously", ["ravishingly", "reverently", "rigorously"]),
 ("Gatsby took what he could get, ravenously and ___.", "unscrupulously", ["unsuspiciously", "unsuccessfully", "unscripted"]),
 ("He might have ___ himself, for he had taken Daisy under false pretences.", "despised", ["despaired", "disguised", "devised"]),
 ("Even with Daisy gone, his idea of Louisville was ___ with a melancholy beauty.", "pervaded", ["persuaded", "paraded", "provided"]),
 ("Gatsby looked at Nick anxiously, as if he hoped Nick would ___ that Daisy would call.", "corroborate", ["collaborate", "co-operate", "commemorate"]),
 ("Nick imagined some ___ man telling over and over what had happened at the garage.", "garrulous", ["generous", "glorious", "gregarious"]),
 ("Telephoning a friend of George's was a ___ hope; he had no friends.", "forlorn", ["foreign", "forgotten", "formal"]),
 ("An ashen, fantastic figure glided toward Gatsby through the ___ trees.", "amorphous", ["amorous", "enormous", "anonymous"]),
], discussion=[
 "Gatsby waits all night for a phone call from Daisy that never comes. Why does he keep hoping?",
 "Nick shouts, \"They're a rotten crowd. You're worth the whole damn bunch put together.\" Why does Nick say this, even though he disapproved of Gatsby?",
]),
9: dict(vocab=[
 ("circumstantial", "circumstantial", "adj.", "cir-cum-STAN-tial", "/ˌsɜːrkəmˈstænʃəl/", "정황에 의한; 자세한", "circumstantial evidence · circumstantial details", "The case was based on circumstantial evidence.", "The report was full of circumstantial details."),
 ("surmise", "surmise", "n./v.", "sur-MISE", "/sərˈmaɪz/", "추측(하다)", "pure surmise · surmise that", "That's just surmise; we need facts.", "I surmised that she was angry."),
 ("superfluous", "superfluous", "adj.", "su-PER-flu-ous", "/suːˈpɜːrfluəs/", "불필요한, 쓸데없는", "superfluous words · feel superfluous", "Cut all superfluous words from your essay.", "I felt superfluous at their meeting."),
 ("solidarity", "solidarity", "n.", "sol-i-DAR-i-ty", "/ˌsɑːlɪˈdærəti/", "연대(감), 결속", "in solidarity with · a sense of solidarity", "Workers went on strike in solidarity.", "We stand in solidarity with the victims."),
 ("lingeringly", "lingeringly", "adv.", "LIN-ger-ing-ly", "/ˈlɪŋɡərɪŋli/", "아쉬운 듯 오래, 머뭇거리며", "look lingeringly · hold lingeringly", "She looked lingeringly at the old house.", "He held her hand lingeringly."),
 ("unutterably", "unutterably", "adv.", "un-UT-ter-a-bly", "/ʌnˈʌtərəbli/", "말할 수 없을 만큼", "unutterably sad · unutterably boring", "The news was unutterably sad.", "The lecture was unutterably dull."),
 ("squeamishness", "squeamishness", "n.", "SQUEAM-ish-ness", "/ˈskwiːmɪʃnəs/", "비위가 약함, 지나친 결벽", "moral squeamishness · overcome squeamishness", "Her squeamishness about blood kept her from medicine.", "Business has no room for squeamishness."),
 ("pander", "pandered", "v.", "PAN-der", "/ˈpændər/", "(욕망에) 영합하다, 부추기다", "pander to · pander to the crowd", "Politicians often pander to voters.", "The show panders to cheap tastes."),
 ("transitory", "transitory", "adj.", "TRAN-si-to-ry", "/ˈtrænsətɔːri/", "일시적인, 덧없는", "transitory pleasures · a transitory moment", "Fame can be transitory.", "Youth is transitory."),
 ("commensurate", "commensurate", "adj.", "com-MEN-su-rate", "/kəˈmenʃərət/", "~에 걸맞은, 상응하는", "commensurate with · salary commensurate with experience", "Salary will be commensurate with experience.", "The punishment was not commensurate with the crime."),
], quiz=[
 ("Most newspaper reports were a nightmare—grotesque, ___, eager, and untrue.", "circumstantial", ["substantial", "consequential", "circular"]),
 ("Every ___ about Gatsby, and every practical question, was referred to Nick.", "surmise", ["surprise", "sunrise", "summary"]),
 ("Nick's request that Wolfshiem come seemed ___ when he wrote it.", "superfluous", ["superficial", "supervised", "superstitious"]),
 ("Nick began to feel a scornful ___ between Gatsby and himself against them all.", "solidarity", ["solitude", "solemnity", "similarity"]),
 ("Mr. Gatz held the photograph of the house ___ before Nick's eyes.", "lingeringly", ["laughingly", "loathingly", "loudly"]),
 ("Coming home at Christmas, they were ___ aware of their identity with the Middle West.", "unutterably", ["unalterably", "unbearably", "uncontrollably"]),
 ("Tom went into the jewellery store, rid of Nick's provincial ___ forever.", "squeamishness", ["sweetishness", "selfishness", "skittishness"]),
 ("The vanished trees had once ___ in whispers to the greatest of all human dreams.", "pandered", ["pondered", "pandemic", "wandered"]),
 ("For a ___ enchanted moment man must have held his breath before this continent.", "transitory", ["territory", "transparent", "transmitted"]),
 ("Man faced, for the last time, something ___ to his capacity for wonder.", "commensurate", ["comparative", "compassionate", "commemorative"]),
], discussion=[
 "Almost no one comes to Gatsby's funeral. What does this say about the people who came to his parties?",
 "The book ends: \"So we beat on, boats against the current, borne back ceaselessly into the past.\" What do you think this means? Do you feel this in your own life?",
]),
}

OLD = {
 "negro": ("명사", "(옛·지금은 모욕적) 흑인", "An outdated word for a Black person; today it is offensive (see Chapter 4). Here a Black witness gives important evidence about the yellow car."),
}
IDIOMS = {
 "cahoots": ("한통속, 공모", "in cahoots = secretly working together", "Informal, still used today: \"The two thieves were in cahoots.\" Here Gatsby smiles as if he and Nick had secretly agreed all along."),
}
OLD_MARKS = {7: ["negro"]}
IDIOM_MARKS = {8: ["cahoots"]}

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
