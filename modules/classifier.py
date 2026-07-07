import pickle
import re
import PyPDF2
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from utilitis.skills import Skills, category_map

# ---------------- Load Models ----------------
tfidf = pickle.load(open("models/tfidf.pkl", "rb"))
clf = pickle.load(open("models/clf.pkl", "rb"))

# ---------------- Load Dataset ----------------
dataset = pd.read_csv("datasets/dataset.csv")


def clean(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


dataset["cleaned"] = dataset["Resume"].apply(clean)
dataset_vectors = tfidf.transform(dataset["cleaned"])


# ---------------- PDF Extraction ----------------
def extract_text_from_pdf(filepath):
    text = ""

    with open(filepath, "rb") as f:
        reader = PyPDF2.PdfReader(f)

        for page in reader.pages:
            text += page.extract_text() or ""

    return text.strip()


# ---------------- Skill Extraction ----------------
def extract_skills(resume_text, category):

    skills = Skills.get(category, [])

    if not skills:

        for key in Skills:

            if key.lower() in category.lower() or category.lower() in key.lower():
                skills = Skills[key]
                break

    found = [skill for skill in skills if skill in resume_text]
    missing = [skill for skill in skills if skill not in resume_text]

    return found, missing


# ---------------- ATS Score ----------------
def compute_ats(resume_vector, found, missing):

    similarity = cosine_similarity(resume_vector, dataset_vectors)

    cosine_score = float(similarity.max()) * 100

    total = len(found) + len(missing)

    skill_score = (len(found) / total * 100) if total > 0 else 0

    ats = round((0.6 * cosine_score) + (0.4 * skill_score), 1)

    return ats, round(cosine_score, 1), round(skill_score, 1)


# ---------------- Suggestions ----------------
def get_tips(missing, ats, category):

    tips = []

    if ats < 30:
        tips.append(
            "Very low match. Rewrite your resume to align with the target role."
        )

    elif ats < 50:
        tips.append(
            "Below average. Focus on adding role-specific keywords."
        )

    elif ats < 70:
        tips.append(
            "Decent resume. Add more targeted keywords."
        )

    else:
        tips.append(
            "Strong resume! Keep projects and achievements quantified."
        )

    if missing:
        tips.append(
            "Add these missing skills: " + ", ".join(missing[:6])
        )

    tips.append(
        "Use bullet points, action verbs, and quantify achievements."
    )

    tips.append(
        f"Tailor your resume specifically for {category} roles."
    )

    return tips


# ---------------- Main Function ----------------
def classify_resume(filepath):

    raw_text = extract_text_from_pdf(filepath)

    if not raw_text:
        return {"error": "Could not read PDF."}

    cleaned = clean(raw_text)

    resume_vector = tfidf.transform([cleaned])

    label = clf.predict(resume_vector)[0]

    category = category_map[label]

    found, missing = extract_skills(cleaned, category)

    ats, cos_score, skill_score = compute_ats(
        resume_vector,
        found,
        missing
    )

    tips = get_tips(missing, ats, category)

    if ats < 15:
        category = "Unknown — Resume may be too generic or unrelated."

    return {
        "category": category,
        "ats": ats,
        "cos_score": cos_score,
        "skill_score": skill_score,
        "found_skills": found,
        "missing_skills": missing[:6],
        "tips": tips,
    }