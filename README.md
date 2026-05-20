# Sorting Experiment (Python)

A console application for running controlled sorting algorithm experiments and recording results to CSV.  Built for the Science of Computing & Digital Media (UI110010) UHI BSc Hons, core exercise one.

## Purpose

This application lets you generate integer input files of varying size and ordering, run sorting algorithms against those files a configurable number of times, and record timing and operation count data for analysis. Merge sort is supplied as the baseline algorithm. Your task is to extend the application with two additional sorting algorithms and design a series of experiments using the tools provided.

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point and menu-driven interface |
| `sorting_algorithm.py` | Sorting algorithm implementations |
| `input_generator.py` | Input file generation |
| `experiment_runner.py` | Runs algorithms and records timing and operation counts |
| `result_reporter.py` | Writes results to CSV |
| `sort_result.py` | Dataclass holding the result of a single run |

## Getting Started

Requires Python 3.10 or later.

```bash
python main.py
```

The application will present a menu. Generate an input file first, then run experiments against it.

## Input Generation

The generator produces files containing integers in one of four orderings:

| Ordering | Description |
|----------|-------------|
| `random` | Integers in a random order |
| `sorted` | Integers in ascending order |
| `reverse` | Integers in descending order |
| `nearlysorted` | Sorted with approximately 5% of elements randomly displaced |

Generated files are plain text with one integer per line.

## Running Experiments

Select a previously generated input file, specify its ordering type, and choose how many times to run each algorithm. Each algorithm runs the specified number of times on an identical copy of the input. Results are appended to the specified CSV file.

## CSV Output

Results are written to CSV with the following columns:

| Column | Description |
|--------|-------------|
| `Algorithm` | Algorithm name |
| `InputSize` | Number of integers in the input |
| `OrderingType` | Ordering of the input |
| `RunNumber` | Run index for this algorithm and input |
| `ElapsedMilliseconds` | Wall clock time for the sort |
| `OperationCount` | Number of comparisons performed |

## Operation Counting

An operation is counted each time two elements are compared during sorting. This definition is applied consistently across all algorithms; your implementations must follow the same convention. Each sorting function returns a tuple of `(sorted_list, operation_count)` where `operation_count` is incremented once per comparison.

## Where to Extend

Open `sorting_algorithm.py`. Add your bubble sort and insertion sort implementations following the same pattern as `merge_sort`:

```python
def your_algorithm(array: list[int]) -> tuple[list[int], int]:
    arr = array[:]
    operation_count = 0
    # your implementation here
    return arr, operation_count
```

Then open `main.py` and find the clearly marked comment block in `handle_run()`. Import your functions at the top of the file and add them following the pattern shown for merge sort.

## Sample Data

Two small sample files are included in the `data/` directory for initial testing:

- `sample_small_random.txt` — 20 integers, random ordering
- `sample_small_sorted.txt` — 20 integers, sorted ordering

Verify your implementations produce correct output on these before running larger experiments.

## Notes

- Results are appended to the CSV file if it already exists, allowing multiple sessions to accumulate into a single dataset.
- Each run sorts a fresh copy of the original data; the input array is never modified between runs.
- Timing uses `time.perf_counter` and wraps the sort call only, not file loading or setup.
- Requires Python 3.10 or later for `list[int]` and `tuple[list[int], int]` type hint syntax.