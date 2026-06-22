# CityShield-AI Dataset Source Manifest
**KPI Group 4: Public Safety Hazards**

This manifest documents the exact origins, descriptions, priority weightings, and URLs for the datasets used to train the 5 core intelligence engines of CityShield-AI.

## 1. Fire Intelligence Engine (Priority: 1 - Weightage: 40%)
**Category:** Burning of waste, Smoke / Fire Detection
*   **Description:** Fire and Smoke Detection. Severity and Vulnerability categorization: how severe the fire is and how crowded or dense the locality is (by counting people, buildings).
*   **Analytics & Features:** 
    *   Severity classification: Mild / Moderate / Severe
    *   Vulnerability classification: Mild / Moderate / Severe
    *   Waste or Burning Area/Size estimation (sq. m)
*   **Available Datasets:**
    *   [Roboflow - Eco-Group Fire/Smoke (10k images)](https://universe.roboflow.com/eco-group/fire-smoke-yvnrc)
    *   [Roboflow - Wildfire Smoke (737 images)](https://public.roboflow.com/object-detection/wildfire-smoke/1)
    *   [DataCluster - Domestic Fire & Smoke (40 images)](https://github.com/datacluster-labs/Domestic-Fire-and-Smoke-Dataset/tree/main/sample_datasets)

## 2. Collapse Intelligence Engine (Priority: 2 - Weightage: 20%)
**Category:** Collapsed trees or structures
*   **Description:** Detection of collapsed trees or structures (such as light poles, barricades, other obstructions on the road).
*   **Analytics & Features:** 
    *   Classification into varieties of obstacles
*   **Available Datasets:**
    *   [Roboflow - Fallen Trees with Palms](https://universe.roboflow.com/overflow-thaap/fallen-trees-with-palms)
    *   [DataCluster - Obstructions](https://github.com/datacluster-labs/Domestic-Fire-and-Smoke-Dataset/tree/main/sample_datasets)

## 3. Streetlight Intelligence Engine (Priority: 2 - Weightage: 20%)
**Category:** Damaged Street Lights
*   **Description:** Detection of streetlight anomalies to optimize maintenance.
*   **Analytics & Features:** 
    *   OFF-state detection
    *   Flickering detection
*   **Available Datasets:**
    *   [Roboflow - Damaged Lights (699 images)](https://universe.roboflow.com/godspeed-yqpeo/damaged-lights)
    *   [Roboflow - Streetlight Detection (10k images)](https://universe.roboflow.com/streetlight-detection/sodioum-only-jkq3f)
    *   [Team16Project - Street Light Dataset (800 images)](https://github.com/Team16Project/Street-Light-Dataset)

## 4. Accident Intelligence Engine (Priority: 3 - Weightage: 10%)
**Category:** Dark Spots / Black Spots
*   **Description:** A segment of road or an intersection where a concentrated number of traffic accidents or fatalities have historically occurred.
*   **Analytics & Features:** 
    *   Detect accidents on roads
    *   Identify dark spots (location) by frequency of accidents (count)
*   **Available Datasets:**
    *   [Kaggle - Accident (2000 videos)](https://www.kaggle.com/datasets/picekl/accident)
    *   [Kaggle - Road Crossing Dataset (104 videos)](https://www.kaggle.com/datasets/siddhi17/road-crossing-dataset)

## 5. Animal Intelligence Engine (Priority: 3 - Weightage: 10%)
**Category:** Dead or Stray Animals on Road
*   **Description:** Animal type categorization to prevent hazards.
*   **Analytics & Features:** 
    *   Dead or Alive
    *   Count & dwell time (no. of animals and how long they are present)
*   **Available Datasets:**
    *   [Kaggle - Stray Animals (400k images)](https://www.kaggle.com/datasets/bsridevi/modes-dataset-of-stray-animals)

