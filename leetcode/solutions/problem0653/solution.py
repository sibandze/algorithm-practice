# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Problem: "Two Sum IV - Input is a BST"
#Problem statement: "Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise."
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left = root
        right = root
        if not root.left and not root.right:
            return False # No two elements
        
        left_queue = []
        while left.left:
            left_queue.append(left)
            left = left.left
        
        right_queue = []
        while right.right:
            right_queue.append(right)
            right = right.right
        
        while left.val != right.val:
            if left.val + right.val == k:
                return True
            
            elif left.val + right.val > k:
                node = right.left
                while node:
                    right_queue.append(node)
                    node = node.right
                
                right = right_queue.pop()
            
            else:
                node = left.right
                while node:
                    left_queue.append(node)
                    node = node.left
                
                left = left_queue.pop()
            
        return False        
