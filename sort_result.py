# sort_result.py
#
# A simple data class that holds the result of a single sorting experiment run.
# Records the algorithm name, input characteristics, timing, and operation count.
# You do not need to modify this file.

from dataclasses import dataclass

@dataclass
class SortResult:
    algorithm_name: str
    input_size: int
    ordering_type: str
    run_number: int
    elapsed_milliseconds: float
    operation_count: int