# experiment_runner.py
#
# Runs a sorting algorithm a specified number of times on a given input file,
# timing each run and recording operation counts.
#
# The input file is read once and a fresh copy of the data is passed to the
# algorithm for each run, ensuring that every run sorts an identical input
# and results are directly comparable across algorithms.

import time
from typing import Callable
from sort_result import SortResult


def load_data(file_path: str) -> list[int]:
    """Reads an input file and returns a list of integers."""
    with open(file_path, "r") as f:
        return [int(line.strip()) for line in f if line.strip()]


def run_experiment(
    algorithm_name: str,
    sort_function: Callable[[list[int]], tuple[list[int], int]],
    input_file: str,
    ordering_type: str,
    number_of_runs: int
) -> list[SortResult]:
    """
    Runs a sorting algorithm a specified number of times on the given input file.

    Parameters:
        algorithm_name:  Display name for the algorithm, used in CSV output.
        sort_function:   A callable matching the signature: (list[int]) -> (list[int], int)
        input_file:      Path to the input file.
        ordering_type:   The ordering type of the input, used for reporting.
        number_of_runs:  How many times to run the algorithm on this input.

    Returns:
        A list of SortResult objects, one per run.
    """
    original_data = load_data(input_file)
    results = []

    for run in range(1, number_of_runs + 1):
        working_copy = original_data[:]

        start_time = time.perf_counter()
        _, operation_count = sort_function(working_copy)
        end_time = time.perf_counter()

        elapsed_ms = (end_time - start_time) * 1000

        result = SortResult(
            algorithm_name=algorithm_name,
            input_size=len(original_data),
            ordering_type=ordering_type,
            run_number=run,
            elapsed_milliseconds=elapsed_ms,
            operation_count=operation_count
        )

        results.append(result)
        print(f"  Run {run}/{number_of_runs} complete. "
              f"Time: {elapsed_ms:.2f}ms, Operations: {operation_count:,}")

    return results