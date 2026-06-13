import os
import json
from pathlib import Path
from datetime import datetime

class ExperimentTracker:
    def __init__(self, experiment_id: str, base_dir: Path):
        self.experiment_id = experiment_id
        self.exp_dir = base_dir / "experiments" / experiment_id
        self.exp_dir.mkdir(parents=True, exist_ok=True)
        
    def save_config(self, config_dict: dict):
        with open(self.exp_dir / "config.json", "w") as f:
            json.dump(config_dict, f, indent=2)
            
    def save_metrics(self, metrics: dict):
        with open(self.exp_dir / "metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)
            
    def save_benchmark(self, benchmark_data: dict):
        with open(self.exp_dir / "benchmark.json", "w") as f:
            json.dump(benchmark_data, f, indent=2)
            
    def get_weights_dir(self):
        w_dir = self.exp_dir / "weights"
        w_dir.mkdir(exist_ok=True)
        return w_dir

# Simple WandB wrapper for later integration
def init_wandb(config: dict, project="CityShield_AI"):
    # import wandb
    # wandb.init(project=project, name=config["experiment_id"], config=config["yolo"])
    print(f"W&B Integration stub for {config['experiment_id']}")
