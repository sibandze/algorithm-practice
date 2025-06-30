/*
Problem: "Two Sum IV - Input is a BST"
Problem statement: "Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise."
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.Deque;
import java.util.ArrayDeque;
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        TreeNode left = root, right = root, node = null;
        if (root.left == null && root.right == null){
            return false; // No two elements
        }
        Deque<TreeNode> left_parents = new ArrayDeque<>();
        while (left.left!=null){
            left_parents.push(left);
            left = left.left;
        }
        Deque<TreeNode> right_parents = new ArrayDeque<>();
        while (right.right != null){
            right_parents.push(right);
            right = right.right;
        }
        while (left.val != right.val){
            if (left.val + right.val == k){
                return true;
            }
            else if (left.val + right.val > k){
                node = right.left;
                while (node != null){
                    right_parents.push(node);
                    node = node.right;
                }
                right = right_parents.pop();
            }
            else{
                node = left.right;
                while (node!=null){
                    left_parents.push(node);
                    node = node.left;
                }
                left = left_parents.pop();
            }
        }
        return false;
    }  
}
