Leetcode 5 Longest Palindromic Substring
---

### **Algorithm Analysis: Longest Palindromic Substring**

This problem asks us to find the longest substring within a given string `s` that is a palindrome. A palindrome is a string that reads the same forwards and backwards.

#### **Core Idea: Expand Around Center**

The most intuitive and commonly used approach for this problem is the "Expand Around Center" method. The core idea is that every palindrome has a "center." This center can be either a single character (for odd-length palindromes like "aba") or two adjacent identical characters (for even-length palindromes like "abba").

By iterating through every possible center in the string and expanding outwards, we can check all potential palindromes and keep track of the longest one found.

#### **Step-by-Step Algorithm**

1.  **Initialization:**
    * `n`: Stores the length of the input string `s`.
    * `longest_palindrome`: This variable is a list `[length, [start_index, end_index]]` used to keep track of the longest palindrome found so far. It's initialized to `[1, [0, 0]]` assuming a single character is the smallest possible palindrome (if `s` is not empty).

2.  **`expand_around_center(left, right)` Helper Function:**
    * This function takes two indices, `left` and `right`, representing the potential center(s) of a palindrome.
    * **Expansion Loop:** It uses a `while` loop to expand outwards:
        * The loop continues as long as `left` is within the string bounds (`>= 0`), `right` is within the string bounds (`< n`), and the characters at `s[left]` and `s[right]` are equal.
        * In each iteration, `left` is decremented, and `right` is incremented.
    * **Calculate Length and Update Longest:**
        * Once the `while` loop terminates (meaning characters no longer match or bounds are exceeded), the palindrome found extends from `left + 1` to `right - 1`. The length of this palindrome is `(right - 1) - (left + 1) + 1`, which simplifies to `right - left - 1`.
        * If this `length` is greater than the current `longest_palindrome[0]`, then `longest_palindrome` is updated with this new length and its corresponding `[start_index, end_index]` (`[left + 1, right - 1]`).

3.  **Iterate Through All Possible Centers:**
    * The main loop `for i in range(n)` iterates through each character in the string, considering `i` as a potential center.
    * **Odd-Length Palindromes:** `expand_around_center(i, i)`: Here, `i` itself is the center. This handles palindromes like "a", "aba", "racecar".
    * **Even-Length Palindromes:** `expand_around_center(i, i + 1)`: Here, the space between `s[i]` and `s[i+1]` is the center. This handles palindromes like "aa", "abba", "noon".

4.  **Return Result:**
    * After checking all possible centers, `longest_palindrome[1]` will contain the `[start_index, end_index]` of the longest palindromic substring.
    * The function then extracts and returns this substring using string slicing: `s[longest_palindrome[1][0]:longest_palindrome[1][1] + 1]`.

#### **Complexity Analysis**

* **Time Complexity: $O(N^2)$**
    * The main loop iterates `N` times (for `i` from `0` to `n-1`).
    * Inside the loop, the `expand_around_center` function is called twice.
    * In the worst case, for each call to `expand_around_center`, the `while` loop can expand almost the entire length of the string. For example, if the string is `aaaaa`, it will expand to `N/2` in each direction.
    * Therefore, the total time complexity is roughly $N \times O(N)$, which results in $O(N^2)$.

* **Space Complexity: $O(1)$**
    * The algorithm uses only a few constant variables (`n`, `longest_palindrome`, `left`, `right`, `length`).
    * It does not use any data structures whose size grows with the input string size (beyond the fixed space for string representation).

#### **Advantages of this Algorithm**

* **Simplicity:** The logic is quite straightforward and easy to understand.
* **Optimal for Simple Cases:** It's a highly competitive solution for this problem, often preferred over more complex dynamic programming or Manacher's algorithm unless extremely strict performance guarantees are needed for very long strings.
* **Constant Space:** It achieves the solution without requiring significant additional memory.
