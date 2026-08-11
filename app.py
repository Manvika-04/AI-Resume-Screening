from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text_from_pdf(filepath):
    text = ""

    try:
        reader = PdfReader(filepath)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print("PDF ERROR:", e)

    return text


def calculate_ats_score(job_description, resume_text):
    if not job_description.strip() or not resume_text.strip():
        return 0

    try:
        documents = [
            job_description,
            resume_text
        ]

        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        tfidf_matrix = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        score = round(similarity * 100, 2)

        return score

    except Exception as e:
        print("SCORING ERROR:", e)
        return 0


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    job_description = request.form.get("job_description", "").strip()

    files = request.files.getlist("resumes")

    results = []

    if not job_description:
        return "Please enter a job description."

    if not files:
        return "Please upload at least one resume."

    for file in files:

        if file.filename == "":
            continue

        if not allowed_file(file.filename):
            continue

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        resume_text = extract_text_from_pdf(filepath)

        score = calculate_ats_score(
            job_description,
            resume_text
        )

        results.append({
            "filename": filename,
            "score": score
        })

    if not results:
        return "No valid PDF resumes were uploaded."

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return render_template(
        "results.html",
        results=results
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )