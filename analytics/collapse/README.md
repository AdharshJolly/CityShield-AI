# Collapse Intelligence (Workstream D)

## Objective
Identify severe infrastructure failures including collapsed buildings, fallen trees, and blocked roadways to dispatch emergency rescue teams.

## Inputs
Consumes the `DetectionStream` contract. Focuses on spatial mapping of custom trained classes and background heuristics.

## Outputs
Emits the `EventPayload` contract back to the centralized broker.

## Deliverables
*   Fallen tree detection heuristics.
*   Collapsed structure tracking.
*   Road obstruction intelligence.
*   Debris classification logic.
*   Hazard scoring calculation.

## Example Event Types
*   `infrastructure_collapse`
*   `road_obstruction`

## Required Unit Tests
*   `test_hazard_scoring.py`
*   `test_obstruction_mapping.py`

## Definition of Done
Successfully identifies and maps debris/collapse events with accurate, high-priority PSRI hazard scores attached to the `EventPayload`.

## Integration Notes
Rely heavily on the `risk_weights.yaml` configuration to determine PSRI (Project Specific Risk Index) severity modifiers.
