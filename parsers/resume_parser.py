from schemas.candidate_schema import (
    CandidateProfile
)

from utils.json_cleaner import (
    clean_llm_json
)

from llm_client import llm_client


def parse_resume(resume_text):

    prompt = f"""
You are an expert resume parser and HR information extraction system.

Your task is to extract structured candidate information from the given resume.

Return ONLY valid JSON.

The JSON MUST strictly follow this structure:

{{
    "name": "string",

    "email": "string",

    "phone": "string",

    "linkedin_url": "string",

    "skills": ["skill1", "skill2"],

    "soft_skills": ["skill1", "skill2"],

    "experiences": [
        {{
            "company": "string",

            "role": "string",

            "duration": "string",

            "description": "string"
        }}
    ],

    "education": [
        {{
            "institution": "string",

            "degree": "string",

            "field": "string",

            "year": "string"
        }}
    ],

    "projects": [
        {{
            "title": "string",

            "description": "string",

            "technologies": ["tech1", "tech2"]
        }}
    ],

    "certifications": ["cert1", "cert2"],

    "achievements": ["achievement1", "achievement2"],

    "total_experience": "string",

    "current_role": "string",

    "domain": "string"
}}

Rules:
- Return ONLY JSON.
- Do not include markdown.
- Do not include explanations.
- Use empty strings or empty arrays if information is missing.
- Avoid duplicate entries.
- Extract concise and clean values.
- Skills and technologies should be short phrases only.
- Keep descriptions concise but informative.

Resume:
{resume_text}
"""

    response = llm_client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a highly accurate resume parsing assistant "
                    "that converts resumes into structured JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1,
        max_tokens=1500
    )

    content = response.choices[0].message.content

    parsed_json = clean_llm_json(
        content
    )

    validated = CandidateProfile(
        **parsed_json
    )

    return validated.model_dump()