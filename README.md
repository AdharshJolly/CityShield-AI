# CityShield AI

Real-Time Public Safety Intelligence Platform designed to analyze CCTV feeds and identify urban hazards (Fire, Collapse, Accident, Animals, Streetlights).

## Getting Started
1. Review `CONTRIBUTING.md` for the Git branch and PR strategy.
2. Review `docs/DAY3_STARTER_CHECKLISTS.md` for your specific workstream assignments.
3. Use the `core/contracts/` schemas to mock your APIs and test analytics endpoints.

## Project Structure
- `ml_engine/`: Unified YOLO training and Model Deployment (Owned by Lead Architect)
- `analytics/`: Hazard specific detection logic (Isolated by Workstream)
- `core/`: Shared ByteTrack implementation and JSON schemas.
- `platform/`: FastAPI Backend, Next.js Dashboard, PostgreSQL.
