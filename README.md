# 🚀 Intelligent-Resume-Screening-and-Career-Insights-System

An AI-powered recruitment platform that streamlines the hiring process by leveraging Machine Learning and Natural Language Processing (NLP). The system helps classify resumes, evaluate resume-job compatibility, predict suitable career roles based on skills, and provide valuable career insights for job seekers.

---

## 📌 Features

### 📄 Resume Classifier

* Upload resumes in PDF format.
* Predicts the most suitable job category using Machine Learning.
* Calculates an ATS-inspired score based on resume similarity and skill coverage.
* Identifies existing and missing skills.
* Generates personalized resume improvement suggestions.

---

### 🎯 ATS Job Matcher

* Compares a resume with a job description.
* Uses Sentence Transformers for semantic similarity.
* Calculates an ATS compatibility score.
* Helps candidates optimize resumes for specific job postings.

---

### 💼 Skill-Based Job Prediction

* Predicts suitable job roles based on user-entered technical skills.
* Displays confidence scores for the top predicted careers.
* Assists users in identifying career opportunities aligned with their skill set.

---

### 📊 Career Insights

* Provides detailed information for various career domains.
* Includes:

  * Salary Range
  * Required Skills
  * Career Overview
  * Frequently Asked Interview Questions
* Allows users to compare different career paths.

---

## 🛠️ Technology Stack

### Programming Languages

* Python
* HTML
* CSS
* JavaScript

### Framework

* Flask

### Machine Learning & NLP

* Scikit-learn
* Sentence Transformers
* TF-IDF Vectorizer
* Cosine Similarity

### Libraries

* Pandas
* NumPy
* PyPDF2
* PDFPlumber
* NLTK
* Pickle

---

## 📂 Project Structure

```text
AI-Recruitment-System/
│
├── app.py
├── modules/
│   ├── resume_classifier.py
│   ├── job_matcher.py
│   ├── job_prediction.py
│   └── career_insights.py
│
├── models/
│
├── datasets/
│
├── utilities/
│   ├── skills.py
│   └── career_data.py
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│
├── uploads/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aryan-Singhal04/Intelligent-Resume-Screening-and-Career-Insights-System.git
```

### 2. Navigate to the project

```bash
cd AI-Recruitment-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Application Modules

* 🏠 Dashboard
* 📄 Resume Classifier
* 🎯 ATS Job Matcher
* 💼 Skill-Based Job Prediction
* 📊 Career Insights

> Add screenshots of each module inside a `screenshots` folder and reference them here.

---

## 🎯 Future Enhancements

* User Authentication
* Resume Builder
* AI Resume Optimization
* Job Recommendation Engine
* Company Dashboard
* Recruiter Portal
* Resume Ranking System
* Database Integration
* Cloud Deployment
* REST API Support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Aryan Singhal**

* B.Tech Computer Science Graduate
* Machine Learning & Data Analytics Enthusiast
* Passionate about AI, NLP, and Software Development

If you found this project helpful, consider giving it a ⭐ on GitHub.
