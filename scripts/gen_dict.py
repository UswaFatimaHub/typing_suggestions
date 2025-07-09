# from app.db.mongo import get_all_docs
# from app.utils.vocab_builder import build_corpus_frequency_dict, save_vocab_to_file

# docs = get_all_docs()
# print("Total docs:", len(docs))

# counter = build_corpus_frequency_dict(docs)
# save_vocab_to_file(counter, "frequency_dictionary.txt")
# print("✅ Dictionary saved.")

# scripts/generate_medical_dict.py

input_file = "medical_wordlist.txt"  # List of words, one per line
output_file = "frequency_dictionary.txt"  # Flat freq = 1

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        word = line.strip().lower()
        if word:
            f_out.write(f"{word}\t1\n")

print("✅ frequency_dictionary.txt created with flat frequencies.")
