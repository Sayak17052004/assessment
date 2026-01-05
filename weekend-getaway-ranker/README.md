# Weekend Getaway Ranker

A data-driven recommendation engine that ranks top weekend places
within a selected city using real engagement data.

## Tech Stack
- Python
- Pandas

## Dataset
India’s Must-See Places (CSV)

## How It Works
- User enters a source city
- Places within that city are filtered
- Ranking is based on:
  - Google review rating
  - Number of Google reviews
- Scores are normalized and sorted

## Scoring Formula
Final Score =
0.6 × Rating +
0.4 × Popularity

## How to Run
```bash
pip install -r requirements.txt
python src/weekend_getaway_ranker.py
