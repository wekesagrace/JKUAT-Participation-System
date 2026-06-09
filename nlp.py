import re

# ══════════════════════════════════════════════════════════
# EXPANDED KEYWORD LISTS
# ══════════════════════════════════════════════════════════

NEGATIVE_WORDS = [
    # Strong negative
    'terrible','horrible','awful','disgusting','pathetic',
    'useless','broken','crashed','crashing','poor','bad',
    'worst','dirty','filthy','unsafe','dangerous','unfair',
    'unacceptable','disappointing','frustrated','frustrating',
    'slow','ignored','unresponsive','overpriced','never',
    'failing','failed','problem','issue','complaint','angry',
    'disappointed','inadequate','insufficient','lacking',
    'denied','refused','blocked','stuck','delayed','late',
    'absent','missing','unavailable','closed','locked',
    'broken down','not working','does not work','no water',
    'no wifi','no internet','no power','no electricity',
    'cut off','shut down','keeps crashing','very slow',
    'too slow','extremely slow','always slow','never works',
    'always down','always off','always closed','no response',
    'not responding','never respond','poor service','bad service',
    'terrible service','horrible service','very bad','so bad',
    'really bad','extremely bad','very poor','so poor',
    'really poor','extremely poor','not clean','very dirty',
    'really dirty','not safe','very unsafe','really unsafe',
    'not fair','very unfair','really unfair','cannot access',
    'can not access','unable to access','hard to access',
    'difficult to access','overcrowded','congested','noisy',
    'smelly','leaking','flooded','dark','cold','hot',
    'uncomfortable','inconvenient','inefficient','ineffective',
    'incompetent','rude','arrogant','dismissive','unhelpful',
    'disorganised','disorganized','chaotic','messy','untidy',
    'outdated','old','ancient','obsolete','not enough',
    'too few','too little','too much','too expensive',
    'overcharged','exploitation','corrupt','corruption',
    'bribery','unfairness','discrimination','harassment',
    'bullying','intimidation','insecurity','theft','stolen',
    'vandalism','neglect','abandoned','deteriorating',
    'dilapidated','run down','falling apart','collapsing'
]

POSITIVE_WORDS = [
    # Strong positive
    'excellent','fantastic','wonderful','amazing','great',
    'outstanding','superb','brilliant','perfect','helpful',
    'clean','modern','improved','organised','supportive',
    'accessible','efficient','professional','impressive',
    'well equipped','well maintained','very good','love',
    'appreciate','thank','best','recommend','happy','pleased',
    'satisfied','comfortable','convenient','reliable','fast',
    'quick','responsive','friendly','kind','welcoming',
    'accommodating','understanding','cooperative','dedicated',
    'hardworking','diligent','thorough','careful','neat',
    'tidy','spacious','bright','quiet','peaceful','safe',
    'secure','fair','transparent','accountable','inclusive',
    'diverse','innovative','creative','progressive','modern',
    'up to date','state of the art','cutting edge','advanced',
    'high quality','top notch','first class','world class',
    'very good','so good','really good','extremely good',
    'very clean','really clean','extremely clean','very safe',
    'really safe','very helpful','really helpful','very fast',
    'really fast','very efficient','really efficient',
    'very friendly','really friendly','very organised',
    'really organised','very well','really well','works well',
    'working well','working perfectly','works perfectly',
    'highly recommend','strongly recommend','love it',
    'enjoy it','great experience','good experience',
    'positive experience','wonderful experience',
    'fantastic experience','excellent service','great service',
    'good service','wonderful service','fantastic service'
]

NEUTRAL_INDICATORS = [
    'will','schedule','notice','inform','update','announce',
    'reminder','note','please','kindly','attention','hereby',
    'effective','commencing','starting','beginning','ending',
    'closing','opening','meeting','session','held','conducted',
    'organised','planned','proposed','suggested','recommended',
    'discussed','presented','shared','communicated','notified',
    'reminded','informed','advised','instructed','directed',
    'required','requested','invited','welcome','attend',
    'participate','register','submit','apply','collect',
    'receive','obtain','access','visit','contact','reach',
    'call','email','report','daily','weekly','monthly',
    'every','each','all','every day','every week','regularly'
]

TOPIC_KEYWORDS = {
    'Infrastructure': [
        'building','road','hall','lab','computer','internet',
        'wifi','network','electricity','water','toilet',
        'facility','equipment','room','class','classroom',
        'library','hostel','construction','repair','lift',
        'elevator','parking','gate','fence','wall','floor',
        'roof','ceiling','window','door','light','lighting',
        'power','generator','borehole','tank','pipe','drainage'
    ],
    'Student Welfare': [
        'hostel','food','cafeteria','health','clinic','mental',
        'stress','counselling','welfare','accommodation','safety',
        'security','transport','bus','fees','scholarship','loan',
        'water','hygiene','sanitation','healthcare','doctor',
        'nurse','medicine','treatment','insurance','allowance',
        'stipend','bursary','grant','support','assistance',
        'disability','special needs','counselor','psychologist'
    ],
    'Academic': [
        'lecture','exam','course','unit','grade','marks',
        'study','research','assignment','project','timetable',
        'schedule','lecturer','professor','tutorial','seminar',
        'curriculum','class','teaching','learning','degree',
        'diploma','certificate','graduation','attachment',
        'internship','industrial','practical','laboratory',
        'field','thesis','dissertation','supervisor','results',
        'transcript','academic','semester','trimester','module'
    ],
    'Administration': [
        'registration','portal','fee','payment','document',
        'office','staff','management','policy','rule',
        'regulation','process','admission','clearance',
        'certificate','transcript','admin','response','service',
        'helpdesk','customer','finance','accounts','bursar',
        'registrar','dean','principal','vice','chancellor',
        'director','manager','coordinator','secretary','clerk',
        'identification','id','card','letter','application'
    ],
    'Student Activities': [
        'club','sport','event','activity','association','union',
        'student','leader','election','representation','meeting',
        'conference','competition','tournament','recreation',
        'social','games','athletics','football','basketball',
        'volleyball','rugby','swimming','chess','debate',
        'drama','music','choir','dance','art','culture',
        'community','outreach','charity','volunteer','award'
    ]
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def count_matches(text_lower, word_list):
    """Count how many words from the list appear in text"""
    count = 0
    for word in word_list:
        if word in text_lower:
            count += 1
    return count


def analyze_sentiment(text):
    """
    Rule-based sentiment analysis using expanded
    keyword lists. Much more accurate for Kenyan
    student feedback than TextBlob alone.
    """
    text_lower  = text.lower()
    cleaned     = clean_text(text)

    neg_count   = count_matches(text_lower, NEGATIVE_WORDS)
    pos_count   = count_matches(text_lower, POSITIVE_WORDS)
    neu_count   = count_matches(text_lower, NEUTRAL_INDICATORS)

    # Decision logic
    if neg_count == 0 and pos_count == 0:
        # No strong keywords found — use neutral
        # unless neutral indicators confirm it
        sentiment = 'Neutral'

    elif neg_count > pos_count:
        sentiment = 'Negative'

    elif pos_count > neg_count:
        sentiment = 'Positive'

    elif pos_count == neg_count:
        # Tie — check neutral indicators
        if neu_count > 0:
            sentiment = 'Neutral'
        else:
            sentiment = 'Neutral'
    else:
        sentiment = 'Neutral'

    keywords = extract_keywords(cleaned)
    return sentiment, keywords


def extract_keywords(text):
    """Extract top 5 meaningful keywords"""
    stop_words = {
        'the','is','in','it','of','and','a','to','was',
        'that','he','she','they','we','you','i','my','our',
        'are','be','been','being','have','has','had','do',
        'does','did','will','would','could','should','may',
        'this','with','for','on','at','by','an','as','or',
        'but','not','so','if','its','from','very','also',
        'just','more','than','there','their','about','which',
        'when','what','who','how','all','each','both','been'
    }
    words    = text.split()
    keywords = [w for w in words
                if w not in stop_words and len(w) > 3]
    seen = []
    for word in keywords:
        if word not in seen:
            seen.append(word)
    return ', '.join(seen[:5])


def detect_topic(text):
    """Detect main topic using keyword matching"""
    cleaned = clean_text(text)
    words   = set(cleaned.split())
    scores  = {}
    for topic, keywords in TOPIC_KEYWORDS.items():
        score = len(words.intersection(set(keywords)))
        scores[topic] = score
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else 'General'


def analyze_topics_lda(feedback_list):
    """Count topics across all feedback"""
    if not feedback_list:
        return {}
    topic_counts = {t: 0 for t in TOPIC_KEYWORDS}
    topic_counts['General'] = 0
    for text in feedback_list:
        topic = detect_topic(text)
        topic_counts[topic] = topic_counts.get(topic, 0) + 1
    return {k: v for k, v in topic_counts.items() if v > 0}