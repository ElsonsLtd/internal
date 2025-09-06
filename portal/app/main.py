from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import os

# Optional Redis (async) — works even if not configured
try:
    import redis.asyncio as aioredis  # type: ignore
except Exception:                      # pragma: no cover
    aioredis = None

app = FastAPI(title="Elsons Portal")

templates = Jinja2Templates(directory="templates")

def _read_secret(path: str | None) -> str | None:
    if not path:
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

# ---- Redis wiring (optional) ----
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_PASSWORD = _read_secret(os.getenv("REDIS_PASSWORD_FILE"))

_redis = None
async def get_redis():
    global _redis
    if aioredis is None:
        return None
    if _redis is None:
        _redis = aioredis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD or None,
            decode_responses=True,
            socket_keepalive=True,
            health_check_interval=30,
        )
    return _redis

@app.get("/healthz", response_class=JSONResponse)
async def healthz():
    # Basic app liveness + optional redis ping
    redis_ok = None
    if aioredis is not None:
        try:
            r = await get_redis()
            if r is not None:
                await r.ping()
                redis_ok = True
            else:
                redis_ok = None
        except Exception:
            redis_ok = False
    return {"ok": True, "redis": redis_ok}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Elsons Portal"}
    )
