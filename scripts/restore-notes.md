# Restore Notes (quick)

1) Provision Ubuntu host; install Docker + Compose plugin.
2) `git clone` this repo (or copy from backup).
3) Create shared network: `./scripts/bootstrap.sh proxy`.
4) Configure DNS for:
   - internal.elsons.co.uk
   - grafana.elsons.co.uk
5) Cloudflare Access: create apps/policies for both hostnames.
6) INTERNAL:
   - Fill `internal-portal/.env`
   - `cd internal-portal && docker compose up -d --build`
7) MONITORING:
   - Fill `monitoring/.env`
   - `cd monitoring && docker compose up -d`
8) Grafana:
   - Login with admin credentials from `.env`
   - Verify datasources (Prometheus, Loki)
   - Import dashboards (drop JSON into provisioning directory or import via UI)
