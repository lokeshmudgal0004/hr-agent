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

from reports.skill_gap import (
    find_missing_skills
)


def evaluate_candidate(
    jd,
    candidate,
    raw_resume_text
):

    scores = {}

    scores["skills_match"] = hybrid_skill_score(
        jd.get("required_skills", []),
        candidate.get("skills", [])
    )

    scores["experience_relevance"] = (
        score_experience(
            jd.get("responsibilities", []),
            candidate.get("experiences", [])
        )
    )

    scores["education_certs"] = (
        score_education(
            jd.get("education_requirements", []),
            candidate.get("education", []),
            jd.get("certifications", []),
            candidate.get("certifications", [])
        )
    )

    scores["project_portfolio"] = (
        hybrid_project_score(
            jd.get("required_skills", []),
            candidate.get("projects", [])
        )
    )

    scores["communication_quality"] = (
        score_communication(
            raw_resume_text
        )
    )

    total = calculate_total(
        scores
    )

    recommendation = (
        generate_recommendation(
            total
        )
    )

    missing_skills = (
        find_missing_skills(
            jd.get("required_skills", []),
            candidate.get("skills", [])
        )
    )

    fit_label = (
        "Excellent Fit"
        if total >= 8.5
        else "Strong Fit"
        if total >= 7
        else "Moderate Fit"
        if total >= 5
        else "Weak Fit"
    )

    return {
        "candidate_name": candidate.get(
            "name",
            "Unknown Candidate"
        ),

        "candidate_email": candidate.get(
            "email",
            ""
        ),

        "current_role": candidate.get(
            "current_role",
            ""
        ),

        "domain": candidate.get(
            "domain",
            ""
        ),

        "candidate_skills": candidate.get(
            "skills",
            []
        ),

        "top_skills": candidate.get(
            "skills",
            []
        )[:8],

        "projects": candidate.get(
            "projects",
            []
        ),

        "experiences": candidate.get(
            "experiences",
            []
        ),

        "education": candidate.get(
            "education",
            []
        ),

        "certifications": candidate.get(
            "certifications",
            []
        ),

        "missing_skills": missing_skills,

        "scores": scores,

        "weighted_total": round(
            total,
            2
        ),

        "recommendation": recommendation,

        "fit_label": fit_label
    }