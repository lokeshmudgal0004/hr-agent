import json
from llm_client import client


def generate_summary(
    jd,
    candidate
):

    prompt = f"""
    Analyze the candidate.

    Return STRICT JSON:

    {{
        "strengths": [],
        "weaknesses": []
    }}

    JOB:
    {jd}

    CANDIDATE:
    {candidate}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content":
                    "You are a hiring analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={
            "type": "json_object"
        }
    )

    return json.loads(
        response.choices[0].message.content
    )