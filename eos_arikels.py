import json
import os

FILE_PATH = "manual_articles.json"

# Load existing data
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        articles = json.load(f)
else:
    articles = []

print("📝 Voeg artikels toe. Typ 'stop' om te stoppen.\n")

while True:
    title = input("Titel: ")
    if title.lower() == "stop":
        break

    url = input("Link: ")
    if url.lower() == "stop":
        break

    articles.append({
        "title": title,
        "url": url
    })
    print("✅ Toegevoegd!\n")

# Save all at the end
with open(FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"💾 Alles opgeslagen in {FILE_PATH}. Totaal: {len(articles)} artikels.")