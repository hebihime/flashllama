# flashllama

feed it markdown study notes, get question/answer flashcards back.
runs a quantized LLaMA-family model locally via llama.cpp — no api
key, no cloud, generation happens on my own laptop. wild that this
works now.

## setup

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

then get a model: any LLaMA-family 7B chat model quantized to GGML
q4_0 format works. search Hugging Face for "7b ggml q4_0", download
the `.bin` (about 4 GB) and save it as `models/7b-chat-q4_0.bin`.
the `models/` dir is gitignored for obvious reasons.

## run

    python flashllama.py examples/photosynthesis.md

cards land in `out/cards.json`, one q/a pair per card, a few cards
per markdown heading.

## anki

    python flashllama.py examples/photosynthesis.md --csv

also writes `out/cards.csv`. in anki: Import File, front/back, done.
