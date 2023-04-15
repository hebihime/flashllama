"""flashllama — study notes in, flashcards out. all local, no api key."""

from llama_cpp import Llama

MODEL_PATH = "models/7b-chat-q4_0.bin"


def main():
    llm = Llama(model_path=MODEL_PATH)
    out = llm(
        "Q: What gas do plants take in for photosynthesis? A:",
        max_tokens=32,
        stop=["Q:", "\n"],
    )
    print(out["choices"][0]["text"].strip())


if __name__ == "__main__":
    main()
