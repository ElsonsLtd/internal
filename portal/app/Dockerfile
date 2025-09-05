FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# system deps
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app
COPY app ./app
COPY uvicorn.sh ./uvicorn.sh
RUN chmod +x ./uvicorn.sh

EXPOSE 8000
CMD ["./uvicorn.sh"]
