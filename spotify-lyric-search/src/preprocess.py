# src/preprocess.py

import re
import string
from nltk.corpus import stopwords

# Load stopwords AFTER they are installed
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))

    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words and len(t) > 2]

    return " ".join(tokens)
