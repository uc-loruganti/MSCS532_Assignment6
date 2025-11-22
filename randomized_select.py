import random
import argparse

# Function to partition the array around the pivot and return the pivot index
# This will rearrange the elements in the array so that all elements less than the pivot
# are on the left, and all elements greater than the pivot are on the right.
def partition(arr, low, high):
    pivot_value = arr[high]
    print(f"Chosen pivot: {pivot_value}")
    print(f"Current array state: {arr}")
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized Select function to find the k-th smallest element (order statistic) in the array
def RANDOMIZED_SELECT(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_index = random.randint(left, right)
    
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    pivot_index = partition(arr, left, right)
    print(f"Pivot index after partition: {pivot_index}")
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return RANDOMIZED_SELECT(arr, left, pivot_index - 1, k)
    else:
        return RANDOMIZED_SELECT(arr, pivot_index + 1, right, k)


if __name__ == "__main__":
    # To run the script with different inputs, provide the k value and the list of elements as command line arguments
    parser = argparse.ArgumentParser(description="Find the k-th smallest element in an array.")
    parser.add_argument("-elements", nargs='+', type=int, help="The list of integers.")
    parser.add_argument("-k", type=int, help="The order of the smallest element to find.")
    args = parser.parse_args()
    arr = args.elements
    k = args.k

    if k < 1 or k > len(arr):
        print("Error: k should be between 1 and the length of the array.")
        exit(1)
    
    if(arr is None or len(arr) == 0):
        print("Error: The array should not be empty.")
        exit(1)
    
    print(f"Original array: {arr}")
    print(f"Finding the {k}-th smallest element...")

    kth_smallest = RANDOMIZED_SELECT(arr, 0, len(arr) - 1, k - 1)
    print(f"The {k}-th smallest element is: {kth_smallest}")