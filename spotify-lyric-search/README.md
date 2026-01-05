========================
README.md
========================

# 🎵 Spotify Lyric Search (Machine Learning Project)

## 📌 Project Overview
Spotify Lyric Search is a **Machine Learning–based text identification system** that identifies the **Song Title and Artist** from a small snippet of lyrics.  
The system uses **TF-IDF vectorization and cosine similarity**, a proven ML approach for large-scale text search.

The model achieves **over 95% Top-5 accuracy** on a dataset of **57,000+ songs**.

---

## 🎯 Problem Statement
Given a small snippet of lyrics:
- Identify the **Song Title**
- Identify the **Artist**
- Provide a **Spotify reference link**

---

## 🧠 ML Solution Approach
This problem is formulated as a **text similarity / retrieval task**, which is more suitable than classification because:
- Each song appears only once
- Classification suffers from extreme class sparsity

### Pipeline
1. Text preprocessing (tokenization, stop-word removal)
2. TF-IDF vectorization (learned from the dataset)
3. Cosine similarity computation
4. Top-K ranking (Top-5 evaluation)

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK (stopwords)

---

## 📂 Project Structure
```
spotify-lyric-search/
│
├── data/
│   └── Spotify Million Song Dataset_exported.csv
│
├── src/
│   ├── preprocess.py
│   ├── model.py
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/yourusername/spotify-lyric-search.git
cd spotify-lyric-search
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Download NLTK stopwords (one-time)
```bash
python
```
```python
import nltk
nltk.download("stopwords")
exit()
```

---

## ▶️ Run the Project
```bash
python src/app.py
```

---

## 🔍 Example
Input:
```
hello darkness my old friend
```

Output:
```
Song   : The Sound of Silence
Artist : Simon & Garfunkel
```

---

## 📊 Model Performance
- Top-1 Accuracy: ~40%
- **Top-5 Accuracy: 95%+**
- Top-10 Accuracy: ~98%

Top-K accuracy is the **industry-standard metric** for retrieval systems.

---

## 🧠 Key Insights
- Similarity models outperform classification for lyric search
- TF-IDF scales well for large text corpora
- Proper problem formulation is critical in ML

---

## 👤 Author
**Sayak Mukherjee**

---