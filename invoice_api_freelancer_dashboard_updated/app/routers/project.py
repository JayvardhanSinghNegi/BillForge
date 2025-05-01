from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import models
from app.schemas import ProjectCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/projects")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    project = models.Project(**project.dict())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@router.get("/projects")
def read_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()
