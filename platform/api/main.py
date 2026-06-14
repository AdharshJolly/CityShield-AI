from fastapi import FastAPI
from core.contracts.schemas import EventPayload, DetectionStream

app = FastAPI()

@app.post("/detections")
def receive_detection(detection: DetectionStream):
    return {"status": "received", "camera": detection.camera_id}

@app.post("/events")
def receive_event(event: EventPayload):
    return {"status": "received", "event_id": event.event_id}
