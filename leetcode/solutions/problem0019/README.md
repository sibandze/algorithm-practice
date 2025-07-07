LeetCode 19 "Remove Nth Node From End of List"
---

### **Algorithm Analysis: Remove Nth Node From End of List**

This problem requires us to remove the $n$-th node from the end of a given singly-linked list and return the head of the modified list.

#### **Core Idea: Two Pointers with a Gap (Single Pass)**

The most efficient and commonly used approach for this problem is a **single-pass solution using two pointers**, typically named `fast` and `slow`. The central idea is to establish a gap of `n` nodes between these two pointers. By the time the `fast` pointer reaches the end of the list (or `None`), the `slow` pointer will naturally be positioned at the node *just before* the $n$-th node from the end, allowing for a straightforward removal.

To elegantly handle the edge case where the head node itself needs to be removed (e.g., if `n` is equal to the list's total length), a **dummy node** is prepended to the list. This ensures that the node *before* the target node always exists, even if the target is the original head.

#### **Step-by-Step Algorithm**

1.  **Handle Empty List:**
    * `if not head: return head`: If the input list is empty, there's nothing to remove, so return `None` (the original `head`).

2.  **Create a Dummy Node:**
    * `dummy = ListNode()`: A `dummy` node is created.
    * `dummy.next = head`: This `dummy` node is placed before the actual `head` of the list. This simplifies handling cases where the original head needs to be removed, as `slow` will always have a valid `next` to point to.

3.  **Initialize Two Pointers:**
    * `fast = dummy`: The `fast` pointer starts at the `dummy` node.
    * `slow = dummy`: The `slow` pointer also starts at the `dummy` node.

4.  **Advance `fast` Pointer to Create the Gap:**
    * `while fast and n >= 0:`: This loop moves the `fast` pointer `n+1` steps ahead of the `slow` pointer.
        * `fast = fast.next`: Move `fast` one step.
        * `n -= 1`: Decrement `n`.
    * After this loop, `fast` will be exactly `n+1` nodes ahead of `slow`. If `n` was the count from the end, `fast` is `n` nodes ahead of the node to be removed. The `+1` offset in initial `n` steps ensures `slow` lands *before* the node to remove.

5.  **Move Both Pointers Simultaneously:**
    * `while fast:`: This loop continues until the `fast` pointer reaches the end of the list (becomes `None`).
    * In each iteration:
        * `fast = fast.next`: `fast` advances one step.
        * `slow = slow.next`: `slow` also advances one step.
    * Because `fast` initially started `n+1` steps ahead of `slow`, when `fast` reaches `None`, `slow` will be positioned at the node immediately preceding the $n$-th node from the end of the *original* list.

6.  **Perform Removal:**
    * `slow.next = slow.next.next`: At this point, `slow.next` is the $n$-th node from the end (the node to be removed). By setting `slow.next` to `slow.next.next`, we effectively bypass and remove the target node.

7.  **Return New Head:**
    * `return dummy.next`: Since `dummy.next` always points to the actual head of the (potentially modified) list, this is returned as the result.

#### **Complexity Analysis**

* **Time Complexity: $O(L)$**
    * The `fast` pointer traverses the entire list at most once (first for `n+1` steps, then alongside `slow` until the end).
    * The `slow` pointer also traverses the list at most once.
    * Since each node is visited a constant number of times, the total time taken is directly proportional to the length of the linked list (`L`).

* **Space Complexity: $O(1)$**
    * The algorithm uses a fixed, small number of extra variables (`dummy`, `fast`, `slow`, `n`).
    * It does not allocate any additional data structures whose size grows with the input list.

#### **Advantages of this Algorithm**

* **Single Pass Efficiency:** It solves the problem by traversing the linked list only once, making it very efficient.
* **Constant Space:** It uses a minimal amount of auxiliary memory, satisfying strict space constraints.
* **Robust Edge Case Handling:** The use of a `dummy` node simplifies the logic for all cases, including removing the head of the list, without needing special conditional checks for it.
