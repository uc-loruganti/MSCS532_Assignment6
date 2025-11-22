#  Find the k-th smallest element in an array using the Median of Medians algorithm
import argparse

# Function to partition the array around the pivot and return the pivot index
def partition(arr, low, high, pivot_index):
    print(f"Pivot Index: {pivot_index}")
    # print(f"Pivot Valuearr[pivot_index]}")
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

# Median of Medians algorithm to find the k-th smallest element
# This function recursively finds the k-th smallest element in the array
def median_of_medians(arr, k):
    if not arr:
        return None

    # Divide the array by 5  to split the array into subarrays of 5 elements each
    subarrays = []
    for i in range(0, len(arr), 5):
        subarrays.append(arr[i:i+5])

    # Find the median of each subarray
    medians = []
    for subarray in subarrays:
        # Sort the subarray and find the median
        subarray.sort()
        # If the subarray has an odd number of elements, take the middle one as median else take the lower middle
        median = subarray[len(subarray) // 2] if len(subarray) % 2 == 1 else subarray[len(subarray) // 2 - 1]
        medians.append(median)

    # Find the median of the medians
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = median_of_medians(medians, len(medians) // 2)

    # Partition the original array around the pivot
    pivot_index = partition(arr, 0, len(arr) - 1, pivot)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return median_of_medians(arr[:pivot_index], k)
    else:
        return median_of_medians(arr[pivot_index + 1:], k - pivot_index - 1)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the k-th smallest element in an array using Median of Medians.")
    parser.add_argument("-elements", nargs='+', type=int, help="The list of integers.")
    parser.add_argument("-k", type=int, help="The order of the smallest element to find.")
    args = parser.parse_args()
    arr = args.elements
    k = args.k

    if k < 1 or k > len(arr):
        print("Error: k should be between 1 and the length of the array.")
        exit(1)

    if arr is None or len(arr) == 0:
        print("Error: The array should not be empty.")
        exit(1)

    print(f"Original array: {arr}")
    print(f"Finding the {k}-th smallest element...")

    kth_smallest = median_of_medians(arr, k - 1)
    print(f"The {k}-th smallest element is: {kth_smallest}")