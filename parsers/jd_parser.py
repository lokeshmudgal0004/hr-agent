from schemas.jd_schema import (
    JDRequirements
)

from utils.json_cleaner import (
    clean_llm_json
)

from llm_client import llm_client


def parse_jd(jd_text):

    prompt = f"""
You are an expert HR recruiter and information extraction system.

Your task is to extract structured hiring requirements from the given Job Description.

Return ONLY valid JSON.

The JSON MUST strictly follow this structure:

{{
    "role": "string",

    "required_skills": ["skill1", "skill2"],

    "preferred_skills": ["skill1", "skill2"],

    "minimum_experience": "string",

    "education_requirements": ["education1", "education2"],

    "certifications": ["cert1", "cert2"],

    "responsibilities": ["responsibility1", "responsibility2"],

    "tools_and_technologies": ["tool1", "tool2"],

    "soft_skills": ["skill1", "skill2"],

    "domain": "string",

    "seniority_level": "string"
}}

Rules:
- Return ONLY JSON.
- Do not include markdown.
- Do not include explanations.
- Use empty strings or empty arrays if information is missing.
- Extract concise and clean values.
- Avoid duplicate entries.
- Skills should be short phrases only.

Job Description:
{jd_text}
"""

    response = llm_client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a highly accurate HR information extraction assistant "
                    "that converts job descriptions into structured JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1,
        max_tokens=1200
    )

    content = response.choices[0].message.content

    parsed_json = clean_llm_json(
        content
    )

    validated = JDRequirements(
        **parsed_json
    )

    return validated.model_dump()