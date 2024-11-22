
# Arrays
class Array:
    def __init__(self, size):
        # Initialize the array with None values and set the size
        self.array = [None] * size
        self.size = size

    def insert(self, index, value):
        # Insert value at the specified index if within bounds
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def delete(self, index):
        # Delete value at the specified index if within bounds
        if 0 <= index < self.size:
            self.array[index] = None
        else:
            raise IndexError("Index out of bounds")

    def access(self, index):
        # Access value at the specified index if within bounds
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")


# Stack
class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.stack = []

    def push(self, value):
        # Push value onto the stack
        self.stack.append(value)

    def pop(self):
        # Pop value from the stack if not empty
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        # Peek at the top value of the stack if not empty
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0


# Queue
class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.queue = []

    def enqueue(self, value):
        # Enqueue value to the queue
        self.queue.append(value)

    def dequeue(self):
        # Dequeue value from the queue if not empty
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Queue is empty")

    def peek(self):
        # Peek at the front value of the queue if not empty
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Queue is empty")

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0


# Linked List
class Node:
    def __init__(self, value):
        # Initialize a node with a value and no next node
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty linked list
        self.head = None

    def insert(self, value):
        # Insert a new node with the given value at the end of the list
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        # Delete the first node with the given value
        if not self.head:
            raise ValueError("List is empty")
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.value != value:
                current = current.next
            if current.next:
                current.next = current.next.next
            else:
                raise ValueError(f"Value {value} not found in the list")

    def traverse(self):
        # Traverse the list and return a list of values
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements


# Demonstration of all data structures
def demonstrate():
    print("Demonstrating Array:")
    arr = Array(5)
    arr.insert(0, 15)
    arr.insert(2, 25)
    arr.delete(0)
    print("Access index 2:", arr.access(2))

    print("\nDemonstrating Stack:")
    stack = Stack()
    stack.push(5)
    stack.push(10)
    print("Popped value:", stack.pop())

    print("\nDemonstrating Queue:")
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue(12)
    print("Dequeued value:", queue.dequeue())

    print("\nDemonstrating Linked List:")
    ll = SinglyLinkedList()
    ll.insert(7)
    ll.insert(14)
    ll.delete(7)
    print("Linked List Traversal:", ll.traverse())


# Run the demonstration
if __name__ == "__main__":
    demonstrate()