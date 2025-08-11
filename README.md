# Profile Matcher

A microservices-based profile matching system that evaluates player eligibility for campaigns using FastAPI and MongoDB.

## Overview

This system consists of two FastAPI microservices:

- **Campaign Service** (port 8001): Manages campaigns stored in MongoDB
- **Matcher Service** (port 8000): Retrieves player profiles, fetches active campaigns, evaluates matching rules, and updates player configurations

## Project Structure

```
.
├── docker-compose.yml
├── mongo-init/
│   └── seed.js
├── campaign_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── db.py
│       ├── models/
│       ├── repositories/
│       ├── services/
│       └── routers/
└── matcher_service/
    ├── Dockerfile
    ├── requirements.txt
    └── app/
        ├── main.py
        ├── db.py
        ├── models/
        ├── repositories/
        ├── services/
        └── routers/
```

## Prerequisites

- Docker Desktop (with Docker Compose)
- Available ports: 8000, 8001, 27017
- Python 3.8+ and pip (for local development)

## Quick Start

1. **Start all services:**
   ```bash
   docker compose up --build
   ```

2. **Clean restart (with fresh data):**
   ```bash
   docker compose down -v
   docker compose up --build
   ```

## Service Endpoints

| Service | URL | Description |
|---------|-----|-------------|
| Campaign Service | http://localhost:8001 | Campaign management API |
| Matcher Service | http://localhost:8000 | Profile matching API |
| MongoDB | mongodb://root:root@localhost:27017/game_db | Database |

## Testing the System

### Verify Campaign Service
```bash
curl http://localhost:8001/campaigns
```
*Expected: Returns list with "mycampaign"*

### Test Matcher (Active Campaign Window)
```bash
curl "http://localhost:8000/get_client_config/97983be2-98b7-11e7-90cf-082e5f28d836?now=2022-01-30T00:00:00Z"
```
*Expected: `active_campaigns` includes "mycampaign"*

### Test Matcher (Inactive Campaign Window)
```bash
curl "http://localhost:8000/get_client_config/97983be2-98b7-11e7-90cf-082e5f28d836?now=2023-01-01T00:00:00Z"
```
*Expected: `active_campaigns` is empty*

## Development

### Database Management

**Reset database with seed data:**
```bash
docker compose down -v
docker compose up --build
```

**View logs:**
```bash
docker compose logs -f [service_name]
```

## API Documentation

Once services are running, visit:
- Campaign Service: http://localhost:8001/docs
- Matcher Service: http://localhost:8000/docs

## Shutdown

**Stop services (preserve data):**
```bash
docker compose down
```

**Stop services and remove data:**
```bash
docker compose down -v
```

## Troubleshooting

- **Port conflicts**: Ensure ports 8000, 8001, and 27017 are available
- **Database connection issues**: Try `docker compose down -v && docker compose up --build`
- **Service startup order**: Services will retry database connections automatically
