"""Weekly Coding — Royal Text Analysis Engine."""

from __future__ import annotations

from pathlib import Path


def load_text(path: str) -> str:

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return ""

    except OSError:
        return ""


def normalize_text(text: str) -> str:

    normalized_characters: list[str] = []

    for character in text.lower():

        if character.isalnum() or character == " ":
            normalized_characters.append(character)

    return "".join(normalized_characters)


def tokenize(text: str) -> list[str]:

    if not text:
        return []

    return text.split()


def count_words(
    words: list[str],
) -> dict[str, int]:

    word_counts: dict[str, int] = {}

    for word in words:

        word_counts[word] = (
            word_counts.get(word, 0) + 1
        )

    return word_counts


def top_n_words(
    counts: dict[str, int],
    n: int,
) -> list[tuple[str, int]]:

    if n <= 0:
        return []

    ranked_words = list(counts.items())

    ranked_words.sort(
        key=lambda item: (-item[1], item[0])
    )

    return ranked_words[:n]


def extra_insight(
    words: list[str],
    counts: dict[str, int],
) -> float:

    if not words:
        return 0.0

    total_characters = 0

    for word in words:
        total_characters += len(word)

    average_word_length = (
        total_characters / len(words)
    )

    return average_word_length


def run_demo(
    path: str,
    n: int = 10,
) -> dict[str, object]:

    raw_text = load_text(path)

    normalized_text = normalize_text(raw_text)

    tokenized_words = tokenize(normalized_text)

    word_counts = count_words(tokenized_words)

    analysis_results = {
        "total_words": len(tokenized_words),
        "unique_words": len(word_counts),
        "top_words": top_n_words(word_counts, n),
        "extra_insight": extra_insight(
            tokenized_words,
            word_counts,
        ),
    }

    return analysis_results


if __name__ == "__main__":

    demo_file_path = Path("data/sample.txt")

    if demo_file_path.exists():

        analysis_output = run_demo(
            str(demo_file_path),
            n=10,
        )

        print("---- TEXT ANALYSIS RESULTS ----")

        for result_key, result_value in (
            analysis_output.items()
        ):
            print(
                f"{result_key}: {result_value}"
            )

    else:
        print(
            "No demo file found at data/sample.txt"
        )