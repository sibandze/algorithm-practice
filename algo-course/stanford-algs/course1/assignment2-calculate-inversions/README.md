# Counting Inversions Algorithm

This repository contains an implementation of an algorithm to count inversions in an array, also utilizing the Divide and Conquer paradigm. This algorithm is essentially a modified Merge Sort.

## Problem Description

An **inversion** in an array is a pair of indices $(i, j)$ such that $i < j$ and $A[i] > A[j]$. In simpler terms, an inversion occurs when two elements in an array are out of their natural sorted order.

**Examples:**

* In the array `[1, 2, 3, 4]`, there are no inversions.
* In the array `[4, 3, 2, 1]`, every pair is an inversion: `(4,3), (4,2), (4,1), (3,2), (3,1), (2,1)`. Total 6 inversions.
* In the array `[1, 5, 2, 4, 3]`:
    * `(5,2)` is an inversion.
    * `(5,4)` is an inversion.
    * `(5,3)` is an inversion.
    * `(4,3)` is an inversion.
    * Total 4 inversions.

Counting inversions is useful in various applications, such as measuring the "sortedness" of an array or in ranking algorithms.

## Solution Approach: Divide and Conquer (Modified Merge Sort)

The most efficient way to count inversions is by modifying the Merge Sort algorithm. Merge Sort itself is a Divide and Conquer algorithm that sorts an array by recursively dividing it into halves, sorting them, and then merging the sorted halves.

The key insight for counting inversions is that inversions can be of three types:

1.  **Left Inversions:** Pairs $(i, j)$ where both $A[i]$ and $A[j]$ are in the left half, and $A[i] > A[j]$.
2.  **Right Inversions:** Pairs $(i, j)$ where both $A[i]$ and $A[j]$ are in the right half, and $A[i] > A[j]$.
3.  **Split Inversions:** Pairs $(i, j)$ where $A[i]$ is in the left half, $A[j]$ is in the right half, and $A[i] > A[j]$.

The algorithm proceeds as follows:

1.  **Divide:** The array is recursively split into two halves until individual elements are reached.
2.  **Conquer:** The left and right halves are recursively sorted, and their respective inversions are counted.
3.  **Combine (and Count Split Inversions):** This is the crucial step. When merging the two sorted halves, we also count the "split inversions."
    * During the merge process, if an element from the right half `right[r]` is moved into the merged array before an element from the left half `left[l]`, it means `right[r]` is smaller than `left[l]`.
    * Crucially, since `left` is already sorted, `right[r]` must also be smaller than *all* remaining elements in the `left` array from index `l` onwards.
    * Therefore, if `right[r]` is chosen, it forms an inversion with `(len(left) - l)` remaining elements in the left array. These are the "split inversions."

### High-Level Pseudocode

```
function CALCULATE_INVERSIONS(Array nums):
    n = length of nums

    // Base Case
    if n <= 1:
        return 0, nums (no inversions, array is sorted)

    // Divide
    mid = n / 2
    left_half = nums[0 ... mid-1]
    right_half = nums[mid ... n-1]

    // Conquer
    (left_inversions, sorted_left_half) = CALCULATE_INVERSIONS(left_half)
    (right_inversions, sorted_right_half) = CALCULATE_INVERSIONS(right_half)

    // Combine and Count Split Inversions (Merge Step)
    (split_inversions, merged_sorted_array) = MERGE_AND_COUNT_SPLIT_INVERSIONS(sorted_left_half, sorted_right_half, nums)

    // Total Inversions = Left Inversions + Right Inversions + Split Inversions
    return (left_inversions + right_inversions + split_inversions), merged_sorted_array

function MERGE_AND_COUNT_SPLIT_INVERSIONS(left_arr, right_arr, original_nums_ref):
    i = 0  // pointer for left_arr
    j = 0  // pointer for right_arr
    k = 0  // pointer for merged_arr (original_nums_ref)
    split_count = 0

    while i < length(left_arr) and j < length(right_arr):
        if left_arr[i] <= right_arr[j]:
            original_nums_ref[k] = left_arr[i]
            i = i + 1
        else: // An inversion is found! left_arr[i] > right_arr[j]
            original_nums_ref[k] = right_arr[j]
            j = j + 1
            // All remaining elements in left_arr from index 'i' onwards
            // are greater than right_arr[j]
            split_count = split_count + (length(left_arr) - i)
        k = k + 1

    // Copy remaining elements (if any)
    while i < length(left_arr):
        original_nums_ref[k] = left_arr[i]
        i = i + 1
        k = k + 1
    while j < length(right_arr):
        original_nums_ref[k] = right_arr[j]
        j = j + 1
        k = k + 1

    return split_count, original_nums_ref // original_nums_ref now holds the sorted array
```

## Analysis of the Solution

### 1. Time Complexity

The time complexity of the Counting Inversions algorithm is $\mathbf{O(N \log N)}$. This is the same as Merge Sort because the inversion counting is seamlessly integrated into the merge step without increasing its asymptotic complexity.

Let $T(N)$ be the time complexity for an array of size $N$.

* **Recursive Step `calculate_inversions(nums)`:**
    * **Divide:** Slicing the array (`nums[:n//2]`, `nums[n//2:]`) takes $O(N)$ time.
    * **Conquer:** Two recursive calls on halves of the input: $2 \cdot T(N/2)$.
    * **Combine (`calculate_split_inversions`):** This function performs a standard merge operation, iterating through the combined length of the two halves ($N$ elements). Each element is compared and placed, and inversion counts are updated in $O(1)$ time per element. Therefore, the merge step takes $O(N)$ time.

* **Recurrence Relation:**
    The recurrence relation for the time complexity $T(N)$ is:
    $$T(N) = 2 \cdot T(N/2) + O(N)$$
    By the Master Theorem, this recurrence relation solves to $\mathbf{T(N) = O(N \log N)}$.

### 2. Space Complexity

The space complexity of the algorithm is $\mathbf{O(N)}$.

* **Temporary Arrays:** The recursive nature of the algorithm involves creating new sub-arrays (`left`, `right`) at each level of recursion due to slicing (`nums[:n//2]`).
* **Merge Operation:** The `calculate_split_inversions` function modifies the `nums` array in place (after it's passed as a reference and then assigned to in the main function). However, `left` and `right` arrays are passed to it, which are copies.
* **Recursive Call Stack:** The maximum depth of the recursion is $O(\log N)$. At each level, temporary arrays are created. In a typical implementation of Merge Sort, the auxiliary space used for merging is $O(N)$. Here, due to the slicing and passing around of copies in Python, the space used for storing `left` and `right` arrays at each level of the recursion can sum up to $O(N \log N)$ if not managed carefully. However, since the lists are created and discarded as the recursion unwinds, the dominant space comes from the auxiliary space needed for merging, which is $O(N)$. The specific Python implementation's use of slicing creates new lists at each recursive call, making the conceptual auxiliary space $O(N)$ for each merge operation, which means the overall space complexity on the stack and for temporary arrays totals to $O(N)$.

### 3. Advantages

* **Efficiency:** Counts inversions in $O(N \log N)$ time, which is optimal for this problem.
* **Simultaneously Sorts:** As a modified Merge Sort, it also returns a sorted version of the input array as a byproduct.

### 4. Disadvantages/Considerations

* **Not In-Place:** While Merge Sort can be implemented mostly in-place for the merge operation, this Python implementation uses slicing which creates copies of subarrays, contributing to the $O(N)$ space complexity.
* **Recursion Overhead:** For very small arrays, the overhead of recursive calls might make a simple $O(N^2)$ brute-force approach (though not shown here) slightly faster due to smaller constant factors. The base case handles this by stopping recursion at `n <= 1`.

