import pickle
import numpy as np

# Load model artifacts
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/cv.pkl", "rb"))
lb = pickle.load(open("models/label_encoder.pkl", "rb"))


def get_top_predictions(skills_vector, top_n=3):
    """Return top-N predicted jobs with confidence percentages."""

    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(skills_vector)[0]
        top_idx = np.argsort(probs)[::-1][:top_n]
        top_jobs = lb.inverse_transform(top_idx)
        top_scores = [round(probs[i] * 100, 1) for i in top_idx]
    else:
        prediction = model.predict(skills_vector)
        top_jobs = [lb.inverse_transform(prediction)[0]]
        top_scores = [100.0]

    return list(zip(top_jobs, top_scores))


def predict_job(skills):
    """Predict the best job based on skills."""

    if not skills.strip():
        return {"error": "Please enter at least one skill."}

    try:
        skills_vector = vectorizer.transform([skills])
        top_predictions = get_top_predictions(skills_vector)

        best_job, best_score = top_predictions[0]
        other_predictions = top_predictions[1:]

        if best_score >= 75:
            verdict = ("Strong Match", "strong")
        elif best_score >= 45:
            verdict = ("Moderate Match", "moderate")
        else:
            verdict = ("Low Confidence", "low")

        return {
            "prediction": best_job,
            "score": best_score,
            "verdict": verdict,
            "others": other_predictions,
            "skills_input": skills,
        }

    except Exception as e:
        return {"error": str(e)}