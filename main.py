# main.py
#
# Entry point for the sorting experiment application.
# Menu-driven interface; follow the prompts to generate input files
# or run sorting experiments.

import os
from input_generator import generate
from experiment_runner import run_experiment
from result_reporter import write_results
from sorting_algorithm import merge_sort

# --- Import your algorithms here once implemented ---
# from sorting_algorithm import bubble_sort, insertion_sort


def handle_generate() -> None:
    print("\n-- Generate Input File --")

    size = prompt_int("Number of integers to generate: ", min_val=1)

    print("Ordering types: random, sorted, reverse, nearlysorted")
    ordering = prompt_string("Ordering type: ",
                             ["random", "sorted", "reverse", "nearlysorted"])

    output_file = prompt_path("Output file path (e.g. data/random_10000.txt): ")

    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else ".", exist_ok=True)
    generate(output_file, size, ordering)


def handle_run() -> None:
    print("\n-- Run Sorting Experiments --")

    input_file = prompt_existing_file("Input file path: ")

    print("Ordering types: random, sorted, reverse, nearlysorted")
    ordering = prompt_string("Ordering type of this file: ",
                             ["random", "sorted", "reverse", "nearlysorted"])

    runs = prompt_int("Number of runs per algorithm: ", min_val=1)

    results_file = prompt_path("Results file path (e.g. results/results.csv): ")
    os.makedirs(os.path.dirname(results_file) if os.path.dirname(results_file) else ".", exist_ok=True)

    print(f"\nRunning experiments on: {input_file}")
    print(f"Ordering: {ordering}, Runs per algorithm: {runs}\n")

    # --- Merge Sort ---
    print("Running Merge Sort...")
    results = run_experiment("MergeSort", merge_sort, input_file, ordering, runs)
    write_results(results, results_file)

    # --- Add your algorithms below this line ---
    # Follow the same pattern as MergeSort above.
    # Example structure (do not uncomment, implement your own):
    #
    # print("Running Bubble Sort...")
    # results = run_experiment("BubbleSort", bubble_sort, input_file, ordering, runs)
    # write_results(results, results_file)
    #
    # print("Running Insertion Sort...")
    # results = run_experiment("InsertionSort", insertion_sort, input_file, ordering, runs)
    # write_results(results, results_file)

    print(f"\nResults written to: {results_file}")


def prompt_int(message: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        try:
            value = int(input(message).strip())
            if min_val is not None and value < min_val:
                print(f"Please enter a value of at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a value of at most {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def prompt_string(message: str, valid_options: list[str]) -> str:
    while True:
        value = input(message).strip().lower()
        if value in valid_options:
            return value
        print(f"Please enter one of: {', '.join(valid_options)}")


def prompt_path(message: str) -> str:
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Please enter a valid file path.")


def prompt_existing_file(message: str) -> str:
    while True:
        value = input(message).strip()
        if os.path.isfile(value):
            return value
        print(f"File not found: {value}. Please try again.")


def main() -> None:
    print("\nSorting Experiment")
    print("==================")

    running = True
    while running:
        print("\nWhat would you like to do?")
        print("  1. Generate an input file")
        print("  2. Run sorting experiments")
        print("  3. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            handle_generate()
        elif choice == "2":
            handle_run()
        elif choice == "3":
            running = False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()