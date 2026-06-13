import os
import cv2
from pathlib import Path

def verify_image_integrity(image_path: Path):
    try:
        img = cv2.imread(str(image_path))
        if img is None: return False
        return True
    except:
        return False

def check_bbox_bounds(label_path: Path):
    with open(label_path, 'r') as f:
        lines = f.readlines()
        
    valid_lines = []
    for line in lines:
        parts = line.strip().split()
        if not parts: continue
        
        coords = [float(x) for x in parts[1:5]]
        if any(c < 0.0 or c > 1.0 for c in coords):
            continue # Drop invalid box
        valid_lines.append(line.strip())
        
    if len(valid_lines) != len(lines):
        if not valid_lines:
            return False # No valid boxes left
        with open(label_path, 'w') as f:
            f.write("\n".join(valid_lines) + "\n")
    return True

def prune_orphans_and_validate(interim_dir: Path):
    print("--- Starting Validation ---")
    interim_images = interim_dir / "images"
    interim_labels = interim_dir / "labels"
    
    orphans = 0
    corrupted = 0
    invalid_bboxes = 0
    
    for img_file in interim_images.glob("*.jpg"):
        label_file = interim_labels / (img_file.stem + ".txt")
        
        if not label_file.exists():
            img_file.unlink()
            orphans += 1
            continue
            
        if not verify_image_integrity(img_file):
            img_file.unlink()
            label_file.unlink()
            corrupted += 1
            continue
            
        if not check_bbox_bounds(label_file):
            img_file.unlink()
            label_file.unlink()
            invalid_bboxes += 1
            continue
            
    print(f"Validation Complete. Orhpans removed: {orphans}. Corrupted: {corrupted}. Invalid BBoxes fixed/removed: {invalid_bboxes}.")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    prune_orphans_and_validate(BASE_DIR / "data/interim")
