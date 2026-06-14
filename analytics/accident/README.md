# Accident Intelligence (Workstream C)

## Objective
Detect vehicle collisions and pedestrian safety hazards using advanced velocity tracking and object intersection heuristics.

## Inputs
Consumes the `DetectionStream` contract. Filters for COCO fallback classes:
*   `vehicle`
*   `person`

## Outputs
Emits the `EventPayload` contract back to the centralized broker.

## Deliverables
*   ByteTrack integration for multi-object persistence.
*   Speed estimation logic based on camera calibration constraints.
*   Collision detection (IoU intersection combined with sudden velocity drops).
*   Blackspot analytics.

## Example Event Types
*   `vehicle_collision`
*   `pedestrian_hazard`

## Required Unit Tests
*   `test_collision_intersection.py`
*   `test_sudden_stop.py`

## Definition of Done
Generates an accurate `EventPayload` when two active tracking IDs intersect and immediately drop to zero velocity.

## Integration Notes
This workstream owns the shared `core/tracking/` ByteTrack implementation and is responsible for making it available to other modules if needed.
