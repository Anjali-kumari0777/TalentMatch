from fastapi import APIRouter

from app.schemas.search import SearchRequest

from app.services.embedding_service import generate_embedding
from app.services.qdrant_service import client

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post("/")
def search_freelancers(
    request: SearchRequest
):

    vector = generate_embedding(
        request.project_description
    )

    results = client.query_points(
        collection_name="freelancers",
        query=vector,
        limit=20
    )

    response = []

    for point in results.points:

        response.append(
            {
                "score": point.score,
                "name": point.payload["name"],
                "bio": point.payload["bio"],
                "experience_years": point.payload["experience_years"],
                "hourly_rate": point.payload["hourly_rate"],
                "skills": point.payload["skills"]
            }
        )

    return response