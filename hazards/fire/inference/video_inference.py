from ultralytics import YOLO

def infer_video(video_path, model_path="best.pt"):
    model = YOLO(model_path)
    # Return generator
    return model(video_path, stream=True)

if __name__ == "__main__":
    pass
