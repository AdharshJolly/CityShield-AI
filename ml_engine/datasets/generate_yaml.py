import os
import yaml
from pathlib import Path
from taxonomy import CITYSHIELD_CLASSES

def create_yaml(processed_dir: Path):
    print("--- Generating data.yaml ---")
    data_dict = {
        "train": str((processed_dir / "train" / "images").resolve()),
        "val": str((processed_dir / "val" / "images").resolve()),
        "test": str((processed_dir / "test" / "images").resolve()),
        "nc": len(CITYSHIELD_CLASSES),
        "names": CITYSHIELD_CLASSES
    }
    
    yaml_path = processed_dir / "data.yaml"
    with open(yaml_path, 'w') as f:
        yaml.dump(data_dict, f, sort_keys=False)
        
    print(f"data.yaml generated at {yaml_path}")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    create_yaml(BASE_DIR / "data/processed/cityshield_v1")
