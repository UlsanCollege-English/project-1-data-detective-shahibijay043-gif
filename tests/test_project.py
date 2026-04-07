from src.project import (
    count_words,
    normalize_text,
    tokenize,
    top_n_words,
)


def test_normalize_text_lowercases_text() -> None:
    assert normalize_text("Hello WORLD") == "hello world"


def test_tokenize_splits_words() -> None:
    assert tokenize("one two three") == ["one", "two", "three"]


def test_count_words_counts_repeated_words() -> None:
    words = ["red", "blue", "red"]
    assert count_words(words) == {"red": 2, "blue": 1}


def test_count_words_empty_list() -> None:
    assert count_words([]) == {}


def test_top_n_words_returns_most_common_items() -> None:
    counts = {"apple": 3, "banana": 1, "carrot": 2}
    assert top_n_words(counts, 2) == [("apple", 3), ("carrot", 2)]


def test_top_n_words_with_non_positive_n_returns_empty_list() -> None:
    counts = {"apple": 3}
    assert top_n_words(counts, 0) == []


def test_top_n_words_with_n_greater_than_length() -> None:
    counts = {"a": 1, "b": 2}
    assert top_n_words(counts, 5) == [("b", 2), ("a", 1)]