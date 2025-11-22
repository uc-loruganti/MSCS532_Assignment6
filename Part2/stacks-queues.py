# Class which implements Stack
class Stack:
    def __init__(self):
        self.items = []

    # Push item onto stack
    def push(self, item):
        self.items.append(item)

    # Pop item from stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    # Return top item from stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    # Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return size of stack
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Class which implements Queue
class Queue:
    def __init__(self):
        self.items = []

    # Add item to the end of the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # Remove item from the front of the queue   
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("dequeue from empty queue")

    # Return front item from queue
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    # Check if queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return size of queue
    def size(self):
        return len(self.items)

    # String representation of the queue
    def __str__(self):
        return str(self.items)

def stacks_queues_examples():
    # Stack Example
    print("Stack Example:")
    my_stack = Stack()
    print("Is stack empty?", my_stack.is_empty())
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    print("Stack after pushes:", my_stack)
    print("Top element is:", my_stack.peek())
    print("Popped element:", my_stack.pop())
    print("Stack after pop:", my_stack)
    print("Stack size:", my_stack.size())

    print("\n" + "="*20 + "\n")

    # Queue Example
    print("Queue Example:")
    my_queue = Queue()
    print("Is queue empty?", my_queue.is_empty())
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    print("Queue after enqueues:", my_queue)
    print("Front element is:", my_queue.peek())
    print("Dequeued element:", my_queue.dequeue())
    print("Queue after dequeue:", my_queue)
    print("Queue size:", my_queue.size())


if __name__ == "__main__":
    stacks_queues_examples()
