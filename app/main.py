from fastapi import FastAPI
from app.api.search import router as search_router
from app.database import Base, engine
from app.models.freelancer import Freelancer
from app.models.skills import Skill

from app.api.freelancer import router as freelancer_router

app = FastAPI(title="TalentMatch")

Base.metadata.create_all(bind=engine)

app.include_router(freelancer_router)
app.include_router(search_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to TalentMatch API"}
