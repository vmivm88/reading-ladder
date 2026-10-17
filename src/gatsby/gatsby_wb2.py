# The Great Gatsby workbook, chapters 4–6. vocab: lemma, surface-in-text, pos, stress, ipa, korean, collocations, ex1, ex2 (examples are original)
import json, os, re

WB = {
4: dict(vocab=[
 ("generality", "generalities", "n.", "gen-er-AL-i-ty", "/ˌdʒenəˈræləti/", "일반론, 막연한 말", "speak in generalities · vague generalities", "He spoke only in generalities.", "Let's move from generalities to details."),
 ("resourcefulness", "resourcefulness", "n.", "re-SOURCE-ful-ness", "/rɪˈsɔːrsfəlnəs/", "수완, 재치", "show resourcefulness · great resourcefulness", "Her resourcefulness saved the trip.", "Camping teaches resourcefulness."),
 ("sporadic", "sporadic", "adj.", "spo-RAD-ic", "/spəˈrædɪk/", "산발적인, 이따금 일어나는", "sporadic fighting · sporadic rain", "There was sporadic rain all day.", "His visits were sporadic."),
 ("punctilious", "punctilious", "adj.", "punc-TIL-i-ous", "/pʌŋkˈtɪliəs/", "격식을 꼼꼼히 차리는, 깍듯한", "punctilious manners · punctilious about", "He was punctilious about being on time.", "She has a punctilious, polite manner."),
 ("labyrinth", "labyrinth", "n.", "LAB-y-rinth", "/ˈlæbərɪnθ/", "미로", "a labyrinth of streets · bureaucratic labyrinth", "The old town is a labyrinth of narrow streets.", "I got lost in a labyrinth of rules."),
 ("evasion", "evasions", "n.", "e-VA-sion", "/ɪˈveɪʒən/", "회피, 얼버무림", "tax evasion · polite evasions", "His answer was just an evasion.", "Tax evasion is a crime."),
 ("elicit", "elicited", "v.", "e-LIC-it", "/ɪˈlɪsɪt/", "(반응·정보를) 이끌어 내다", "elicit a response · elicit information", "The joke elicited a big laugh.", "The police elicited a confession."),
 ("incredulity", "incredulity", "n.", "in-cre-DU-li-ty", "/ˌɪnkrəˈduːləti/", "믿지 못함, 의심", "in incredulity · stare in incredulity", "She stared at him in incredulity.", "The news was met with incredulity."),
 ("succulent", "succulent", "adj.", "SUC-cu-lent", "/ˈsʌkjələnt/", "즙이 많은, 맛있는", "a succulent steak · succulent fruit", "We ate succulent grilled chicken.", "The peaches were sweet and succulent."),
 ("unfathomable", "unfathomable", "adj.", "un-FATH-om-a-ble", "/ʌnˈfæðəməbl/", "헤아릴 수 없는, 깊은", "unfathomable depths · an unfathomable mystery", "The ocean is unfathomable.", "Her reasons were unfathomable to me."),
], quiz=[
 ("The names on the old timetable give a better impression of Gatsby's guests than Nick's ___.", "generalities", ["generations", "generosities", "galleries"]),
 ("Gatsby balanced on the dashboard of his car with that ___ of movement so peculiarly American.", "resourcefulness", ["restlessness", "resentfulness", "respectfulness"]),
 ("American grace came from the formless grace of our nervous, ___ games.", "sporadic", ["spastic", "sporting", "spiritual"]),
 ("Gatsby's restlessness kept breaking through his ___ manner.", "punctilious", ["punctual", "pretentious", "puncturing"]),
 ("Gatsby's car was terraced with a ___ of windshields that mirrored a dozen suns.", "labyrinth", ["laboratory", "lavatory", "lavender"]),
 ("When Gatsby asked his opinion of him, Nick began the generalized ___ which that question deserves.", "evasions", ["invasions", "elevations", "equations"]),
 ("Gatsby showed a medal from Montenegro and the circumstances that had ___ this tribute.", "elicited", ["illicit", "elected", "eclipsed"]),
 ("Nick's ___ was submerged in fascination as Gatsby showed his photograph from Oxford.", "incredulity", ["incredibility", "insecurity", "integrity"]),
 ("A ___ hash arrived, and Mr. Wolfshiem began to eat with ferocious delicacy.", "succulent", ["succinct", "successful", "sufficient"]),
 ("Daisy used to look at the young officer with ___ delight, Jordan said.", "unfathomable", ["unforgivable", "unfashionable", "unfavorable"]),
], discussion=[
 "Gatsby tells Nick the story of his life, but it sounds too perfect. Why do you think Gatsby needs this story? Do people today create \"perfect\" life stories online?",
 "Jordan says Gatsby bought his house to be across the bay from Daisy. Is this romantic or unhealthy? Why?",
]),
5: dict(vocab=[
 ("tactlessly", "tactlessly", "adv.", "TACT-less-ly", "/ˈtæktləsli/", "눈치 없이, 무신경하게", "speak tactlessly · tactlessly ask", "He tactlessly asked about her divorce.", "She tactlessly mentioned his weight."),
 ("harrowed", "harrowed", "adj.", "HAR-rowed", "/ˈhæroʊd/", "괴로운, 심란한", "feel harrowed · a harrowed look", "She looked tired and harrowed.", "He felt harrowed by the news."),
 ("exhilarating", "exhilarating", "adj.", "ex-HIL-a-rat-ing", "/ɪɡˈzɪləreɪtɪŋ/", "신나게 하는, 아주 상쾌한", "an exhilarating ride · exhilarating experience", "The roller coaster was exhilarating.", "Skiing in fresh snow is exhilarating."),
 ("defunct", "defunct", "adj.", "de-FUNCT", "/dɪˈfʌŋkt/", "고장 난, 더 이상 쓰이지 않는", "a defunct company · defunct machine", "The factory is now defunct.", "He collects defunct phones."),
 ("distraught", "distraught", "adj.", "dis-TRAUGHT", "/dɪˈstrɔːt/", "몹시 괴로워하는, 제정신이 아닌", "distraught parents · look distraught", "The distraught mother searched for her child.", "He was distraught after the accident."),
 ("reproach", "reproach", "n./v.", "re-PROACH", "/rɪˈproʊtʃ/", "꾸짖음, 비난", "a look of reproach · beyond reproach", "She gave him a look of reproach.", "His behavior was beyond reproach."),
 ("dishevelled", "dishevelled", "adj.", "di-SHEV-elled", "/dɪˈʃevəld/", "(머리·옷이) 헝클어진", "dishevelled hair · look dishevelled (US: disheveled)", "He came in dishevelled from the wind.", "She looked dishevelled after the long flight."),
 ("inconceivable", "inconceivable", "adj.", "in-con-CEIV-a-ble", "/ˌɪnkənˈsiːvəbl/", "상상할 수 없는", "it is inconceivable that · inconceivable pain", "It's inconceivable that he lied.", "The change was inconceivable ten years ago."),
 ("nebulous", "nebulous", "adj.", "NEB-u-lous", "/ˈnebjələs/", "흐릿한, 모호한", "a nebulous idea · nebulous plans", "He had only a nebulous plan.", "The sky was a nebulous gray."),
 ("illusion", "illusion", "n.", "il-LU-sion", "/ɪˈluːʒən/", "환상, 착각", "be under the illusion · an optical illusion", "He's under the illusion that he's always right.", "The mirror creates an illusion of space."),
], quiz=[
 ("Gatsby offered Nick work so obviously and ___ in return for a favor that Nick had to cut him off.", "tactlessly", ["tastelessly", "tirelessly", "tunefully"]),
 ("Nick, a little ___ himself, went out into the yard when Daisy's car arrived.", "harrowed", ["harvested", "hollowed", "harnessed"]),
 ("The ___ ripple of Daisy's voice was a wild tonic in the rain.", "exhilarating", ["exhausting", "exasperating", "exaggerating"]),
 ("Gatsby's head rested against the face of a ___ mantelpiece clock.", "defunct", ["defiant", "deficient", "default"]),
 ("From this position his ___ eyes stared down at Daisy.", "distraught", ["distrust", "draught", "dissolved"]),
 ("When Nick called him rude, Gatsby looked at him with unforgettable ___.", "reproach", ["approach", "reprieve", "rapport"]),
 ("In one room a ___ man in pyjamas was doing liver exercises on the floor.", "dishevelled", ["dissolved", "distilled", "devilled"]),
 ("Gatsby had waited with his teeth set at an ___ pitch of intensity.", "inconceivable", ["inconsiderable", "inconvenient", "unconscionable"]),
 ("Klipspringer wore duck trousers of a ___ hue.", "nebulous", ["nervous", "fabulous", "nebulizing"]),
 ("Daisy fell short of his dreams because of the colossal vitality of his ___.", "illusion", ["allusion", "elusion", "inclusion"]),
], discussion=[
 "When Gatsby finally meets Daisy again, he is terribly nervous. Why do you think the meeting is so hard for him?",
 "Nick says Daisy \"tumbled short of his dreams\" because Gatsby's dream was too big. Can a dream be more powerful than the real person?",
]),
6: dict(vocab=[
 ("transpire", "transpired", "v.", "tran-SPIRE", "/trænˈspaɪər/", "(사실이) 드러나다, 밝혀지다", "it transpired that · what transpired", "It transpired that he had lied.", "Nobody knows what transpired that night."),
 ("notoriety", "notoriety", "n.", "no-to-RI-e-ty", "/ˌnoʊtəˈraɪəti/", "악명, 좋지 않은 평판", "gain notoriety · notoriety for", "The scandal brought him notoriety.", "The town gained notoriety for crime."),
 ("insidious", "insidious", "adj.", "in-SID-i-ous", "/ɪnˈsɪdiəs/", "서서히 해를 끼치는, 교활한", "an insidious disease · insidious effects", "Stress can have insidious effects.", "It was an insidious plan."),
 ("meretricious", "meretricious", "adj.", "mer-e-TRI-cious", "/ˌmerəˈtrɪʃəs/", "겉만 번지르르한, 저속한", "meretricious glamour · meretricious beauty", "The hotel had a meretricious kind of luxury.", "Don't be fooled by meretricious ads."),
 ("ineffable", "ineffable", "adj.", "in-EF-fa-ble", "/ɪnˈefəbl/", "말로 표현할 수 없는", "ineffable beauty · ineffable joy", "The view had an ineffable beauty.", "She felt an ineffable sadness."),
 ("reverie", "reveries", "n.", "REV-er-ie", "/ˈrevəri/", "몽상, 공상", "lost in reverie · a happy reverie", "She was lost in a reverie by the window.", "His reveries were full of adventure."),
 ("perturbed", "perturbed", "adj.", "per-TURBED", "/pərˈtɜːrbd/", "불안한, 동요한", "perturbed by · look perturbed", "He seemed perturbed by the news.", "She wasn't at all perturbed."),
 ("obtrusive", "obtrusive", "adj.", "ob-TRU-sive", "/əbˈtruːsɪv/", "눈에 거슬리는, 너무 드러나는", "obtrusive advertising · not obtrusive", "The music was loud and obtrusive.", "The new building is too obtrusive."),
 ("elusive", "elusive", "adj.", "e-LU-sive", "/ɪˈluːsɪv/", "붙잡기 어려운, 기억이 잘 안 나는", "an elusive goal · elusive memory", "Happiness can be elusive.", "The answer remained elusive."),
 ("incarnation", "incarnation", "n.", "in-car-NA-tion", "/ˌɪnkɑːrˈneɪʃən/", "화신, 구현", "the incarnation of · a past incarnation", "She is the incarnation of kindness.", "In a past incarnation, he was a teacher."),
], quiz=[
 ("It ___ that the reporter had only heard Gatsby's name around his office.", "transpired", ["transported", "perspired", "inspired"]),
 ("Gatsby's ___ was spread by the hundreds who had accepted his hospitality.", "notoriety", ["notary", "priority", "authority"]),
 ("Young James Gatz saw Dan Cody's yacht drop anchor over the most ___ flat on Lake Superior.", "insidious", ["invidious", "industrious", "studious"]),
 ("Gatsby gave himself to the service of a vast, vulgar, and ___ beauty.", "meretricious", ["meritorious", "mysterious", "malicious"]),
 ("A universe of ___ gaudiness spun itself out in his brain at night.", "ineffable", ["ineffective", "inedible", "inflatable"]),
 ("For a while these ___ gave his imagination an outlet.", "reveries", ["revelries", "reverses", "rivalries"]),
 ("Tom was evidently ___ at Daisy's running around alone.", "perturbed", ["perfumed", "purchased", "perjured"]),
 ("Daisy was appalled by West Egg's raw vigour and the too ___ fate that herded its people.", "obtrusive", ["abusive", "obsessive", "obsolete"]),
 ("Gatsby's words reminded Nick of something—an ___ rhythm, a fragment of lost words.", "elusive", ["exclusive", "abusive", "effusive"]),
 ("At his lips' touch she blossomed for him like a flower and the ___ was complete.", "incarnation", ["incantation", "carnation", "incarceration"]),
], discussion=[
 "James Gatz invented \"Jay Gatsby\" at seventeen. Is it possible to completely reinvent yourself? What do you gain and lose?",
 "Gatsby says, \"Can't repeat the past? Why of course you can!\" Do you agree with him? Why is this belief dangerous?",
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
