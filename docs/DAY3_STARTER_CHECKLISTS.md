# Day 3 Starter Checklists

### Lead Architect
- [ ] Initialize Python venv and install dependencies.
- [ ] Run `phase1_data_pipeline.py` to harmonize datasets.
- [ ] Verify YOLOv12-L training environment (CUDA, PyTorch).
- [ ] Review and lock `core/contracts/schemas.py`.

### Workstream A (Streetlights)
- [ ] Pull `dev` branch.
- [ ] Create branch `feature/streetlight/mock-luma`.
- [ ] Create `analytics/streetlight/analyzer.py`.
- [ ] Write a script to ingest a mock `DetectionStream` and print average luma.

### Workstream B (Animals)
- [ ] Pull `dev` branch.
- [ ] Create branch `feature/animal/mock-dwell`.
- [ ] Create `analytics/animal/analyzer.py`.
- [ ] Write a script to calculate dwell time from mock tracked objects.

### Workstream C (Accidents)
- [ ] Pull `dev` branch.
- [ ] Create branch `feature/accident/bytetrack`.
- [ ] Implement ByteTrack wrapper in `core/tracking/bytetrack_wrapper.py`.
- [ ] Write a test script feeding mock YOLO outputs into the tracker.

### Workstream D (Platform & Collapse)
- [ ] Pull `dev` branch.
- [ ] Create branch `feature/platform/fastapi-mock`.
- [ ] Set up FastAPI scaffold in `platform/api/main.py`.
- [ ] Create an endpoint `POST /events` that accepts `EventPayload`.
- [ ] Initialize `analytics/collapse/analyzer.py`.
