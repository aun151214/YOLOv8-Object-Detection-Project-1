# 🚀 YOLOv8 Object Detection Project (OpenImages Subset)

This project demonstrates how to build an end-to-end **Object Detection pipeline with YOLOv8**, using a curated subset of the **OpenImages V6** dataset.  
We go from dataset preparation → training → evaluation → inference → documentation, in a fully reproducible way.

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
│ └── predictions/ # Example predictions for README
│ ├── 3.jpg
│ └── 4.jpg
│
│── notebooks/
│ └── yolov8_colab_train.ipynb # Google Colab notebook (10 epochs)
│
│── README.md
│── requirements.txt
│── .gitignore


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

1. CPU Run (50 Epochs)

Model: yolov8n

Epochs: 50

Results: [Release: CPU 50 Epochs](https://github.com/aun151214/YOLOv8-Object-Detection-Project-1/releases/tag/v1.0.0)

2. Google Colab Run (10 Epochs, GPU)

Model: yolov8n

Epochs: 10 (Colab free GPU)

Results: [Release: Colab 10 Epochs](https://github.com/aun151214/YOLOv8-Object-Detection-Project-1/releases/tag/colab-10ep)

Command used:

yolo detect train model=yolov8n.pt data=configs/data.yaml imgsz=320 epochs=50 batch=16 name=oi_yolov

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

yolo detect predict model=runs/detect/oi_yolov8n/weights/best.pt source=samples/test_images/ save=True

Predicted images are saved automatically under:

runs/detect/predict/


Example:
If you put images in samples/test_images/, the results will appear in runs/detect/predict/.

📦 Pretrained Weights & Outputs

To avoid bloating the repo, we host model weights and results as a GitHub Release:

🏋️ Best model weights: Download best.pt and last.pt below
[best.zip](https://github.com/user-attachments/files/22014412/best.zip)
[last.zip](https://github.com/user-attachments/files/22014414/last.zip)
📉 Training curves: Download results.png below
[Results](https://github.com/user-attachments/assets/af93cfb5-92df-4e2c-b377-5d096a95aa51)

⚡ How to Reproduce

Clone this repo:

git clone https://github.com/aun151214/YOLOv8-Object-Detection-Project-1.git
cd YOLOv8-Object-Detection-Project-1


Create a virtual environment:

python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Prepare dataset:

python src/prepare_openimages.py


Train or run inference 🚀

🔮 Future Work & Lessons Learned

This project successfully demonstrated a full end-to-end pipeline for training YOLOv8 on a curated subset of OpenImages V6.
However, there are many ways this work can be extended:

✅ Lessons Learned

Training large models on CPU is very slow → Colab GPU is a better option.

Data preparation is just as important as training — fixing labels, cleaning splits, and exporting in YOLO format took significant effort.

Small models (YOLOv8-nano) train fast but may struggle with rare classes (e.g., Bicycle, Motorcycle).

🚀 Future Work

Train Larger Models

Run YOLOv8-s/m/l/x on Colab or Kaggle GPUs.

Compare accuracy vs. training time.

Hyperparameter Tuning

Experiment with different learning rates, augmentations, and image sizes.

Extend Dataset

Add more OpenImages samples or move to a domain-specific dataset (e.g., industrial defect detection).

Deployment

Convert model to ONNX / TensorRT for faster inference.

Deploy a demo app with Gradio or Streamlit.

Hugging Face Demo (Optional)

Host the model on Hugging Face Spaces so anyone can try it online without setup.

✍️ Maintained by Aun Ali
