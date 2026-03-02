# MusicMeter / Song Success Predictor

AI-assisted dashboard for evaluating song potential across streaming and social platforms. This repo is the cleaned-up export of the original Replit prototype with the groundwork laid for a production deployment.

## What's included

- Streamlit multi-page app (`app.py` + `pages/`)
- Centralized configuration via [`config.py`](config.py) using environment variables / `.env`
- SQLAlchemy models (`models/database.py`) ready for PostgreSQL + Alembic migrations
- Upload + payment flow groundwork (Stripe Checkout, file storage, metadata extraction)
- Mock data generators to keep the UI functional until live signals are wired in
- Dependency management via `pyproject.toml` / `uv.lock`

## Local development

```bash
# 1. Clone repo & enter directory
cd musicmeter

# 2. Create virtualenv (uv or venv)
uv venv
source .venv/bin/activate
uv pip sync uv.lock

# 3. Copy env template and edit credentials
cp .env.example .env

# 4. Run migrations (once Alembic is configured)
# alembic upgrade head

# 5. Start Streamlit
STREAMLIT_SERVER_ADDRESS=0.0.0.0 streamlit run app.py --server.headless true
```

_Alternatively use `pip install -r requirements.txt` if `uv` is not available._

## Environment variables

See [`.env.example`](.env.example). Minimum required:

- `DATABASE_URL`
- `STRIPE_SECRET_KEY` / `STRIPE_PUBLISHABLE_KEY` (if payments enabled)

Optional:

- `OPENAI_API_KEY` for AI-assisted scoring
- `FAN_ENGAGE_*` for Fan Engage API calls
- `UPLOADS_DIR`, `TEMP_DIR` to override local storage paths

## Deployment notes

- Build a Docker image with the included dependencies and run `streamlit run app.py` behind Nginx / Caddy.
- Use managed Postgres (Supabase, RDS, etc.) and object storage (S3) instead of local folders for uploads.
- Stripe webhooks should be handled by a small FastAPI/Flask service or serverless function to mark payments complete.
- Schedule ingestion/analysis jobs via OpenClaw, Celery, or cloud schedulers to populate trends + sentiment tables.

## Next steps (recommended)

1. Wire real data sources (Spotify, Fan Engage, Chartmetric) into `utils/` and persist results.
2. Add Alembic migrations and seed scripts for the SQLAlchemy models.
3. Implement Stripe webhook + background analysis jobs so the Streamlit UI stays responsive.
4. Replace mocked analytics with real metrics and expose a downloadable scorecard per song.
5. Add CI (lint/test) and Docker build pipeline before handing to engineering.

This version is ready for your engineering team to extend without the Replit-specific plumbing.
