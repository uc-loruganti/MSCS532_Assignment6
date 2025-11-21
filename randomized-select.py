import random

def partition(arr, low, high):
    pivot_value = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def RANDOMIZED_SELECT(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    pivot_index = partition(arr, left, right)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return RANDOMIZED_SELECT(arr, left, pivot_index - 1, k)
    else:
        return RANDOMIZED_SELECT(arr, pivot_index + 1, right, k)

if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    kth_smallest = RANDOMIZED_SELECT(arr, 0, len(arr) - 1, k - 1)