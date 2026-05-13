from schemas.jd_schema import (
    JDRequirements
)

from utils.json_cleaner import (
    clean_llm_json
)

from llm_client import client

def parse_jd(jd_text):

    prompt = f"""
    You are an expert HR recruiter.

    Extract structured information from the following job description.

    Return ONLY valid JSON.
    Example:
    {{
        "score": 8,
        "reason": "Strong alignment"
    }}

    Job Description:
    {jd_text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You extract structured hiring requirements."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type":"json_object"}
    )

    content = response.choices[0].message.content

    parsed_json = clean_llm_json(
        content
    )

    validated = JDRequirements(
        **parsed_json
    )

    return validated.dict()