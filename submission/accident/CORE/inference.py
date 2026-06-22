import argparse
import os
import cv2
import pandas as pd
from ultralytics import YOLO

def run_inference(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    model = YOLO("best.pt")
    
    predictions = []
    
    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)
        if not os.path.isfile(img_path): continue
        
        results = model.predict(img_path, conf=0.25, verbose=False)
        annotated = results[0].plot()
        cv2.imwrite(os.path.join(output_dir, img_name), annotated)
        
        # Parse for predictions.csv
        for box in results[0].boxes:
            x_c, y_c, w, h = box.xywhn[0].tolist()
            cls_id = int(box.cls[0].item())
            cls_name = model.names[cls_id]
            conf = box.conf[0].item()
            
            predictions.append({
                "frame": img_name,
                "class_id": cls_id,
                "class_name": cls_name,
                "x_center": round(x_c, 4),
                "y_center": round(y_c, 4),
                "width": round(w, 4),
                "height": round(h, 4),
                "confidence": round(conf, 4)
            })
            
    df = pd.DataFrame(predictions, columns=["frame", "class_id", "class_name", "x_center", "y_center", "width", "height", "confidence"])
    df.to_csv("predictions.csv", index=False)
    print("Inference complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run_inference(args.input, args.output)
