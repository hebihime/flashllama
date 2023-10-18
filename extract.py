"""Get flashcards out of whatever the model says."""

import json
import re

ARRAY_RE = re.compile(r"\[.*\]", re.DOTALL)
TRAILING_COMMA_RE = re.compile(r",\s*([\]}])")


def extract_cards(text: str) -> list[dict]:
    """Parse the model response into a list of {"q": ..., "a": ...} dicts.

    The model rarely returns bare JSON. It says "Sure! Here are your
    flashcards:" first, or wraps the array in backticks, so dig the
    array out instead of trusting the whole response.
    """
    match = ARRAY_RE.search(text)
    if match is None:
        raise ValueError(f"no JSON array in model output: {text[:80]!r}")
    blob = match.group(0)
    # the model is very fond of a trailing comma before ] — fine by it,
    # not fine by json.loads
    blob = TRAILING_COMMA_RE.sub(r"\1", blob)
    return json.loads(blob)
