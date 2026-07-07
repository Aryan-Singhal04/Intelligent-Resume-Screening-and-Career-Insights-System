from flask import Flask, render_template, request, jsonify
from modules.classifier import classify_resume
from modules.job_predictor import predict_job
from modules.job_matcher import match_resume
from modules.insights import get_career_details, answer_question
import os

app = Flask(__name__)

# ---------------- Dashboard ----------------
@app.route("/")
def dashboard():
    return render_template("dashboard.html")


# ---------------- Resume Classifier ----------------
@app.route("/resume-classifier", methods=["GET", "POST"])
def resume_classifier():

    if request.method == "POST":

        file = request.files["file"]

        filepath = os.path.join("uploads", file.filename)

        os.makedirs("uploads", exist_ok=True)

        file.save(filepath)

        result = classify_resume(filepath)

        return render_template(
            "classifier.html",
            **result
        )

    return render_template("classifier.html")


# ---------------- ATS Job Matcher ----------------
@app.route("/job-matcher", methods=["GET", "POST"])
def job_matcher():

    if request.method == "POST":

        file = request.files["resume"]
        job_desc = request.form["jobdesc"]

        result = match_resume(file, job_desc)

        return render_template(
            "matcher.html",
            **result
        )

    return render_template("matcher.html")
# ---------------- Job Prediction ----------------
@app.route("/job-prediction", methods=["GET", "POST"])
def job_prediction():

    if request.method == "POST":
        skills = request.form.get("skills", "")
        result = predict_job(skills)

        return render_template("prediction.html", **result)

    return render_template("prediction.html")


# ---------------- Career Insights ----------------
@app.route("/career-insights", methods=["GET", "POST"])
def career_insights():

    if request.method == "POST":

        selected = request.form.get("category")
        compare = request.form.get("compare_category")

        result = get_career_details(selected, compare)

        return render_template(
            "career.html",
            **result
        )

    # Initial page load
    result = get_career_details(None)

    return render_template(
        "career.html",
        **result
    )


# ---------------- Career Q&A ----------------
@app.route("/ask", methods=["POST"])
def ask():

    body = request.get_json()

    question = body.get("question", "").strip()
    career = body.get("career", "").strip()

    result = answer_question(career, question)

    if "error" in result:
        return jsonify({"answer": result["error"]}), 404

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)