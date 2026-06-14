import argparse
from pathlib import Path
from ml_engine.training.experiment_tracker import ExperimentTracker
from ultralytics import YOLO

def run_evaluation(exp_id: str, dataset_version: str):
    print(f"--- Running Evaluation for {exp_id} ---")
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    tracker = ExperimentTracker(exp_id, BASE_DIR)
    
    yaml_path = BASE_DIR / "data/processed" / dataset_version / "data.yaml"
    weights_path = tracker.exp_dir / "weights" / "best.pt"
    
    if not weights_path.exists():
        print(f"Error: Weights file not found at {weights_path}")
        return
        
    # 1. YOLO Evaluation
    model = YOLO(str(weights_path))
    metrics_obj = model.val(
        data=str(yaml_path), 
        split="test", 
        project=str(tracker.exp_dir.parent), 
        name=f"{exp_id}_eval", 
        exist_ok=True
    )
    
    import torch
    
    # 2. Extract metrics
    metrics = {
        "mAP50": float(metrics_obj.box.map50),
        "mAP50-95": float(metrics_obj.box.map),
        "precision": float(metrics_obj.box.mp),
        "recall": float(metrics_obj.box.mr),
        "hardware": {
            "gpu_model": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "None",
            "cuda_version": torch.version.cuda if torch.cuda.is_available() else "None",
            "vram_gb": round(torch.cuda.get_device_properties(0).total_memory / (1024**3), 2) if torch.cuda.is_available() else 0.0
        }
    }
    
    # Try to load config to append training info
    config_path = tracker.exp_dir / "config.json"
    if config_path.exists():
        import json
        with open(config_path, "r") as f:
            cfg = json.load(f)
            yolo_cfg = cfg.get("yolo", {})
            metrics["training_params"] = {
                "effective_batch_size": yolo_cfg.get("batch_size"),
                "augmentation_mosaic": yolo_cfg.get("mosaic"),
                "optimizer": yolo_cfg.get("optimizer")
            }
    
    # 3. Save to tracker
    tracker.save_metrics(metrics)
    print(f"Evaluation Complete. Metrics: {metrics}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=str, default="exp001")
    parser.add_argument("--version", type=str, default="cityshield_v1")
    args = parser.parse_args()
    
    run_evaluation(args.exp, args.version)
