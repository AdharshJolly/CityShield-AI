import os
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = BASE_DIR / "core" / "config"

def load_yaml(filename: str) -> dict:
    with open(CONFIG_DIR / filename, "r") as f:
        return yaml.safe_load(f)

# Expose global settings
CLASSES = load_yaml("classes.yaml")["classes"]
THRESHOLDS = load_yaml("thresholds.yaml")
RISK_WEIGHTS = load_yaml("risk_weights.yaml")

# Environment / API Settings
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/cityshield")
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY", "")
KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME", "")
KAGGLE_KEY = os.getenv("KAGGLE_KEY", "")
