from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)

    freelancer_id = Column(
        Integer,
        ForeignKey("freelancers.id")
    )

    skill_name = Column(
        String,
        nullable=False
    )

    freelancer = relationship(
        "Freelancer",
        back_populates="skills"
    )