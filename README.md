# flashllama

feed it markdown study notes, get question/answer flashcards back.
runs a quantized LLaMA-family model locally via llama.cpp — no api
key, no cloud, generation happens on my own laptop. wild that this
works now.

## setup

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

then get a model: I use llama-2-7b-chat quantized to GGML q4_0.
grab a q4_0 `.bin` of it from Hugging Face (about 4 GB) and save it
as `models/llama-2-7b-chat.q4_0.bin`. the `models/` dir is
gitignored for obvious reasons.

## run

    python flashllama.py examples/photosynthesis.md

cards land in `out/cards.json`, one q/a pair per card, a few cards
per markdown heading.

## anki

    python flashllama.py examples/photosynthesis.md --csv

also writes `out/cards.csv`. in anki: Import File, front/back, done.

## quantization showdown

same notes, same prompt, same laptop (see `bench.py`):

| quant | size   | speed     | cards any good?             |
|-------|--------|-----------|-----------------------------|
| q4_0  | 3.8 GB | 8.9 tok/s | yes, occasionally weird     |
| q5_1  | 5.1 GB | 8.9 tok/s | a bit better than q4_0      |
| q8_0  | 7.2 GB | 4.1 tok/s | best, but the fan takes off |
