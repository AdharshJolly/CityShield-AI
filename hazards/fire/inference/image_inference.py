from ultralytics import YOLO

def infer_image(image_path, model_path="best.pt"):
    model = YOLO(model_path)
    results = model(image_path)
    return results

if __name__ == "__main__":
    pass
