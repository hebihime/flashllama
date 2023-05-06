"""flashllama — study notes in, flashcards out. all local, no api key."""

import argparse
import json
from pathlib import Path

from llama_cpp import Llama

from extract import extract_cards
from prompts import build_prompt

MODEL_PATH = "models/7b-chat-q4_0.bin"
# a token is roughly 4 chars of english; keep prompt + answer inside n_ctx
N_CTX = 2048
MAX_SECTION_CHARS = 4000


def parse_notes(text: str) -> list[tuple[str, str]]:
    """Split markdown notes into (heading, body) sections."""
    sections = []
    heading = "Notes"
    body: list[str] = []
    for line in text.splitlines():
        if line.startswith("#"):
            if "\n".join(body).strip():
                sections.append((heading, "\n".join(body).strip()))
            heading = line.lstrip("#").strip()
            body = []
        else:
            body.append(line)
    if "\n".join(body).strip():
        sections.append((heading, "\n".join(body).strip()))
    return sections


def main():
    ap = argparse.ArgumentParser(description="turn markdown notes into flashcards")
    ap.add_argument("notes", help="markdown file of study notes")
    ap.add_argument("-n", type=int, default=4, help="cards per section")
    args = ap.parse_args()

    sections = parse_notes(Path(args.notes).read_text())
    print(f"{len(sections)} sections, loading model (takes a moment)...")
    llm = Llama(model_path=MODEL_PATH, n_ctx=N_CTX)

    all_cards = []
    for heading, body in sections:
        if len(body) > MAX_SECTION_CHARS:
            print(f"({heading} is long, trimming to {MAX_SECTION_CHARS} chars)")
            body = body[:MAX_SECTION_CHARS]
        prompt = build_prompt(heading, body, n=args.n)
        out = llm(prompt, max_tokens=512)
        cards = extract_cards(out["choices"][0]["text"])
        for card in cards:
            card["topic"] = heading
        all_cards.extend(cards)
        print(f"{heading}: {len(cards)} cards")

    outfile = Path("out/cards.json")
    outfile.parent.mkdir(exist_ok=True)
    outfile.write_text(json.dumps(all_cards, indent=2))
    print(f"\nwrote {len(all_cards)} cards to {outfile}")


if __name__ == "__main__":
    main()
