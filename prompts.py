"""Prompt templates. This file gets edited more than anything else here."""

ALPACA = """Below is an instruction that describes a task, paired with an input
that provides further context. Write a response that appropriately
completes the request.

### Instruction:
Write {n} question and answer flashcards for the study notes below.
Respond with a JSON array where each card is {{"q": "...", "a": "..."}}.

### Input:
Notes on {topic}:

{notes}

### Response:
"""


def build_prompt(topic: str, notes: str, n: int = 4) -> str:
    return ALPACA.format(topic=topic, notes=notes, n=n)
