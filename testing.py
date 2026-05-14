import os
import json

from parsers.text_extractors import (
    extract_text_from_pdf,
    extract_text_from_docx
)

from utils.json_cleaner import (
    clean_llm_json
)

from parsers.resume_parser import parse_resume

JD_FOLDER = "jd"

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

RESUME_FOLDER = "resumes"


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

      print(parsed_candidate)

    print(
        "\nAll resumes parsed successfully."
    )


if __name__ == "__main__":
    main()

    
    
    