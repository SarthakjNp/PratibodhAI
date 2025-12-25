import json
import os

BASE_DIR = "data"
VERSE_FILE = os.path.join(BASE_DIR, "verse.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "Geeta.json")

# -------- LOAD VERSES --------
with open(VERSE_FILE, "r", encoding="utf-8") as f:
    verses_raw = json.load(f)

print(f"[INFO] Loaded Sanskrit verses: {len(verses_raw)}")

final_verses = []

for v in verses_raw:
    try:
        chapter = int(v["chapter_number"])
        verse = int(v["verse_number"])

        final_verses.append({
            "id": f"GITA_{chapter}_{verse}",
            "chapter": chapter,
            "verse": verse,
            "reference": f"{chapter}.{verse}",
            "sanskrit": v.get("text", "").strip(),
            "transliteration": v.get("transliteration", "").strip(),
            "word_meanings": v.get("word_meanings", "").strip(),
            "context_tags": [],
            "speaker": "Krishna" if chapter > 1 else "Dhritarashtra",
            "audience": "Arjuna" if chapter > 1 else "Sanjaya"
        })

    except Exception:
        continue

# -------- SORT --------
final_verses.sort(key=lambda x: (x["chapter"], x["verse"]))

# -------- FINAL JSON --------
gita_json = {
    "meta": {
        "text": "Bhagavad Gita",
        "mode": "contextual_retrieval",
        "language": "Sanskrit",
        "total_chapters": 18,
        "total_verses": len(final_verses)
    },
    "verses": final_verses
}

# -------- SAVE --------
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(gita_json, f, ensure_ascii=False, indent=2)

print("\n[SUCCESS] Geeta.json generated (Option 2)")
print(f"Total verses written: {len(final_verses)}")
print(f"Saved at: {OUTPUT_FILE}")
