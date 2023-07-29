"""Prompt templates. This file gets edited more than anything else here."""

# llama-2-chat wants its own format: [INST] blocks and a <<SYS>> preamble.
LLAMA2_CHAT = """[INST] <<SYS>>
You write study flashcards. You always respond with a JSON array where
each card is {{"q": "...", "a": "..."}}. You never add commentary or
extra questions of your own.
<</SYS>>

Write {n} question and answer flashcards for these notes on {topic}:

{notes} [/INST]
"""

# the old alpaca-style template, kept around for pre-llama-2 models
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

STOP = ["</s>", "[INST]"]


def build_prompt(topic: str, notes: str, n: int = 4) -> str:
    return LLAMA2_CHAT.format(topic=topic, notes=notes, n=n)
