import os
import sys
from pathlib import Path

# Ensure core configuration can be loaded
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from core.config.settings import CLASSES

CITYSHIELD_CLASSES = [
    CLASSES[i]
    for i in range(len(CLASSES))
]
