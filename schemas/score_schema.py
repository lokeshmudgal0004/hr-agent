from pydantic import BaseModel
from typing import Dict


class RubricDimension(BaseModel):
    score: float
    justification: str


class CandidateScore(BaseModel):
    candidate_name: str

    skills_match: RubricDimension
    experience_relevance: RubricDimension
    education_certs: RubricDimension
    project_portfolio: RubricDimension
    communication_quality: RubricDimension

    weighted_total: float

    recommendation: str