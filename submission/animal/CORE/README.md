# Animal Intelligence Module

## 1. Approach
We utilize edge-optimized YOLO11n object detection.

## 2. Model Architecture
- **Base model:** YOLO11n
- **Classes:** stray_animal, wildlife
- **Input Image Size:** 640x640

## 3. Training Details
- **Framework:** PyTorch & Ultralytics
- **Base weights:** yolov11n.pt

## 4. Environment Setup
`pip install -r requirements.txt`

## 5. How to Run Inference
Run from the `CORE` directory:
`python inference.py --input ../DATA/test_images/input_frames --output ../DATA/test_images/output_frames`

## 6. Known Issues / Limitations
Requires adequate lighting.
