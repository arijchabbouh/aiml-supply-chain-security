# AI/ML Supply Chain Security & Risk Assessment Platform

> Secure AI/ML artifacts before they enter production.

A platform that analyzes AI/ML projects (models, datasets, dependencies, containers), combines security scanners with trained ML detectors, and outputs an explained **ALLOW / REVIEW / BLOCK** decision.

**Team:** Mohamed Bayrem Bejaoui (AI Security) · Arij Chabbouh (AI Engineering) — ENICarthage, 2026–2027

## Getting started

Requirements: Python 3.12, [uv](https://docs.astral.sh/uv/), Docker.

```bash
cp .env.example .env          # then edit the password
docker compose up -d          # PostgreSQL + pgvector
cd backend
uv sync                       # creates the virtual env and installs dependencies
uv run uvicorn app.main:app --reload
```

Open http://localhost:8000/docs

## Tests and lint

```bash
cd backend
uv run ruff check .
uv run pytest
```

## Rules

- No secrets in the repo: use `.env` (gitignored).
- No real malicious samples or backdoored models committed: download them locally with scripts into gitignored folders.
- One branch and one pull request per task: `feat/T03-fastapi-postgres`.
