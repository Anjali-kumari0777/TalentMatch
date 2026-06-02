from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Freelancer(Base):
    __tablename__ = "freelancers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    bio = Column(String, nullable=False)

    experience_years = Column(Integer, nullable=False)

    hourly_rate = Column(Float, nullable=False)

    skills = relationship(
        "Skill",
        back_populates="freelancer",
        cascade="all, delete-orphan"
    )