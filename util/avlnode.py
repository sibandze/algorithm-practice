from util import BSTNode
class AVLNode(BSTNode):
    """
    Represents a node specifically for an AVL Tree.
    Inherits from BSTNode, gaining data, left, and right pointers.
    Adds the 'height' attribute crucial for AVL balancing.
    """
    def __init__(self, data):
        super().__init__(data) # Initialize data, left, right from BSTNode
        self.height = 1 # AVL nodes start with a height of 1 (a leaf node)
        # You might also include a parent pointer if your AVL implementation needs it:
        # self.parent = None

    def __repr__(self):
        # Extend BSTNode's repr to include height
        return f"AVLNode(data={self.data}, height={self.height}, left={repr(self.left)}, right={repr(self.right)})"
