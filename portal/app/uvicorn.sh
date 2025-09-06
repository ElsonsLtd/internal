#!/usr/bin/env bash
set -euo pipefail

# Start uvicorn
exec uvicorn main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --workers 2
