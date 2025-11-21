from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    resumetype = Column(String)
    occupation = Column(String)
    filename = Column(String)
    chroma_id = Column(String)
    snippet = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
