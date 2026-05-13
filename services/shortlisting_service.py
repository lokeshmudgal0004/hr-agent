import os

from parsers.text_extractors import (
    extract_text_from_pdf,
    extract_text_from_docx
)

from parsers.jd_parser import parse_jd
from parsers.resume_parser import parse_resume

from scoring.main_scoring_pipeline import (
    evaluate_candidate
)

from scoring.ranking_engine import (
    rank_candidates
)


JD_FOLDER = "uploads/jd"
RESUME_FOLDER = "uploads/resumes"



def run_pipeline():

    jd_file = os.listdir(JD_FOLDER)[0]

    jd_path = os.path.join(
        JD_FOLDER,
        jd_file
    )

    if jd_file.endswith(".pdf"):

        jd_text = extract_text_from_pdf(
            jd_path
        )

    else:

        jd_text = extract_text_from_docx(
            jd_path
        )

    parsed_jd = parse_jd(jd_text)

    all_candidates = []

    for file in os.listdir(RESUME_FOLDER):

        path = os.path.join(
            RESUME_FOLDER,
            file
        )

        if file.endswith(".pdf"):

            resume_text = extract_text_from_pdf(
                path
            )

        else:

            resume_text = extract_text_from_docx(
                path
            )

        parsed_candidate = parse_resume(
            resume_text
        )

        result = evaluate_candidate(
            parsed_jd,
            parsed_candidate,
            resume_text
        )

        all_candidates.append(result)

    ranked = rank_candidates(
        all_candidates
    )   
    return ranked