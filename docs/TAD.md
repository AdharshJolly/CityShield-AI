# CityShield AI - Technical Architecture Document (TAD)

## Architecture Philosophy

Detection Layer + Analytics Layer + Intelligence Layer

Avoid a single monolithic model.

---

# High-Level Architecture

```text
                    CCTV Feed
                          |
                    Frame Extractor
                          |
                Unified Hazard Detector
                          |
               Accident Detection Engine
                          |
                  Event Processing Layer
                          |
      ------------------------------------------------
      |             |            |           |        |
 Fire Module   Streetlight   Animal    Collapse   Black Spot
               Analytics     Analytics Analytics  Analytics
      ------------------------------------------------
                          |
                  Risk Scoring Engine
                          |
                    Dashboard API
                          |
                     Frontend UI
```

---

# Core Components

## 1. Unified Hazard Detector

### Model
YOLOv12-L

### Classes
- Fire
- Smoke
- Burning Waste
- Collapsed Tree
- Collapsed Pole
- Barricade
- Debris
- Streetlight
- Damaged Streetlight
- Dead Animal
- Stray Animal

---

## 2. Accident Detection Engine

### Model
YOLOv12 + Temporal Analysis

### Classes
- Accident
- Near Accident

---

## 3. Fire Analytics Engine

### Input
- Fire
- Smoke

### Output
- Severity
- Area
- Vulnerability

---

## 4. Streetlight Analytics Engine

### Output
- OFF State Detection
- Flickering Detection

---

## 5. Animal Analytics Engine

### Output
- Count
- Dwell Time
- Dead/Alive Classification

### Tracking
ByteTrack

---

## 6. Black Spot Engine

### Input
Accident Events

### Output
- Heatmaps
- Frequency Analysis
- Black Spot Score

---

## 7. Risk Scoring Engine

### Formula

```text
Risk Score =
Severity × Weight × Persistence × Confidence
```

### Priority Weights

| Hazard | Weight |
|----------|----------|
| Fire | 40 |
| Collapse | 20 |
| Streetlight | 20 |
| Accident Zone | 10 |
| Animal Hazard | 10 |

---

# Technology Stack

## Detection
- YOLOv12-L
- PyTorch
- OpenCV

## Tracking
- ByteTrack

## Analytics
- NumPy
- Pandas

## Backend
- FastAPI

## Frontend
- Next.js
- Tailwind CSS

## Database
- PostgreSQL

---

# Two-Week Execution Plan

## Days 1-2
- Dataset Aggregation
- Dataset Cleaning
- Label Harmonization

## Days 3-5
- Unified Hazard Detector Training

## Days 4-6
- Accident Detection Training

## Days 6-8
- Analytics Engine Development

## Days 8-10
- Risk Scoring Engine
- Dashboard Development

## Days 10-12
- Integration
- Testing

## Days 12-14
- Optimization
- Documentation
- Submission Preparation
