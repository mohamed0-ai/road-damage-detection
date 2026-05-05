
# 🚧 Road Damage Detection System

A YOLOv8-based object detection system that detects and classifies road damage.

## Classes
-  Pothole
-  Crack  
-  Manhole

## Results
| Experiment | Model | Epochs | mAP50 |
|---|---|---|---|
| Exp1 | YOLOv8n | 20 | 0.27 |
| Exp2 | YOLOv8s | 100 | TBD |

## How to Run
```bash
pip install ultralytics
python train.py
python detect.py
```
