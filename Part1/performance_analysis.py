import timeit
import random
import sys
from medianofmedians_select import median_of_medians
from randomized_select import RANDOMIZED_SELECT

sys.setrecursionlimit(20000)

# Function to generate input data
def generate_input(size, distribution):
    """
    Generates an input array of a given size and distribution.
    """
    if distribution == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == "sorted":
        return list(range(size))
    elif distribution == "reverse-sorted":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Invalid distribution type")

# Function to run selection algorithms and measure execution time
def run_selection_algorithm(algorithm, data, k):
    """
    Runs a selection algorithm on the given data and returns the execution time.
    """
    # Make a copy of the data to avoid modifying the original list
    data_copy = data[:]
    
    # Prepare the selection function call
    if algorithm == "deterministic":
        select_func = median_of_medians
        # median_of_medians expects k as a 0-based index
        k_index = k - 1
    elif algorithm == "randomized":
        select_func = RANDOMIZED_SELECT
        # RANDOMIZED_SELECT expects k as a 0-based index
        k_index = k - 1
    else:
        raise ValueError("Invalid algorithm type")

    # Time the execution
    start_time = timeit.default_timer()
    if algorithm == "deterministic":
         select_func(data_copy, k_index)
    else:
         select_func(data_copy, 0, len(data_copy) - 1, k_index)
    end_time = timeit.default_timer()
    
    return end_time - start_time

def main():
    """
    Main function to run the performance analysis.
    """
    input_sizes = [10, 50, 100, 200, 500, 1000, 10000]
    distributions = ["random", "sorted", "reverse-sorted"]
    algorithms = ["deterministic ", "randomized"]

    print("| Input Size | Distribution | Algorithm | Execution Time (s) |")
    print("|---|---|---|---|")

    for size in input_sizes:
        for dist in distributions:
            for algo in algorithms:
                # Generate the input data
                input_data = generate_input(size, dist)
                
                # For selection algorithms, we need to choose a k
                # Let's find the median, so k = size // 2
                k = size // 2
                
                # Run the selection algorithm and measure execution time
                execution_time = run_selection_algorithm(algo, input_data, k)
                
                # Print the results in a markdown table format
                print(f"| {size} | {dist} | {algo} | {execution_time:.6f} |")

if __name__ == "__main__":
    main()