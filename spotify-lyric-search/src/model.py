# src/model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess_text

class SpotifyLyricSearch:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)[["artist", "song", "link", "text"]].dropna()
        self.df["clean_lyrics"] = self.df["text"].apply(preprocess_text)

        self.vectorizer = TfidfVectorizer(
            max_features=50000,
            ngram_range=(1, 2),
            sublinear_tf=True
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["clean_lyrics"])

    def search(self, snippet, top_k=5):
        snippet_clean = preprocess_text(snippet)
        snippet_vec = self.vectorizer.transform([snippet_clean])

        similarities = cosine_similarity(snippet_vec, self.tfidf_matrix)[0]
        top_indices = similarities.argsort()[::-1][:top_k]

        results = []
        for idx in top_indices:
            results.append({
                "song": self.df.iloc[idx]["song"],
                "artist": self.df.iloc[idx]["artist"],
                "link": self.df.iloc[idx]["link"],
                "confidence": round(similarities[idx] * 100, 2)
            })
        return results
