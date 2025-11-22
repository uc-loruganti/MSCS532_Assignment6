# MSCS532 Assignment 6: Selection Algorithms

This assignment explores two non-comparison-based selection algorithms for finding the k-th smallest element in an unordered list: Randomized Select and Median of Medians.

## Algorithms

### Randomized Select

The `randomized_select.py` script implements the randomized selection algorithm. This algorithm finds the k-th smallest element in an array by recursively partitioning the array and searching only in the part of the array that contains the desired element.

#### How to Run

To run the script, provide the list of elements and the value of `k` as command-line arguments.

```bash
python randomized_select.py -elements <list of integers> -k <k-th smallest element>
```

**Example:**

```bash
python randomized_select.py -elements 10 4 5 8 6 11 26 -k 3
```

This will output the 3rd smallest element in the given list.

### Median of Medians

The `medianofmedians_select.py` script implements the Median of Medians algorithm. This algorithm guarantees finding the k-th smallest element in linear time O(n). It works by dividing the array into groups of five elements, finding the median of each group, and then recursively finding the median of those medians to use as a pivot.

#### How to Run

To run the script, provide the list of elements and the value of `k` as command-line arguments.

```bash
python medianofmedians_select.py -elements <list of integers> -k <k-th smallest element>
```

**Example:**

```bash
python medianofmedians_select.py -elements 10 4 5 8 6 11 26 -k 3
```

This will output the 3rd smallest element in the given list.
