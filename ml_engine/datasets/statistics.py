import os
import json
from datetime import datetime
from pathlib import Path
from ml_engine.datasets.taxonomy import CITYSHIELD_CLASSES

def generate_statistics(processed_dir: Path, version_name: str):
    print("--- Generating Statistics & Manifest ---")
    
    import hashlib
    tax_string = ",".join(CITYSHIELD_CLASSES)
    tax_hash = hashlib.sha256(tax_string.encode('utf-8')).hexdigest()
    
    manifest = {
        "dataset_version": version_name,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "taxonomy_hash": tax_hash,
        "class_counts": {cls: 0 for cls in CITYSHIELD_CLASSES},
        "source_datasets": {},
        "split_counts": {
            "train_images": 0,
            "val_images": 0,
            "test_images": 0
        },
        "augmentation_recommendations": {}
    }
    
    # Calculate splits
    for split in ["train", "val", "test"]:
        split_dir = processed_dir / split / "images"
        if split_dir.exists():
            manifest["split_counts"][f"{split}_images"] = len(list(split_dir.glob("*.jpg")))
            
            # Count classes in this split
            lbl_dir = processed_dir / split / "labels"
            for lbl_file in lbl_dir.glob("*.txt"):
                with open(lbl_file, 'r') as f:
                    for line in f:
                        parts = line.strip().split()
                        if parts:
                            c_id = int(parts[0])
                            if 0 <= c_id < len(CITYSHIELD_CLASSES):
                                manifest["class_counts"][CITYSHIELD_CLASSES[c_id]] += 1
                                
    # Determine Augmentation Recommendations
    max_count = max(manifest["class_counts"].values()) if any(manifest["class_counts"].values()) else 1
    min_count = min([c for c in manifest["class_counts"].values() if c > 0], default=1)
    
    if max_count / min_count > 3:
        manifest["augmentation_recommendations"]["mosaic"] = 1.0
        manifest["augmentation_recommendations"]["focal_loss_gamma"] = 1.5
        manifest["augmentation_recommendations"]["note"] = "High class imbalance detected. Strong augmentations and Focal Loss recommended."
    else:
        manifest["augmentation_recommendations"]["note"] = "Dataset is relatively balanced."
        
    manifest_path = processed_dir / "dataset_manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
        
    print(f"Manifest generated at {manifest_path}")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    generate_statistics(BASE_DIR / "data/processed/cityshield_v1", "cityshield_v1")
