# syntax=docker/dockerfile:1
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps
RUN apt-get update -qq \
 && apt-get install -y --no-install-recommends curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY . /app/

# Uvicorn entry
RUN chmod +x /app/uvicorn.sh
EXPOSE 8000
CMD ["/app/uvicorn.sh"]
