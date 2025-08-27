# src/prepare_openimages.py
import os
import shutil
import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import types as fot

# A small, CPU-friendly subset (you can raise later)
CLASSES = ["Person", "Car", "Bicycle", "Motorcycle", "Traffic light", "Stop sign"]
MAX_TRAIN = 800   # images total in train split
MAX_VAL   = 200   # images total in val split

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(ROOT)
OUT_DIR = os.path.join(PROJ, "data", "openimages_yolo")

# Clean previous export to avoid merge confusion
if os.path.isdir(OUT_DIR):
    print(f"🧹 Removing previous export at: {OUT_DIR}")
    shutil.rmtree(OUT_DIR)
os.makedirs(OUT_DIR, exist_ok=True)

# Download/load Open Images via the Zoo
print("➡️ Downloading Open Images (train subset)…")
train_ds = foz.load_zoo_dataset(
    "open-images-v6",
    split="train",
    label_types=["detections"],
    classes=CLASSES,
    max_samples=MAX_TRAIN,
    # IMPORTANT: put labels into this field
    label_field="ground_truth",
)

print("➡️ Downloading Open Images (validation subset)…")
val_ds = foz.load_zoo_dataset(
    "open-images-v6",
    split="validation",
    label_types=["detections"],
    classes=CLASSES,
    max_samples=MAX_VAL,
    label_field="ground_truth",
)

# Sanity: ensure the label field exists
for name, ds in [("train", train_ds), ("val", val_ds)]:
    if not ds.has_sample_field("ground_truth"):
        print(f"❌ '{name}' dataset has no 'ground_truth' field. Fields: {list(ds.get_field_schema().keys())}")
        raise SystemExit(1)

# Export to YOLO format (YOLOv5/YOLOv8 share the same dataset format)
print("➡️ Exporting YOLO dataset (train)…")
train_ds.export(
    export_dir=OUT_DIR,
    dataset_type=fot.YOLOv5Dataset,
    label_field="ground_truth",
    classes=CLASSES,
    split="train",
)

print("➡️ Exporting YOLO dataset (val)…")
val_ds.export(
    export_dir=OUT_DIR,
    dataset_type=fot.YOLOv5Dataset,
    label_field="ground_truth",
    classes=CLASSES,
    split="val",
)

# Write data.yaml that YOLOv8 expects
yolo_path = OUT_DIR.replace("\\", "/")  # avoid backslash issues
yaml_text = (
    "# configs/data.yaml\n"
    f"path: {yolo_path}\n"
    "train: images/train\n"
    "val: images/val\n\n"
    f"nc: {len(CLASSES)}\n"
    f"names: {CLASSES}\n"
)

cfg_dir = os.path.join(PROJ, "configs")
os.makedirs(cfg_dir, exist_ok=True)
with open(os.path.join(cfg_dir, "data.yaml"), "w", encoding="utf-8") as f:
    f.write(yaml_text)

print("✅ Done. YOLO dataset at:", OUT_DIR)
print("📄 Config written to: configs/data.yaml")
