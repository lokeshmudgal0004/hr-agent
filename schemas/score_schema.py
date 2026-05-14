from pydantic import BaseModel, Field
from typing import Literal


class RubricDimension(BaseModel):

    score: float = Field(
        ge=0,
        le=10
    )

    justification: str


class CandidateScore(BaseModel):

    candidate_name: str

    skills_match: RubricDimension

    experience_relevance: RubricDimension

    education_certs: RubricDimension

    project_portfolio: RubricDimension

    communication_quality: RubricDimension

    weighted_total: float = Field(
        ge=0,
        le=10
    )

    recommendation: str