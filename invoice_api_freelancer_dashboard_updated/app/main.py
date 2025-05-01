from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import models
from fastapi.responses import FileResponse
from weasyprint import HTML
from jinja2 import Template
from datetime import datetime

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/invoices/{project_id}")
def get_invoice(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    client = db.query(models.Client).filter(models.Client.id == project.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    timelogs = db.query(models.TimeLog).filter(models.TimeLog.project_id == project_id).all()
    total = sum([log.hours * project.hourly_rate for log in timelogs])

    with open("app/templates/invoice_template.html") as f:
        template = Template(f.read())

    html = template.render(
        client=client,
        project=project,
        timelogs=timelogs,
        total=total,
        date=datetime.now().strftime("%Y-%m-%d")
    )

    output_path = f"app/invoices/invoice_{project_id}.pdf"
    HTML(string=html).write_pdf(output_path)

    return FileResponse(output_path, media_type="application/pdf", filename=f"invoice_{project_id}.pdf")
