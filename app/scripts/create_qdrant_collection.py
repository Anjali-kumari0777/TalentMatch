from qdrant_client.models import Distance
from qdrant_client.models import VectorParams

from app.qdrant_service import client

client.recreate_collection(
    collection_name="freelancers",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

print("Collection created")