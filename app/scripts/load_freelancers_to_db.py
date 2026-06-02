from faker import Faker
from random import randint, sample, uniform

from app.database import SessionLocal
from app.models.freelancer import Freelancer
from app.models.skills import Skill

fake = Faker()

db = SessionLocal()

BACKEND_SKILLS = [
    "Python",
    "FastAPI",
    "Django",
    "PostgreSQL",
    "Docker",
    "Redis"
]

FRONTEND_SKILLS = [
    "React",
    "Next.js",
    "JavaScript",
    "TypeScript"
]

FULLSTACK_SKILLS = [
    "React",
    "Next.js",
    "Python",
    "FastAPI",
    "PostgreSQL",
    "Docker"
]

MOBILE_SKILLS = [
    "Flutter",
    "React Native",
    "Firebase"
]

AI_SKILLS = [
    "Python",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
    "Data Science"
]


def create_freelancer(role, skills_pool):

    selected_skills = sample(
        skills_pool,
        min(len(skills_pool), randint(3, 5))
    )

    freelancer = Freelancer(
        name=fake.name(),
        bio=role,
        experience_years=randint(1, 10),
        hourly_rate=round(
            uniform(10, 80),
            2
        )
    )

    db.add(freelancer)
    db.commit()
    db.refresh(freelancer)

    for skill in selected_skills:

        db_skill = Skill(
            freelancer_id=freelancer.id,
            skill_name=skill
        )

        db.add(db_skill)

    db.commit()


for _ in range(250):
    create_freelancer(
        "Backend Developer",
        BACKEND_SKILLS
    )

for _ in range(250):
    create_freelancer(
        "Frontend Developer",
        FRONTEND_SKILLS
    )

for _ in range(200):
    create_freelancer(
        "Full Stack Developer",
        FULLSTACK_SKILLS
    )

for _ in range(150):
    create_freelancer(
        "Mobile Developer",
        MOBILE_SKILLS
    )

for _ in range(150):
    create_freelancer(
        "AI Engineer",
        AI_SKILLS
    )

print("1000 freelancers inserted successfully")