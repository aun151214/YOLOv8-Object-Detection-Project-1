# 🚀 YOLOv8 Object Detection Project (OpenImages Subset)

This project demonstrates how to build an **end-to-end Object Detection pipeline with YOLOv8**, using a curated subset of the **OpenImages V6 dataset**.  
The idea is to showcase real, practical deep learning work — dataset prep, training, evaluation, inference, and documentation — in a way that’s easy to reproduce.

---

## 📂 Project Structure

YOLOv8-Object-Detection-Project-1/
│── configs/
│ └── data.yaml # YOLO dataset config
│
│── data/
│ └── openimages_yolo/ # Exported YOLO dataset (generated automatically)
│
│── src/
│ └── prepare_openimages.py # Script to download & prepare dataset
│
│── samples/
│ └── test_images/ # Custom images for inference
│
│── README.md
│── requirements.txt
│── .gitignore

markdown
Copy code

---

## 📊 Dataset

- **Source**: [OpenImages V6](https://storage.googleapis.com/openimages/web/index.html)  
- **Classes chosen**:  
  - Person, Car, Bicycle, Motorcycle, Traffic light, Stop sign
- **Samples**:  
  - 800 training images  
  - 200 validation images  

Everything is prepared with one command:

```bash
python src/prepare_openimages.py
🏋️ Training
We trained the YOLOv8-nano model (yolov8n) for 50 epochs.
The smaller model was chosen for speed since we trained on CPU/Colab.

Command used:

bash
Copy code
yolo detect train model=yolov8n.pt data=configs/data.yaml imgsz=320 epochs=50 batch=16 name=oi_yolov8n
📈 Results
Performance on validation set (200 images, 504 objects):

Class	Precision	Recall	mAP50	mAP50-95
Person	0.24	0.21	0.10	0.05
Car	0.53	0.70	0.67	0.49
Bicycle	1.00	0.00	0.01	0.01
Motorcycle	1.00	0.00	0.03	0.02
Overall	0.69	0.23	0.20	0.14

Training curves:


🔮 Inference
Run inference on your own images:

bash
Copy code
yolo detect predict model=runs/detect/oi_yolov8n/weights/best.pt source=samples/test_images/ save=True
Predicted images are saved automatically under:

bash
Copy code
runs/detect/predict/
Example:
If you put images in samples/test_images/, the results will appear in runs/detect/predict/.

📦 Pretrained Weights & Outputs
To avoid bloating the repo, we host model weights and results as a GitHub Release:

🏋️ Best model weights: Download best.pt

📉 Training curves: Download results.png

⚡ How to Reproduce
Clone this repo:

bash
Copy code
git clone https://github.com/aun151214/YOLOv8-Object-Detection-Project-1.git
cd YOLOv8-Object-Detection-Project-1
Create a virtual environment:

bash
Copy code
python -m venv .venv
.venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Prepare dataset:

bash
Copy code
python src/prepare_openimages.py
Train or run inference 🚀
