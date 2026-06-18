from ultralytics import YOLO
import os

def train():
    model = YOLO("yolo11n.pt")

    results = model.train(
        data=os.path.abspath("hazards/collapse/data/dataset.yaml"),
        epochs=100,
        imgsz=640,
        batch=8,
        project="runs",
        name="collapse_v1",
        save=True,
        plots=True,
        device=0        # use GPU
    )

    print("Training complete!")
    print(f"Best weights saved to: runs/collapse_v1/weights/best.pt")

if __name__ == "__main__":
    train()