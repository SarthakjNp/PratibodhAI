import json

print("---- INSPECT verse.json ----")
with open("data/verse.json", encoding="utf-8") as f:
    verses = json.load(f)

print("Type:", type(verses))
print("Length:", len(verses))
print("Sample entry:")
print(verses[0])
print("Keys:", verses[0].keys())

print("\n---- INSPECT translation.json ----")
with open("data/translation.json", encoding="utf-8") as f:
    translations = json.load(f)

print("Type:", type(translations))
print("Length:", len(translations))
print("Sample entry:")
print(translations[0])
print("Keys:", translations[0].keys())
