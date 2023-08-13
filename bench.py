"""Time the same prompt against each quantization of the same model.

usage: python bench.py models/llama-2-7b-chat.q4_0.bin [more .bin files]
"""

import sys
import time

from llama_cpp import Llama

from prompts import STOP, build_prompt

NOTES = (
    "Plants make their own food using sunlight, water and carbon "
    "dioxide. This happens in the chloroplasts, which contain the "
    "green pigment chlorophyll."
)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python bench.py model.bin [model.bin ...]")
    prompt = build_prompt("Photosynthesis", NOTES, n=3)
    for path in sys.argv[1:]:
        llm = Llama(model_path=path, n_ctx=2048)
        start = time.time()
        out = llm(prompt, max_tokens=256, stop=STOP)
        elapsed = time.time() - start
        tokens = out["usage"]["completion_tokens"]
        print(f"{path}: {tokens} tokens in {elapsed:.1f}s "
              f"({tokens / elapsed:.1f} tok/s)")


if __name__ == "__main__":
    main()
