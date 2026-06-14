# Team Operations

## 1. Team Hierarchy & Workstream Ownership

| Role | Owner | Directory Ownership | Core Deliverables |
| :--- | :--- | :--- | :--- |
| **Lead Architect** | Adharsh | `ml_engine/`, `core/`, `analytics/fire/` | Base YOLO engine, Model training, Schema contracts, Fire analytics |
| **Workstream A** | TBD | `analytics/streetlight/` | OFF-state detection, Flicker detection, Brightness thresholds |
| **Workstream B** | TBD | `analytics/animal/` | COCO animal mapping, Dwell-time analysis, Dead/alive heuristics |
| **Workstream C** | TBD | `analytics/accident/`, `core/tracking/`| ByteTrack integration, Speed estimation, Collision derivation |
| **Workstream D** | TBD | `analytics/collapse/` | Dataset acquisition, Annotation, Dataset harmonization, Collapse heuristic development, v2 taxonomy proposal |

*(Note: Platform Engineering components in `platform/` are shared integration areas post-MVP).*

## 2. Branch Strategy & PR Workflow
*   **Main Branch (`main`):** Protected, production-ready code.
*   **Feature Branches:** Named `feature/<name>` (e.g., `feature/ws-a-flicker-detection`).
*   **PR Reviews:**
    *   **Core/ML Code:** Lead Architect review.
    *   **Analytics Code:** Lead Architect + 1 Cross-functional peer review.
    *   **Platform/Integration Code:** Collective review.

## 3. Definition of Done & Acceptance Criteria

A workstream feature is "Done" when it is isolated within its designated `analytics/` folder, demonstrates end-to-end functionality via local mock testing, contains isolated unit tests via `pytest`, and outputs a cleanly formatted JSON `EventPayload`.

### Lead Architect
*   **Required tests:** Dataset splitting validation, YOLO output parsing.
*   **Acceptance Criteria:** Model trains without OOM, outputs reliable bounding boxes, `DetectionStream` pushed correctly.

### Workstream A: Streetlight Intelligence
*   **Required tests:** `test_flicker_threshold.py`, `test_day_night_logic.py`.
*   **Acceptance Criteria:** Successfully identifies damaged lights at night without false positives during the day.

### Workstream B: Animal Intelligence
*   **Required tests:** `test_dwell_time.py`, `test_animal_counting.py`.
*   **Acceptance Criteria:** Distinguishes a moving dog from a roadkill hazard using bounding box persistence.

### Workstream C: Accident Intelligence
*   **Required tests:** `test_collision_intersection.py`, `test_sudden_stop.py`.
*   **Acceptance Criteria:** Generates an event when two tracking IDs intersect at high velocity.

### Workstream D: Collapse Intelligence
*   **Required tests:** `test_hazard_scoring.py`, `test_obstruction_mapping.py`.
*   **Acceptance Criteria:** Identifies and maps debris/collapse events with high-priority hazard scores.

## 4. Cross-Cutting PSRI Risk Engine
PSRI (Project Specific Risk Index) is a shared aggregation layer, not a standalone workstream. All workstreams must output standardized `EventPayload` objects. The central architecture will use these payloads for:
1.  Risk Scoring
2.  Hazard Prioritization
3.  Alert Ranking
