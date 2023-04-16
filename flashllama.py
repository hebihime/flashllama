"""flashllama — study notes in, flashcards out. all local, no api key."""

import argparse
from pathlib import Path


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
    args = ap.parse_args()

    sections = parse_notes(Path(args.notes).read_text())
    print(f"found {len(sections)} sections:")
    for heading, body in sections:
        print(f"  {heading} ({len(body)} chars)")


if __name__ == "__main__":
    main()
