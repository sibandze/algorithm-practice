LeetCode 2379 "Minimum Recolors to Get K Consecutive Black Blocks"
---

### **Algorithm Analysis: Minimum Recolors to Get K Consecutive Black Blocks**

This problem asks us to find the minimum number of operations (recoloring 'W' to 'B') needed to achieve at least `k` consecutive black blocks within a given string `blocks` composed of 'W' and 'B'.

#### **Core Idea: Sliding Window**

The problem boils down to finding a subarray (or substring) of length `k` that has the maximum number of 'B's. Once we find this window, the number of 'W's within that window will be the minimum operations needed to make all blocks in that window black.

A **sliding window** technique is perfectly suited for this. We maintain a window of size `k`, efficiently updating the count of 'B's (or 'W's) as the window slides along the string.

#### **Algorithm Breakdown**

1.  **Initialization:**
    * `n = len(blocks)`: Get the total length of the `blocks` string.
    * `i, j = 0, 0`: Initialize two pointers, `i` for the start of the window and `j` for the end of the window.
    * `black_blocks_in_range = 0`: Initialize a counter for black blocks within the current window.

2.  **Initialize the First Window (Size `k`):**
    * `while j < k:`: This loop processes the first `k` characters to set up the initial window.
        * `black_blocks_in_range += blocks[j] == 'B'`: If the current block `blocks[j]` is 'B', increment the `black_blocks_in_range` counter.
        * `j += 1`: Move the `j` pointer to expand the window.
    * `max_black_blocks_in_range = black_blocks_in_range`: After the first window is formed, its `black_blocks_in_range` count is the initial maximum.

3.  **Slide the Window:**
    * `while j < n:`: This loop continues until the `j` pointer reaches the end of the string.
        * `black_blocks_in_range += blocks[j] == 'B'`: As the window slides one position to the right, the new character `blocks[j]` is included. Update the count if it's 'B'.
        * `black_blocks_in_range -= blocks[i] == 'B'`: The character `blocks[i]` is now leaving the window. Decrement the count if it was 'B'.
        * `i += 1`: Move the `i` pointer one position to the right (contract the window from the left).
        * `j += 1`: Move the `j` pointer one position to the right (expand the window from the right).
        * `if max_black_blocks_in_range < black_blocks_in_range:`: After each slide, compare the current window's black block count with the `max_black_blocks_in_range` found so far and update if necessary.

4.  **Calculate Minimum Operations:**
    * `return k - max_black_blocks_in_range`: The minimum number of operations needed is `k` (the desired total black blocks) minus the maximum number of black blocks already found in any window of size `k`. This difference represents the number of 'W's that need to be recolored to 'B' in that optimal window.

#### **Example Trace (`blocks = "WBBWWBBWBW"`, `k = 7`)**

`n = 10`

1.  **Initialization:** `i=0`, `j=0`, `black_blocks_in_range=0`, `max_black_blocks_in_range=0`

2.  **First Window (j < k): `k=7`**
    * `j=0`: `blocks[0] = 'W'`, `black_blocks_in_range=0`. `j=1`.
    * `j=1`: `blocks[1] = 'B'`, `black_blocks_in_range=1`. `j=2`.
    * `j=2`: `blocks[2] = 'B'`, `black_blocks_in_range=2`. `j=3`.
    * `j=3`: `blocks[3] = 'W'`, `black_blocks_in_range=2`. `j=4`.
    * `j=4`: `blocks[4] = 'W'`, `black_blocks_in_range=2`. `j=5`.
    * `j=5`: `blocks[5] = 'B'`, `black_blocks_in_range=3`. `j=6`.
    * `j=6`: `blocks[6] = 'B'`, `black_blocks_in_range=4`. `j=7`.
    * First window `blocks[0:7]` is "WBBWWBB", `black_blocks_in_range = 4`.
    * `max_black_blocks_in_range = 4`.

3.  **Slide the Window (j < n): `n=10`**
    * **Iter 1:** `j=7`, `i=0`
        * Add `blocks[7] = 'W'`, `black_blocks_in_range` remains `4`. (Window: "WBBWWBB**W**")
        * Remove `blocks[0] = 'W'`, `black_blocks_in_range` remains `4`. (Window: "**W**BBWWBBW" -> "BBWWBBW")
        * `i=1`, `j=8`.
        * `max_black_blocks_in_range` (4) not less than `black_blocks_in_range` (4). No update.
    * **Iter 2:** `j=8`, `i=1`
        * Add `blocks[8] = 'B'`, `black_blocks_in_range` becomes `5`. (Window: "BBWWBBW**B**")
        * Remove `blocks[1] = 'B'`, `black_blocks_in_range` becomes `4`. (Window: "**B**BWWBBWB" -> "BWWBBWB")
        * `i=2`, `j=9`.
        * `max_black_blocks_in_range` (4) not less than `black_blocks_in_range` (4). No update.
    * **Iter 3:** `j=9`, `i=2`
        * Add `blocks[9] = 'W'`, `black_blocks_in_range` remains `4`. (Window: "BWWBBWB**W**")
        * Remove `blocks[2] = 'B'`, `black_blocks_in_range` becomes `3`. (Window: "**B**WWBBWBW" -> "WWBBWBW")
        * `i=3`, `j=10`.
        * `max_black_blocks_in_range` (4) not less than `black_blocks_in_range` (3). No update.
    * Loop ends as `j` is no longer less than `n`.

4.  **Calculate Minimum Operations:**
    * `return k - max_black_blocks_in_range = 7 - 4 = 3`.

This means the window "WBBWWBB" (from index 0 to 6) has 4 black blocks. To get 7 black blocks, we need to recolor `7 - 4 = 3` white blocks. This is the minimum.

#### **Complexity Analysis**

Let $n$ be the length of the `blocks` string.

* **Time Complexity:** $O(n)$
    * The first `while` loop runs `k` times.
    * The second `while` loop runs `n - k` times.
    * Inside both loops, operations are constant time (character comparison, addition, subtraction, pointer increments).
    * Therefore, the total time complexity is $O(k + (n - k)) = O(n)$, which is linear with the length of the input string. This is optimal as every character must be processed at least once.

* **Space Complexity:** $O(1)$
    * The solution uses only a few constant variables (`n`, `i`, `j`, `black_blocks_in_range`, `max_black_blocks_in_range`). No additional data structures are used whose size depends on the input size.

#### **Advantages of this Algorithm**

* **Optimal Efficiency:** Achieves the best possible time and space complexity for this problem.
* **Simplicity:** The sliding window approach is elegant and relatively easy to understand and implement.
* **Direct Solution:** Directly calculates the maximum number of 'B's in any window, which then directly yields the minimum recolors.
* **No Edge Cases Missed:** Correctly handles cases where `k` is equal to `n`, or when there are no 'B's, or when all are 'B's.
