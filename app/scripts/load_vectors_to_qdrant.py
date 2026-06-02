from qdrant_client.models import PointStruct
from app.models.skills import Skill
from app.database import SessionLocal
from app.models.freelancer import Freelancer

from app.services.embedding_service import generate_embedding
from app.services.profile_service import build_profile_text
from app.services.qdrant_service import client


db = SessionLocal()

freelancers = db.query(Freelancer).all()

points = []

for freelancer in freelancers:

    skills = [
        skill.skill_name
        for skill in freelancer.skills
    ]

    profile_text = build_profile_text(
        freelancer,
        skills
    )

    embedding = generate_embedding(
        profile_text
    )

    points.append(
        PointStruct(
            id=freelancer.id,
            vector=embedding,
            payload={
                "freelancer_id": freelancer.id,
                "name": freelancer.name,
                "bio": freelancer.bio,
                "experience_years": freelancer.experience_years,
                "hourly_rate": freelancer.hourly_rate,
                "skills": skills
            }
        )
    )

    if len(points) >= 100:

        client.upsert(
            collection_name="freelancers",
            points=points
        )

        print(
            f"Uploaded {len(points)} vectors"
        )

        points = []

# upload remaining points

if points:

    client.upsert(
        collection_name="freelancers",
        points=points
    )

print(
    f"Finished uploading {len(freelancers)} freelancers"
)