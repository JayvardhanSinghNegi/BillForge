from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import models
from app.schemas import ClientCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clients")
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    client = models.Client(**client.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@router.get("/clients")
def read_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()
