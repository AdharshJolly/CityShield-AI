from pydantic import BaseModel
from typing import Optional

class YOLOConfig(BaseModel):
    model_name: str = "yolo11n.pt"  # Nano model to fit in 4GB VRAM
    dataset_version: str = "cityshield_v1"
    epochs: int = 20
    batch_size: int = -1  # -1 uses AutoBatch to fully utilize available VRAM
    imgsz: int = 640
    learning_rate: float = 0.001
    optimizer: str = "AdamW"
    patience: int = 10  # Early stopping
    
    # Augmentations (to be overridden by dataset_manifest recommendations if needed)
    mosaic: float = 1.0
    mixup: float = 0.1
    focal_loss_gamma: float = 1.5

class ExperimentConfig(BaseModel):
    experiment_id: str
    yolo: YOLOConfig
    tags: list[str] = ["baseline", "yolo11n"]
    track_wandb: bool = False
