import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

nlp = spacy.load("en_core_web_sm")

def analyze_resume(resume_text, jd_text=''):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text) if jd_text else set()

    match_score = calculate_match_score(resume_text, jd_text) if jd_text else 0
    impact_score = calculate_impact_score(resume_text)
    clarity_score = calculate_clarity_score(resume_text)

    fit_score = int(match_score * 0.5 + impact_score * 0.3 + clarity_score * 0.2)

    return {
        "summary": generate_summary(resume_keywords),
        "fit_score": fit_score,
        "missing_keywords": list(jd_keywords - resume_keywords)[:10],
        "strengths": identify_strengths(resume_keywords),
        "weaknesses": identify_weaknesses(resume_keywords, resume_text),
        "metrics_found": bool(impact_score >= 20)
    }

def extract_keywords(text):
    doc = nlp(text.lower())
    return {token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.is_alpha}

def calculate_match_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(similarity[0][0] * 100, 2)  # percentage

def calculate_impact_score(resume_text):
    # Look for metrics like numbers, percentages, currency
    impact_keywords = re.findall(r"\b\d+[%KkMm$]?\b", resume_text)
    return min(len(impact_keywords) * 5, 100)  # max 100

def calculate_clarity_score(text):
    sentences = list(nlp(text).sents)
    if not sentences:
        return 0
    avg_sentence_length = sum(len(sent.text.split()) for sent in sentences) / len(sentences)
    return max(0, 100 - abs(avg_sentence_length - 20) * 5)  # ideal ~20 words per sentence

def generate_summary(keywords):
    return f"Resume covers key areas like: {', '.join(sorted(keywords)[:10])}"

def identify_strengths(keywords):
    strengths = {'python', 'leadership', 'teamwork', 'communication', 'management'}
    return list(keywords & strengths)

def identify_weaknesses(keywords, resume_text):
    common_weaknesses = {'lazy', 'inexperienced', 'nervous', 'disorganized'}
    found = [w for w in common_weaknesses if w in resume_text.lower()]
    return found
