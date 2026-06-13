from pydantic import BaseModel
from typing import Optional

class YOLOConfig(BaseModel):
    model_name: str = "yolov12-l.pt"
    dataset_version: str = "cityshield_v1"
    epochs: int = 100
    batch_size: int = 16
    imgsz: int = 640
    learning_rate: float = 0.001
    optimizer: str = "AdamW"
    
    # Augmentations (to be overridden by dataset_manifest recommendations if needed)
    mosaic: float = 1.0
    mixup: float = 0.1
    focal_loss_gamma: float = 1.5

class ExperimentConfig(BaseModel):
    experiment_id: str
    yolo: YOLOConfig
    tags: list[str] = ["baseline", "yolov12"]
    track_wandb: bool = False
