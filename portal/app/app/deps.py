from pathlib import Path
import os
import redis
from functools import lru_cache

def read_secret(path_env: str, default: str | None = None) -> str:
    """
    Read a secret from a file whose path is given by env var `path_env`.
    If the env var is empty or the file missing and default is not None, return default.
    """
    p = os.getenv(path_env, "")
    if p and Path(p).exists():
        return Path(p).read_text().strip()
    if default is not None:
        return default
    raise RuntimeError(f"Secret file not found via env {path_env}: {p}")

@lru_cache
def get_secret_key() -> str:
    return read_secret("SECRET_KEY_FILE")

@lru_cache
def get_redis_client() -> redis.Redis:
    host = os.getenv("REDIS_HOST", "redis")
    port = int(os.getenv("REDIS_PORT", "6379"))
    pwd  = read_secret("REDIS_PASSWORD_FILE", default="")
    return redis.Redis(host=host, port=port, password=pwd, decode_responses=True)
