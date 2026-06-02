from app.services.embedding_service import generate_embedding

text = """
Python FastAPI PostgreSQL Docker
Backend Developer
"""

vector = generate_embedding(text)

print("Vector Length:", len(vector))
print("First 5 Values:", vector[:5])