LeetCode 23 "Merge k Sorted Lists"
---

### **Algorithm Analysis: Merge k Sorted Lists**

This problem asks us to merge `k` sorted linked lists into a single sorted linked list. Each of the `k` input linked lists is already sorted in ascending order.

#### **Core Idea: Divide and Conquer (Merge Sort Approach)**

A brute-force approach would involve iteratively merging one list at a time with the growing merged list, or putting all elements into an array, sorting it, and rebuilding the list. These approaches can be inefficient.

The most efficient approach, implemented here, is based on the **Divide and Conquer** paradigm, similar to **Merge Sort**. We recursively divide the array of `k` linked lists into two halves until we are left with single lists. Then, we merge these single lists back up, combining two sorted lists at a time, until all lists are merged into one.

This approach leverages the `mergeTwoLists` function, which is efficient for merging two sorted lists.

#### **Step-by-Step Algorithm**

1.  **Base Case and Initial Checks:**
    * `if not lists: return None`: If the input `lists` array is empty, there's nothing to merge, so return `None`.

2.  **Recursive Helper Function `_mergeKLists(start, end)`:**
    * This function takes `start` and `end` indices, representing the range of lists in the `lists` array to be merged.
    * **Base Case for Recursion:**
        * `if start == end: return lists[start]`: If `start` and `end` are the same, it means we have a single list. This is our base case; simply return that list.
    * **Divide Step:**
        * `mid = (start + end + 1) // 2`: Calculate the middle index. The `+1` ensures that `mid` is always at least `start + 1` when `start < end`, preventing infinite recursion for `mid-1`.
        * `left = _mergeKLists(start, mid - 1)`: Recursively call `_mergeKLists` to merge the lists in the left half (from `start` to `mid - 1`).
        * `right = _mergeKLists(mid, end)`: Recursively call `_mergeKLists` to merge the lists in the right half (from `mid` to `end`).
    * **Conquer (Merge) Step:**
        * `return self.mergeTwoLists(left, right)`: Once `left` and `right` sub-problems return their merged (and sorted) lists, call the `mergeTwoLists` helper function to merge these two sorted lists into one, and return the result.

3.  **`mergeTwoLists(list1, list2)` Helper Function:**
    * This is a standard and efficient function to merge two sorted linked lists, as seen in LeetCode 21.
    * It uses a `dummy` node to simplify handling the head of the new list.
    * It iteratively compares the `val` of the current nodes in `list1` and `list2`, linking the smaller one to the `current.next` of the merged list, and advancing the respective pointer.
    * After one list is exhausted, it appends the remaining part of the other list to the merged list.
    * It returns `dummy.next`, which is the head of the newly merged sorted list.

4.  **Initial Call:**
    * `return _mergeKLists(0, len(lists) - 1)`: The main `mergeKLists` function initiates the recursive process by calling the helper function with the full range of list indices.

#### **Complexity Analysis**

Let `k` be the number of linked lists and `N` be the total number of nodes across all `k` linked lists.

* **Time Complexity: $O(N \log k)$**
    * The `_mergeKLists` function effectively forms a balanced binary tree of merge operations. There are `log k` levels of merging.
    * At each level of merging, every node in the entire set of `k` lists is processed exactly once by a `mergeTwoLists` call. A `mergeTwoLists` call for two lists of total length `L` takes $O(L)$ time.
    * Since the total number of nodes across all lists is `N`, each level of merging takes $O(N)$ time.
    * With `log k` levels, the total time complexity is **$O(N \log k)$**.

* **Space Complexity: $O(\log k)$ (for recursion stack) + $O(1)$ (for `mergeTwoLists` variables)**
    * The recursive calls for `_mergeKLists` build up a recursion stack. The maximum depth of this recursion is `log k` (due to the divide-and-conquer strategy on `k` lists).
    * The `mergeTwoLists` function itself uses only $O(1)$ extra space.
    * Therefore, the dominant space complexity comes from the recursion stack, resulting in **$O(\log k)$**.

#### **Advantages of this Algorithm**

* **Efficiency:** $O(N \log k)$ is a very efficient time complexity for this problem, significantly better than brute-force or simply merging one by one (which could be $O(N \cdot k)$ in worst case).
* **Leverages Existing Solution:** Reuses the efficient `mergeTwoLists` function, promoting modularity.
* **Scalability:** The divide-and-conquer approach scales well with a large number of input lists `k`.
