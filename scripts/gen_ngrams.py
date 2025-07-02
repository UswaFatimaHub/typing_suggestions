# scripts/generate_ngrams.py

import json
from pathlib import Path
from collections import Counter
from nltk.util import ngrams
from bs4 import BeautifulSoup
import re
import nltk
from app.core.config import collection


# Download NLTK data
nltk.download("punkt")


def clean_html(html: str) -> str:
    if not html:
        return ""
    return BeautifulSoup(html, "html.parser").get_text(separator=" ").strip()

def extract_ngrams_from_text(text, n=2):
    tokens = re.findall(r"\b\w+\b", text.lower()) 
    return list(ngrams(tokens, n))


def build_ngram_freqs(docs, min_freq=2, max_n=3):
    counter = Counter()

    for doc in docs:
        text = " ".join([
            doc.get("title", ""),
            doc.get("summary", ""),
            clean_html(doc.get("answer", "")),
            " ".join(doc.get("tags", [])),
        ])

        for n in range(2, max_n + 1):
            for ng in extract_ngrams_from_text(text, n):
                counter[" ".join(ng)] += 1

    return {ng: freq for ng, freq in counter.items() if freq >= min_freq}

def main():
    # Load all docs
    docs = list(collection.find({}))

    # Build n-gram frequencies
    ngram_freqs = build_ngram_freqs(docs, min_freq=2, max_n=3)

    # Save to JSON
    OUTPUT_PATH = Path("ngram_freqs.json")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(ngram_freqs, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {len(ngram_freqs)} n-grams to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
