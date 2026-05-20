# result_reporter.py
#
# Writes experiment results to a CSV file.
# Each row represents one run of one algorithm on one input file.
#
# Results are appended if the output file already exists, allowing multiple
# experiment sessions to accumulate into a single output file for analysis.
# The header row is written only when the file is first created.

import os
from sort_result import SortResult


def write_results(results: list[SortResult], output_file: str) -> None:
    """
    Appends a list of SortResult objects to the specified CSV file.
    Creates the file with a header row if it does not already exist.
    """
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else ".", exist_ok=True)

    file_exists = os.path.isfile(output_file)

    with open(output_file, "a") as f:
        if not file_exists:
            f.write("Algorithm,InputSize,OrderingType,RunNumber,ElapsedMilliseconds,OperationCount\n")

        for result in results:
            f.write(
                f"{result.algorithm_name},"
                f"{result.input_size},"
                f"{result.ordering_type},"
                f"{result.run_number},"
                f"{result.elapsed_milliseconds:.4f},"
                f"{result.operation_count}\n"
            )