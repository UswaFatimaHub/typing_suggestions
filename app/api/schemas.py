from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    query: str

class WordSuggestion(BaseModel):
    original: str
    suggested: str
    confidence: float

class SuggestionResponse(BaseModel):
    input: str
    suggestions: List[WordSuggestion]



class AutocompleteRequest(BaseModel):
    prefix: str
    top_k: int = 5

class Suggestion(BaseModel):
    word: str
    # score: int

class AutocompleteResponse(BaseModel):
    prefix: str
    suggestions: list[Suggestion]
