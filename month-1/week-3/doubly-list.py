class DNode:
    def __init__(self, data):
        self.data = data  # Store the node's data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the doubly linked list

    def insert_at_end(self, data):
        # Create a new node with the given data
        new_node = DNode(data)
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
        new_node.prev = current

    def delete_node(self, key):
        current = self.head

        # Find the node to delete
        while current and current.data != key:
            current = current.next

        if not current:
            return  # Key not found

        # If it's the head node
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev

    def display(self):
        # Print the elements of the list
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.display()  # Output: 1 <-> 2 <-> 3 <-> None
dll.delete_node(2)
dll.display()  # Output: 1 <-> 3 <-> None
