# HR Resume & LinkedIn Shortlisting Agent

AI-Powered Hybrid Resume Screening & Candidate Ranking System

---
# Demo Video Link
https://youtu.be/FajVAzzGipY

---

# Overview

The HR Resume & LinkedIn Shortlisting Agent is an AI-powered hiring assistant designed to automate the initial screening, semantic matching, and ranking of candidates using:

- Job Descriptions (JD)
- Candidate Resumes
- LinkedIn Profiles

The system combines:

- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Hybrid AI Scoring
- Vector Similarity Search
- Explainable AI Reasoning
- Automated Report Generation

This project was designed as a scalable ATS-style AI hiring platform rather than a simple chatbot.

---

# Core Features

## Resume & JD Parsing

- Extracts structured information from:
  - PDFs
  - DOCX files
  - LinkedIn profile text
- Converts unstructured data into validated schemas

---

## Semantic Candidate Matching

Uses embeddings to compare:

- Skills
- Experience
- Projects
- Education

instead of relying only on keyword matching.

---

## Hybrid AI Scoring System

Combines:

### Deterministic Semantic Retrieval
using embeddings and vector search

with

### LLM-based Reasoning
for explainable candidate evaluation.

---

## Explainable AI Rankings

Every candidate receives:

- Final score
- Strengths
- Weaknesses
- Missing skills
- Human-readable explanations

---

## Automated Report Generation

Generates:

- JSON reports
- HTML recruiter reports
- PDF shortlist reports

---

# System Architecture

```text
JD Upload
   ↓
JD Parsing
   ↓
Resume / LinkedIn Parsing
   ↓
Schema Validation
   ↓
Chunk Generation
   ↓
Sentence Transformer Embeddings
   ↓
FAISS Vector Search
   ↓
Semantic Candidate Retrieval
   ↓
Hybrid Rubric Scoring
   ↓
Candidate Ranking
   ↓
HTML / PDF / JSON Report Generation
```

---

# Models Used

# 1. Embedding Model

## Model

```python
sentence-transformers/all-MiniLM-L6-v2
```

## Why this model?

- Completely free
- Lightweight
- Fast inference
- Strong semantic similarity performance
- Runs locally
- Excellent for resume/JD similarity

## Purpose

- Resume embeddings
- Skill similarity
- Project similarity
- Semantic retrieval
- FAISS indexing

---

# 2. LLM Reasoning Model

## Model

```python
llama-3.3-70b-versatile
```

Provider:

```text
Groq API
```

## Why this model?

- High inference speed
- Strong reasoning capability
- Good JSON formatting
- Free-tier accessibility
- Excellent structured extraction

## Purpose

- Resume parsing
- JD parsing
- Candidate evaluation
- Communication scoring
- Strengths & weaknesses generation

---

# Key Design Decisions

# Hybrid Scoring Instead of Pure LLM Scoring

The system intentionally avoids relying entirely on LLM outputs.

Instead:

- Embeddings handle semantic similarity
- LLMs provide reasoning and explanations

## Benefits

- Lower hallucination risk
- Better reproducibility
- Faster retrieval
- Lower cost
- Better scalability

---

# Section-wise Embeddings

Instead of embedding the full resume as one block, resumes are divided into:

- Skills
- Experience
- Projects
- Education

## Benefits

- Better retrieval accuracy
- More explainable scoring
- Improved semantic search

---

# Retrieval Before Scoring

The system first retrieves top candidates using FAISS before expensive LLM evaluation.

## Benefits

- Reduces API calls
- Faster inference
- Better scalability

---

# Schema Validation Layer

All LLM outputs are validated using Pydantic schemas.

## Benefits

- Prevents malformed JSON crashes
- Ensures consistent structure
- Handles missing fields safely

---

# Explainable AI Design

Every score contains:

- Numerical value
- Human-readable explanation

This improves:

- HR trust
- Transparency
- Auditability

---

# Tech Stack

# Core AI Stack

- sentence-transformers
- FAISS
- LangChain
- Groq API
- Pydantic

---

# Backend

- Flask
- Flask-CORS

---

# Parsing & File Processing

- PyMuPDF
- python-docx
- json
- regex (re)

---

# Report Generation

- Jinja2
- WeasyPrint

---

# Utilities

- NumPy
- scikit-learn
- python-dotenv

---

# FAISS Vector Database

FAISS is used as the local vector database.

## Responsibilities

- Store candidate embeddings
- Perform semantic similarity search
- Retrieve top matching candidates

## Why FAISS?

- Completely local
- Extremely fast
- Lightweight
- No cloud setup required
- Ideal for MVP-scale systems

---

# Input Sanitization & Security

# Schema Validation

All parsed outputs pass through Pydantic validation.

---

# JSON Cleaning Layer

Custom JSON cleaning handles:

- Markdown wrappers
- Malformed JSON
- Broken LLM outputs

---

# Safe Dictionary Access

The system avoids:

```python
candidate['skills']
```

and uses:

```python
candidate.get('skills', [])
```

to prevent runtime crashes.

---

# Graceful Failure Handling

Resume parsing and scoring are wrapped inside:

```python
try/except
```

blocks to prevent complete pipeline failure.

---

# Environment Variable Security

Sensitive credentials are stored in:

```text
.env
```

instead of hardcoded source files.

---

# Hybrid Rubric Scoring System

| Category | Weight |
|---|---|
| Skills Match | 30% |
| Experience Relevance | 25% |
| Education & Certifications | 15% |
| Project Portfolio | 20% |
| Communication Quality | 10% |

---

# Generated Outputs

The system generates:

- JSON ranking reports
- HTML recruiter reports
- PDF shortlist reports

Reports include:

- Candidate rankings
- Rubric scores
- Explanations
- Missing skills
- Strengths
- Weaknesses
- Final recommendations

---

# Example Folder Structure

```text
project/
│
├── app.py
├── requirements.txt
├── .env
│
├── parsing/
│   ├── jd_parser.py
│   ├── resume_parser.py
│
├── scoring/
│   ├── hybrid_scorer.py
│   ├── experience_scorer.py
│   ├── education_scorer.py
│   ├── communication_scorer.py
│   ├── weighted_engine.py
│
├── embeddings/
│   ├── embedding_engine.py
│   ├── faiss_store.py
│
├── reports/
│   ├── templates/
│   ├── pdf_generator.py
│
├── utils/
│   ├── json_cleaner.py
│   ├── validators.py
│
└── data/
    ├── resumes/
    ├── job_descriptions/
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/hr-shortlisting-agent.git
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# Running the Project

```bash
python app.py
```

---

# Future Improvements

Planned enhancements include:

- React Dashboard
- Async Resume Processing
- Redis + Celery Workers
- ATS Integration
- Candidate Comparison Charts
- HR Feedback Learning
- Cloud Deployment
- Interview Recommendation System

---

# Final Outcome

The project evolved from a simple resume parser into a scalable AI-assisted hiring platform featuring:

- Retrieval-Augmented Generation (RAG)
- Semantic Candidate Retrieval
- Hybrid AI Scoring
- Explainable Ranking
- PDF/HTML Reporting
- Enterprise-style Architecture

---

## SS
<img width="1799" height="1350" alt="Screenshot 2026-05-13 113041" src="https://github.com/user-attachments/assets/9956c6ce-041b-405d-af7a-fd546329ea51" />


# Author

## Lokesh Mudgal

B.Tech - Artificial Intelligence & Machine Learning

---

# License

This project is licensed under the MIT License.
