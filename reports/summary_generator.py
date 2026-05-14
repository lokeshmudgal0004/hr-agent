from llm_client import llm_client

from utils.json_cleaner import (
    clean_llm_json
)


def generate_summary(
    jd,
    candidate
):

    prompt = f"""
You are an expert hiring analyst and recruiter.

Analyze the candidate against the job requirements.

JOB DESCRIPTION:
{jd}

CANDIDATE:
{candidate}

Instructions:
- Identify the candidate's strongest qualities.
- Identify important weaknesses or gaps.
- Consider technical skills, projects, experience, communication, and domain relevance.
- Mention missing skills if relevant.
- Keep points concise and recruiter-friendly.
- Avoid generic statements.
- Be objective and realistic.

Return ONLY valid JSON.

Required JSON format:

{{
    "strengths": [
        "strength 1",
        "strength 2"
    ],

    "weaknesses": [
        "weakness 1",
        "weakness 2"
    ]
}}
"""

    response = llm_client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        temperature=0.1,
        max_tokens=400,
        messages=[
            {
                "role": "system",
                "content":
                    (
                        "You are a professional hiring analyst "
                        "specialized in candidate evaluation."
                    )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content.strip()

    parsed_json = clean_llm_json(
        content
    )

    return parsed_json