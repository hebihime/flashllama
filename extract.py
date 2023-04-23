"""Get flashcards out of whatever the model says."""

import json


def extract_cards(text: str) -> list[dict]:
    """Parse the model response into a list of {"q": ..., "a": ...} dicts."""
    return json.loads(text)
