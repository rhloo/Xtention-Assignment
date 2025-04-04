class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize empty linked list

    def insert(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node  # Insert at the end

    def display(self):
        """Print the linked list."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev to current
            current = next_node  # Move current to next
        self.head = prev  # Update head to the new first node
# Create a linked list and insert elements
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

print("Original Linked List:")
ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Reverse the linked list
ll.reverse()

print("Reversed Linked List:")
ll.display()  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
