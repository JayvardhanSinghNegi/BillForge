from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel
from weasyprint import HTML
import tempfile

invoice_router = APIRouter()

class InvoiceData(BaseModel):
    client_name: str
    client_email: str
    freelancer_name: str
    freelancer_email: str
    project_description: str
    hours: float
    rate: float

@invoice_router.post("/download")
def download_invoice(data: InvoiceData):
    total = data.hours * data.rate

    html_content = f"""
    <html>
    <head>
         <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 30px;
            color: #eee;
            background: #121212;
        }}
        h1 {{
            color: #fff;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        td, th {{
            border: 1px solid #444;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background: #222;
        }}
        .logo {{
            display: block;
            margin: 0 auto 30px;
            width: 100px;
        }}
        .footer {{
            margin-top: 50px;
            text-align: center;
            color: #aaa;
            font-size: 14px;
        }}
    </style>
    </head>
    <body>
        <img src="https://localhost:8080/static/logo.png" alt="BillForge Logo" class="logo" />
        <h1>Invoice</h1>
        <p><strong>Freelancer Name:</strong> {data.freelancer_name}</p>
        <p><strong>Freelancer Email:</strong> {data.freelancer_email}</p>
        <p><strong>Client Name:</strong> {data.client_name}</p>
        <p><strong>Client Email:</strong> {data.client_email}</p>
        <p><strong>Project:</strong> {data.project_description}</p>

        <table>
            <tr>
                <th>Hours</th>
                <th>Rate</th>
                <th>Total</th>
            </tr>
            <tr>
                <td>{data.hours}</td>
                <td>₹{data.rate:.2f}</td>
                <td>₹{total:.2f}</td>
            </tr>
        </table>
        <div class="footer">
            Invoice generated using <strong>BillForge</strong>
        </div>
    </body>
    </html>
    """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        HTML(string=html_content).write_pdf(tmp_file.name)
        return FileResponse(path=tmp_file.name, filename="invoice.pdf", media_type="application/pdf")
