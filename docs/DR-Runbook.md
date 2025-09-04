# DR Runbook — Internal Portal & Monitoring

## Prereqs
- DNS: internal.elsons.co.uk, grafana.elsons.co.uk → new host IP
- Cloudflare Access: recreate apps/policies
- Ubuntu LTS, Docker + Compose

## Steps
1) Clone repo to /srv/elsons-internal
2) `./scripts/bootstrap.sh proxy`
3) INTERNAL:
   - Copy `internal-portal/.env.example` to `.env`, fill secrets
   - `docker compose -f internal-portal/docker-compose.yml up -d --build`
4) MONITORING:
   - Copy `monitoring/.env.example` to `.env`, fill
   - `docker compose -f monitoring/docker-compose.yml up -d`
5) Verify:
   - `https://internal.elsons.co.uk` (Access login → portal)
   - `https://grafana.elsons.co.uk` (Access login → Grafana)
6) Post-restore:
   - Import/restore dashboards
   - Sanity checks: Prometheus targets up, logs in Loki
