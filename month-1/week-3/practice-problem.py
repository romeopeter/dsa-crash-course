"""Reverse a singly linked list and return the head of the list"""


class Node:
    def __init__(self, data):
        self.data = data  # Store the node's data
        self.next = None  # Pointer to the next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list

    def insert_at_end(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        if not self.head:
            # If the list is empty, the new node becomes the head
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        # Link the last node to the new node
        current.next = new_node

    def reverse(self):
        # Reverse the linked list
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev and current one step forward
            current = next_node
        self.head = prev  # The prev pointer will be the new head of the list

    def display(self):
        # Print the elements of the list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)

print("Original list:")
sll.display()  # Output: 1 -> 2 -> 3 -> 4 -> None

sll.reverse()  # Reverse the list

print("Reversed list:")
sll.display()  # Output: 4 -> 3 -> 2 -> 1 -> None
