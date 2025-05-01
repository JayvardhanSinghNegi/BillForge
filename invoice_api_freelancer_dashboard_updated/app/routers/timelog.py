from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import models
from app.schemas import TimeLogCreate
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/timelogs")
def create_timelog(timelog: TimeLogCreate, db: Session = Depends(get_db)):
    timelog = models.TimeLog(**timelog.dict())
    db.add(timelog)
    db.commit()
    db.refresh(timelog)
    return timelog

@router.get("/timelogs")
def read_timelogs(db: Session = Depends(get_db)):
    return db.query(models.TimeLog).all()
