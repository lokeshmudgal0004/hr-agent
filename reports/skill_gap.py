def find_missing_skills(
    jd_skills,
    candidate_skills
):

    candidate_set = set(
        skill.lower()
        for skill in candidate_skills
    )

    missing = []

    for skill in jd_skills:

        if skill.lower() not in candidate_set:

            missing.append(skill)

    return missing