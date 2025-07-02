import re
from collections import Counter
from app.utils.cleaner import clean_html
from app.core.config import collection


def tokenize(text: str):
    return re.findall(r"\b[a-zA-Zéèêàùûôâçîïë\-]{2,}\b", text.lower())

def build_corpus_frequency_dict(docs):
    counter = Counter()
    for doc in docs:
        text = " ".join([
            doc.get("title", ""),
            doc.get("summary", ""),
            clean_html(doc.get("answer", "")),
            " ".join(doc.get("tags", []))
        ])
        counter.update(tokenize(text))
    return counter

def save_vocab_to_file(counter, path="frequency_dictionary.txt"):
    with open(path, "w", encoding="utf-8") as f:
        for word, freq in counter.items():
            f.write(f"{word} {freq}\n")

docs = list(collection.find())
print("total docs: ", len(docs))
freq_counter = build_corpus_frequency_dict(docs)
save_vocab_to_file(freq_counter, "frequency_dictionary.txt")
