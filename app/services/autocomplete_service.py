from llama_cpp import Llama
LLAMA_MODEL_PATH = "model/unsloth.Q4_K_M.gguf"

# Load GGUF model once
llm = Llama(
    model_path=LLAMA_MODEL_PATH,
    # n_threads=8,
    # n_ctx=512,
    # use_mmap=True,
    # use_mlock=True,
    verbose=False
)

# Alpaca-style prompt template
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Generate the next few words in a medically relevant way.

### Input:
{}

### Response:
"""

def suggest_next_words(input_text: str, max_tokens: int = 10, temperature: float = 0.7, num_suggestions: int = 1):
    prompt = alpaca_prompt.format(input_text)
    # print(f"Prompt:\n{prompt}\nSuggestions:")

    completions = []

    for i in range(num_suggestions):
        output = llm(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_k=40,
            top_p=0.9,
            repeat_penalty=1.1,
        )
        full_completion = output["choices"][0]["text"].strip()
        # print(f"{i+1}. {full_completion}")
        completions.append(full_completion)

    return completions


suggestions = suggest_next_words("Appendicitis is")
for s in suggestions:
    print("→", s)


