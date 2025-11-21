from pydantic import BaseModel
from datetime import datetime

class ResumeMeta(BaseModel):
    id: int
    name: str | None
    resumetype: str | None
    occupation: str | None
    filename: str
    chroma_id: str
    snippet: str | None
    created_at: datetime

    class Config:
        orm_mode = True
