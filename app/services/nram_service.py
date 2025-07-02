import json
from pathlib import Path
from app.services.llm_fallback import predict_with_llm

NGRAM_PATH = Path("ngram_freqs.json")

def load_ngram_freqs(path=NGRAM_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# def suggest_next_words(prefix, ngram_freqs, top_k=5):
#     prefix = prefix.lower().strip()
#     suggestions = {}

#     for ngram, freq in ngram_freqs.items():
#         if ngram.startswith(prefix + " "):
#             next_word = ngram[len(prefix):].strip().split(" ")[0]
#             suggestions[next_word] = suggestions.get(next_word, 0) + freq

#     return sorted(suggestions.items(), key=lambda x: -x[1])[:top_k]


def suggest_next_words(prefix, ngram_freqs, top_k=5):
    prefix = prefix.lower().strip()
    suggestions = {}

    # 1. Search N-grams for prefix matches
    for ngram, freq in ngram_freqs.items():
        if ngram.startswith(prefix + " "):
            remaining = ngram[len(prefix):].strip()
            if remaining:
                suggestions[remaining] = suggestions.get(remaining, 0) + freq

    if suggestions:
        sorted_suggestions = sorted(suggestions.items(), key=lambda x: -x[1])
        return sorted_suggestions[:top_k]

    # 2. Fallback to LLM if no corpus match
    print("🔁 used llm")
    return predict_with_llm(prefix, top_k=top_k)
