import json

from llm_client import llm_client

from utils.json_cleaner import (
    clean_llm_json
)

from schemas.score_schema import (
    RubricDimension
)


def evaluate_dimension(
    dimension,
    jd_context,
    candidate_context
):

    prompt = f"""
You are an expert HR evaluator and hiring assessment system.

Your task is to evaluate ONLY ONE hiring dimension.

Dimension to Evaluate:
{dimension}

Job Requirement:
{jd_context}

Candidate Information:
{candidate_context}

Evaluation Instructions:
- Be strict and objective.
- Compare relevance, depth, and alignment.
- Give realistic scores.
- Do not inflate scores.
- Consider missing requirements negatively.

Scoring Guidelines:
- 0-2  -> Very poor alignment
- 3-4  -> Weak alignment
- 5-6  -> Moderate alignment
- 7-8  -> Strong alignment
- 9-10 -> Exceptional alignment

Return ONLY valid JSON.

Required JSON format:

{{
    "score": 0,
    "justification": "short concise explanation"
}}
"""

    response = llm_client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a strict and accurate hiring evaluator "
                    "that scores candidates objectively."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1,
        max_tokens=300
    )

    content = response.choices[0].message.content

    parsed_json = clean_llm_json(
        content
    )

    validated = RubricDimension(
        **parsed_json
    )

    return validated.model_dump()