# input_generator.py
#
# Generates integer input files for sorting experiments.
# Supports four ordering types:
#   random      - integers in a random order
#   sorted      - integers in ascending order
#   reverse     - integers in descending order
#   nearlysorted - mostly sorted with a small number of random swaps applied
#
# Nearly sorted input simulates real-world data that is mostly ordered but not
# perfectly so. The swap fraction constant below controls how many elements are
# displaced from their sorted positions.

import random
import os

NEARLY_SORTED_SWAP_FRACTION = 0.05


def generate(file_path: str, size: int, ordering_type: str, seed: int = 42) -> None:
    """
    Generates an input file at the specified path.

    Parameters:
        file_path:     Destination file path.
        size:          Number of integers to generate.
        ordering_type: One of: random, sorted, reverse, nearlysorted
        seed:          Random seed for reproducibility.
    """
    rng = random.Random(seed)
    data = _generate_data(size, ordering_type, rng)

    os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else ".", exist_ok=True)

    with open(file_path, "w") as f:
        for value in data:
            f.write(f"{value}\n")

    print(f"Generated {size} integers ({ordering_type}) -> {file_path}")


def _generate_data(size: int, ordering_type: str, rng: random.Random) -> list[int]:
    data = list(range(1, size + 1))

    if ordering_type == "random":
        rng.shuffle(data)
        return data

    elif ordering_type == "sorted":
        return data

    elif ordering_type == "reverse":
        return list(reversed(data))

    elif ordering_type == "nearlysorted":
        return _nearly_sort(data, rng)

    else:
        raise ValueError(
            f"Unknown ordering type: '{ordering_type}'. "
            f"Use random, sorted, reverse, or nearlysorted."
        )


def _nearly_sort(data: list[int], rng: random.Random) -> list[int]:
    nearly = data[:]
    swap_count = max(1, int(len(data) * NEARLY_SORTED_SWAP_FRACTION))

    for _ in range(swap_count):
        a = rng.randrange(len(nearly))
        b = rng.randrange(len(nearly))
        nearly[a], nearly[b] = nearly[b], nearly[a]

    return nearly