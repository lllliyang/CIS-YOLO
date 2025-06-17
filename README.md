# CIS-YOLO

This repository contains the improved YOLO-based object detection framework **CIS‑YOLO**, specifically tailored for detecting rubber tree planting pits from UAV imagery.

## 📁 Project Structure

CIS-YOLO/
├── data/
│ ├── images/
│ │ └── test/
│ └── labels/
│ └── test/
├── ultralytics/
│ └── nn/
│ └── Addmodule/ # Custom modules (e.g., DDF, iEMA)
├── CIS-YOLO.pt # Trained model weights (our improved model)
├── YOLOv11N.pt # Baseline YOLOv11N model weights
├── test.py # Script to run inference and evaluation
└── README.md # Project description

markdown
Copy
Edit

## 🚀 How to Use

1. **Install dependencies**:

```bash
pip install -r requirements.txt
Run the test script:

bash
Copy
Edit
python test.py
This script will run object detection on test images from data/images/test/ using both CIS-YOLO.pt and YOLOv11N.pt models and compare the outputs.

🔧 Model Details
CIS-YOLO.pt: Trained model with custom modules integrated into Ultralytics YOLO, including:

C3k2_DDF (efficient multi-scale feature extraction)

iEMA (improved attention for weak/blurred targets)

SCDown (lightweight downsampling)

YOLOv11N.pt: Baseline model used for comparison.

🧪 Dataset Format
Images: data/images/test/*.png

Labels: data/labels/test/*.txt in YOLO format

Each image has a corresponding label file with bounding box annotations.

📦 Notes
The ultralytics/nn/Addmodule directory contains your custom modules. They are integrated into tasks.py and automatically loaded during model construction.


📜 License
This project is for academic and research use only.
