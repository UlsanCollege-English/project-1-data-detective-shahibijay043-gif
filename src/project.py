

from __future__ import annotations
from pathlib import Path


def load_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

def normalize_text(text: str) -> str:
    result = ""

    for ch in text:
        ch = ch.lower()
        if ch.isalnum() or ch == " ":
            result += ch

    return result

def tokenize(text: str) -> list[str]:
    if text == "":
        return []
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    counts = {}

    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1

    return counts


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    if n <= 0:
        return []

    items = list(counts.items())

    items.sort(key=lambda x: (-x[1], x[0]))

    return items[:n]

def extra_insight(words: list[str], counts: dict[str, int]) -> object:
    if len(words) == 0:
        return 0.0

    total = 0
    for w in words:
        total += len(w)

    return total / len(words)


def run_demo(path: str, n: int = 10) -> dict[str, object]:
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

        print("---- RESULT ----")
        for key, value in results.items():
            print(key, ":", value)
    else:
        print("No demo file found at data/sample.txt")