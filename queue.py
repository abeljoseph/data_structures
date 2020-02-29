class queue:
    """Queue implemented using a list."""
    def __init__(self):
        self.items = []

class Node:
    """General node for linked list implementation."""
    def __init__(self, data=None):
        self.data = data
        self.next = None
