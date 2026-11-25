#!/usr/bin/env python3
"""make.fun tagline: check the fixed entry, then write it out.

Your agent builds, the judge decides, you get paid: the whole site in
nine words. This program never accepts outside text: it holds exactly
one tagline, proves that tagline is well formed, and saves it to a
file. There is no input, no network access, no clock, and no
randomness anywhere in here.
"""

import sys

ENTRY = "Your agent builds. The judge decides. You get paid."
CHAR_LIMIT = 100
DESTINATION = "/output/entry.txt"
ENDERS = (".", "!", "?")
FILLER = set(".,!?;:'\"-() ")


def fail(problem):
    """Print why the entry was refused and stop without writing."""
    print(f"refused: {problem}", file=sys.stderr)
    raise SystemExit(1)


def guard_nonempty(text):
    return bool(text and text.strip())


def guard_short_enough(text):
    return len(text) <= CHAR_LIMIT


def guard_no_controls(text):
    return all(ord(letter) >= 32 for letter in text)


def guard_tidy_spacing(text):
    stripped = text.strip()
    return text == stripped and "  " not in text and "\t" not in text


def guard_has_letters(text):
    return any(letter.isalpha() for letter in text)


def guard_not_only_marks(text):
    return not all(letter in FILLER for letter in text)


def guard_not_only_digits(text):
    return not text.strip().isdigit()


def guard_ends_with_mark(text):
    return text.rstrip().endswith(ENDERS)


def guard_names_agent(text):
    return "agent" in text.lower()


def guard_opens_capital(text):
    # A tagline opens with a capital letter, like a headline.
    return text[:1].isupper()


def guard_digit_free(text):
    # A tagline is words, not a serial number.
    return not any(letter.isdigit() for letter in text)


# Every guard is listed with the complaint shown when it trips. The
# checker runs them in this order and stops at the first failure, so a
# bad entry never reaches the file.
RULES = [
    ("entry must mention the agent", guard_names_agent),
    ("entry must start with a capital letter", guard_opens_capital),
    ("entry must not contain digits", guard_digit_free),
    ("entry is empty", guard_nonempty),
    ("entry is longer than the 100 character limit", guard_short_enough),
    ("entry contains control characters", guard_no_controls),
    ("entry has ragged spacing or a tab", guard_tidy_spacing),
    ("entry contains no letters", guard_has_letters),
    ("entry is punctuation only", guard_not_only_marks),
    ("entry is digits only", guard_not_only_digits),
    ("entry does not end with punctuation", guard_ends_with_mark),
]


def check_entry(text):
    for problem, guard in RULES:
        if not guard(text):
            fail(problem)


def main():
    check_entry(ENTRY)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
