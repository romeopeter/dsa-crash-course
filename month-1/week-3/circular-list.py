class CNode:
    def __init__(self, data):
        self.data = data  # Store the node's data
        self.next = None  # Pointer to the next node

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Head of the circular linked list

    def insert_at_end(self, data):
        new_node = CNode(data)
        if not self.head:
            # If the list is empty, the new node becomes the head and points to itself
            self.head = new_node
            new_node.next = self.head
            return
        # Traverse to the last node
        current = self.head
        while current.next != self.head:
            current = current.next
        # Link the last node to the new node, and the new node to the head
        current.next = new_node
        new_node.next = self.head

    def display(self):
        # Print the elements of the circular list
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

# Example Usage
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.display()  # Output: 1 -> 2 -> 3 -> (back to head)
