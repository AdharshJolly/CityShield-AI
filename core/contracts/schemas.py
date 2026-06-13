from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class BoundingBox(BaseModel):
    x_center: float
    y_center: float
    width: float
    height: float

class Detection(BaseModel):
    class_id: int
    class_name: str
    confidence: float
    bbox: BoundingBox
    track_id: Optional[int] = None

class DetectionStream(BaseModel):
    frame_id: int
    timestamp: str
    detections: List[Detection]

class EventDetails(BaseModel):
    velocity_drop: Optional[bool] = None
    iou_intersection: Optional[float] = None
    involved_tracks: Optional[List[int]] = None
    dwell_time_sec: Optional[int] = None
    area_percentage: Optional[float] = None

class EventPayload(BaseModel):
    event_id: str
    timestamp: str
    hazard_type: str
    severity_level: str
    psri_score: float
    details: EventDetails
