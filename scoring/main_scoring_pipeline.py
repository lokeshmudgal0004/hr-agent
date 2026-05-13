from scoring.hybrid_scorer import (
    hybrid_skill_score,
    hybrid_project_score
)

from scoring.experience_scorer import (
    score_experience
)

from scoring.education_scorer import (
    score_education
)

from scoring.communication_scorer import (
    score_communication
)

from scoring.weighted_engine import (
    calculate_total
)

from scoring.recommendation_engine import (
    generate_recommendation
)


def evaluate_candidate(
    jd,
    candidate,
    raw_resume_text
):

    scores = {}

    scores["skills_match"] = hybrid_skill_score(
        jd.get("required_skills"),
        candidate.get("skills")
    )

    scores["experience_relevance"] = (
        score_experience(
            jd.get("responsibilities"),
            candidate.get("experiences")
        )
    )

    scores["education_certs"] = (
        score_education(
            jd.get("education_requirements"),
            candidate.get("education"),
            jd.get("certifications"),
            candidate.get("certifications")
        )
    )

    scores["project_portfolio"] = (
        hybrid_project_score(
            jd.get("required_skills"),
            candidate.get("projects")
        )
    )

    scores["communication_quality"] = (
        score_communication(
            raw_resume_text
        )
    )

    total = calculate_total(scores)

    recommendation = (
        generate_recommendation(total)
    )

    return {
        "candidate_name": candidate.get("name"),
        "scores": scores,
        "weighted_total": total,
        "recommendation": recommendation
    }