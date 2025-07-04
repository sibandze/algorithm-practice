"3Sum" problem (LeetCode 15)
---

### **Algorithm Analysis: 3Sum**

The "3Sum" problem asks us to find all unique triplets `[nums[i], nums[j], nums[k]]` in a given integer array `nums` such that their sum is zero (`nums[i] + nums[j] + nums[k] == 0`). The solution set must not contain duplicate triplets.

#### **Core Idea: Sorting + Two-Pointer Technique**

A brute-force approach to this problem would involve checking every possible combination of three numbers, leading to an $O(N^3)$ time complexity. This is too slow for typical constraints.

The provided solution optimizes this significantly by combining two powerful techniques:

1.  **Sorting:** Sorting the input array `nums` is the crucial first step. It allows us to efficiently manage duplicates and use the two-pointer technique.
2.  **Two-Pointer Technique:** After fixing one element (the first number of the triplet), the problem effectively reduces to a "Two Sum" problem on the remaining sorted portion of the array. The two-pointer approach is then used to find the remaining two numbers.

#### **Step-by-Step Algorithm**

1.  **Sort the Array:**
    * `nums.sort()`: The input array `nums` is sorted in non-decreasing order. This operation is fundamental for the subsequent steps to work efficiently and to handle duplicates easily.

2.  **Iterate with the First Pointer (`i`):**
    * The main loop iterates with a pointer `i` from `0` up to `len(nums) - 3` (because we need at least two more elements for a triplet). This `nums[i]` will be the first element of our potential triplet.

3.  **Skip Duplicate `i` Values:**
    * `if i > 0 and nums[i] == nums[i - 1]: continue`: To prevent duplicate triplets in the result, if the current `nums[i]` is the same as the previous one (`nums[i-1]`), we skip this iteration. This ensures that we only consider unique values for the first element of the triplet.

4.  **Early Termination/Skipping Optimizations:**
    * `if nums[i] + nums[i + 1] + nums[i + 2] > 0: break`: If the sum of `nums[i]` and the *two smallest* numbers after it is already greater than 0, then any subsequent `nums[left]` values (which would be larger) would also result in a sum greater than 0. Since the array is sorted, we can safely `break` the loop because no more triplets summing to 0 can be found with the current or any subsequent `nums[i]`.
    * `if nums[i] + nums[-1] + nums[-2] < 0: continue`: If the sum of `nums[i]` and the *two largest* numbers in the array is less than 0, then `nums[i]` is too small to reach a sum of 0 with any combination. We can `continue` to the next `i` value.

5.  **Initialize Two Pointers (`left`, `right`):**
    * `left = i + 1`: The `left` pointer starts immediately after `i`.
    * `right = len(nums) - 1`: The `right` pointer starts at the end of the array.

6.  **Inner Two-Pointer Loop:**
    * `while left < right:`: This loop aims to find two numbers (`nums[left]` and `nums[right]`) that, when added to `nums[i]`, sum to 0.
    * **Calculate `total`:** `total = nums[i] + nums[left] + nums[right]`
    * **Adjust Pointers based on `total`:**
        * `if total < 0:`: The sum is too small. Move `left` pointer to the right (`left += 1`) to try a larger number.
        * `elif total > 0:`: The sum is too large. Move `right` pointer to the left (`right -= 1`) to try a smaller number.
        * `else (total == 0):`: We found a triplet!
            * Add `[nums[i], nums[left], nums[right]]` to the `ans` list.
            * **Skip Duplicate `left` and `right` Values:** To avoid duplicate triplets, move `left` and `right` pointers past any identical consecutive elements.
                * `while left < right and nums[left] == nums[left + 1]: left += 1`
                * `while left < right and nums[right] == nums[right - 1]: right -= 1`
            * Finally, move both pointers one more step (`left += 1`, `right -= 1`) to search for the next unique pair.

7.  **Return Result:**
    * After all iterations, `ans` will contain all unique triplets that sum to zero.

#### **Complexity Analysis**

* **Time Complexity: $O(N^2)$**
    * **Sorting:** The initial sort operation takes $O(N \log N)$ time.
    * **Outer Loop (`i`):** This loop runs $N$ times.
    * **Inner Two-Pointer Loop (`left`, `right`):** For each `i`, the `left` and `right` pointers traverse at most $N$ elements. Each pointer moves monotonically.
    * The sum of operations within the inner `while` loop (comparisons, additions, pointer movements, and duplicate skips) for a fixed `i` is $O(N)$.
    * Therefore, the dominant part is $N \times O(N)$, leading to an overall time complexity of **$O(N^2)$**.

* **Space Complexity: $O(1)$ (or $O(N)$ depending on sorting implementation)**
    * The algorithm uses a constant amount of extra space for pointers (`i`, `left`, `right`, `total`) and the `ans` list to store results.
    * However, if the sorting algorithm used by `nums.sort()` is not in-place (e.g., Python's `list.sort()` is in-place, but some other languages' sort might use $O(N)$ auxiliary space), then the space complexity could be considered $O(N)$ due to sorting. Assuming standard in-place quicksort/mergesort variations for the underlying sort, the *additional* space beyond input and output storage is **$O(1)$**.

#### **Advantages of this Algorithm**

* **Efficiency:** $O(N^2)$ is significantly better than the naive $O(N^3)$ approach and is generally considered optimal for the 3Sum problem.
* **Handles Duplicates Effectively:** The sorting combined with the skipping logic (e.g., `if i > 0 and nums[i] == nums[i - 1]: continue`) elegantly handles the requirement of unique triplets in the output.
* **Clear Logic:** The Two-Pointer technique is intuitive and easy to follow once the array is sorted.
