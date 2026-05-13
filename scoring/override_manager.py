def apply_override(
    candidate_result,
    overrides
):

    if not overrides["enabled"]:
        return candidate_result

    for dimension, updated_score in (
        overrides["updated_scores"].items()
    ):

        candidate_result["scores"][dimension][
            "score"
        ] = updated_score

    return candidate_result