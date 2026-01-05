# src/app.py

from model import SpotifyLyricSearch

DATA_PATH = "data/Spotify Million Song Dataset_exported.csv"

print("🚀 Loading Spotify Lyric Search Model...")
model = SpotifyLyricSearch(DATA_PATH)
print("✅ Model ready!")

while True:
    query = input("\n🎵 Enter lyric snippet (or type 'exit'): ")
    if query.lower() == "exit":
        break

    results = model.search(query, top_k=5)

    print("\n🔍 Top Results:")
    for i, r in enumerate(results, 1):
        print(f"\nRank {i}")
        print("Song      :", r["song"])
        print("Artist    :", r["artist"])
        print("Link      :", r["link"])
        print("Confidence:", f"{r['confidence']}%")
