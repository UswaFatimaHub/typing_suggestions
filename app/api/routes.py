from fastapi import APIRouter
from app.services.symspell_service import suggest_typo_for_text
from app.services.autocomplete_service import suggest_next_words
from app.api.schemas import QueryRequest, SuggestionResponse, AutocompleteRequest, AutocompleteResponse, Suggestion

router = APIRouter()

@router.post("/typo-suggest", response_model=SuggestionResponse)
def typo_suggest(req: QueryRequest):
    suggestions = suggest_typo_for_text(req.query)
    return SuggestionResponse(input=req.query, suggestions=suggestions)


# ngram_freqs = load_ngram_freqs()
@router.post("/autocomplete", response_model=AutocompleteResponse)
def autocomplete(req: AutocompleteRequest):
    raw_suggestions = suggest_next_words(input_text = req.prefix, num_suggestions = req.top_k)
    return AutocompleteResponse(
        prefix=req.prefix,
        suggestions=[Suggestion(word=word) for word in raw_suggestions]
    )

