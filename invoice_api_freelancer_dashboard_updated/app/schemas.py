
from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    email: str
    company: str

class ProjectCreate(BaseModel):
    title: str
    hourly_rate: float
    client_id: int

class TimeLogCreate(BaseModel):
    project_id: int
    hours: float
