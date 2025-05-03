from fastapi import APIRouter
from pydantic import BaseModel

client_router = APIRouter()

class Client(BaseModel):
    name: str
    email: str

clients = []

@client_router.post("/")
def add_client(client: Client):
    clients.append(client)
    return {"message": "Client added successfully", "client": client}