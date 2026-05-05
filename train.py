
from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data="data.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    name="road_damage",
    device=0,
    fliplr=0.5,
    flipud=0.1,
    degrees=15.0,
    mosaic=1.0,
    mixup=0.1,
    patience=30,
)
