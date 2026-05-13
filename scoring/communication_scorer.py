from scoring.llm_evaluator import (
    evaluate_dimension
)


def score_communication(resume_text):

    result = evaluate_dimension(
        "Communication Quality",
        "Professional resume clarity",
        resume_text
    )

    return result