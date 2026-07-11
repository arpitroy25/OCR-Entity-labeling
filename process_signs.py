import easyocr
import json
from pathlib import Path
from tqdm import tqdm
import os

# ==========================================
# CONFIG
# ==========================================

IMAGE_DIR = Path(r"A:\entity and label\downloaded_images")
OUTPUT_FILE = Path(r"A:\entity and label\pilot_annotations.jsonl")

MIN_CONFIDENCE = 0.70
MIN_TEXT_LENGTH = 3

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def convert_bbox(bbox):
    return [[int(x), int(y)] for x, y in bbox]

def bbox_area(bbox):
    xs = [p[0] for p in bbox]
    ys = [p[1] for p in bbox]
    return (max(xs) - min(xs)) * (max(ys) - min(ys))

# ==========================================
# LOAD OCR
# ==========================================

print("Loading EasyOCR...")
reader = easyocr.Reader(['en'])
print("EasyOCR Loaded Successfully!")

# ==========================================
# FIND IMAGES
# ==========================================

images = []

for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
    images.extend(IMAGE_DIR.rglob(ext))

print(f"\nTotal Images Found: {len(images)}")
print(f"Saving output to:\n{OUTPUT_FILE.resolve()}\n")

# ==========================================
# PROCESS IMAGES
# ==========================================

records_written = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

    for image_path in tqdm(images):

        try:

            # DO NOT use paragraph=True
            results = reader.readtext(str(image_path))

            candidates = []

            for bbox, text, conf in results:

                text = text.strip()

                if conf < MIN_CONFIDENCE:
                    continue

                if len(text) < MIN_TEXT_LENGTH:
                    continue

                if not any(ch.isalpha() for ch in text):
                    continue

                candidates.append({
                    "entity_name": text,
                    "bbox": convert_bbox(bbox),
                    "confidence": round(float(conf), 4),
                    "area": bbox_area(bbox)
                })

            if candidates:

                best = max(
                    candidates,
                    key=lambda x: (x["area"], x["confidence"])
                )

                record = {
                    "id": image_path.stem,
                    "task": "entity_region_grounding",
                    "entity_name": best["entity_name"],
                    "bbox": best["bbox"],
                    "confidence": best["confidence"]
                }

            else:

                record = {
                    "id": image_path.stem,
                    "task": "entity_region_grounding",
                    "entity_name": None,
                    "bbox": None,
                    "confidence": None
                }

            outfile.write(
                json.dumps(record, ensure_ascii=False) + "\n"
            )

            outfile.flush()

            records_written += 1

            print(f"✓ Saved: {image_path.name}")

        except Exception as e:

            print(f"\n✗ Error processing {image_path.name}")
            print(type(e).__name__, e)

print("\n===================================")
print(f"Finished!")
print(f"Records Written : {records_written}")
print(f"Images Processed: {len(images)}")
print(f"Output File     : {OUTPUT_FILE.resolve()}")

if OUTPUT_FILE.exists():
    print(f"File Size       : {OUTPUT_FILE.stat().st_size} bytes")
else:
    print("Output file was not created!")

print("===================================")