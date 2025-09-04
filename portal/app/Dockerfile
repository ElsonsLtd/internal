FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# uvicorn will serve on 0.0.0.0:8080 for Traefik
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
