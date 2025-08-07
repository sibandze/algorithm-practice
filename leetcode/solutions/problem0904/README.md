Leetcode 904: Fruits Into Basket
---
The solution uses a sliding window approach to find the longest subarray with at most two distinct fruit types, which directly translates to the maximum number of fruits you can collect. The window represents the range of trees you're picking from.
***

### Algorithm Breakdown

1.  **Initialization**:
    * `left`: A pointer marking the start of the current window, initialized to `0`.
    * `count`: A hash map (dictionary in Python) to keep track of the fruit types and their counts within the current window.
    * `fruits_collected`: A variable to store the maximum number of fruits collected so far, initialized to `0`.

2.  **Expanding the Window**:
    * The code uses a `for` loop with a `right` pointer to expand the window by moving one tree at a time to the right.
    * For each new tree at index `right`, the fruit type `fruits[right]` is added to the `count` map. If the fruit type is already in the map, its count is incremented; otherwise, it's added with a count of `1`.

3.  **Shrinking the Window**:
    * After expanding the window, a `while` loop checks if the number of distinct fruit types in the `count` map (`len(count)`) is greater than 2. This means you have more than two fruit types, which violates the rule.
    * To fix this, the window must shrink from the left.
    * The fruit at the `left` pointer, `fruits[left]`, has its count decremented in the `count` map.
    * If the count of `fruits[left]` becomes `0`, it means that type of fruit is no longer in the window, so it's removed from the `count` map entirely using `del`.
    * The `left` pointer is then incremented, shrinking the window. This process repeats until the window contains at most two fruit types.

4.  **Tracking Maximum Length**:
    * After each expansion and potential shrinking of the window, the current window size (`right - left + 1`) represents a valid collection of fruits.
    * This length is compared with `fruits_collected`, and `fruits_collected` is updated to store the maximum length seen so far.

5.  **Return Value**:
    * After the `for` loop finishes iterating through all the trees, `fruits_collected` will hold the maximum number of fruits that could be picked, and the function returns this value.

***

### Complexity Analysis

* **Time Complexity**: The time complexity is **$O(N)$**, where $N$ is the number of fruit trees. Both the `right` and `left` pointers traverse the array at most once. Each fruit is added and removed from the `count` map a constant number of times.
* **Space Complexity**: The space complexity is **$O(1)$**. The `count` map will store at most three distinct fruit types at any given time (two valid types plus a third one that triggers the shrinking of the window). Therefore, the space used does not grow with the input size.
