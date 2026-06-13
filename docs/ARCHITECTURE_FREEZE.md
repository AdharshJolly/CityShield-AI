# CityShield AI: Architecture Freeze & Conflict Resolution

This document serves as the absolute, immutable source of truth for the CityShield AI project. By reaching this gate, all ambiguity across the legacy Product Requirements Document (PRD), System Design Document (SDD), and Technical Architecture Document (TAD) is officially resolved.

---

## 1. Conflict Resolution Report (Legacy Documentation Audit)

During the repository-wide consistency audit, several conflicts were identified between the initial hackathon drafts and the newly engineered ML specifications.

| Artifact | Identified Conflict | Formal Resolution (Frozen) |
| :--- | :--- | :--- |
| **Global** | Project named as "CityLens" in several docs and `package.json`. | All references normalized to **CityShield AI**. |
| **PRD / TAD** | Implied multiple separate object detection models (e.g., one for Fire, one for Traffic). | **Architecture Conflict Resolved:** We are using a **Single Unified YOLOv12-L Model** with 10 classes to hit the `<150ms` latency KPI. |
| **SDD** | Implied that Kaggle accident videos would be used for training YOLO. | **Dataset Conflict Resolved:** Videos lack YOLO bounding boxes. Accident detection is entirely offloaded to ByteTrack velocity/trajectory heuristics on the `vehicle` class. |
| **ML Spec** | Unclear distinction between "Platform" and "Collapse" roles. | **Ownership Conflict Resolved:** The Lead Architect absorbed Fire Intelligence to allow Workstream D to explicitly own both Platform and Collapse. |
| **Raw Datasets**| Raw YAML for Fire dataset had garbage class names (`----`). | **Taxonomy Conflict Resolved:** `ml_engine/datasets/taxonomy.py` is established as the sole source of truth. Raw data is forcefully remapped during harmonization. |

---

## 2. Final Frozen Architecture

The system operates on a decoupled **Mock-First** structure.
1. **Inference Layer (Lead Architect):** A single YOLOv12-L stream pushing bounding boxes via the `DetectionStream` contract.
2. **Heuristic Layer (Workstreams A, B, C, D):** Isolated mathematical engines (ByteTrack, Temporal Buffers, Area ratios) consuming bounding boxes and emitting hazards.
3. **Integration Layer (Workstream D):** FastAPI REST backend accepting `EventPayload` items, storing them in PostgreSQL, and serving a Next.js Dashboard.

---

## 3. Final Team Ownership

| Contributor | Domain | Core Responsibilities |
| :--- | :--- | :--- |
| **Lead Architect** | ML System & Fire | Dataset Harmonization, Unified YOLO Training, Fire Severity/Vulnerability Analytics, `core/config/` management. |
| **Workstream A** | Streetlight | OFF-State detection, Flickering temporal logic, Luma extraction. |
| **Workstream B** | Animal | ByteTrack dwell-time logic, Dead/Alive heuristics. |
| **Workstream C** | Accident | Collision physics (Velocity Drop + IoU), Heatmap generation matrix. |
| **Workstream D** | Platform & Collapse | Next.js Dashboard, FastAPI backend, PostgreSQL schema, Collapse Detection/Classification. |

---

## 4. Final Dataset Strategy

All dataset preparation executes sequentially: `harmonize.py` -> `validate.py` -> `split_dataset.py` -> `generate_yaml.py` -> `statistics.py`.

*   **Version Control:** All data outputs to `data/processed/cityshield_v1/`.
*   **Splits:** Strictly stratified via fixed random seeds into `Train (70%)`, `Val (20%)`, `Test (10%)`.
*   **Capping:** Massive datasets (like 400k animals) are downsampled to 5,000 images to prevent drowning the Fire classes.
*   **Auditability:** A `dataset_manifest.json` is generated for every version, tracking exact file distributions.

---

## 5. Final Taxonomy & KPI Mapping

Defined explicitly in `core/config/classes.yaml` and `core/config/risk_weights.yaml`.

| Class ID | Class Name | Target KPI Weight | Primary Analytics Consumer |
| :--- | :--- | :--- | :--- |
| 0 | `fire` | 40% | Lead Architect (Severity) |
| 1 | `smoke` | 40% | Lead Architect (Vulnerability) |
| 2 | `burning_waste` | 40% | Lead Architect |
| 3 | `fallen_tree` | 20% | Workstream D |
| 4 | `collapsed_structure` | 20% | Workstream D |
| 5 | `streetlight_normal` | 20% | Workstream A |
| 6 | `streetlight_damaged`| 20% | Workstream A |
| 7 | `animal` | 10% | Workstream B |
| 8 | `vehicle` | 10% | Workstream C (Accidents) |
| 9 | `person` | 40% | Lead Architect (Vulnerability Proximity) |

---

## 6. Final Inter-Team Contracts

### A. The `DetectionStream` Contract
*Pushed by the ML Engine frame-by-frame.*
```json
{
  "frame_id": 1042,
  "timestamp": "2026-06-13T23:25:11Z",
  "camera_id": "CAM_014",
  "location_id": "MG_ROAD_JUNCTION",
  "detections": [
    {"class_id": 8, "class_name": "vehicle", "confidence": 0.89, "bbox": {"x_center": 0.5, "y_center": 0.5, "width": 0.2, "height": 0.1}, "track_id": 12}
  ]
}
```

### B. The `EventPayload` Contract
*Pushed by Analytics engines to the Backend.*
```json
{
  "event_id": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2026-06-13T23:25:15Z",
  "hazard_type": "accident",
  "severity_level": "critical",
  "psri_score": 85.5,
  "details": {"velocity_drop": true, "involved_tracks": [12, 14]}
}
```

---

## 7. Architecture Freeze Checklist

No further architectural changes are permitted. Ensure these steps are complete before writing implementation code:

- [x] All "CityLens" references purged. Name standardized to **CityShield AI**.
- [x] All `.md` documents consolidated into `docs/`.
- [x] `.gitignore` hardened and Git LFS active.
- [x] `core/config/` initialized with global parameters.
- [x] ML Architecture and Experiment Tracking specification approved.
- [x] Team ownership mapped directly to repository folder structure.
- [ ] Initial Git commit pushed to `main` branch.
- [ ] `dev` branch cut and distributed to Workstreams A, B, C, and D.

**Status: ARCHITECTURE FROZEN.**
