Leetcode 167 Two Sum II - Input Array Is Sorted
---

### **Algorithm Analysis: Two Sum II - Input Array Is Sorted**

This problem is a variation of the classic "Two Sum" problem, with the crucial additional constraint that the input array `numbers` is already sorted in non-decreasing order. This sorting allows for a highly efficient solution that uses only constant extra space.

#### **Core Idea: The Two-Pointer Technique**

The fundamental idea behind this solution is the **Two-Pointer Technique**. Since the array is sorted, we can use two pointers, one starting from the beginning (smallest elements) and one from the end (largest elements), and strategically move them towards each other based on the sum of the elements they point to.

This approach eliminates the need for a hash map, thus meeting the $O(1)$ extra space requirement, while still achieving optimal time complexity.

#### **Step-by-Step Algorithm**

1.  **Initialize Pointers:**
    * Set a `left` pointer to the first index of the array (index 0).
    * Set a `right` pointer to the last index of the array (index `length - 1`).

2.  **Iterate and Converge:**
    * Start a loop that continues as long as the `left` pointer is less than the `right` pointer. This ensures we are always considering two distinct elements (`index1 < index2`).

3.  **Calculate Current Sum:**
    * Inside the loop, calculate the sum of the numbers at the current `left` and `right` pointers: `current_sum = numbers[left] + numbers[right]`.

4.  **Compare and Adjust Pointers:**
    * **Case 1: `current_sum == target`**
        * If the `current_sum` equals the `target`, we have found our solution.
        * Return the 1-indexed positions: `[left + 1, right + 1]`.
    * **Case 2: `current_sum > target`**
        * If the `current_sum` is greater than the `target`, it means our sum is too large. Since the array is sorted in non-decreasing order, to decrease the sum, we must consider a smaller number from the right side.
        * Move the `right` pointer one step to the left: `right--`.
    * **Case 3: `current_sum < target`**
        * If the `current_sum` is less than the `target`, it means our sum is too small. To increase the sum, we must consider a larger number from the left side.
        * Move the `left` pointer one step to the right: `left++`.

5.  **Termination:**
    * The loop continues, narrowing the search range with each step. Because the problem guarantees exactly one solution, the `current_sum == target` condition will eventually be met, and the function will return the indices. The pointers will never cross without finding a solution.

#### **Why This Works (Efficiency through Sortedness)**

The efficiency stems from the array being sorted. At each step, we effectively eliminate a portion of the array from future consideration:
* If `current_sum > target`, any pair involving `numbers[right]` with `numbers[left]` or any `numbers[k]` where `k > left` would also be greater than `target` (since `numbers[k] >= numbers[left]`). Thus, `numbers[right]` cannot be part of the solution, and we safely discard it by moving `right` inwards.
* If `current_sum < target`, similarly, any pair involving `numbers[left]` with `numbers[right]` or any `numbers[k]` where `k < right` would also be less than `target`. Thus, `numbers[left]` cannot be part of the solution, and we discard it by moving `left` inwards.

This systematic elimination ensures optimal performance.

#### **Complexity Analysis**

* **Time Complexity: $O(N)$**
    * The `left` pointer starts at `0` and only moves right. The `right` pointer starts at `N-1` and only moves left.
    * In each iteration, at least one of the pointers moves. In the worst case, they traverse the entire array once.
    * Therefore, the number of operations is directly proportional to the number of elements in the array.

* **Space Complexity: $O(1)$**
    * The algorithm uses only a constant number of variables (`left`, `right`, `current_sum`).
    * It does not allocate any additional data structures whose size depends on the input array's size. This satisfies the "constant extra space" requirement.
