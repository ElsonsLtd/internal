#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../monitoring"
cp -n .env.example .env || true
echo "Edit monitoring/.env then run:"
echo "  docker compose pull --ignore-pull-failures"
echo "  docker compose up -d"
