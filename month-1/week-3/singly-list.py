class Node:
    def __init__(self, data):
        self.data = data  # Store the node's data
        self.next = None  # Pointer to the next node (default is None)

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

    def delete_node(self, key):
        # Delete the first occurrence of the key in the list
        current = self.head

        if current and current.data == key:
            # If the head is the node to be deleted
            self.head = current.next
            return

        # Traverse to find the node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            return  # Key not found

        # Skip the node to be deleted
        prev.next = current.next

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
sll.display()  # Output: 1 -> 2 -> 3 -> None
sll.delete_node(2)
sll.display()  # Output: 1 -> 3 -> None
