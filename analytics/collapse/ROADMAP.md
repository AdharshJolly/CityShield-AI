# Collapse Intelligence Roadmap

## Phase 1: Preparation (Active)
*   Dataset acquisition (Kaggle/Roboflow)
*   Annotation standardization
*   Mock payload development (`mock_samples/`)

## Phase 2: Detector Integration
*   Deliver finalized `CITYSHIELD_V2` dataset to Lead Architect
*   Retrain YOLO11n to support `fallen_tree`, `collapsed_structure`, and `debris`

## Phase 3: Severity Scoring
*   Develop heuristics to calculate obstruction percentage using bounding box dimensions.
*   Cross-reference detections with road masks (future scope).

## Phase 4: PSRI Integration
*   Emit standardized `EventPayload` objects carrying `infrastructure_collapse` tags to the central PSRI Risk Engine.
