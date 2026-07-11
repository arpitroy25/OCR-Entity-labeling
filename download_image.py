import json, os, time, requests, urllib.parse
from pathlib import Path

JSONL_PATH = r"A:\entity and label\signs.jsonl"      # path to your jsonl file on your PC
OUTPUT_DIR   = "downloaded_images"  # folder to save images
PILOT_N      = 50                   # start with 30

os.makedirs(OUTPUT_DIR, exist_ok=True)

headers = {
    "User-Agent": "IndianCultureDatasetProject/1.0 (academic-research; your@email.com)",
}

records = []
with open(JSONL_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            records.append(json.loads(line))

print(f"Downloading first {PILOT_N} images...")

for record in records[:PILOT_N]:
    img_id  = record["id"]
    img_url = record["image_url"]
    
    # figure out file extension from URL
    ext = img_url.split(".")[-1].split("?")[0].lower()
    if ext not in ["jpg", "jpeg", "png", "gif", "webp"]:
        ext = "jpg"
    
    save_path = os.path.join(OUTPUT_DIR, f"{img_id}.{ext}")
    
    if os.path.exists(save_path):
        print(f"  ✓ Already exists: {img_id}")
        continue
    
    try:
        resp = requests.get(img_url, headers=headers, timeout=30)
        resp.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(resp.content)
        print(f"  ✅ Downloaded: {img_id}")
        time.sleep(0.5)   # be polite to wikimedia
    except Exception as e:
        print(f"  ❌ Failed {img_id}: {e}")

print("Done!")
