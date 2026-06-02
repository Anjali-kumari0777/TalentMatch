from pydantic import BaseModel


class FreelancerCreate(BaseModel):
    name: str
    bio: str
    experience_years: int
    hourly_rate: float
    skills: list[str]