# Linked Lists: Singly, doubly, and circular linked lists.

Linked lists are linear data structures where elements, called nodes, are linked using pointers. <br/> 
Unlike arrays, linked lists do not have a fixed size, making them more flexible for dynamic memory usage.

# Key Concepts

1. Singly Linked List
    - Each node contains:
        - Data.
        - A pointer to the next node.
    - Traversal is one-way (from head to tail).

2. Doubly Linked List
    - Each node contains:
        - Data.
        - A pointer to the next node
        - A pointer to the previous node.
    - Traversal can happen in both directions.

3. Circular Linked List
- Similar to singly or doubly linked lists, but the last node links back to the first node, creating a cycle.


# Why Are Linked Lists Useful?

1. **Dynamic Memory Allocation**: Elements can be added or removed without resizing.
2. **Efficient Insert/Delete**: O(1) insertion and deletion (with a known node).
3. **Use Cases**:
    - Implementing stacks, queues, or hash maps.
    - Undo functionality in text editors (using doubly linked lists).

# When to Use Linked Lists
  - When frequent insertions or deletions are needed.
  - To avoid resizing issues in arrays.
  - When memory usage needs to be dynamic (e.g., real-time systems).

# Code Samples

1. Singly Linked List. See `singley-list.py` for code.

2. Doubly Linked List. See `Doubly-list.py` for code.

3. Circular linked List. See `circular-list.py` for code.

# How To Analyze Complexity
- **Singly/Doubly/Circular Linked Lists**:
    - Insert at head: 0(1)
    - Insert at end: 0(n) (traversal needed)
    - Delete node: 0(n) (If traversal needed)
    - Search: 0(n)

- Space Complexity:
 - Each node requires O(1) space.
 - Total space: O(n) for n nodes.

 # Practice Problem
 Wrote a function to reverse a singly linked list that returns the new head of the list. See `practice-problem.py` for code.