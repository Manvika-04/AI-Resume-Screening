# 🤖 AI Resume Screening System

An intelligent and automated **AI-powered Resume Screening System** that evaluates resumes against a given job description and generates an ATS-style compatibility score.

The system allows recruiters, HR professionals, and developers to upload multiple PDF resumes, compare them with a target job description, and rank candidates based on textual similarity using **Natural Language Processing (NLP)** and **TF-IDF-based cosine similarity**.

---

## 📌 Project Overview

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing every resume is time-consuming and can result in inconsistent candidate evaluation.

The **AI Resume Screening System** addresses this problem by automating the initial resume screening process.

The application:

- Accepts a job description from the recruiter.
- Allows multiple PDF resumes to be uploaded.
- Extracts textual content from resumes.
- Processes and analyzes resume content.
- Compares resume content with the job description.
- Calculates an ATS-style similarity score.
- Ranks resumes according to their matching score.
- Displays results through a professional web interface.

The project is designed as a lightweight and easy-to-deploy web application using **Python Flask**.

---

## 🎯 Objectives

The primary objectives of this project are:

1. Automate the initial resume screening process.
2. Reduce the time required for manual resume evaluation.
3. Compare resumes with job-specific requirements.
4. Generate an objective similarity score.
5. Support screening of multiple resumes simultaneously.
6. Provide a simple and professional recruiter-friendly interface.
7. Demonstrate the practical use of NLP in recruitment automation.

---

## ✨ Key Features

### 📄 Multiple Resume Upload

Recruiters can upload multiple resumes in PDF format simultaneously.

### 📝 Job Description Input

The recruiter can enter or paste the complete job description into the web application.

### 🤖 Automated Resume Analysis

The system automatically extracts text from uploaded PDF resumes and compares it against the job description.

### 📊 ATS Similarity Score

Each resume receives a percentage-based similarity score.

Example:

| Resume | ATS Score |
|---|---:|
| Candidate_A.pdf | 86.42% |
| Candidate_B.pdf | 72.18% |
| Candidate_C.pdf | 48.65% |

### 🏆 Candidate Ranking

Resumes are automatically sorted from the highest matching score to the lowest.

### 🎯 Match Classification

The application classifies candidates based on their ATS score:

- **75% and above** → Excellent Match
- **50% – 74%** → Good Match
- **30% – 49%** → Average Match
- **Below 30%** → Low Match

### ⚡ Fast Processing

Multiple resumes can be processed in a single request.

### 🌐 Web-Based Interface

The application provides a browser-based interface built with:

- HTML
- CSS
- Flask
- Jinja2

### 📱 Responsive Design

The interface is designed to work across:

- Desktop
- Laptop
- Tablet
- Mobile devices

### 🔒 Local File Processing

Uploaded resumes are processed locally by the Flask application and are not required to be publicly hosted.

---

# 🧠 How the System Works

The system follows the pipeline below:

```text
                    ┌─────────────────────┐
                    │   Job Description   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Text Input       │
                    │    Processing       │
                    └──────────┬──────────┘
                               │
                               │
┌─────────────────┐            │
│  PDF Resumes    │            │
│ Candidate 1     │            │
│ Candidate 2     │            │
│ Candidate 3     │            │
└────────┬────────┘            │
         │                     │
         ▼                     ▼
┌────────────────────────────────────┐
│       PDF Text Extraction          │
│             PyPDF2                 │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│         Text Processing            │
│            TF-IDF                 │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│       Cosine Similarity             │
│                                    │
│ Resume ↔ Job Description           │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│          ATS Score                 │
│             0–100%                 │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│       Candidate Ranking            │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│       Results Web Page             │
└────────────────────────────────────┘


