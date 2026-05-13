from rag.embeddings import generate_embedding
from scoring.semantic_matcher import (
    compute_similarity,
    similarity_to_score
)

from scoring.llm_evaluator import (
    evaluate_dimension
)


def score_experience(
    jd_responsibilities,
    candidate_experiences
):

    jd_text = " ".join(jd_responsibilities)

    experience_text = ""

    for exp in candidate_experiences:

        experience_text += (
            exp.get("role")
            + " "
            + exp.get("description")
            + "\n"
        )

    jd_embedding = generate_embedding(jd_text)

    experience_embedding = generate_embedding(
        experience_text
    )

    similarity = compute_similarity(
        jd_embedding,
        experience_embedding
    )

    semantic_score = similarity_to_score(
        similarity
    )

    llm_result = evaluate_dimension(
        "Experience Relevance",
        jd_text,
        experience_text
    )

    llm_score = llm_result["score"]

    final_score = (
        0.7 * semantic_score
        +
        0.3 * llm_score
    )

    return {
        "score": round(final_score, 2),
        "semantic_similarity": similarity,
        "justification": llm_result["justification"]
    }