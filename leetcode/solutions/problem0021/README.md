LeetCode 21 "Merge Two Sorted Lists"
---

### **Algorithm Analysis: Merge Two Sorted Lists**

This problem requires merging two sorted singly-linked lists, `list1` and `list2`, into a single new sorted linked list. The new list should be formed by splicing together the nodes of the original two lists.

#### **Core Idea: Iterative Merging with a Dummy Node**

The most straightforward and efficient way to merge two sorted linked lists is to use an **iterative approach** with a **dummy node**. The dummy node simplifies the logic by providing a common starting point for the merged list, eliminating the need for special handling of the head node. We then traverse both input lists simultaneously, comparing their current nodes' values and linking the smaller node to the merged list.

#### **Step-by-Step Algorithm**

1.  **Initialize Dummy Node:**
    * `head = ListNode()`: Create a `dummy` node (named `head` in the code). This node will serve as a placeholder for the beginning of our merged list. Its `next` pointer will eventually point to the actual head of the merged list.
    * `current = head`: Initialize a `current` pointer to the `dummy` node. This `current` pointer will always point to the last node added to our merged list, making it easy to append new nodes.

2.  **Iterate and Compare (Main Merging Loop):**
    * `while list1 != None and list2 != None:`: This loop continues as long as both `list1` and `list2` have nodes remaining.
    * **Compare Values:**
        * `if list1.val >= list2.val:`: If the current value in `list2` is less than or equal to the current value in `list1` (the problem states non-decreasing, so equal values are fine), we pick the node from `list2`.
            * `current.next = list2`: Link the `list2`'s current node to the merged list (via `current.next`).
            * `list2 = list2.next`: Advance `list2` to its next node.
        * `else:` (i.e., `list1.val < list2.val`): If the current value in `list1` is smaller, we pick the node from `list1`.
            * `current.next = list1`: Link the `list1`'s current node to the merged list.
            * `list1 = list1.next`: Advance `list1` to its next node.
    * **Advance `current`:**
        * `current = current.next`: In both `if` and `else` branches, after linking a node, the `current` pointer must advance to this newly added node so that the next node can be appended correctly.

3.  **Append Remaining Nodes:**
    * `current.next = list2 or list1`: After the loop finishes, one of the lists (or both, if they ended simultaneously) will be exhausted (`None`). The other list might still have remaining nodes. Since both original lists were sorted, all remaining nodes in the non-exhausted list are already sorted and are greater than or equal to all nodes already added to the merged list.
    * We simply append the remainder of the non-exhausted list to the end of our merged list. Python's `or` operator is handy here: `list2 or list1` will return `list2` if `list2` is not `None`, otherwise it returns `list1` (which could also be `None`). This correctly handles the cases where `list1` is exhausted, `list2` is exhausted, or both are exhausted.

4.  **Return Merged List Head:**
    * `return head.next`: The actual head of the merged list is the node immediately after our `dummy` node (`head` in the code).

#### **Complexity Analysis**

* **Time Complexity: $O(M + N)$**
    * Where `M` is the length of `list1` and `N` is the length of `list2`.
    * The `while` loop continues until one of the lists is exhausted. In each iteration, we perform constant-time operations and move the pointer of one of the lists forward by one node.
    * In total, each node from both `list1` and `list2` is visited and processed exactly once.
    * Therefore, the total time taken is proportional to the sum of the lengths of the two input lists.

* **Space Complexity: $O(1)$**
    * The algorithm uses a constant number of extra variables (`head`/`dummy`, `current`, `list1`, `list2`).
    * It does not create any new nodes (it re-links existing nodes from the input lists) or use data structures whose size grows with the input.

#### **Advantages of this Algorithm**

* **Efficiency:** Achieves optimal linear time complexity, as each node is visited only once.
* **Constant Space:** Uses a minimal amount of auxiliary memory, making it very space-efficient.
* **Simplicity and Readability:** The iterative approach with a dummy node is generally straightforward to implement and understand.
* **In-Place Modification:** The solution modifies the `next` pointers of the existing nodes rather than creating entirely new nodes, which is efficient in terms of memory allocation.
