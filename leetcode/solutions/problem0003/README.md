### **Algorithm Analysis: Leetcode 3: Longest Substring Without Repeating Characters**
---
This problem requires finding the length of the longest substring within a given string `s` that contains no duplicate characters.

#### **Core Idea: Sliding Window with a Hash Set**

The most efficient approach to this problem is the **Sliding Window** technique. We maintain a "window" (a substring) within the given string `s`. This window expands to the right, and if a duplicate character is encountered, it shrinks from the left to remove the duplicate and ensure all characters within the window are unique. A **hash set** (or Python's `set`) is used to efficiently keep track of the characters currently present within this window.

#### **Step-by-Step Algorithm**

1.  **Initialization:**
    * Initialize two pointers, `i` (left pointer) and `j` (right pointer), both starting at the beginning of the string (index 0).
    * Initialize `char_set` as an empty hash set. This set will store all unique characters currently within the window `s[i...j]`.
    * Initialize `ans` to 0, which will store the maximum length found so far.

2.  **Expand Window (Right Pointer `j`):**
    * Iterate the `j` pointer from the beginning (`0`) to the end of the string (`n-1`). In each iteration, `s[j]` is the character we attempt to add to our current window.

3.  **Handle Duplicates (Shrink Window from Left):**
    * **Before adding `s[j]`:** Check if `s[j]` is already present in `char_set`.
    * **If `s[j]` is found in `char_set` (a duplicate is detected):** This means the current window contains a duplicate. To fix this:
        * Remove `s[i]` (the character at the left end of the window) from `char_set`.
        * Increment `i` (move the left pointer one position to the right).
        * Repeat this shrinking process (the `while` loop) until `s[j]` is no longer in `char_set`.

4.  **Add Current Character and Update Max Length:**
    * Once `s[j]` is guaranteed to be unique within the current window (after potential shrinking), add `s[j]` to `char_set`.
    * Update `ans = max(ans, len(char_set))`. `len(char_set)` gives the current length of the unique substring `s[i...j]`.

5.  **Early Exit Optimization:**
    * After updating `ans`, check if `ans` is already greater than or equal to the maximum possible length that can be achieved from the current point onward.
    * The maximum potential length is `len(current_unique_substring) + remaining_characters_count`.
    * `len(char_set)` is `current_unique_substring` length.
    * `n - j - 1` is `remaining_characters_count` (total length `n` minus `j`'s current index and `j` itself).
    * If `ans >= len(char_set) + n - j - 1`, it means no longer unique substring can be found. Break the loop.

6.  **Return Result:**
    * After the `j` pointer has traversed the entire string, `ans` will hold the length of the longest substring without repeating characters.

#### **Complexity Analysis**

* **Time Complexity: $O(N)$**
    * The right pointer `j` iterates through the string once, performing `N` steps.
    * The left pointer `i` also moves forward at most `N` times throughout the entire process (it never moves backward).
    * Each character in the string is added to the `char_set` at most once and removed from the `char_set` at most once.
    * Hash set operations (`add`, `remove`, `in` check) have an average time complexity of $O(1)$.
    * Therefore, the total time complexity is linear, proportional to the length of the string.

* **Space Complexity: $O(min(N, M))$**
    * The `char_set` stores unique characters from the current window.
    * In the worst case, if all characters in the string are unique, the set might store up to `N` characters.
    * If the character set (alphabet) is limited (e.g., ASCII characters, where $M=256$), the maximum size of the set is bounded by `M`.
    * Hence, the space complexity is bounded by the smaller of `N` (string length) and `M` (alphabet size). Often, for fixed alphabets, this is simplified to $O(1)$.

---
