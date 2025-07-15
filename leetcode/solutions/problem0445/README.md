LeetCode 445 "Add Two Numbers II"
---

### **Algorithm Analysis: Add Two Numbers II**

This problem is a variation of "Add Two Numbers" (LeetCode 2). Here, the input linked lists represent non-negative integers where the **most significant digit comes first** (i.e., digits are in *forward* order). We need to return the sum as a new linked list, also in forward order. The follow-up question specifically asks if it can be solved without reversing the input lists.

#### **Core Idea: Using Stacks for Reverse Traversal**

Since the digits are given in forward order (MSB first), direct traversal from head to tail is like reading from left to right. However, for addition, we need to process digits from right to left (LSB first) to handle `carry` correctly.

The most common way to achieve this "reverse traversal" without actually reversing the linked lists themselves is to use **stacks**. By pushing all nodes of each list onto a stack, the last-in (LSB) will be the first-out, allowing us to process digits from right to left.

Once we have the digits summed with carries, we will have them in reverse (LSB first) order. To construct the final linked list in the required forward (MSB first) order, we can either:
1.  Push the sum digits onto *another* stack and then pop them to build the list.
2.  Prepend new nodes to a growing list.

The provided solution uses the first approach (another stack).

#### **Step-by-Step Algorithm**

1.  **Populate Stacks with Input List Nodes:**
    * `l1_stack = []` and `l2_stack = []`: Initialize two empty lists (which will function as stacks).
    * `while l1: l1_stack.append(l1); l1 = l1.next`: Traverse `l1`, pushing each `ListNode` onto `l1_stack`.
    * `while l2: l2_stack.append(l2); l2 = l2.next`: Traverse `l2`, pushing each `ListNode` onto `l2_stack`.
    * After these loops, the top of `l1_stack` (and `l2_stack`) will contain the LSB node of the original list.

2.  **Perform Columnar Addition Using Stacks:**
    * `ans_stack = []`: Initialize another empty list to store the `ListNode`s of the sum in reverse order (LSB first).
    * `carry = 0`: Initialize `carry` to 0.
    * `while l1_stack or l2_stack:`: This loop continues as long as there are digits left in either input stack.
        * `total = carry`: Start `total` with the current `carry`.
        * **Conditional Summing:**
            * `if l1_stack and l2_stack:`: If both stacks have digits, pop their values and add to `total`.
            * `elif l1_stack:`: If only `l1_stack` has digits, pop its value and add to `total`.
            * `else:` (Only `l2_stack` has digits): Pop its value and add to `total`.
        * `ans_stack.append(ListNode(total % 10))`: Create a new `ListNode` with the current digit (`total % 10`) and push it onto `ans_stack`. At this point, `ans_stack` will be filled with digits in LSB-first order.
        * `carry = total // 10`: Calculate the new `carry` for the next iteration.

3.  **Handle Final Carry:**
    * `if carry != 0:`: After the loop, if there's any remaining `carry` (e.g., adding `[5]` and `[5]` results in `[1,0]`), create a new node for it and push it onto `ans_stack`. This will be the new MSB.

4.  **Construct Result Linked List from `ans_stack`:**
    * `dummy = ListNode()`: Create a `dummy` head node to simplify building the result list.
    * `node = dummy`: Initialize a `node` pointer to `dummy`.
    * `while ans_stack:`: This loop builds the final linked list.
        * `node.next = ans_stack.pop()`: Pop a `ListNode` from `ans_stack`. Since `ans_stack` was built LSB-first and we are popping, we are retrieving nodes MSB-first. This `pop`ed node becomes the `next` of the current `node` in our result list.
        * `node = node.next`: Move `node` to the newly attached node.
    * `return dummy.next`: Return the `next` of the `dummy` node, which is the true head of the sum linked list (now in MSB-first order).

#### **Example Trace (`l1 = [7,2,4,3]`, `l2 = [5,6,4]`) representing `7243 + 564 = 7807`**

1.  **Populate Stacks:**
    * `l1_stack = [ListNode(7), ListNode(2), ListNode(4), ListNode(3)]` (bottom to top: 7->2->4->3)
    * `l2_stack = [ListNode(5), ListNode(6), ListNode(4)]` (bottom to top: 5->6->4)

2.  **Columnar Addition:**
    * `ans_stack = []`, `carry = 0`
    * **Iter 1 (LSB: 3, 4):**
        * `total = 3 + 4 + 0 = 7`
        * `ans_stack.append(ListNode(7))` (`ans_stack = [ListNode(7)]`)
        * `carry = 0`
    * **Iter 2 (next: 4, 6):**
        * `total = 4 + 6 + 0 = 10`
        * `ans_stack.append(ListNode(0))` (`ans_stack = [ListNode(7), ListNode(0)]`)
        * `carry = 1`
    * **Iter 3 (next: 2, 5):**
        * `total = 2 + 5 + 1 = 8`
        * `ans_stack.append(ListNode(8))` (`ans_stack = [ListNode(7), ListNode(0), ListNode(8)]`)
        * `carry = 0`
    * **Iter 4 (only l1: 7):**
        * `total = 7 + 0 = 7`
        * `ans_stack.append(ListNode(7))` (`ans_stack = [ListNode(7), ListNode(0), ListNode(8), ListNode(7)]`)
        * `carry = 0`
    * `l1_stack` and `l2_stack` are empty. Loop ends.

3.  **Handle Final Carry:** `carry` is `0`. No new node.

4.  **Construct Result List:**
    * `dummy = [0]`, `node = dummy`
    * `while ans_stack:`
        * **Pop 1:** `ListNode(7)` (MSB) from `ans_stack`. `node.next = ListNode(7)`. `node` moves to `7`. `result = [0->7]`
        * **Pop 2:** `ListNode(8)` from `ans_stack`. `node.next = ListNode(8)`. `node` moves to `8`. `result = [0->7->8]`
        * **Pop 3:** `ListNode(0)` from `ans_stack`. `node.next = ListNode(0)`. `node` moves to `0`. `result = [0->7->8->0]`
        * **Pop 4:** `ListNode(7)` (LSB) from `ans_stack`. `node.next = ListNode(7)`. `node` moves to `7`. `result = [0->7->8->0->7]`
    * `ans_stack` is empty. Loop ends.

5.  **Return `dummy.next`:** Returns the list `[7,8,0,7]`. Correct!

#### **Complexity Analysis**

Let $M$ be the length of `l1` and $N$ be the length of `l2`.

* **Time Complexity:** $O(M + N)$
    * Populating `l1_stack` takes $O(M)$ time.
    * Populating `l2_stack` takes $O(N)$ time.
    * The addition loop runs $O(\max(M, N))$ times. Each stack `pop` and `append` (for Python lists acting as stacks) is $O(1)$ on average.
    * The final loop to construct the result list runs $O(\max(M, N))$ times, with each `pop` and node assignment being $O(1)$.
    * Therefore, the total time complexity is linear with respect to the combined length of the input lists.

* **Space Complexity:** $O(M + N)$
    * `l1_stack` stores $M$ nodes.
    * `l2_stack` stores $N$ nodes.
    * `ans_stack` stores up to $\max(M, N) + 1$ nodes.
    * The space used for the stacks is directly proportional to the total number of digits in the input lists.
    * The newly constructed linked list also takes $O(\max(M, N))$ space, but this is output space. When analyzing auxiliary space, we consider the stacks.

#### **Advantages of this Algorithm**

* **Follows Up Constraint:** Solves the problem without reversing the input linked lists explicitly.
* **Clear and Intuitive:** The use of stacks makes the "reverse traversal" and columnar addition logic straightforward to understand.
* **Robust:** Handles lists of unequal lengths and final carry propagation correctly.
* **Does Not Modify Inputs:** Preserves the original `l1` and `l2` linked lists.
