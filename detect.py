
from ultralytics import YOLO
import cv2
import os

model = YOLO("weights/best.pt")
class_names = ["pothole", "crack", "manhole"]

def detect(image_path):
    results = model(image_path, conf=0.25)
    boxes = results[0].boxes
    
    print(f"Total damages: {len(boxes)}")
    for box in boxes:
        cls = class_names[int(box.cls)]
        conf = float(box.conf)
        x1,y1,x2,y2 = map(int, box.xyxy[0])
        area = (x2-x1)*(y2-y1)
        severity = "HIGH" if area > 50000 else "MEDIUM" if area > 20000 else "LOW"
        print(f"  → {cls} | conf: {conf:.2f} | severity: {severity}")
