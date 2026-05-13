from llm_client import client
from schemas.candidate_schema import (
    CandidateProfile
)

def parse_resume(resume_text):

    prompt = f"""
    You are an expert resume parser.

    Extract structured information from the following resume.

    Return ONLY valid JSON.
    Return ONLY valid JSON.
    Example:
    {{
        "score": 8,
        "reason": "Strong alignment"
    }}

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Extract structured candidate information."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content