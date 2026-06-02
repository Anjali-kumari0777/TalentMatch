from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.freelancer import Freelancer
from app.models.skills import Skill

from app.schemas.freelancer import FreelancerCreate

router = APIRouter(
    prefix="/freelancers",
    tags=["Freelancers"]
)

@router.post("/test")
def test():
    return {"message": "working"}
    
@router.post("/")
def create_freelancer(
    freelancer: FreelancerCreate,
    db: Session = Depends(get_db)
):

    db_freelancer = Freelancer(
        name=freelancer.name,
        bio=freelancer.bio,
        experience_years=freelancer.experience_years,
        hourly_rate=freelancer.hourly_rate
    )

    db.add(db_freelancer)

    db.commit()

    db.refresh(db_freelancer)

    for skill in freelancer.skills:

        db_skill = Skill(
            freelancer_id=db_freelancer.id,
            skill_name=skill
        )

        db.add(db_skill)

    db.commit()

    return {
        "message": "Freelancer created",
        "freelancer_id": db_freelancer.id
    }