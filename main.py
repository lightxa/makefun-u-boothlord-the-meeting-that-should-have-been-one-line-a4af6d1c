"""The Meeting That Should Have Been One Line.

Writes a single sentence to /output/entry.txt: the one line that could
have replaced an entire pointless meeting. No context, no explanation,
no setup. The line is fixed and deterministic; the program's only job
is to put it on disk exactly as written.

The line is built around one concrete deadpan incident: a meeting with
forty-seven invitees and no agenda whose only outcome is a second
meeting to decide what the first one was for. That kills the meeting
outright (its sole product is another meeting), it is drawn from real
office life (the invite list with no agenda, the follow-up meeting),
and the twist lands in the final words. It deliberately avoids the
worn "this meeting could have been an email" trope.
"""

import os

ENTRY = (
    "Forty-seven people, no agenda, one hour, and the only decision "
    "was to schedule another meeting to figure out what this one was for."
)


def main() -> None:
    """Write the entry line to /output/entry.txt."""
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise ValueError("entry must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
