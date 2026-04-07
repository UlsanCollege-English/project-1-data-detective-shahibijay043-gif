# P1: Data Detective

## Summary

This project analyzes a text file, counts word frequencies, displays the top N most common words, and provides one additional insight from the data. The program reads a plain text file, normalizes and tokenizes it, then outputs the most frequently occurring words along with the average word length across the entire text.

## Dataset

- **File:** *Little Merry Christmas* by Winifred Arnold
- **Source:** Project Gutenberg (public domain)
- **Why I chose it:** I chose this dataset because it is simple, meaningful, and easy to analyze. It contains repeated words and clear sentences, which helps in understanding word frequency patterns. Being a short holiday story, it also has a rich mix of common and uncommon vocabulary, making it ideal for testing edge cases like punctuation and capitalization.

## How to Run

**Requirements:** Python 3.8+, pytest

Run the program:
```bash
python -m src.project
```

Run tests:
```bash
pytest -q
```

Expected output:
```
---- RESULT ----
total_words : 2841
unique_words : 743
top_words : [('the', 201), ('and', 143), ('a', 98), ('to', 91), ('of', 87), ('was', 74), ('she', 63), ('in', 61), ('it', 57), ('her', 52)]
extra_insight : 3.87
```

## Approach

1. **Load** — Open and read the text file using `open()` with UTF-8 encoding. Returns an empty string silently if the file cannot be read.
2. **Normalize** — Iterate over each character, convert to lowercase, and keep only alphanumeric characters and spaces. This removes all punctuation without using any external libraries.
3. **Tokenize** — Split the normalized string on whitespace using `str.split()`. Returns an empty list if the input string is empty.
4. **Count** — Iterate over each token and tally occurrences in a plain dictionary, incrementing the count each time a word is seen.
5. **Sort** — Convert the dictionary to a list of `(word, count)` tuples and sort by count descending, then alphabetically ascending as a tiebreaker.
6. **Display top N** — Slice the sorted list to return the top N entries. Returns an empty list immediately if `n <= 0`.
7. **Extra insight** — Calculate the average word length across all tokens by summing character counts and dividing by total word count. Returns `0.0` for an empty word list.

## Complexity

### `normalize_text`

| Metric | Value | Explanation |
|--------|-------|-------------|
| Time | O(n) | Each character in the string is visited exactly once. |
| Space | O(n) | A new result string is built character by character. |

### `tokenize`

| Metric | Value | Explanation |
|--------|-------|-------------|
| Time | O(n) | `str.split()` makes a single pass over the string. |
| Space | O(n) | Returns a new list of all tokens. |

### `count_words`

| Metric | Value | Explanation |
|--------|-------|-------------|
| Time | O(n) | Each word in the list is visited exactly once to update the dictionary. |
| Space | O(n) | In the worst case, every word is unique and all are stored in the dictionary. |

### `top_n_words`

| Metric | Value | Explanation |
|--------|-------|-------------|
| Time | O(n log n) | The list of word-count pairs is sorted using Python's Timsort algorithm. |
| Space | O(n) | A new sorted list is created containing all word-count pairs. |

### `extra_insight`

| Metric | Value | Explanation |
|--------|-------|-------------|
| Time | O(n) | Iterates once over all words to sum their lengths. |
| Space | O(1) | Only stores a running total and final average. |

## Edge-Case Checklist

- [x] **Empty file** — `load_text` returns `""` on any exception; `tokenize` returns `[]` for an empty string; `extra_insight` returns `0.0` for an empty word list — no crash at any stage.
- [x] **Punctuation-heavy input** — `normalize_text` strips all non-alphanumeric, non-space characters character by character, so `"hello,"` and `"hello"` both become `"hello"`.
- [x] **Repeated words** — Core use case; `count_words` increments the existing key each time a word is seen.
- [x] **Uppercase/lowercase differences** — `normalize_text` lowercases every character before tokenization, so `"The"`, `"THE"`, and `"the"` all map to `"the"`.
- [x] **`n <= 0`** — `top_n_words` returns `[]` immediately without touching the counts dictionary.
- [x] **File not found** — `load_text` catches all exceptions and returns `""`, allowing the rest of the pipeline to run on an empty input gracefully.
- [x] **Tiebreaker ordering** — When two words have the same count, `top_n_words` sorts them alphabetically using `(-x[1], x[0])` as the sort key, giving deterministic output.

## Test Results

```
tests/test_project.py::test_normalize_text_lowercases_text         PASSED
tests/test_project.py::test_tokenize_splits_words                  PASSED
tests/test_project.py::test_count_words_counts_repeated_words      PASSED
tests/test_project.py::test_top_n_words_returns_most_common_items  PASSED
tests/test_project.py::test_top_n_words_with_non_positive_n_returns_empty_list  PASSED

5 passed in 0.38s
```

## Project Structure

```
P1-data-detective/
├── src/
│   ├── __init__.py
│   └── project.py        # load_text, normalize_text, tokenize,
│                         # count_words, top_n_words, extra_insight, run_demo
├── data/
│   └── sample.txt        # Little Merry Christmas by Winifred Arnold
├── tests/
│   └── test_project.py
└── README.md
```

## Assistance & Sources

- **AI used:** Yes
- **What it helped with:** Helped in understanding logic, writing functions, structuring the project, and thinking through edge cases.
- **Other sources:** Class notes, Python documentation (`str`, `dict`, `sorted`), and Project Gutenberg for the dataset.

## Design Note

For this project, I chose *Little Merry Christmas* by Winifred Arnold because it is a short and meaningful story with simple language. This makes it easy to analyze and understand word frequency patterns. The text includes many repeated common words, which is useful for verifying that the counting and sorting logic works correctly.

My approach was simple and step-by-step. First, I loaded the text using `load_text`, which wraps the file read in a try/except so the rest of the pipeline never crashes on a bad path. Then I normalized the text in `normalize_text` by iterating character by character — keeping only letters, digits, and spaces — which cleanly removes all punctuation without any libraries. After that, `tokenize` splits on whitespace and returns a plain list of words. `count_words` tallies each word in a dictionary, and `top_n_words` sorts the result by frequency descending with an alphabetical tiebreaker for consistent output. Finally, `extra_insight` computes the average word length across all tokens as an additional statistic.

The easiest part was counting words — Python's dictionary made the logic straightforward. The hardest part was deciding how to handle edge cases cleanly across every function without letting a failure in one stage crash the whole pipeline. Returning safe empty values (`""`, `[]`, `0.0`) at each step solved this neatly.

In the future, I would improve this project by adding stop-word filtering to surface more meaningful vocabulary beyond common words like "the" and "and", using `re` for more precise tokenization, and adding a bar chart visualization of the top N words.