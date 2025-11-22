import argparse
import sys

def median_of_medians(arr, k):

    if arr is None or k < 0 or k >= len(arr):
        return None

    # Base case: If the array is small, sort it and return the k-th element.
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide the array into subarrays of 5 elements.
    subarrays = []
    for i in range(0, len(arr), 5):
        subarrays.append(sorted(arr[i:i + 5]))

    # Step 2: Find the median of each subarray.
    medians = []
    for sub in subarrays:
        median = sub[len(sub) // 2] if len(sub) % 2 == 1 else (sub[len(sub) // 2 - 1] + sub[len(sub) // 2]) / 2
        medians.append(median)

    # Step 3: Recursively find the median of the medians to use as a pivot.
    # This recursive call is on a list of size n/5, leading to the O(n) guarantee.
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = median_of_medians(medians, len(medians) // 2)

    # Step 4: Partition the array around the pivot.
    # Elements are grouped into less than, equal to, and greater than the pivot.
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    # Step 5: Recurse on the appropriate partition.
    if k < len(smaller):
        return median_of_medians(smaller, k)
    elif k < len(smaller) + len(equal):
        # The k-th element is the pivot itself.
        return pivot
    else:
        # Adjust k and recurse on the 'larger' partition.
        return median_of_medians(larger, k - len(smaller) - len(equal))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find the k-th smallest element among unique elements in an array using the Median of Medians algorithm.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-elements", nargs='+', type=int, help="A space-separated list of integers.")
    parser.add_argument("-k", type=int, help="The order of the smallest element to find (e.g., 1 for 1st smallest).")
    args = parser.parse_args()

    arr = args.elements
    k = args.k

    if arr is None or len(arr) == 0:
        print("Error: The array cannot be empty.", file=sys.stderr)
        exit(1)

    if k < 1 or k > len(arr):
        print(f"Error: k ({k}) is out of bounds. It must be between 1 and the number of unique elements ({len(arr)}).", file=sys.stderr)
        exit(1)

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted(arr)}")
    # print(f"Finding the {k}-th smallest unique element...")

    # The algorithm uses a 0-based index, so convert k.
    kth_smallest = median_of_medians(arr, k - 1)
    
    print(f"The {k}-th smallest element is: {kth_smallest}")
