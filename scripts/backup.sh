#!/usr/bin/env bash
set -euo pipefail
STAMP=$(date +%Y%m%d-%H%M%S)
DEST=${1:-"$HOME/elsons-backups/$STAMP"}
mkdir -p "$DEST"

# App configs
tar czf "$DEST/internal-portal.tgz" -C "$(dirname "$0")/.." internal-portal
tar czf "$DEST/monitoring.tgz" -C "$(dirname "$0")/.." monitoring

echo "Backups written under $DEST"
echo "Remember to also back up Traefik ACME (from your Traefik stack)."
