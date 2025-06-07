from fastapi import APIRouter
from pydantic import BaseModel

freelancer_router = APIRouter()

class Freelancer(BaseModel):
    name: str
    email: str

freelancers = []

@freelancer_router.post("/")
def add_freelancer(freelancer: Freelancer):
    freelancers.append(freelancer)
    return {"message": "Freelancer added successfully", "freelancer": freelancer}
