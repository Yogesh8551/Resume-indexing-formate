from sqlalchemy.orm import Session
from .models import Resume

def create_resume(db: Session, **data):
    obj = Resume(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def query_resumes(db: Session, name=None, resumetype=None, occupation=None):
    q = db.query(Resume)
    if name:
        q = q.filter(Resume.name.ilike(f"%{name}%"))
    if resumetype:
        q = q.filter(Resume.resumetype.ilike(f"%{resumetype}%"))
    if occupation:
        q = q.filter(Resume.occupation.ilike(f"%{occupation}%"))
    return q.all()
