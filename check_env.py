import sys
import json
import torch
import ultralytics
import wandb

def generate_report():
    cuda_available = torch.cuda.is_available()
    device_count = torch.cuda.device_count() if cuda_available else 0
    gpu_name = torch.cuda.get_device_name(0) if cuda_available else "None"
    vram_bytes = torch.cuda.get_device_properties(0).total_memory if cuda_available else 0
    vram_gb = vram_bytes / (1024 ** 3)
    
    report = {
        "python_version": sys.version,
        "pytorch_version": torch.__version__,
        "cuda_available": cuda_available,
        "cuda_version": torch.version.cuda if cuda_available else "None",
        "gpu_model": gpu_name,
        "available_vram_gb": round(vram_gb, 2),
        "ultralytics_version": ultralytics.__version__,
        "wandb_version": wandb.__version__
    }
    
    with open("environment_report.json", "w") as f:
        json.dump(report, f, indent=2)
        
    print(f"Generated environment_report.json. GPU: {gpu_name} ({round(vram_gb, 2)} GB)")

if __name__ == "__main__":
    generate_report()
