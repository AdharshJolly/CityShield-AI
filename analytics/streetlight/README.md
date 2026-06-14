# Streetlight Intelligence (Workstream A)

## Objective
Detect damaged, broken, or flickering streetlights during night operations to improve public safety and maintenance dispatch.

## Inputs
Consumes the `DetectionStream` contract (see `core/contracts/schemas.py`), specifically parsing for:
*   `streetlight_normal`
*   `streetlight_damaged`

## Outputs
Emits the `EventPayload` contract back to the centralized broker.

## Deliverables
*   Day/Night bounding toggle.
*   Flicker detection heuristic (rapid status toggling across sequential frames).
*   OFF-state detection at night.

## Example Event Types
*   `streetlight_flickering`
*   `streetlight_off`

## Required Unit Tests
*   `test_flicker_threshold.py`
*   `test_day_night_logic.py`

## Definition of Done
Successfully identifies damaged lights at night without false positives during the day, wrapped in an isolated module with 100% test coverage.

## Integration Notes
Do not modify `core/contracts/schemas.py`. Simply import `DetectionStream` and map its output to your logic.
