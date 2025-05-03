from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.routes.clients import client_router
from app.routes.freelancers import freelancer_router
from app.routes.invoices import invoice_router
import os

app = FastAPI()

# Adjusted for correct relative path inside container
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(client_router, prefix="/api/clients")
app.include_router(freelancer_router, prefix="/api/freelancers")
app.include_router(invoice_router, prefix="/api/invoices")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("app/templates/index.html", "r") as f:
        return HTMLResponse(content=f.read())
