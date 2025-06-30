Leetcode 653: Two Sum IV - Input is a BST
___
### **Algorithm Analysis: Two Sum IV - Input is a BST**

This problem extends the "Two Sum" concept to a Binary Search Tree (BST). Given the root of a BST and a target sum `k`, we need to determine if there exist two distinct nodes in the BST whose values sum up to `k`.

#### **Core Idea: Two-Pointer Technique on a BST**

The solution cleverly adapts the Two-Pointer Technique, which is highly effective for sorted arrays, to a BST. A BST inherently stores its elements in a sorted manner (in-order traversal yields elements in non-decreasing order). The challenge is to efficiently access the "next smallest" and "next largest" elements without converting the entire BST into a sorted array, which would require $O(N)$ extra space.

This algorithm uses two pointers (or rather, two "current node" references) and two auxiliary stacks to simulate an in-order traversal from the leftmost node (ascending order) and a reverse in-order traversal from the rightmost node (descending order).

#### **Step-by-Step Algorithm**

1.  **Handle Empty/Single Node Tree:**
    * A preliminary check for an empty tree (`if not root: return False`) is implicitly handled by how `left` and `right` are used. If `root` is a single node (no children), both `left` and `right` will point to `root`. The main `while left.val != right.val:` loop condition will be `False`, and the function correctly returns `False` (as a single node cannot form a sum with another distinct element).

2.  **Initialize Pointers and Stacks:**
    * `left` pointer: Initialized to `root`.
    * `right` pointer: Initialized to `root`.
    * `left_parents`: An empty stack (list) to store ancestor nodes during the leftward traversal.
    * `right_parents`: An empty stack (list) to store ancestor nodes during the rightward traversal.

3.  **Find Initial Smallest (`left`) and Largest (`right`) Elements:**
    * **Smallest (`left`):** Traverse from `root` down its left child chain. For each node encountered (except the leftmost node itself), push it onto `left_parents`. When `left` reaches the leftmost node (the smallest value in the BST), the `left_parents` stack will contain its ancestors.
    * **Largest (`right`):** Symmetrically, traverse from `root` down its right child chain. Push each node onto `right_parents`. When `right` reaches the rightmost node (the largest value in the BST), the `right_parents` stack will contain its ancestors.

4.  **Two-Pointer Convergence Loop:**
    * Enter a `while` loop that continues as long as `left.val` is not equal to `right.val`. This condition ensures we are considering two distinct nodes.

5.  **Calculate Current Sum and Adjust Pointers:**
    * Calculate `current_sum = left.val + right.val`.
    * **Case 1: `current_sum == k`**
        * If the sum equals `k`, we've found the pair. Return `True`.
    * **Case 2: `current_sum > k`**
        * The sum is too large. We need to decrease the sum by moving `right` to the next smaller element (its in-order predecessor).
        * If `right` has a left child: The predecessor is the rightmost node in `right.left`'s subtree. The code handles this by setting `node = right.left`, then pushing `node` and its right-descendants onto `right_parents`, and finally popping the actual predecessor.
        * If `right` has no left child: The predecessor is found by traversing up `right_parents` until an ancestor is found where `right` was in its right subtree. The code implicitly handles this by simply popping from `right_parents`.
        * The `right = right_parents.pop()` (after potentially pushing more nodes) effectively moves `right` to its in-order predecessor.
    * **Case 3: `current_sum < k`**
        * The sum is too small. We need to increase the sum by moving `left` to the next larger element (its in-order successor).
        * This logic is symmetric to Case 2. If `left` has a right child, the successor is the leftmost node in `left.right`'s subtree. Otherwise, it's found by moving up `left_parents`.
        * The `left = left_parents.pop()` (after potentially pushing more nodes) effectively moves `left` to its in-order successor.

6.  **No Solution:**
    * If the loop finishes (i.e., `left.val == right.val`), it means all possible distinct pairs have been checked, and no solution was found. Return `False`.

#### **Complexity Analysis**

* **Time Complexity: $O(N)$**
    * **Initialization:** The initial traversal to find the leftmost and rightmost nodes takes $O(H)$ time, where $H$ is the height of the BST.
    * **Main Loop:** In each iteration, either the `left` pointer advances to the next in-order successor or the `right` pointer advances to the next in-order predecessor. Each node in the BST is pushed onto a stack at most once and popped from a stack at most once. The total work performed in advancing the pointers throughout the entire algorithm is proportional to the number of nodes.
    * Therefore, the overall time complexity is **$O(N)$**, where $N$ is the number of nodes in the BST.

* **Space Complexity: $O(H)$**
    * The `left_parents` and `right_parents` stacks store nodes on the path from the root to the current `left` and `right` nodes, respectively. The maximum size of these stacks is equal to the height of the BST.
    * In the worst case (a completely skewed tree, like a linked list), $H = O(N)$, so the space complexity is **$O(N)$**.
    * In the best/average case (a balanced BST), $H = O(\log N)$, resulting in **$O(\log N)$** space complexity.

#### **Advantages of this Algorithm**

* **Efficient Time Complexity:** Achieves an optimal $O(N)$ time complexity for traversing all necessary nodes.
* **No Full Array Conversion:** Avoids converting the entire BST into a sorted array, which would also require $O(N)$ space. This method is generally preferred over converting the tree to an array when extra space is a concern beyond just $O(N)$.
* **Direct BST Manipulation:** Operates directly on the BST structure, leveraging its properties.
