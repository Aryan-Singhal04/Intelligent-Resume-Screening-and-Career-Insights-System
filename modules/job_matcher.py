import pdfplumber
import re
import nltk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Download once
nltk.download("stopwords")
nltk.download("wordnet")

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


# ---------------- TEXT CLEANING ----------------
def clean_text(text):
    text = text.lower()

    # Remove URLs and emails
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z ]", " ", text)

    return text


# ---------------- PDF EXTRACTION ----------------
def extract_text(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return clean_text(text)


# ---------------- KEYWORD OVERLAP ----------------
def keyword_overlap(resume, job):

    resume_words = set(resume.split())
    job_words = set(job.split())

    overlap = resume_words.intersection(job_words)

    if len(job_words) == 0:
        return 0

    return len(overlap) / len(job_words)


# ---------------- SIMILARITY ----------------
def calculate_similarity(resume, job):

    embeddings = model.encode([resume, job])

    semantic_score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    keyword_score = keyword_overlap(resume, job)

    final_score = (0.7 * semantic_score) + (0.3 * keyword_score)

    return min(82, round(final_score * 100, 2) + 30)


# ---------------- MAIN FUNCTION ----------------
def match_resume(pdf_file, job_desc):

    job_desc = clean_text(job_desc)

    resume_text = extract_text(pdf_file)

    score = calculate_similarity(resume_text, job_desc)

    return {
        "score": score
    }