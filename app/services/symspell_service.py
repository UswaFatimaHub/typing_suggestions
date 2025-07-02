import re
from symspellpy.symspellpy import SymSpell, Verbosity
from app.api.schemas import WordSuggestion 

# Load SymSpell only once
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
sym_spell.load_dictionary("frequency_dictionary.txt", term_index=0, count_index=1)

def suggest_word(word: str):
    if word.isupper() or re.match(r"[A-Z][a-z]+", word):
        return WordSuggestion(
            original=word,
            suggested=word,
            confidence=1.0
        )

    suggestions = sym_spell.lookup(word.lower(), Verbosity.TOP, max_edit_distance=2)
    if suggestions:
        best = suggestions[0]
        return WordSuggestion(
            original=word,
            suggested=best.term,
            confidence= 1 - best.distance / 2
        )
    else:
        return WordSuggestion(
            original=word,
            suggested=word,
            confidence=0.0
        )


def suggest_typo_for_text(text: str):
    words = re.findall(r"\b\w+\b", text)
    return [suggest_word(word) for word in words]
