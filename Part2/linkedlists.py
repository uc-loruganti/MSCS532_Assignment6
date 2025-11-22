# Node and LinkedList classes implementation
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    # Insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Delete a node by value
    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    # Traverse and print the linked list
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    
    def __str__(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(elements) + " -> None"


def linked_list_examples():
    # Linked List Example
    print("Linked List Example:")
    linked_list = LinkedList()

    print("Is list empty?", linked_list.is_empty()) 

    linked_list.insert_at_beginning(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_beginning(0)
    linked_list.insert_at_end(3)

    print("List after insertions:", linked_list)
    print("List size:", linked_list.size())

    print("Traversing the list:")
    linked_list.traverse()
    
    linked_list.delete(2)
    print("List after deleting 2:", linked_list)
    
    linked_list.delete(0)
    print("List after deleting 0:", linked_list)

if __name__ == "__main__":
    linked_list_examples()
