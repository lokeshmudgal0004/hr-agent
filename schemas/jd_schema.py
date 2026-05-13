from pydantic import BaseModel
from typing import List


class JDRequirements(BaseModel):

    role: str = ""

    required_skills: List[str] = []

    preferred_skills: List[str] = []

    minimum_experience: str = ""

    education_requirements: List[str] = []

    certifications: List[str] = []

    responsibilities: List[str] = []

    tools_and_technologies: List[str] = []

    soft_skills: List[str] = []

    domain: str = ""

    seniority_level: str = ""