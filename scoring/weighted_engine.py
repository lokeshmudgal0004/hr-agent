WEIGHTS = {
    "skills_match": 0.30,
    "experience_relevance": 0.25,
    "education_certs": 0.15,
    "project_portfolio": 0.20,
    "communication_quality": 0.10
}


def calculate_total(scores):

    total = 0

    for dimension, weight in WEIGHTS.items():

        total += (
            scores[dimension]["score"]
            * weight
        )

    return round(total, 2)