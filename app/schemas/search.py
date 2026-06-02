from pydantic import BaseModel


class SearchRequest(BaseModel):
    project_description: str