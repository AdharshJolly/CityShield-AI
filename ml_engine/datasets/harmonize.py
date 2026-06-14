import os
import shutil
import sys
from pathlib import Path
from ml_engine.datasets.taxonomy import CITYSHIELD_CLASSES

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from core.config.settings import DATASET_MAPPINGS

CLASS_MAPPINGS = {}
for ds_name, mapping in DATASET_MAPPINGS.get("dataset_mappings", {}).items():
    CLASS_MAPPINGS[ds_name] = {}
    for old_id, class_name in mapping.items():
        if class_name in CITYSHIELD_CLASSES:
            CLASS_MAPPINGS[ds_name][old_id] = CITYSHIELD_CLASSES.index(class_name)

MAX_SAMPLES_PER_CLASS = {}
for cls_name, count in DATASET_MAPPINGS.get("max_samples", {}).items():
    if cls_name in CITYSHIELD_CLASSES:
        MAX_SAMPLES_PER_CLASS[CITYSHIELD_CLASSES.index(cls_name)] = count

def load_source_yaml(dataset_path: Path):
    pass # Implementation omitted for MVP

def remap_label_file(source_file: Path, dest_file: Path, class_map: dict, class_counts: dict):
    with open(source_file, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        parts = line.strip().split()
        if not parts: continue
        
        old_class_id = int(parts[0])
        if old_class_id in class_map:
            new_class_id = class_map[old_class_id]
            
            # Capping logic
            if new_class_id in MAX_SAMPLES_PER_CLASS:
                if class_counts.get(new_class_id, 0) >= MAX_SAMPLES_PER_CLASS[new_class_id]:
                    continue
            
            class_counts[new_class_id] = class_counts.get(new_class_id, 0) + 1
            new_parts = [str(new_class_id)] + parts[1:]
            new_lines.append(" ".join(new_parts))
            
    if new_lines:
        with open(dest_file, 'w') as f:
            f.write("\n".join(new_lines) + "\n")
        return True
    return False

def merge_into_interim(raw_dir: Path, interim_dir: Path):
    print("--- Starting Dataset Harmonization ---")
    interim_images = interim_dir / "images"
    interim_labels = interim_dir / "labels"
    interim_images.mkdir(parents=True, exist_ok=True)
    interim_labels.mkdir(parents=True, exist_ok=True)
    
    global_class_counts = {}

    for dataset_name, mapping in CLASS_MAPPINGS.items():
        print(f"Processing {dataset_name}...")
        ds_path = raw_dir / dataset_name / "train"
        if not ds_path.exists():
            continue
            
        labels_dir = ds_path / "labels"
        images_dir = ds_path / "images"
        
        for label_file in labels_dir.glob("*.txt"):
            img_file = images_dir / (label_file.stem + ".jpg")
            if not img_file.exists():
                continue
                
            prefix = dataset_name.split("-")[0]
            new_label_name = f"{prefix}_{label_file.name}"
            new_img_name = f"{prefix}_{img_file.name}"
            
            dest_label = interim_labels / new_label_name
            dest_img = interim_images / new_img_name
            
            if remap_label_file(label_file, dest_label, mapping, global_class_counts):
                shutil.copy2(img_file, dest_img)
                
    print("Harmonization Complete.")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    merge_into_interim(BASE_DIR / "data/raw", BASE_DIR / "data/interim")
