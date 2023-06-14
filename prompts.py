"""Prompt templates. This file gets edited more than anything else here."""

ALPACA = """Below is an instruction that describes a task, paired with an input
that provides further context. Write a response that appropriately
completes the request.

### Instruction:
Write {n} question and answer flashcards for the study notes below.
Respond with a JSON array where each card is {{"q": "...", "a": "..."}}.
Return ONLY the JSON array. Do not add commentary, notes, or extra
questions of your own.

### Input:
Notes on {topic}:

{notes}

### Response:
"""

# things the model says when it is done and should stop talking
STOP = ["###", "\n\n\n"]


def build_prompt(topic: str, notes: str, n: int = 4) -> str:
    return ALPACA.format(topic=topic, notes=notes, n=n)
