FROM python:3.11-slim

RUN apt-get update && apt-get install -y     build-essential     libpango1.0-0     libgdk-pixbuf2.0-0     libffi-dev     libcairo2     libpangoft2-1.0-0     libpangocairo-1.0-0     libglib2.0-0     libxml2     libxslt1.1     libjpeg-dev     zlib1g-dev     && apt-get clean     && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]

