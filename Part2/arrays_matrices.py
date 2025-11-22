# Class which implements Array functionality
class Array:
    def __init__(self, size=0, initial_values=None):
        if initial_values:
            self.data = list(initial_values)
            self.size = len(initial_values)
        else:
            self.data = [None] * size
            self.size = size

    def insert(self, index, value):
        if 0 <= index < self.size:
            self.data.insert(index, value)
            self.size += 1
        else:
            raise IndexError("Index out of bounds for insertion")

    def delete(self, index):
        if 0 <= index < self.size:
            del self.data[index]
            self.size -= 1
        else:
            raise IndexError("Index out of bounds for deletion")

    def access(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds for access")

    def __str__(self):
        return str(self.data[:self.size])

# Class which implements Matrix functionality
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[None for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                self.data[r][c] = None

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Matrix index out of bounds")

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Matrix index out of bounds")

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

def array_matrix_examples():
    # Array Usage Example
    print("Array Example:")
    my_array = Array(initial_values=[1, 2, 3, 4, 5])
    print("Initial array:", my_array)
    my_array.insert(2, 10)
    print("After inserting 10 at index 2:", my_array)
    my_array.delete(3)
    print("After deleting element at index 3:", my_array)
    print("Element at index 1:", my_array.access(1))

    print("\n" + "="*20 + "\n")

    # Matrix Usage Example
    print("Matrix Example:")
    my_matrix = Matrix(3, 4)
    print("Initial 3x4 matrix:")
    print(my_matrix)
    
    # Set some values
    print("\nSetting some values in the matrix: (0, 0, 1), (1, 1, 2), (2, 2, 3)")
    my_matrix.set(0, 0, 1)
    my_matrix.set(1, 1, 2)
    my_matrix.set(2, 2, 3)
    print("\nMatrix after setting some values:")
    print(my_matrix)
    
    print("\nElement at (1, 1):", my_matrix.get(1, 1))

if __name__ == "__main__":
    array_matrix_examples()
