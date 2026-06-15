from dataclasses import dataclass

@dataclass
class FireEvent:
    incident_id: str
    timestamp: float
    severity_score: float
    vulnerability_score: float
    psri_score: float
    hazard_type: str
    status: str
