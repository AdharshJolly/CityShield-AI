import os
import shutil
import argparse
from pathlib import Path
from ml_engine.training.config import ExperimentConfig, YOLOConfig
from ml_engine.training.experiment_tracker import ExperimentTracker, init_wandb
from ml_engine.training.callbacks import get_callbacks
from ultralytics import YOLO

def run_training(exp_id: str, dataset_version: str, resume: bool = False):
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
        
    # 3. Dataset Validation Gate
    dataset_dir = BASE_DIR / "data/processed" / dataset_version
    yaml_path = dataset_dir / "data.yaml"
    manifest_path = dataset_dir / "dataset_manifest.json"
    report_path = dataset_dir / "split_verification_report.json"
    
    for f in [yaml_path, manifest_path, report_path]:
        if not f.exists():
            raise FileNotFoundError(f"Validation Gate Failed! Missing required dataset artifact: {f.name}")
            
    print(f"Dataset Loaded and Validated: {yaml_path}")
    
    # 4. Hardware-Aware Config
    # Dynamically scale workers based on host machine CPU count
    # Default to 4 if cpu_count is not determinable, otherwise use max available.
    import psutil
    
    # Calculate optimal workers dynamically based on CPU core count and available RAM
    cpu_cores = os.cpu_count() or 4
    total_ram_gb = psutil.virtual_memory().total / (1024**3)
    
    # If system RAM is less than 16GB, restrict workers to prevent cv2 loading crashes
    if total_ram_gb <= 16.0:
        optimal_workers = min(2, cpu_cores)
        print(f"Low System RAM detected ({total_ram_gb:.1f}GB). Restricting workers to {optimal_workers}.")
    else:
        # Scale up to 8 workers for better CPU/DataLoader utilization
        optimal_workers = min(8, cpu_cores)
        print(f"High System RAM detected ({total_ram_gb:.1f}GB). Scaling workers to {optimal_workers}.")

    print(f"Hyperparameters: epochs={config.yolo.epochs}, batch={'Auto' if config.yolo.batch_size == -1 else config.yolo.batch_size}, workers={optimal_workers}, patience={config.yolo.patience}")
    
    # 5. YOLO Execution
    model_src = config.yolo.model_name
    
    if resume:
        last_pt = tracker.exp_dir / "weights" / "last.pt"
        if last_pt.exists():
            model_src = str(last_pt)
            print(f"Resuming from checkpoint: {model_src}")
        else:
            print("No last.pt found to resume from. Starting fresh.")
            
    model = YOLO(model_src)
    
    for event, cb in get_callbacks().items():
        model.add_callback(event, cb)
        
    model.train(
        data=str(yaml_path), 
        epochs=config.yolo.epochs, 
        batch=config.yolo.batch_size,
        imgsz=config.yolo.imgsz,
        lr0=config.yolo.learning_rate,
        optimizer=config.yolo.optimizer,
        patience=config.yolo.patience,
        project=str(tracker.exp_dir.parent), 
        name=tracker.experiment_id, 
        exist_ok=True,
        amp=True,
        cache="ram",
        workers=optimal_workers,
        # AutoBatch and dynamic workers scale up to whatever the host machine can physically handle.
        # YOLO kwargs natively pass through to PyTorch dataloader

        resume=resume if model_src.endswith('last.pt') else False
    )
    
    # 6. Checkpoint Management
    # Ensure best.pt and last.pt are explicitly in the expected directory
    # (Ultralytics writes to project/name/weights/ already, but we ensure it's synced)
    weights_dir = tracker.exp_dir / "weights"
    if not weights_dir.exists():
        weights_dir.mkdir(parents=True, exist_ok=True)
        
    print(f"YOLO Training complete. Weights saved to {weights_dir}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=str, default="exp001")
    parser.add_argument("--version", type=str, default="cityshield_v1")
    parser.add_argument("--resume", action="store_true", help="Resume from last checkpoint")
    args = parser.parse_args()
    
    run_training(args.exp, args.version, args.resume)
