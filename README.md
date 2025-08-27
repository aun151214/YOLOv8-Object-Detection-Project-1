# 🚀 YOLOv8 Object Detection Project (Open Images)

This project implements **YOLOv8** for object detection using a subset of the **Open Images V6 dataset**.  
It is designed to demonstrate **real-world object detection** (people, vehicles, traffic signs) and to serve as a **portfolio-ready project** for applying to AI/ML jobs.  

---

## 📂 Project Structure

YOLOv8-Object-Detection-Project-1/
│── configs/
│ └── data.yaml # Dataset configuration
│
│── data/
│ └── openimages_yolo/ # Exported YOLO dataset
│ ├── images/
│ │ ├── train/
│ │ └── val/
│ └── labels/
│ ├── train/
│ └── val/
│
│── runs/
│ └── detect/
│ └── oi_yolov8n/ # Training results (50 epochs)
│ ├── results.png # Training curve
│ ├── results.csv # Metrics log
│ └── weights/
│ ├── best.pt # Best model weights
│ └── last.pt # Last epoch weights
│
│── samples/
│ └── test_images/ # Custom images for inference
│
│── src/
│ └── prepare_openimages.py # Script to download & prep dataset
│
│── .gitignore
│── requirements.txt
│── README.md

yaml
Copy code

---

## 📊 Training Results

![Training Results](runs/detect/oi_yolov8n/results.png)

- **mAP50-95**: ~0.14 (on validation set)  
- **Classes trained**: Person, Car, Bicycle, Motorcycle, Traffic light, Stop sign  
- Model: `YOLOv8n` (nano, lightweight, CPU-friendly)  
- Epochs: 50  

---

## 🏋️ Training

Train the model locally or on Google Colab:

```bash
yolo detect train model=yolov8n.pt data=configs/data.yaml epochs=50 imgsz=640 batch=16 name=oi_yolov8n
✅ Validation
Evaluate trained model on validation set:

bash
Copy code
yolo detect val model=runs/detect/oi_yolov8n/weights/best.pt data=configs/data.yaml imgsz=640
🔍 Inference
Run inference on custom images (placed inside samples/test_images/):

bash
Copy code
yolo detect predict model=runs/detect/oi_yolov8n/weights/best.pt source=samples/test_images/ save=True
Results will be saved to:

bash
Copy code
runs/detect/predict/
📥 Pretrained Weights
Download pretrained weights from the release section:

Download best.pt (zipped)

Download last.pt (zipped)

Unzip before using:

bash
Copy code
unzip best.pt.zip
⚙️ Setup
Clone repo:

bash
Copy code
git clone https://github.com/aun151214/YOLOv8-Object-Detection-Project-1.git
cd YOLOv8-Object-Detection-Project-1
Create & activate virtual env:

bash
Copy code
python -m venv .venv
.\.venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
