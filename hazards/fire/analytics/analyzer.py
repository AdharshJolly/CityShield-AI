from typing import List
from shared.contracts.detection import Detection
from hazards.fire.analytics.severity import calculate_severity
from hazards.fire.analytics.vulnerability import calculate_vulnerability
from hazards.fire.analytics.incident_manager import IncidentManager

def analyze_detections(detections: List[Detection], manager: IncidentManager):
    fire_area = sum(d.bbox[2]*d.bbox[3] for d in detections if d.class_name == "fire")
    smoke_area = sum(d.bbox[2]*d.bbox[3] for d in detections if d.class_name == "smoke")
    
    sev = calculate_severity(fire_area, smoke_area, 1.0, len(detections))
    vul = calculate_vulnerability(0, 0, 0) # Mocked
    
    return manager.create(sev, vul)
