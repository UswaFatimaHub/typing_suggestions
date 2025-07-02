from transformers import pipeline
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

EN_STOPWORDS = set(stopwords.words("english"))
FR_STOPWORDS = set(stopwords.words("french"))
ALL_STOPWORDS = EN_STOPWORDS.union(FR_STOPWORDS)

generator = pipeline(
    "text-generation",
    model="bigscience/bloom-560m",
    device=-1 #cpu
)

def is_useful(text: str) -> bool:
    tokens = text.lower().split()
    # At least one token should not be a stopword
    return any(token not in ALL_STOPWORDS for token in tokens)

def cleanup_completion(text: str) -> str:
    text = text.replace("\n", " ").replace("\t", " ")
    text = text.split(".")[0]
    return text.strip()

def predict_with_llm(prefix: str, top_k: int = 5, max_tokens: int = 12):
    results = generator(
        prefix,
        max_new_tokens=max_tokens,
        num_return_sequences=top_k * 2,  # Generate extra to filter
        do_sample=True,
        temperature=0.7
    )

    suggestions = []
    seen = set()

    for result in results:
        full = result["generated_text"]
        completion = cleanup_completion(full[len(prefix):].strip())

        if completion and completion not in seen and is_useful(completion):
            suggestions.append((completion, 1.0))  # Score is static for now
            seen.add(completion)

        if len(suggestions) >= top_k:
            break

    return suggestions
