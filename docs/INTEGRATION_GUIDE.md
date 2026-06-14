# Integration Guide

## 1. Central Contract Flow
`DetectionStream` (Input) -> `Analytics Module` (Heuristic Logic) -> `EventPayload` (Output)

All schemas are defined in `core/contracts/schemas.py`.
Sample payloads are available in `samples/`.

## 2. Integration Phases
*   **Phase 1: Independent Feature Development** (Local mock data, baseline YOLO training).
*   **Phase 2: Analytics Integration** (Analytics consume real `DetectionStream` from YOLO engine).
*   **Phase 3: EventPayload Standardization** (All heuristic models emit `EventPayload` on triggers).
*   **Phase 4: Backend Integration (Post-MVP)** (FastStream/FastAPI brokers ingest `EventPayload` to PostgreSQL).
*   **Phase 5: Dashboard Integration (Post-MVP)** (Next.js UI maps events from WebSocket/DB).
*   **Phase 6: End-to-end Testing** (Raw CCTV feed -> YOLO -> Analytics -> EventPayload).

## 3. Analytics Integration Interfaces

### Workstream A: Streetlight Intelligence
*   **Input:** `DetectionStream` (Filtering for `streetlight_normal`, `streetlight_damaged`)
*   **Output:** `EventPayload` (`streetlight_flickering`, `streetlight_off`)
*   **Integration:** Natively accepts bounding boxes, applies day/night and multi-frame toggling logic.

### Workstream B: Animal Intelligence
*   **Input:** `DetectionStream` (Filtering for `animal`)
*   **Output:** `EventPayload` (`animal_hazard`)
*   **Integration:** Relies on tracking IDs to calculate dwell time and velocity.

### Workstream C: Accident Intelligence
*   **Input:** `DetectionStream` (Filtering for `vehicle`, `person`)
*   **Output:** `EventPayload` (`vehicle_collision`, `pedestrian_hazard`)
*   **Integration:** Relies on tracking ID intersection (IoU) and sudden velocity drops.

### Workstream D: Collapse Intelligence
*   **Input:** `DetectionStream` 
*   **Output:** `EventPayload` (`infrastructure_collapse`, `road_obstruction`)
*   **Integration:** Applies spatial mapping of debris and structure collapse risk weighting.
