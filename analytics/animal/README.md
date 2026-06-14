# Animal Intelligence (Workstream B)

## Objective
Detect and monitor large animals on urban roadways to prevent traffic accidents and dispatch animal control.

## Inputs
Consumes the `DetectionStream` contract. Filters for COCO fallback class:
*   `animal`

## Outputs
Emits the `EventPayload` contract back to the centralized broker.

## Deliverables
*   COCO mapping integration.
*   Animal counting mechanism.
*   Dwell-time analytics (how long has the animal been stationary?).
*   Dead/alive heuristic mapping.

## Example Event Types
*   `animal_hazard`

## Required Unit Tests
*   `test_dwell_time.py`
*   `test_animal_counting.py`

## Definition of Done
Can distinguish a moving dog from a roadkill hazard using bounding box persistence, outputting `animal_hazard` payloads.

## Integration Notes
You will need to integrate heavily with `core/tracking/` to persist object IDs over multiple frames.
