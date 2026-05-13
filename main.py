import os
import json

from parsers.text_extractors import (
    extract_text_from_pdf,
    extract_text_from_docx
)

from utils.json_cleaner import (
    clean_llm_json
)

from parsers.jd_parser import parse_jd
from parsers.resume_parser import parse_resume

from rag.vector_store import create_vector_store

from scoring.main_scoring_pipeline import (
    evaluate_candidate
)

from scoring.ranking_engine import (
    rank_candidates
)

from reports.main_report_pipeline import (
    generate_full_report
)


JD_FOLDER = "jd"
RESUME_FOLDER = "resumes"


def load_file_text(file_path):

    if file_path.endswith(".pdf"):

        return extract_text_from_pdf(
            file_path
        )

    elif file_path.endswith(".docx"):

        return extract_text_from_docx(
            file_path
        )

    elif file_path.endswith(".md"):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    else:

        raise ValueError(
            f"Unsupported file format: {file_path}"
        )


def create_candidate_chunks(candidate):

    chunks = []

    name = candidate.get(
        "name",
        "Unknown"
    )

    # Skills chunk
    skills = candidate.get("skills", [])

    if skills:

        chunks.append(
            f"""
            Candidate: {name}
            Section: Skills

            {' '.join(skills)}
            """
        )

    # Experience chunk
    experiences = candidate.get(
        "experiences",
        []
    )

    exp_text = ""

    for exp in experiences:

        exp_text += (
            f"""
            Role: {exp.get('role', '')}

            Company: {exp.get('company', '')}

            Description:
            {exp.get('description', '')}
            """
        )

    if exp_text.strip():

        chunks.append(
            f"""
            Candidate: {name}
            Section: Experience

            {exp_text}
            """
        )

    # Projects chunk
    projects = candidate.get(
        "projects",
        []
    )

    project_text = ""

    for project in projects:

        project_text += (
            f"""
            Project:
            {project.get('title', '')}

            Description:
            {project.get('description', '')}

            Technologies:
            {' '.join(project.get('technologies', []))}
            """
        )

    if project_text.strip():

        chunks.append(
            f"""
            Candidate: {name}
            Section: Projects

            {project_text}
            """
        )

    return chunks


def main():

    print("\n========== HR SHORTLISTING AGENT ==========\n")

    # --------------------------------------------------
    # STEP 1 — LOAD JD
    # --------------------------------------------------

    jd_files = os.listdir(JD_FOLDER)

    if len(jd_files) == 0:

        raise Exception(
            "No JD file found."
        )

    jd_file = jd_files[0]

    jd_path = os.path.join(
        JD_FOLDER,
        jd_file
    )

    print(f"\nLoading JD: {jd_file}")

    jd_text = load_file_text(
        jd_path
    )

    print("\nParsing JD...")

    parsed_jd = parse_jd(jd_text)

    if isinstance(parsed_jd, str):

        parsed_jd = clean_llm_json(
            parsed_jd
        )
        print("\nJD Parsed Successfully.")

    # --------------------------------------------------
    # STEP 2 — LOAD RESUMES
    # --------------------------------------------------

    resume_files = os.listdir(
        RESUME_FOLDER
    )

    if len(resume_files) == 0:

        raise Exception(
            "No resumes found."
        )

    all_candidates = []

    all_chunks = []

    print(
        f"\nFound {len(resume_files)} resumes."
    )

    # --------------------------------------------------
    # STEP 3 — PARSE RESUMES
    # --------------------------------------------------

    for file in resume_files:

        print(f"\nProcessing Resume: {file}")

        file_path = os.path.join(
            RESUME_FOLDER,
            file
        )

        resume_text = load_file_text(
            file_path
        )

        parsed_candidate = parse_resume(
            resume_text
        )

        if isinstance(parsed_candidate, str):

            parsed_candidate = clean_llm_json(
                parsed_candidate
            )

        parsed_candidate[
            "raw_resume_text"
        ] = resume_text

        all_candidates.append(
            parsed_candidate
        )

        # Create semantic chunks
        candidate_chunks = (
            create_candidate_chunks(
                parsed_candidate
            )
        )

        all_chunks.extend(
            candidate_chunks
        )

    print(
        "\nAll resumes parsed successfully."
    )

    # --------------------------------------------------
    # STEP 4 — CREATE VECTOR STORE
    # --------------------------------------------------

    print(
        "\nCreating FAISS Vector Store..."
    )

    vector_db = create_vector_store(
        all_chunks
    )

    print(
        "\nFAISS Vector Store Created."
    )

    # --------------------------------------------------
    # STEP 5 — RETRIEVE TOP MATCHES
    # --------------------------------------------------

    print(
        "\nRunning Semantic Retrieval..."
    )

    jd_query = " ".join(
        parsed_jd.get(
            "required_skills",
            []
        )
    )

    retrieved_docs = (
        vector_db.similarity_search(
            jd_query,
            k=10
        )
    )

    relevant_candidate_names = set()

    for doc in retrieved_docs:

        content = doc.page_content

        if "Candidate:" in content:

            lines = content.split("\n")

            for line in lines:

                if "Candidate:" in line:

                    candidate_name = (
                        line.replace(
                            "Candidate:",
                            ""
                        ).strip()
                    )

                    relevant_candidate_names.add(
                        candidate_name
                    )

    print(
        "\nTop Relevant Candidates Retrieved:"
    )

    for name in relevant_candidate_names:

        print(f"- {name}")

    # --------------------------------------------------
    # STEP 6 — RUN HYBRID SCORING
    # --------------------------------------------------

    print(
        "\nRunning Hybrid Rubric Scoring..."
    )

    scored_candidates = []

    for candidate in all_candidates:

        if (
            candidate.get("name")
            not in relevant_candidate_names
        ):

            continue

        result = evaluate_candidate(
            parsed_jd,
            candidate,
            candidate.get(
                "raw_resume_text"
            )
        )

        # IMPORTANT
        # Needed for report generation

        result["candidate_skills"] = (
            candidate.get(
                "skills",
                []
            )
        )

        scored_candidates.append(
            result
        )

        print(
            f"\nScored: {candidate.get('name')}"
        )

    # --------------------------------------------------
    # STEP 7 — RANK CANDIDATES
    # --------------------------------------------------

    print(
        "\nRanking Candidates..."
    )

    ranked_candidates = rank_candidates(
        scored_candidates
    )

    # --------------------------------------------------
    # STEP 8 — SAVE RANKINGS
    # --------------------------------------------------

    os.makedirs(
        "output",
        exist_ok=True
    )

    with open(
        "output/ranked_candidates.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            ranked_candidates,
            file,
            indent=4
        )

    print(
        "\nRankings saved."
    )

    # --------------------------------------------------
    # STEP 9 — GENERATE REPORTS
    # --------------------------------------------------

    print(
        "\nGenerating Reports..."
    )

    generate_full_report(
        parsed_jd,
        ranked_candidates
    )

    print(
        "\nReports Generated Successfully."
    )

    # --------------------------------------------------
    # FINAL OUTPUT
    # --------------------------------------------------

    print("\n========== FINAL RANKINGS ==========\n")

    for idx, candidate in enumerate(
        ranked_candidates,
        start=1
    ):

        print(
            f"""
            Rank #{idx}

            Candidate:
            {candidate['candidate_name']}

            Score:
            {candidate['weighted_total']}

            Recommendation:
            {candidate['recommendation']}
            """
        )

    print(
        "\n========== PIPELINE COMPLETED ==========\n"
    )


if __name__ == "__main__":

    main()