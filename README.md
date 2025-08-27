# 🚀 YOLOv8 Object Detection on OpenImages

This project implements **YOLOv8** for object detection using a subset of the [OpenImages V6 dataset](https://storage.googleapis.com/openimages/web/index.html).  
The goal is to build an end-to-end pipeline: dataset preparation → training → validation → inference → results visualization.

---

## 📂 Project Structure

YOLOv8-Object-Detection-Project-1/
│── configs/
│ └── data.yaml # YOLO dataset config
│
│── data/
│ └── openimages_yolo/ # Exported YOLO dataset
│
│── runs/ # Training + inference outputs
│ └── detect/
│ └── oi_yolov8n/ # 50-epoch training run
│ ├── results.png # Training curves
│ ├── results.csv
│ └── weights/
│ ├── best.pt
│ └── last.pt
│
│── samples/
│ └── test_images/ # Example images for inference
│
│── src/
│ └── prepare_openimages.py # Script to download & prep dataset
│
│── requirements.txt # Dependencies
│── README.md # This file
│── .gitignore


---

## 📊 Training Results

Model trained for **50 epochs** on YOLOv8n.  

**Training curve:**
![Training Results](runs/detect/oi_yolov8n/results.png)

**Validation Metrics (on 200 images):**
| Metric | Value |
|--------|-------|
| Precision | ~0.69 |
| Recall    | ~0.22 |
| mAP@0.5   | ~0.20 |
| mAP@0.5:0.95 | ~0.14 |

---

## 🔍 Inference Examples

Example detections on custom test images:  
(saved in `runs/detect/predict/`)

<p align="center">
  <img src="runs/detect/predict/example1.jpg" width="45%">
  <img src="runs/detect/predict/example2.jpg" width="45%">
</p>

---

## ⚙️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt


2️⃣ Prepare dataset
python src/prepare_openimages.py

3️⃣ Train
yolo detect train model=yolov8n.pt data=configs/data.yaml epochs=50 imgsz=320 batch=8 name=oi_yolov8n

4️⃣ Validate
yolo detect val model=runs/detect/oi_yolov8n/weights/best.pt data=configs/data.yaml imgsz=320 batch=8

5️⃣ Predict on new images
yolo detect predict model=runs/detect/oi_yolov8n/weights/best.pt source=samples/test_images/ save=True
