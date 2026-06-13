# CityShield AI - Product Requirements Document (PRD)

## Project Name
CityShield AI

### Tagline
Real-Time Public Safety Hazard Intelligence System for Smart Cities

---

## Problem Statement

Urban authorities rely heavily on manual monitoring of CCTV feeds to identify public safety hazards such as fires, collapsed structures, damaged streetlights, accident-prone zones, and stray animals.

Manual monitoring is:
- Slow
- Error-prone
- Non-scalable
- Reactive instead of proactive

CityShield AI provides real-time hazard detection, analytics, and risk prioritization from CCTV streams.

---

## Goals

### Primary Goals
Detect:
1. Fire / Smoke / Burning Waste
2. Collapsed Trees / Structures
3. Damaged Streetlights
4. Accident Events
5. Dead / Stray Animals

### Secondary Goals
Generate:
- Fire severity
- Vulnerability scores
- Animal dwell time
- Streetlight health status
- Accident heatmaps
- Black spot identification

---

## Success Metrics

### Hackathon Metrics

| Metric | Target |
|----------|----------|
| Overall Accuracy | >90% |
| mAP50 | >90% |
| Precision | >90% |
| Recall | >90% |
| Inference Speed | <150ms/frame |

### Business Metrics

| Metric | Target |
|----------|----------|
| Fire Detection Time | <5 sec |
| Streetlight Failure Detection | <30 sec |
| Accident Detection | <10 sec |
| Animal Hazard Alert | <15 sec |

---

## Users

### Primary
Municipal Authorities

### Secondary
Traffic Management Teams

### Tertiary
Emergency Response Teams

---

## Functional Requirements

### FR1
Detect Fire, Smoke, and Burning Waste.

### FR2
Classify fire severity as Mild, Moderate, or Severe.

### FR3
Estimate Fire Area and Smoke Area.

### FR4
Estimate People Count and Building Density.

### FR5
Calculate Vulnerability Score.

### FR6
Detect Collapsed Trees, Collapsed Poles, Barricades, and Road Debris.

### FR7
Detect Dead Animals and Stray Animals.

### FR8
Track Animal Count and Dwell Time.

### FR9
Detect Streetlight Damage, OFF State, and Flickering.

### FR10
Detect Accident Events.

### FR11
Generate Accident Heatmaps and Black Spot Rankings.

---

## Scope

### In Scope
- CCTV Analysis
- Real-Time Detection
- Hazard Analytics
- Risk Scoring
- Dashboard

### Out of Scope
- Emergency Dispatch
- CCTV Camera Control
- Predictive Accident Forecasting
- Face Recognition
- Vehicle Identification
