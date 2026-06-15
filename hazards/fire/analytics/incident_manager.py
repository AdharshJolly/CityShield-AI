import uuid
import time
from shared.contracts.fire_event import FireEvent

class IncidentManager:
    def __init__(self):
        self.incidents = {}

    def create(self, severity, vulnerability):
        incident_id = str(uuid.uuid4())
        event = FireEvent(
            incident_id=incident_id,
            timestamp=time.time(),
            severity_score=severity,
            vulnerability_score=vulnerability,
            psri_score=severity * vulnerability,
            hazard_type="fire",
            status="active"
        )
        self.incidents[incident_id] = event
        return incident_id

    def update(self, incident_id, severity, vulnerability):
        if incident_id in self.incidents:
            self.incidents[incident_id].severity_score = severity
            self.incidents[incident_id].vulnerability_score = vulnerability
            self.incidents[incident_id].psri_score = severity * vulnerability

    def resolve(self, incident_id):
        if incident_id in self.incidents:
            self.incidents[incident_id].status = "resolved"
