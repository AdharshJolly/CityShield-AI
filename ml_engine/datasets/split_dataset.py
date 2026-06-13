import os
import shutil
import random
import json
from pathlib import Path
from collections import defaultdict

def get_rarest_class(label_path: Path, class_counts: dict):
    if not label_path.exists():
        return -1
    classes_in_img = set()
    with open(label_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if parts:
                classes_in_img.add(int(parts[0]))
    if not classes_in_img:
        return -1
    # Return the class that is rarest globally (or locally approximated)
    return min(classes_in_img, key=lambda c: class_counts.get(c, float('inf')))

def stratified_split(interim_dir: Path, processed_dir: Path, train_ratio=0.7, val_ratio=0.2, seed=42):
    print(f"--- Stratified Splitting Dataset (Seed {seed}) ---")
    random.seed(seed)
    
    images_dir = interim_dir / "images"
    labels_dir = interim_dir / "labels"
    
    # 1. Count global classes to identify rarity
    global_counts = defaultdict(int)
    for lbl_path in labels_dir.glob("*.txt"):
        with open(lbl_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    global_counts[int(parts[0])] += 1

    # 2. Assign each image to a bucket based on its rarest class
    buckets = defaultdict(list)
    for img_path in images_dir.glob("*.jpg"):
        lbl_path = labels_dir / (img_path.stem + ".txt")
        rarest = get_rarest_class(lbl_path, global_counts)
        if rarest != -1:
            buckets[rarest].append(img_path)

    # 3. Split each bucket to maintain distribution
    splits = {"train": [], "val": [], "test": []}
    
    for c_id, files in buckets.items():
        random.shuffle(files)
        total = len(files)
        train_end = int(total * train_ratio)
        val_end = train_end + int(total * val_ratio)
        
        splits["train"].extend(files[:train_end])
        splits["val"].extend(files[train_end:val_end])
        splits["test"].extend(files[val_end:])

    # 4. Copy files
    for split_name, files in splits.items():
        split_img_dir = processed_dir / split_name / "images"
        split_lbl_dir = processed_dir / split_name / "labels"
        split_img_dir.mkdir(parents=True, exist_ok=True)
        split_lbl_dir.mkdir(parents=True, exist_ok=True)
        
        for img_path in files:
            lbl_path = labels_dir / (img_path.stem + ".txt")
            shutil.copy2(img_path, split_img_dir / img_path.name)
            shutil.copy2(lbl_path, split_lbl_dir / lbl_path.name)
            
    # 5. Generate Verification Report
    report = {
        "strategy": "rarest-class stratification",
        "seed": seed,
        "counts": {
            "train": len(splits["train"]),
            "val": len(splits["val"]),
            "test": len(splits["test"])
        }
    }
    report_path = processed_dir / "split_verification_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
                
    print(f"Stratified Split Complete. Train: {len(splits['train'])}, Val: {len(splits['val'])}, Test: {len(splits['test'])}.")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    stratified_split(BASE_DIR / "data/interim", BASE_DIR / "data/processed/cityshield_v1")
