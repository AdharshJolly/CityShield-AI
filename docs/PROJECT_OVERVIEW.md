# PROJECT OVERVIEW
## Core Architecture
CityShield has abandoned the monolithic shared-processing architecture. The repository is now fundamentally structured as a collection of fully independent, hazard-specific computer vision models.

## Independent Modules
1. Fire Detection
2. Streetlight Detection
3. Animal Detection
4. Accident Detection
5. Collapse Detection

Each module is 100% self-contained and must be independently trainable, testable, and deployable.
