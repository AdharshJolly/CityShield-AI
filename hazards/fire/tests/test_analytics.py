from hazards.fire.analytics.severity import calculate_severity
from hazards.fire.analytics.vulnerability import calculate_vulnerability
from hazards.fire.analytics.incident_manager import IncidentManager

def test_severity():
    assert calculate_severity(1.0, 0.0, 0.0, 0) == 0.5

def test_vulnerability():
    assert calculate_vulnerability(1.0, 0.0, 0.0) == 0.4

def test_incident_lifecycle():
    manager = IncidentManager()
    iid = manager.create(0.8, 0.5)
    assert manager.incidents[iid].status == "active"
    manager.resolve(iid)
    assert manager.incidents[iid].status == "resolved"
