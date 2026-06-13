# CityShield AI - ML Engineering Specification

# 1. ML Objectives

Build a robust urban hazard intelligence system capable of detecting and analyzing:

- Fire / Smoke / Burning Waste
- Collapsed Structures
- Damaged Streetlights
- Accidents
- Dead / Stray Animals

---

# 2. Model Strategy

## Model A

Unified Hazard Detector

Architecture:
- YOLOv12-L

Classes:
- Fire
- Smoke
- Burning Waste
- Fallen Tree
- Pole
- Barricade
- Debris
- Streetlight
- Damaged Streetlight
- Dead Animal
- Stray Animal

---

## Model B

Accident Detection Engine

Architecture:
- YOLOv12
- Temporal Analysis

Classes:
- Accident
- Near Accident

---

# 3. Dataset Strategy

## Fire

Sources:
- Fire Smoke Dataset
- Wildfire Smoke Dataset
- Domestic Fire Dataset

---

## Collapse

Sources:
- Fallen Trees Dataset

---

## Streetlights

Sources:
- Damaged Lights
- Streetlight Dataset

---

## Animals

Sources:
- Stray Animal Dataset

---

## Accident Detection

Sources:
- Accident Dataset
- Road Crossing Dataset

---

# 4. Data Processing

Steps:
1. Cleaning
2. Label Harmonization
3. Augmentation
4. Dataset Balancing
5. Split Generation

---

# 5. Augmentation

- Rotation
- Scaling
- Flipping
- Brightness Shift
- Motion Blur
- Fog Simulation
- Rain Simulation

---

# 6. Training

Framework:
- PyTorch

Experiment Tracking:
- Weights & Biases

Optimization:
- AdamW

---

# 7. Evaluation

Metrics:
- mAP50
- mAP50-95
- Precision
- Recall
- F1 Score

Target:
- >90% Overall Accuracy

---

# 8. Model Versioning

v0.1 Baseline

v0.2 Improved Dataset

v0.3 Analytics Integration

v1.0 Final Submission
