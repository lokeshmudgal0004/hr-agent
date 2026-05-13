from rag.embeddings import generate_embedding
from scoring.semantic_matcher import (
    compute_similarity,
    similarity_to_score
)

from scoring.llm_evaluator import (
    evaluate_dimension
)


def hybrid_skill_score(
    jd_skills,
    candidate_skills
):

    jd_text = " ".join(jd_skills)
    candidate_text = " ".join(candidate_skills)

    jd_embedding = generate_embedding(jd_text)
    candidate_embedding = generate_embedding(candidate_text)

    similarity = compute_similarity(
        jd_embedding,
        candidate_embedding
    )

    semantic_score = similarity_to_score(similarity)

    llm_result = evaluate_dimension(
        "Skills Match",
        jd_text,
        candidate_text
    )

    llm_score = llm_result["score"]

    final_score = (
        0.8 * semantic_score
        +
        0.2 * llm_score
    )

    return {
        "score": round(final_score, 2),
        "semantic_similarity": similarity,
        "justification": llm_result["justification"]
    }


def hybrid_project_score(
    jd_requirements,
    candidate_projects
):

    jd_text = " ".join(jd_requirements)

    project_text = ""

    for project in candidate_projects:

        project_text += (
            project.get("title")
            + " "
            + project.get("description")
            + " "
            + " ".join(project.get("technologies"))
            + "\n"
        )

    jd_embedding = generate_embedding(jd_text)

    project_embedding = generate_embedding(
        project_text
    )

    similarity = compute_similarity(
        jd_embedding,
        project_embedding
    )

    semantic_score = similarity_to_score(
        similarity
    )

    llm_result = evaluate_dimension(
        "Project Portfolio",
        jd_text,
        project_text
    )

    llm_score = llm_result["score"]

    final_score = (
        0.5 * semantic_score
        +
        0.5 * llm_score
    )

    return {
        "score": round(final_score, 2),
        "semantic_similarity": similarity,
        "justification": llm_result["justification"]
    }