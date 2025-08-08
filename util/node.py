class Node:
    """
    Base class for all nodes.
    Provides a common structure for data and potentially a reference to the next node (for linked lists).
    """
    def __init__(self, data):
        self.data = data
        self.next = None # Primarily for linked list, can be None for trees

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Node({self.data})"
