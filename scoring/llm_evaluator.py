import json

from llm_client import client


def evaluate_dimension(
    dimension,
    jd_context,
    candidate_context
):

    prompt = f"""
    You are an expert HR evaluator.

    Evaluate ONLY the following dimension:

    {dimension}

    JOB REQUIREMENT:
    {jd_context}

    CANDIDATE INFORMATION:
    {candidate_context}

    Return STRICT JSON:

    {{
        "score": number between 0 and 10,
        "justification": "short explanation"
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a strict hiring evaluator."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    return json.loads(
        response.choices[0].message.content
    )