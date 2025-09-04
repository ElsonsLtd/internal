# Cloudflare Access (Zero Trust)

1) Zero Trust → Access → Applications → Add → Self-hosted.
2) App 1: internal.elsons.co.uk
   - Policy: include staff group / emails
   - Require MFA
3) App 2: grafana.elsons.co.uk
   - Policy: admins/ops only
   - Require MFA
4) Ensure DNS orange-cloud proxy ON for both hostnames.
5) Optional: pass identity headers to app; log `CF-Access-Authenticated-User-Email`.
