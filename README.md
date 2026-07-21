# 📝 Entity Region Grounding Annotation using EasyOCR

Automatically generate **entity grounding annotations** from images using **EasyOCR**. This project detects text in images, filters noisy OCR results, selects the most relevant text region, and exports annotations in **JSONL** format for building OCR, Vision-Language, and Entity Grounding datasets.

---

## 📌 Overview

This project processes a collection of images and performs the following steps:

- Detects text using **EasyOCR**
- Extracts bounding boxes for each detected text region
- Filters low-confidence and invalid OCR results
- Selects the most prominent text entity
- Saves annotations in **JSONL** format

The generated dataset can be used for:

- Entity Region Grounding
- OCR Dataset Generation
- Vision-Language Model Fine-tuning
- Scene Text Recognition
- Document Intelligence
- Signboard and Logo Detection

---

## 🚀 Features

- ✅ Automatic text detection using EasyOCR
- ✅ Supports JPG, JPEG, PNG and WEBP images
- ✅ Confidence-based OCR filtering
- ✅ Removes noisy or invalid text detections
- ✅ Selects the largest and most confident text region
- ✅ Generates JSONL annotations
- ✅ Progress bar using tqdm
- ✅ Error handling for corrupted images

---

## 📂 Project Structure

```
Entity-Grounding/
│
├── downloaded_images/
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
│
├── process_signs.py
├── pilot_annotations.jsonl
├── requirements.txt
└── README.md
```
## 🔄 Processing Pipeline

```text
Dataset
   │
   ▼
Load Image
   │
   ▼
EasyOCR Detection
   │
   ▼
Extract Text + Bounding Box
   │
   ▼
Confidence Filtering
   │
   ▼
Rank Candidates
   │
   ▼
Choose Best Entity
   │
   ▼
Generate JSONL Annotation
```
---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/entity-region-grounding.git
cd entity-region-grounding
```

Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually

```bash
pip install easyocr
pip install opencv-python
pip install tqdm
```

---

 ▶️ Usage

Place all images inside

```
downloaded_images/
```

Run the script

```bash
python process_signs.py
```

After processing completes, the annotations will be saved as

```
pilot_annotations.jsonl
```

---

 📄 Output Format

Each image generates one JSON object.

Example:

<img width="4032" height="3024" alt="cave" src="https://github.com/user-attachments/assets/0cbf695e-c0c8-44f9-9ab0-a98f92afcbe9" />


```json
{
    "id": "image0000",
    "task": "entity_region_grounding",
    "AKKANNA MADANNA CAVES", "bbox":
[[1539, 1155], [3050, 1155], [3050, 1290], [1539, 1290]],
 "confidence": 0.9985}
```

 Fields

| Field | Description |
|--------|-------------|
| id | Image filename without extension |
| task | Entity grounding task name |
| entity_name | Detected text entity |
| bbox | Bounding box coordinates |
| confidence | OCR confidence score |

---

## 🖼️ Supported Image Formats

- JPG
- JPEG
- PNG
- WEBP

---

 ⚙️ OCR Filtering

The script automatically removes

- Low confidence detections
- Numeric-only text
- Very short text
- Invalid OCR predictions

This improves annotation quality for training datasets.

---

 📚 Dependencies

- Python 3.9+
- EasyOCR
- OpenCV
- tqdm
- NumPy
- PyTorch

---

 🎯 Applications

This project can be used for

- OCR Dataset Generation
- Entity Region Grounding
- Vision-Language Model Training
- Signboard Detection
- Logo Text Detection
- Scene Text Recognition

---

 📈 Future Improvements

- Support multiple entities per image
- Merge nearby OCR words into complete phrases
- Parallel image processing
- Automatic visualization of bounding boxes
- PaddleOCR integration
- Batch inference optimization
- Annotation quality scoring

---

 🤝 Contributing

Contributions are welcome.

Feel free to fork this repository, create a new branch, and submit a pull request for improvements or bug fixes.

---

 
 ⭐ Acknowledgements

- EasyOCR
- PyTorch
- OpenCV
- tqdm

If you find this project useful, consider giving the repository a ⭐ on GitHub.
