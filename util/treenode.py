from util import Node
class TreeNode(Node):
    """
    Represents a node in a general tree structure.
    Adds left and right child pointers, common for binary trees.
    Inherits data from the base Node class.
    """
    def __init__(self, data):
        super().__init__(data) # Initialize data and next from base Node
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode(data={self.data}, left={repr(self.left)}, right={repr(self.right)})"
