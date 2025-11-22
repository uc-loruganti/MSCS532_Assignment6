from arrays_matrices import array_matrix_examples
from stacks_queues import stacks_queues_examples
from linkedlists import linked_list_examples

if __name__ == "__main__":
    # Interactive menu to select which data structure to test
    while True:
        print("\nWhich data structure would you like to test?")
        print("1. Arrays and Matrices")
        print("2. Stacks and Queues")
        print("3. Linked Lists")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            array_matrix_examples()
        elif choice == '2':
            stacks_queues_examples()
        elif choice == '3':
            linked_list_examples()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")