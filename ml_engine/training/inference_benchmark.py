import time
import torch
import cv2
import argparse
from pathlib import Path
from ml_engine.training.experiment_tracker import ExperimentTracker
from ultralytics import YOLO

def benchmark_inference(exp_id: str, dataset_version: str = "cityshield_v1"):
    print(f"--- Running Inference Benchmark for {exp_id} ---")
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    tracker = ExperimentTracker(exp_id, BASE_DIR)
    
    weights_path = tracker.exp_dir / "weights" / "best.pt"
    if not weights_path.exists():
        print(f"Error: Weights file not found at {weights_path}")
        return
        
    model = YOLO(str(weights_path))
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    # 1. Sample images from test split instead of dummy tensors
    test_images_dir = BASE_DIR / "data/processed" / dataset_version / "test" / "images"
    if not test_images_dir.exists():
        print(f"Error: Test images directory not found at {test_images_dir}")
        return
        
    # Get first 50 test images
    image_paths = list(test_images_dir.glob("*.jpg"))[:50]
    if not image_paths:
        print("Error: No test images found for benchmarking.")
        return
        
    # Pre-load images to isolate inference latency from disk I/O
    images = [cv2.imread(str(img)) for img in image_paths]
    
    # 2. Warmup
    print("Warming up model...")
    for img in images[:10]:
        model(img, verbose=False)
        
    # 3. Benchmark
    print("Running realistic inference benchmark...")
    start = time.time()
    for img in images:
        model(img, verbose=False)
    end = time.time()
    
    latency_ms = ((end - start) / len(images)) * 1000.0
    fps = 1000.0 / latency_ms
    
    benchmark_data = {
        "hardware": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU",
        "num_samples": len(images),
        "latency_ms": round(latency_ms, 2),
        "fps": round(fps, 2),
        "target_met": latency_ms < 150.0
    }
    
    tracker.save_benchmark(benchmark_data)
    print(f"Benchmark Complete: {latency_ms:.1f}ms per frame ({fps:.1f} FPS). Target (<150ms) Met: {benchmark_data['target_met']}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=str, default="exp001")
    parser.add_argument("--version", type=str, default="cityshield_v1")
    args = parser.parse_args()
    
    benchmark_inference(args.exp, args.version)
