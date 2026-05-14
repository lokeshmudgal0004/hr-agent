from datetime import datetime


def build_report(
    job_role,
    ranked_candidates
):

    sorted_candidates = sorted(
        ranked_candidates,
        key=lambda candidate:
            candidate.get(
                "weighted_total",
                0
            ),
        reverse=True
    )

    total_candidates = len(
        sorted_candidates
    )

    average_score = 0

    if total_candidates > 0:

        average_score = round(
            sum(
                candidate.get(
                    "weighted_total",
                    0
                )
                for candidate in sorted_candidates
            ) / total_candidates,
            2
        )

    top_candidate = {}

    if total_candidates > 0:

        top_candidate = {
            "candidate_name":
                sorted_candidates[0].get(
                    "candidate_name",
                    ""
                ),

            "weighted_total":
                sorted_candidates[0].get(
                    "weighted_total",
                    0
                ),

            "recommendation":
                sorted_candidates[0].get(
                    "recommendation",
                    ""
                )
        }

    for index, candidate in enumerate(
        sorted_candidates,
        start=1
    ):

        candidate["rank"] = index

    report = {

        "role": job_role,

        "generated_at":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

        "total_candidates":
            total_candidates,

        "average_score":
            average_score,

        "top_candidate":
            top_candidate,

        "candidates":
            sorted_candidates
    }

    return report