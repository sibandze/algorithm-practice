LeetCode 33 "Search In Rotated Sorted Array"
---

### **Algorithm Analysis: Search In Rotated Sorted Array**

This problem asks us to search for a `target` value in an integer array `nums` that was originally sorted in ascending order but has been rotated at an unknown pivot. The challenge is to do this with $O(\log N)$ runtime complexity, implying a modified binary search.

#### **Core Idea: Modified Binary Search**

The standard binary search algorithm works only on fully sorted arrays. When an array is rotated, it means it's split into two sorted subarrays. For example, `[4,5,6,7,0,1,2]` is `[4,5,6,7]` and `[0,1,2]`.

The core idea is to adapt binary search by, at each step, determining which half of the array (from `nums[i]` to `nums[mid]` or from `nums[mid]` to `nums[j]`) is **sorted**. Once we identify the sorted half, we can then check if our `target` falls within that sorted range. If it does, we narrow our search to that half. Otherwise, the `target` must be in the *other* (unsorted) half, and we search there.

#### **Step-by-Step Algorithm**

1.  **Initialization:**
    * `i`: Left pointer, initialized to `0`.
    * `j`: Right pointer, initialized to `len(nums) - 1`.

2.  **Binary Search Loop:**
    * The `while i <= j:` loop continues as long as the search space is valid.
    * `mid = (i + j) // 2`: Calculate the middle index.

3.  **Target Found:**
    * `if target == nums[mid]: return mid`: If the `target` is found at `mid`, return its index immediately.

4.  **Determine Sorted Half and Adjust Search Space:**

    This is the crucial part. We need to figure out if the left part (`nums[i]` to `nums[mid]`) or the right part (`nums[mid]` to `nums[j]`) is sorted.

    * **Case 1: `nums[i] <= nums[mid]` (Left half is sorted)**
        This means the segment from `i` to `mid` is sorted in ascending order.
        * If `target` falls within this sorted left half (`nums[i] <= target < nums[mid]`):
            * Then, the `target` must be in this left segment. So, we discard the right half: `j = mid - 1`.
        * Else (`target` is not in the sorted left half):
            * The `target` must be in the unsorted right half. So, we discard the left half: `i = mid + 1`.

    * **Case 2: `nums[i] > nums[mid]` (Right half is sorted)**
        This means the segment from `mid` to `j` is sorted in ascending order. The pivot is somewhere in the left half.
        * If `target` falls within this sorted right half (`nums[mid] < target <= nums[j]`):
            * Then, the `target` must be in this right segment. So, we discard the left half: `i = mid + 1`.
        * Else (`target` is not in the sorted right half):
            * The `target` must be in the unsorted left half. So, we discard the right half: `j = mid - 1`.

    * **Note on the provided code's specific conditions:**
        The provided code uses `if nums[i] > nums[j]` to first check if the *entire current segment* `[i...j]` is rotated.
        * If it is rotated (`nums[i] > nums[j]`):
            * `if nums[i] > nums[mid]`: This implies the right half `[mid...j]` is sorted (e.g., `[7,0,1,2]` where `i=0, mid=1`, `nums[i]=7, nums[mid]=0`). The pivot is in `[i...mid]`.
                * `if (target >= nums[i] or target < nums[mid])`: This means `target` is in the unsorted left part (i.e., `target` is greater than or equal to `nums[i]` *or* `target` is smaller than `nums[mid]`). If true, search left: `j = mid - 1`.
                * `else`: `target` must be in the sorted right part. Search right: `i = mid + 1`.
            * `else`: (`nums[i] <= nums[mid]`) This implies the left half `[i...mid]` is sorted (e.g., `[4,5,6,7,0,1,2]` where `i=0, mid=3`, `nums[i]=4, nums[mid]=7`). The pivot is in `[mid...j]`.
                * `if (target > nums[mid] or target < nums[i])`: This means `target` is in the unsorted right part (i.e., `target` is greater than `nums[mid]` *or* `target` is smaller than `nums[i]`). If true, search right: `i = mid + 1`.
                * `else`: `target` must be in the sorted left part. Search left: `j = mid - 1`.
        * If it's not rotated (`nums[i] <= nums[j]`): This is a standard binary search on a sorted segment.
            * `if target < nums[mid]: j = mid - 1`
            * `else: i = mid + 1`

5.  **Target Not Found:**
    * If the loop finishes (`i > j`), it means the `target` was not found in the array. Return `-1`.

#### **Complexity Analysis**

* **Time Complexity: $O(\log N)$**
    * In each iteration of the `while` loop, the search space is effectively halved.
    * This logarithmic reduction in search space is the hallmark of binary search.
    * Therefore, the algorithm achieves the required $O(\log N)$ time complexity.

* **Space Complexity: $O(1)$**
    * The algorithm uses only a few constant variables (`i`, `j`, `mid`).
    * It does not allocate any additional data structures whose size scales with the input array.

#### **Advantages of this Algorithm**

* **Optimal Time Complexity:** Achieves the most efficient $O(\log N)$ runtime possible for searching in a sorted (or partially sorted) array.
* **Constant Space:** Operates with minimal auxiliary memory.
* **Direct Search:** Avoids finding the pivot first, then performing a second binary search. It integrates pivot detection directly into the search process.
