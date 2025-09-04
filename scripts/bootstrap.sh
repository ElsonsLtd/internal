#!/usr/bin/env bash
set -euo pipefail

NET=${1:-proxy}
if ! docker network inspect "$NET" >/dev/null 2>&1; then
  docker network create "$NET"
  echo "Created network: $NET"
else
  echo "Network exists: $NET"
fi
