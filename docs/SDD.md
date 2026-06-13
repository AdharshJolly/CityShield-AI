# CityShield AI - System Design Document (SDD)

# 1. System Overview

CityShield AI is a real-time urban public safety monitoring platform that processes CCTV feeds and generates actionable hazard intelligence.

The platform consists of:
- Detection Layer
- Analytics Layer
- Intelligence Layer
- Visualization Layer

---

# 2. End-to-End Data Flow

CCTV Feed
→ Frame Extraction
→ Hazard Detection
→ Event Processing
→ Analytics Engines
→ Risk Scoring
→ Database
→ Dashboard

---

# 3. Services

## Detection Service
Responsibilities:
- Run Unified Hazard Detector
- Run Accident Detector
- Produce detections and confidence scores

Outputs:
- Bounding Boxes
- Labels
- Confidence Scores

---

## Analytics Service

Responsibilities:
- Fire Severity Analysis
- Vulnerability Analysis
- Streetlight Health Analysis
- Animal Tracking
- Black Spot Analytics

Outputs:
- Severity Levels
- Risk Metrics
- Dwell Time Metrics
- Heatmaps

---

## Intelligence Service

Responsibilities:
- Aggregate events
- Generate alerts
- Prioritize hazards

Output:
- Public Safety Risk Scores

---

## Dashboard Service

Responsibilities:
- Visualization
- Monitoring
- Reporting

---

# 4. Database Design

## Hazard Events

| Field | Type |
|---------|---------|
| event_id | UUID |
| timestamp | DATETIME |
| hazard_type | STRING |
| confidence | FLOAT |
| severity | STRING |
| risk_score | FLOAT |

---

## Accident Events

| Field | Type |
|---------|---------|
| event_id | UUID |
| location_id | STRING |
| timestamp | DATETIME |
| accident_type | STRING |

---

## Animal Tracking

| Field | Type |
|---------|---------|
| track_id | STRING |
| animal_type | STRING |
| dwell_time | FLOAT |

---

# 5. APIs

## Detection API

POST /detect

Input:
- Frame

Output:
- Detections

---

## Analytics API

POST /analyze

Input:
- Detection Data

Output:
- Analytics Data

---

## Risk API

POST /risk-score

Output:
- Risk Score
- Priority Level

---

# 6. Deployment

Development:
- Local GPU

Production:
- Docker
- FastAPI
- PostgreSQL

---

# 7. Monitoring

Track:
- FPS
- Latency
- GPU Usage
- Detection Accuracy
