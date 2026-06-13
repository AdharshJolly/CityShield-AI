import argparse
from pathlib import Path
from config import ExperimentConfig, YOLOConfig
from experiment_tracker import ExperimentTracker, init_wandb
from callbacks import get_callbacks

def run_training(exp_id: str, dataset_version: str):
    print(f"--- Starting Training Run: {exp_id} ---")
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    
    # 1. Load Config
    config = ExperimentConfig(
        experiment_id=exp_id,
        yolo=YOLOConfig(dataset_version=dataset_version)
    )
    
    # 2. Setup Tracker
    tracker = ExperimentTracker(exp_id, BASE_DIR)
    tracker.save_config(config.model_dump())
    
    if config.track_wandb:
        init_wandb(config.model_dump())
        
    yaml_path = BASE_DIR / "data/processed" / dataset_version / "data.yaml"
    if not yaml_path.exists():
        raise FileNotFoundError(f"Dataset YAML not found: {yaml_path}")
        
    print(f"Dataset Loaded: {yaml_path}")
    print(f"Hyperparameters: epochs={config.yolo.epochs}, batch={config.yolo.batch_size}")
    
    # 3. YOLO Mock Execution
    # from ultralytics import YOLO
    # model = YOLO(config.yolo.model_name)
    # for event, cb in get_callbacks().items():
    #     model.add_callback(event, cb)
    # model.train(data=str(yaml_path), epochs=config.yolo.epochs, batch=config.yolo.batch_size)
    
    print("YOLO Training execution triggered (Mocked for architecture setup).")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=str, default="exp001")
    parser.add_argument("--version", type=str, default="cityshield_v1")
    args = parser.parse_args()
    
    run_training(args.exp, args.version)
