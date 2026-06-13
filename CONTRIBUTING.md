# CityShield AI Contributing Guidelines

## Branch Strategy
We use a Workstream-isolated Git Flow to prevent blocking.
- `main`: Production-ready code. (Locked, requires PR).
- `dev`: Active integration branch.
- Feature branches must follow the naming convention:
  `feature/<workstream>/<short-desc>`
  Example: `feature/accident/velocity-tracker` or `feature/ml/unified-yolo`

## Pull Request Workflow
1. Develop on your isolated feature branch.
2. Push to origin and open a PR against `dev`.
3. PRs modifying `core/contracts/` MUST be reviewed and approved by the Lead Architect.
4. Workstream-specific PRs (e.g., inside `analytics/animal/`) do not require external approval but must pass CI/CD unit tests.
5. Squash and Merge into `dev`.

## Integration Workflow
- **Day 3-8 (Mock Phase):** Merge analytics engines into `dev` using mock JSON payloads.
- **Day 9 (Live Integration):** Lead Architect merges the live ML Inference Engine into `dev`. All Workstreams create a final PR to replace mock endpoints with the live YOLO stream.
- **Day 11 (Release Candidate):** `dev` is merged into `main` for end-to-end performance testing.
