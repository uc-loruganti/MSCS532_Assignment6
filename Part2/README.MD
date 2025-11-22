# Data Structures Implementations

This project provides implementations of several common data structures in Python.

## Implemented Data Structures

*   **Arrays and Matrices**: Basic implementation of an array and a matrix with simple operations.
*   **Stacks and Queues**: Implementation of stack (LIFO) and queue (FIFO) data structures.
*   **Linked Lists**: A simple implementation of a singly linked list.

## How to Run the Code

To run the examples for the implemented data structures, execute the `main.py` script:

```bash
python main.py
```

It will prompt to choose a datastructure to run as follows :
```
Which data structure would you like to test?
1. Arrays and Matrices
2. Stacks and Queues
3. Linked Lists
4. Exit
```

This will run a set of predefined examples for each data structure. It also provides an interactive menu to test each data structure individually.

## Example Outputs

### Arrays and Matrices

```
Array Example:
Initial array: [1, 2, 3, 4, 5]
After inserting 10 at index 2: [1, 2, 10, 3, 4, 5]
After deleting element at index 3: [1, 2, 10, 4, 5]
Element at index 1: 2

====================

Matrix Example:
Initial 3x4 matrix:
None    None    None    None
None    None    None    None
None    None    None    None

Setting some values in the matrix: (0, 0, 1), (1, 1, 2), (2, 2, 3)

Matrix after setting some values:
1   None    None    None
None    2   None    None
None    None    3   None

Element at (1, 1): 2
```

### Linked Lists

```
Linked List Example:
Is list empty? True
List after insertions: 0 -> 1 -> 2 -> 3 -> None
List size: 4
Traversing the list:
0 -> 1 -> 2 -> 3 -> None
List after deleting 2: 0 -> 1 -> 3 -> None
List after deleting 0: 1 -> 3 -> None
```

### Stacks and Queues

```
Stack Example:
Is stack empty? True
Stack after pushes: [1, 2, 3]
Top element is: 3
Popped element: 3
Stack after pop: [1, 2]
Stack size: 2

====================

Queue Example:
Is queue empty? True
Queue after enqueues: [30, 20, 10]
Front element is: 10
Dequeued element: 10
Queue after dequeue: [30, 20]
Queue size: 2
```


### Files

*   `main.py`: The main script to run the examples.
*   `arrays_matrices.py`: Contains the implementation of the `Array` and `Matrix` classes.
*   `stacks_queues.py`: Contains the implementation of the `Stack` and `Queue` classes.
*   `linkedlists.py`: Contains the implementation of the `LinkedList` class.

## Time Complexity Analysis

### Array (`arrays_matrices.py`)

| Operation | Time Complexity |
| :--- | :--- |
| `__init__` | O(n) or O(k) |
| `insert` | O(n) |
| `delete` | O(n) |
| `access` | O(1) |

- `__init__`: O(k) if `initial_values` is provided (where k is the length of `initial_values`), O(n) if `size` is provided.
- `insert`: O(n) due to shifting elements.
- `delete`: O(n) due to shifting elements.
- `access`: O(1) for direct access.

### Matrix (`arrays_matrices.py`)

| Operation | Time Complexity |
| :--- | :--- |
| `__init__` | O(rows * cols) |
| `get` | O(1) |
| `set` | O(1) |

- `__init__`: O(rows * cols) to initialize the matrix.
- `get`, `set`: O(1) for direct access.

### Linked List (`linkedlists.py`)

| Operation | Time Complexity |
| :--- | :--- |
| `is_empty` | O(1) |
| `size` | O(n) |
| `insert_at_beginning` | O(1) |
| `insert_at_end` | O(n) |
| `delete` | O(n) |
| `traverse` | O(n) |

- `insert_at_end`, `delete`, `size`, `traverse`: O(n) as they require iterating through the list.
- `insert_at_beginning`, `is_empty`: O(1) as they are constant time operations.

### Stack (`stacks_queues.py`)

| Operation | Time Complexity |
| :--- | :--- |
| `push` | Amortized O(1) |
| `pop` | O(1) |
| `peek` | O(1) |
| `is_empty` | O(1) |
| `size` | O(1) |

- `push`: Amortized O(1).
- `pop`, `peek`, `is_empty`, `size`: O(1).

### Queue (`stacks_queues.py`)

| Operation | Time Complexity |
| :--- | :--- |
| `enqueue` | O(n) |
| `dequeue` | O(1) |
| `peek` | O(1) |
| `is_empty` | O(1) |
| `size` | O(1) |

- `enqueue`: O(n) due to using `list.insert(0, ...)`.
- `dequeue`, `peek`, `is_empty`, `size`: O(1).
