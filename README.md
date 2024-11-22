# MSCS532_Assignment6

This repository contains implementations of various data structures and selection algorithms in Python. Each data structure and algorithm is implemented as a class or function with methods to perform common operations.

## Data Structures

### Array
An array is a collection of elements identified by index or key. The `Array` class provides methods to insert, delete, and access elements.

### Stack
A stack is a collection of elements that follows the Last In First Out (LIFO) principle. The `Stack` class provides methods to push, pop, peek, and check if the stack is empty.

### Queue
A queue is a collection of elements that follows the First In First Out (FIFO) principle. The `Queue` class provides methods to enqueue, dequeue, peek, and check if the queue is empty.

### Singly Linked List
A singly linked list is a collection of nodes where each node contains a value and a reference to the next node in the sequence. The `SinglyLinkedList` class provides methods to insert, delete, and traverse the list.

## Selection Algorithms

### Median of Medians
The `median_of_medians` function is an efficient selection algorithm to find the k-th smallest element in an unsorted list. It uses the median of medians as a pivot to partition the list.

### Randomized Quickselect
The `randomized_quickselect` function is a selection algorithm that uses a random pivot to partition the list and recursively find the k-th smallest element.

## Demonstration

The `demonstrate` function in `dataStructures.py` shows how to use each of the data structures. It performs the following operations:

1. **Array**:
    - Insert values at specific indices.
    - Delete a value at a specific index.
    - Access a value at a specific index.

2. **Stack**:
    - Push values onto the stack.
    - Pop a value from the stack.

3. **Queue**:
    - Enqueue values into the queue.
    - Dequeue a value from the queue.

4. **Singly Linked List**:
    - Insert values into the list.
    - Delete a value from the list.
    - Traverse the list and print the values.

The `test_selection_algorithms` function in `selectionAlgorithmImplementation.py` compares the performance of the `median_of_medians` and `randomized_quickselect` algorithms on different input sizes and distributions.

## Running the Demonstration

To run the demonstration for data structures, execute the `dataStructures.py` file:

```bash
python dataStructures.py
python3 dataStructures.py
```

To run the selection algorithms performance test, execute the `selectionAlgorithmImplementation.py` file:

```bash
python selectionAlgorithmImplementation.py
python3 selectionAlgorithmImplementation.py
```

