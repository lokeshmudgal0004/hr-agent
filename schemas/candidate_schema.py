from pydantic import BaseModel
from typing import List, Optional


class Experience(BaseModel):

    company: str = ""

    role: str = ""

    duration: str = ""

    description: str = ""


class Education(BaseModel):

    institution: str = ""

    degree: str = ""

    field: str = ""

    year: Optional[str] = ""


class Project(BaseModel):

    title: str = ""

    description: str = ""

    technologies: List[str] = []


class CandidateProfile(BaseModel):

    name: str = "Unknown Candidate"

    email: str = ""

    phone: str = ""

    linkedin_url: str = ""

    skills: List[str] = []

    soft_skills: List[str] = []

    experiences: List[Experience] = []

    education: List[Education] = []

    projects: List[Project] = []

    certifications: List[str] = []

    achievements: List[str] = []

    total_experience: str = ""

    current_role: str = ""

    domain: str = ""