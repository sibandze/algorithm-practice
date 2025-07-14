LeetCode 2 "Add Two Numbers", which is an **iterative approach using a dummy head node**
---

### **Algorithm Analysis: Add Two Numbers (Iterative with Dummy Head)**

This problem asks us to add two non-negative integers represented by linked lists, where digits are stored in reverse order. Each node contains a single digit. The goal is to return the sum as a new linked list, also with digits in reverse order. Leading zeros are not allowed, except for the number 0 itself.

The provided solution implements an iterative approach that constructs a *new* linked list to store the sum.

#### **Core Idea: Iterative Columnar Addition with New List Construction**

This method simulates manual columnar addition:
1.  **Iterate through digits:** Traverse both input linked lists simultaneously, starting from their heads (which represent the least significant digits).
2.  **Calculate sum and carry:** At each position (column), add the corresponding digits from `l1` and `l2` (treating `null` as 0), plus any `carry` from the previous column.
3.  **Create new node:** The unit digit of this sum becomes the value of a new node in the result list.
4.  **Propagate carry:** The tens digit of the sum becomes the new `carry` for the next column.
5.  **Handle remaining digits and final carry:** Continue this process until both lists are exhausted and there's no remaining `carry`.

A **dummy head node** is commonly used in linked list problems for simplified construction. It acts as a temporary placeholder before the actual head of the result list, avoiding special-case handling for the first node.

#### **Step-by-Step Algorithm**

1.  **Initialize Result List and Pointers:**
    * `ListNode dummy = new ListNode();`: Create a `dummy` node. This node won't be part of the final sum, but its `next` pointer will point to the actual head of the result list.
    * `ListNode node1 = l1, node2 = l2, node = dummy;`:
        * `node1`: A pointer to traverse `l1`.
        * `node2`: A pointer to traverse `l2`.
        * `node`: A pointer to traverse and build the new result list. It starts at `dummy`.
    * `int carry = 0, total = 0;`: Initialize `carry` to 0 and `total` to 0 for sum calculation.

2.  **Main Iteration Loop:**
    * `while(node1 != null || node2 != null)`: The loop continues as long as there are digits remaining in *either* `l1` or `l2`. This ensures that even if one list is longer, all its digits (and any carries) are processed.
    * **Determine current `total` sum:**
        * `if(node1 == null)`: If `l1` has been exhausted, only consider `node2.val` and `carry`. Then advance `node2`.
        * `else if(node2 == null)`: If `l2` has been exhausted, only consider `node1.val` and `carry`. Then advance `node1`.
        * `else`: If both lists still have nodes, sum `node1.val`, `node2.val`, and `carry`. Then advance both `node1` and `node2`.
    * **Create New Node for Result List:**
        * `node.next = new ListNode(total % 10);`: Create a new `ListNode` with the current digit (`total % 10`) and append it to the result list (by setting `node.next`).
    * **Advance Result List Pointer:**
        * `node = node.next;`: Move the `node` pointer to the newly created node, preparing for the next digit.
    * **Update `carry`:**
        * `carry = total / 10;`: Calculate the new `carry` for the next iteration.

3.  **Handle Final Carry (if any):**
    * `if(carry != 0)`: After the loop finishes, if there's a remaining `carry` (e.g., `[9] + [1]` results in `[0,1]`), a new node must be created for it.
    * `node.next = new ListNode(carry);`: Append this final `carry` as a new node.

4.  **Return Result:**
    * `return dummy.next;`: Return the `next` of the `dummy` node, which is the actual head of the sum linked list.

#### **Example Trace (`l1 = [2,4,3]`, `l2 = [5,6,4]`) representing `342 + 465 = 807`**

1.  **Initial:** `dummy = [0]`, `node1=[2,4,3]`, `node2=[5,6,4]`, `node=dummy`, `carry=0`, `total=0`. `ans = [0 -> null]`

2.  **Loop 1:** (`node1` and `node2` are not null)
    * `total = 2 + 5 + 0 = 7`
    * `node1 = [4,3]`, `node2 = [6,4]`
    * `node.next = new ListNode(7)` (`ans` is now `[0 -> 7]`)
    * `node = 7` node (`ans` is still `[0 -> 7]`, `node` points to `7`)
    * `carry = 0`

3.  **Loop 2:** (`node1` and `node2` are not null)
    * `total = 4 + 6 + 0 = 10`
    * `node1 = [3]`, `node2 = [4]`
    * `node.next = new ListNode(0)` (`ans` is now `[0 -> 7 -> 0]`)
    * `node = 0` node (`ans` is still `[0 -> 7 -> 0]`, `node` points to `0`)
    * `carry = 1`

4.  **Loop 3:** (`node1` and `node2` are not null)
    * `total = 3 + 4 + 1 = 8`
    * `node1 = null`, `node2 = null`
    * `node.next = new ListNode(8)` (`ans` is now `[0 -> 7 -> 0 -> 8]`)
    * `node = 8` node (`ans` is still `[0 -> 7 -> 0 -> 8]`, `node` points to `8`)
    * `carry = 0`

5.  **Loop 4:** (`node1` is null, `node2` is null)
    * Loop condition `node1 != null || node2 != null` is false. Loop terminates.

6.  **Handle Final Carry:**
    * `if (carry != 0)`: `carry` is `0`. Condition is false.

7.  **Return `dummy.next`:** Returns the head of the list `[7,0,8]`. Correct!

#### **Complexity Analysis**

Let $M$ be the length of `l1` and $N$ be the length of `l2`.

* **Time Complexity: $O(\max(M, N))$**
    * The `while` loop iterates once for each position, up to the length of the longer linked list.
    * Each iteration involves a constant number of arithmetic operations, pointer assignments, and `ListNode` creation.
    * Therefore, the total time complexity is linear with respect to the length of the longer input list.

* **Space Complexity: $O(\max(M, N))$**
    * A new `ListNode` is created for each digit of the sum. The sum list will have a length of $\max(M, N)$ or $\max(M, N) + 1$ (if there's a final carry).
    * This space is directly proportional to the length of the result list.

#### **Advantages of this Algorithm**

* **Standard and Robust:** This is a very common and robust iterative solution for adding linked lists. It handles all edge cases (unequal lengths, final carry) gracefully.
* **No Recursion Overhead:** Avoids the potential stack overflow issues that can arise with deep recursion for very long linked lists.
* **New List Construction:** Preserves the original input linked lists (`l1` and `l2`), which is often a desirable property.
* **Clear and Intuitive:** The step-by-step processing of digits and carry, along with the use of a dummy node, makes the logic easy to follow.
