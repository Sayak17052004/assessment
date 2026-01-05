import pandas as pd


# -------------------------------
# Utility: Load Dataset
# -------------------------------
REQUIRED_COLUMNS = {
    "Zone",
    "State",
    "City",
    "Name",
    "Google review rating",
    "Number of google review in lakhs",
    "Best Time to visit"
}

def load_dataset(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    if df.empty:
        raise ValueError("Dataset is empty")

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df


# -------------------------------
# Utility: Normalization
# -------------------------------
def normalize(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min() + 1e-9)


# -------------------------------
# Ranking Logic
# -------------------------------
def rank_destinations(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["rating_norm"] = normalize(df["Google review rating"])
    df["popularity_norm"] = normalize(df["Number of google review in lakhs"])

    # Weighted scoring
    df["final_score"] = (
        0.6 * df["rating_norm"] +
        0.4 * df["popularity_norm"]
    )

    return df.sort_values("final_score", ascending=False)


# -------------------------------
# Recommendation Engine
# -------------------------------
def get_weekend_recommendations(csv_path: str, source_city: str, top_n: int = 5):
    data = load_dataset(csv_path)

    # Case-insensitive matching
    data["City_clean"] = data["City"].astype(str).str.strip().str.lower()
    source_city_clean = source_city.strip().lower()

    if source_city_clean not in data["City_clean"].values:
        return None

    city_data = data[data["City_clean"] == source_city_clean].copy()

    ranked = rank_destinations(city_data)

    return ranked[
        [
            "Zone",
            "State",
            "City",
            "Name",
            "Google review rating",
            "Number of google review in lakhs",
            "Best Time to visit",
            "final_score"
        ]
    ].head(top_n)


# -------------------------------
# Main Entry Point
# -------------------------------
if __name__ == "__main__":
    CSV_PATH = "data/Top Indian Places to Visit.csv"

    city = input("Enter source city: ").strip()

    result = get_weekend_recommendations(CSV_PATH, city)

    if result is None:
        print(f"\nNot available yet for the city: {city}")
    else:
        print(f"\nTop Weekend Places in {city.title()}")
        print("-" * 60)
        print(result.to_string(index=False))
