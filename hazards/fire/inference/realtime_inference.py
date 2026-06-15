from ultralytics import YOLO

def infer_realtime(model_path="best.pt"):
    model = YOLO(model_path)
    return model(source=0, stream=True, show=True)

if __name__ == "__main__":
    pass
