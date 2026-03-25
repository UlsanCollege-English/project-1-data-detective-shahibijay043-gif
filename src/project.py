"""Project 1 starter: Data Detective.

Implement the required functions below.
Use standard library only.
"""

from __future__ import annotations

from pathlib import Path


def load_text(path: str) -> str:
    """Load and return the full text from a UTF-8 file."""
    raise NotImplementedError


def normalize_text(text: str) -> str:
    """Return a normalized version of the text.

    Suggested starter behavior:
    - lowercase the text
    - remove or replace punctuation
    - collapse extra whitespace if helpful
    """
    raise NotImplementedError


def tokenize(text: str) -> list[str]:
    """Split normalized text into a list of words."""
    raise NotImplementedError


def count_words(words: list[str]) -> dict[str, int]:
    """Count how many times each word appears."""
    raise NotImplementedError


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the top N words as (word, count) tuples.

    Suggested behavior:
    - if n <= 0, return []
    - sort by count descending
    - for ties, sort alphabetically
    """
    raise NotImplementedError


def extra_insight(words: list[str], counts: dict[str, int]) -> object:
    """Return one extra insight of your choice.

    Keep it small and well-defined.
    Examples:
    - list of words that appear once
    - average word length
    - longest unique word
    """
    raise NotImplementedError


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run the full analysis pipeline and return summary data."""
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "extra_insight": extra_insight(words, counts),
    }


if __name__ == "__main__":
    demo_path = Path("data/sample.txt")
    if demo_path.exists():
        results = run_demo(str(demo_path), n=10)
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print("No demo file found at data/sample.txt")
