Leetcode 11 Container With Most Water
---

### **Algorithm Analysis: Container With Most Water**

This problem asks us to find two vertical lines in a given array `height` such that, when combined with the x-axis, they form a container that holds the maximum amount of water. The key constraint is that the container cannot be slanted.

#### **Core Idea: Two-Pointer Technique (Optimized)**

A brute-force approach would involve checking every possible pair of lines, calculating the area for each pair, and finding the maximum. This would lead to an $O(N^2)$ time complexity. However, a more efficient approach leverages the **Two-Pointer Technique**.

The area of a container formed by two lines at indices `left` and `right` is determined by the shorter of the two lines and the distance between them: `min(height[left], height[right]) * (right - left)`.

The standard two-pointer approach starts with pointers at the extreme ends of the array (`left = 0`, `right = n-1`) and moves the pointer associated with the *shorter* line inwards. This is because moving the taller line inward cannot increase the height of the container (as it's limited by the shorter line) but would definitely decrease the width. Moving the shorter line inward, however, *might* lead to a taller line, potentially increasing the area despite a reduced width.

The provided solution extends this standard two-pointer approach with a further optimization to skip over unpromising lines.

#### **Step-by-Step Algorithm**

1.  **Initialization:**
    * `left`: Pointer initialized to the first line's index (`0`).
    * `right`: Pointer initialized to the last line's index (`len(height) - 1`).
    * `max_area`: Variable to store the maximum water found so far, initialized to `0`.

2.  **Two-Pointer Convergence Loop:**
    * The `while left < right:` loop continues as long as the pointers haven't crossed or met.

3.  **Calculate Area and Move Pointers:**
    * **Compare Heights:**
        * **If `height[left] < height[right]`:** The left line is shorter.
            * Calculate the current area: `height[left] * (right - left)`.
            * Update `max_area = max(max_area, current_area)`.
            * **Optimization (Skip Unpromising Left Lines):** To potentially find a taller left boundary, we move `left` one step to the right (`left += 1`). Then, an *inner `while` loop* skips all subsequent `left` lines that are shorter than or equal to the `last_left` (the height of the previous left line). This is because any container formed with these shorter lines and the current `right` line would have a height less than or equal to `last_left` but a smaller width, guaranteeing a smaller or equal area.
        * **Else (`height[left] >= height[right]`):** The right line is shorter or equal.
            * Calculate the current area: `height[right] * (right - left)`.
            * Update `max_area = max(max_area, current_area)`.
            * **Optimization (Skip Unpromising Right Lines):** Symmetrically, we move `right` one step to the left (`right -= 1`). An *inner `while` loop* then skips all subsequent `right` lines that are shorter than or equal to `last_right` (the height of the previous right line).

4.  **Return Result:**
    * Once the `while left < right:` loop terminates (when `left` and `right` pointers meet or cross), `max_area` will hold the maximum amount of water that can be contained.

#### **Why This Works (Two-Pointer Logic)**

The core reasoning for moving the shorter pointer is:
* The area is limited by the shorter line.
* To potentially increase the area, we need to find a taller limiting line.
* Moving the *taller* line inward guarantees a decrease in width, and since its height was not the limiting factor, the area will decrease.
* Moving the *shorter* line inward also decreases the width, but it offers the *chance* of encountering a taller line that could compensate for the reduced width, potentially leading to a larger area.

The added optimization of skipping lines (`while height[left] <= last_left` and `while height[right] <= last_right`) further refines this by ensuring that we don't recalculate areas for boundaries that are guaranteed to yield smaller or equal results.

#### **Complexity Analysis**

* **Time Complexity: $O(N)$**
    * Both the `left` and `right` pointers traverse the array only once. The `left` pointer moves from `0` to `n-1`, and the `right` pointer moves from `n-1` to `0`.
    * Although there are nested `while` loops, each line is pointed to by `left` or `right` and then moved past at most once. The total number of operations for pointer movements and area calculations is proportional to `N`.
    * Thus, the algorithm runs in linear time.

* **Space Complexity: $O(1)$**
    * The algorithm only uses a few constant variables (`left`, `right`, `max_area`, `last_left`, `last_right`).
    * It does not use any additional data structures whose size scales with the input array.

---
