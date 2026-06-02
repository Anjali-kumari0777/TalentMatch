from app.services.qdrant_service import client

info = client.get_collection(
    collection_name="freelancers"
)

print(info)