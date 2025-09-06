from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
import httpx
from .deps import get_secret_key, get_redis_client

app = FastAPI(title="Elsons Portal")

templates = Jinja2Templates(directory="app/templates")

@app.get("/healthz")
def healthz():
    # basic health + redis ping
    try:
        r = get_redis_client()
        r.ping()
        redis_ok = True
    except Exception:
        redis_ok = False
    return JSONResponse({"ok": True, "redis": redis_ok})

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Elsons Portal"}
    )

@app.post("/trigger")
async def trigger():
    """
    Optional: calls N8N_WEBHOOK_URL if set.
    """
    url = os.getenv("N8N_WEBHOOK_URL", "").strip()
    if not url:
        return JSONResponse({"status": "skipped", "reason": "N8N_WEBHOOK_URL not set"})
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(url, json={"source": "portal"})
        return JSONResponse({"status": "sent", "code": r.status_code})
