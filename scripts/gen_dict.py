from app.db.mongo import get_all_docs
from app.utils.vocab_builder import build_corpus_frequency_dict, save_vocab_to_file

docs = get_all_docs()
print("Total docs:", len(docs))

counter = build_corpus_frequency_dict(docs)
save_vocab_to_file(counter, "frequency_dictionary.txt")
print("✅ Dictionary saved.")
