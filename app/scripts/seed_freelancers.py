from faker import Faker
from random import randint, sample, uniform

fake = Faker()

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


def generate_profile(role, skills_pool):

    return {
        "name": fake.name(),
        "role": role,
        "skills": sample(
            skills_pool,
            min(len(skills_pool), randint(3, 5))
        ),
        "experience_years": randint(1, 10),
        "hourly_rate": round(
            uniform(10, 80),
            2
        )
    }


freelancers = []

# Backend Developers
for _ in range(250):
    freelancers.append(
        generate_profile(
            "Backend Developer",
            BACKEND_SKILLS
        )
    )

# Frontend Developers
for _ in range(250):
    freelancers.append(
        generate_profile(
            "Frontend Developer",
            FRONTEND_SKILLS
        )
    )

# Full Stack Developers
for _ in range(200):
    freelancers.append(
        generate_profile(
            "Full Stack Developer",
            FULLSTACK_SKILLS
        )
    )

# Mobile Developers
for _ in range(150):
    freelancers.append(
        generate_profile(
            "Mobile Developer",
            MOBILE_SKILLS
        )
    )

# AI Engineers
for _ in range(150):
    freelancers.append(
        generate_profile(
            "AI Engineer",
            AI_SKILLS
        )
    )

print(f"Total freelancers: {len(freelancers)}")

for freelancer in freelancers[:5]:
    print(freelancer)