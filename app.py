from flask import Flask, render_template, request
import os
import pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Folder to store uploaded resumes
UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create resumes folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


# Function to calculate ATS score
def calculate_score(resume_text, job_description):

    documents = [resume_text, job_description]

    cv = CountVectorizer()

    matrix = cv.fit_transform(documents)

    similarity = cosine_similarity(matrix)[0][1]

    return round(similarity * 100, 2)


# Home Route
@app.route("/")
def home():

    return render_template("index.html")


# Analyze Route
@app.route("/analyze", methods=["POST"])
def analyze():

    job_description = request.form["job_description"]

    uploaded_files = request.files.getlist("resumes")

    results = []

    for file in uploaded_files:

        if file.filename.endswith(".pdf"):

            save_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(save_path)

            # Extract text from resume
            resume_text = extract_text_from_pdf(save_path)

            # Calculate ATS score
            score = calculate_score(
                resume_text,
                job_description
            )

            results.append({
                "filename": file.filename,
                "score": score
            })

    # Sort by highest ATS score
    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return render_template(
        "results.html",
        results=results
    )


# Run App
if __name__ == "__main__":

    app.run(debug=True)