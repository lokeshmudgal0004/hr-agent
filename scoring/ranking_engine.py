def rank_candidates(candidate_results):

    ranked = sorted(
        candidate_results,
        key=lambda x: x["weighted_total"],
        reverse=True
    )

    return ranked