import os
import cv2
import zipfile
import subprocess
from pathlib import Path

def setup_directories():
    base_dir = Path("../../../data/processed/accident_v1")
    for split in ["train", "valid", "test"]:
        os.makedirs(base_dir / split / "images", exist_ok=True)
        os.makedirs(base_dir / split / "labels", exist_ok=True)
    return base_dir

def download_datasets():
    print("Downloading Accident Datasets via Kaggle API...")
    # These are massive datasets (15GB+), so we run this in the background
    subprocess.run(["kaggle", "datasets", "download", "-d", "picekl/accident", "-p", "data/raw/accident"])
    subprocess.run(["kaggle", "datasets", "download", "-d", "siddhi17/road-crossing-dataset", "-p", "data/raw/road_crossing"])

def extract_frames(video_path, output_dir, frame_rate=1):
    print(f"Extracting frames from {video_path}...")
    cap = cv2.VideoCapture(str(video_path))
    count = 0
    fps = round(cap.get(cv2.CAP_PROP_FPS))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % (fps // frame_rate) == 0:
            cv2.imwrite(str(output_dir / f"{video_path.stem}_frame{count}.jpg"), frame)
            # Placeholder for YOLO annotation generation (would normally parse dataset labels here)
            with open(output_dir.parent / "labels" / f"{video_path.stem}_frame{count}.txt", "w") as f:
                f.write("0 0.5 0.5 0.5 0.5\n") # Dummy bbox for accident
        count += 1
    cap.release()

if __name__ == "__main__":
    print("Initializing Data Pipeline for Accident & Dark Spot Intelligence")
    out_dir = setup_directories()
    download_datasets() # Unleash the 15GB download
    print("Pipeline optimization complete. Ready for frame extraction.")
