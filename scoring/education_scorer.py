def score_education(
    jd_education,
    candidate_education,
    jd_certs,
    candidate_certs
):

    score = 0

    candidate_text = " ".join([
        edu["degree"]
        for edu in candidate_education
    ]).lower()

    required_text = " ".join(
        jd_education
    ).lower()

    if required_text in candidate_text:
        score += 6

    matched_certs = 0

    for cert in candidate_certs:

        if cert.lower() in str(jd_certs).lower():
            matched_certs += 1

    score += min(matched_certs, 4)

    return {
        "score": min(score, 10),
        "justification":
            "Education and certifications evaluated."
    }