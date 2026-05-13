# AI-Powered HR Resume & LinkedIn Shortlisting Agent

An AI-assisted hiring pipeline that semantically evaluates resumes and LinkedIn profiles against a Job Description (JD) using:

- Hybrid Semantic Search
- LLM-based reasoning
- FAISS vector retrieval
- Rubric-based scoring
- Explainable AI reports

The system parses resumes/JDs, computes semantic relevance, ranks candidates, and generates recruiter-friendly reports in JSON, HTML, and PDF formats.

---

# Features

- Resume Parsing (`.pdf`, `.docx`, `.md`)
- Job Description Parsing
- LinkedIn Profile Support (RapidAPI)
- Semantic Search using FAISS
- Hybrid AI Scoring
- Candidate Ranking
- Explainable AI Evaluation
- PDF / HTML / JSON Report Generation
- HR Override System
- Schema Validation & Input Sanitization
- Fault-Tolerant Pipeline

---

# System Architecture

```text
                    Job Description
                            │
                            ▼
                    JD Parsing Layer
                            │
                            ▼
                   Structured JD JSON
                            │
──────────────────────────────────────────────────
                            │
                            ▼
              Resume / LinkedIn Ingestion
                            │
                            ▼
                Resume Parsing Pipeline
                            │
                            ▼
              Structured Candidate JSON
                            │
                            ▼
                 Embedding Generation
                            │
                            ▼
                     FAISS Vector DB
                            │
                            ▼
                Semantic Candidate Retrieval
                            │
                            ▼
                  Hybrid Rubric Scoring
                            │
                            ▼
                    Candidate Ranking
                            │
                            ▼
                 Explainable AI Reports
                            │
                            ▼
                  PDF / HTML / JSON Output
```
