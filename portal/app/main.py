import os
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
import httpx
import redis

app = FastAPI()
templates = Environment(loader=FileSystemLoader("templates"))

# Redis
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    visits = r.incr("visits")
    tpl = templates.get_template("index.html")
    return tpl.render(request=request, visits=visits)

@app.post("/actions/generate-csv")
async def generate_csv():
    url = os.getenv("N8N_WEBHOOK_GENERATE_CSV")
    if not url:
        return JSONResponse({"error": "N8N webhook not configured"}, status_code=status.HTTP_400_BAD_REQUEST)
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(url, json={"source": "internal-portal"})
    return JSONResponse({"status": "triggered", "n8n_status": resp.status_code})
