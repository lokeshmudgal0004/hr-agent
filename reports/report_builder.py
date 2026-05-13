from datetime import datetime


def build_report(
    job_role,
    ranked_candidates
):

    report = {
        "role": job_role,

        "generated_at":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

        "candidates": ranked_candidates
    }

    return report