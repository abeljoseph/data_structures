class Node:
    def __init__(self, data=None, next=None):
        """Node definition for linked list implementation."""
        self.data = data
        self.next = next
    
    def print_list(self):
        print("---")
        current = self
        while current:
            print(current.data)
            current = current.next


# Create a node with a data point
node_1 = Node(data=1)

# Create a second node; point the first node to it
node_2 = Node(data=2)
node_1.next = node_2

# Print the second node's data using the first node reference
print(node_1.next.data, "\n")

# Create a linked list of 10 nodes, with each node's data point being the integers 1-10, in order
start = Node(data=1)
current = start
for i in range(2,11):
    current.next = Node(data=i)
    current = current.next

# Print the linked list
start.print_list()

# Remove all odd numbers from the linked list
start = start.next  # We know data=1 for the first node
current = start
while current and current.next:
    if current.next.data % 2: 
        current.next = current.next.next  # List ends with even number, so will not throw error
    current = current.next

# Print the even list
start.print_list()

# Re-create linked list of 10 nodes, with each node's data point being the integers 1-10, in order
start = Node(data=1)
current = start
for i in range(2,11):
    current.next = Node(data=i)
    current = current.next

# Remove all even numbers from the linked list
current = start
while current and current.next:
    if (current.next.data % 2) == 0:
        if current.next.next: current.next = current.next.next
        else: current.next = None
    current = current.next

start.print_list()

# Merge two sorted lists, in ascending order
