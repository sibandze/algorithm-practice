LeetCode 3307 "Find the K-th Character in String Game II"
---

### **Algorithm Analysis: Find the K-th Character in String Game II**

This problem is an extension of "Find the K-th Character in String Game I". We start with `word = "a"`. Bob performs a sequence of operations defined by an array `operations`. Each `operations[i]` dictates how the string `word` grows:
* If `operations[i] == 0`: Append a copy of `word` to itself (`word = word + word`).
* If `operations[i] == 1`: Generate a new string by changing each character in `word` to its next character in the English alphabet, and append it to the original `word` (`word = word + shift(word)`).

We need to find the $k$-th character (1-indexed) in the final string after all operations.

#### **Core Idea: Adapting Binary Search with Dynamic Operations**

Similar to LeetCode 3304, the string `word` at step `P` ($S_P$) will have a length of $2^P$ after $P$ operations. The structure remains a recursive decomposition: $S_P$ is composed of $S_{P-1}$ (the first half) and a generated second half (either `S_{P-1}` itself or `shift(S_{P-1})`), based on `operations[P-1]`.

The core idea is still a binary search on this recursive structure. We determine which `S_P` is the smallest string that contains the `k`-th character. Then, we "zoom in" on `k`'s position by repeatedly checking if `k` falls into the first or second half of the current string segment. The key difference from Game I is that when `k` falls into the second half, we must consult the specific `operations[op_index]` to know if a character shift occurred for that segment.

#### **Step-by-Step Algorithm**

1.  **Determine Initial String Level and Length:**
    * `op_count = math.floor(math.log2(k))`: This calculates the largest integer `P` such that $2^P \le k$. This `P` effectively tells us that `k` is contained within a string that is at least $S_P$.
    * `length = 2 ** (op_count + 1)`: This sets `length` to $2^{P+1}$. This is the length of the string $S_{P+1}$, which is guaranteed to be large enough to contain `k`. This `length` will be the starting size of our search space.
    * `op_index = op_count`: This `op_index` points to the index in the `operations` array that corresponds to the operation that *created* the string of length `length` from `length // 2`. (e.g., if `length` is $S_{P+1}$, then `operations[P]` was the operation that generated $S_{P+1}$ from $S_P$).

2.  **Locate Character and Accumulate Shift Recursively (via `while` loop):**
    * `shift = 0`: This variable will accumulate the total alphabetical shift needed for the final character.
    * `while length > 1:`: This loop continues as long as we haven't narrowed down to a single character.
        * `if k > length // 2:`: Check if `k` falls into the *second half* of the current `length` string.
            * `if operations[op_index] == 1:`: If the specific operation that formed this string (`operations[op_index]`) was of type `1` (shift and append):
                * `shift += 1`: Increment the `shift` counter, as this part of the string has undergone an alphabetical shift.
            * `k -= length // 2`: Adjust `k` to be its position relative to the beginning of this second half.
        * `length //= 2`: Halve the `length` for the next iteration, effectively moving down to the previous string generation level (e.g., from $S_P$ to $S_{P-1}$).
        * `op_index -= 1`: Decrement `op_index` to point to the operation that formed the string of the new `length`.

3.  **Calculate the Final Character:**
    * `return chr(ord('a') + (k - 1 + shift) % 26)`:
        * `k - 1`: `k` is 1-indexed, so `k-1` converts it to a 0-indexed position. At the end of the loop, `k` will be `1` (if it was always in the first half) or `1` (if it was in the second half but became `1` after adjustment). This `k-1` effectively represents the base 0-indexed position relative to the initial 'a'.
        * `+ shift`: Add the accumulated `shift` value. This `shift` represents the total number of times the character at this specific recursive path has been transformed alphabetically.
        * `% 26`: Apply the modulo 26 operation to handle wrapping around the English alphabet (e.g., 'z' shifted becomes 'a').
        * `chr(ord('a') + ...)`: Convert the final numerical shift back to its corresponding character.

#### **Complexity Analysis**

* **Time Complexity: $O(\log k)$**
    * The first step involves `math.log2(k)`, which is a logarithmic operation.
    * The main `while` loop iterates as `length` is repeatedly halved until it reaches `1`. This means the loop runs approximately `log(initial_length)` times. Since `initial_length` is roughly `2 * k`, this is proportional to `log k`.
    * All operations inside the loop (comparisons, arithmetic, array access) are constant time.
    * Therefore, the total time complexity is logarithmic with respect to `k`.

* **Space Complexity: $O(1)$**
    * The algorithm uses a fixed, small number of extra variables (`op_count`, `length`, `shift`, `op_index`, `k`).
    * It does not allocate any additional data structures whose size scales with `k` or the length of the `operations` array (beyond the constant-time access to `operations[op_index]`).

#### **Advantages of this Algorithm**

* **Optimal Time Complexity:** Achieves an $O(\log k)$ runtime, which is highly efficient for potentially very large values of `k`.
* **Constant Space:** Uses a minimal amount of auxiliary memory.
* **Dynamic Operation Handling:** Elegantly integrates the variable operation types (`0` or `1`) by consulting the `operations` array at each recursive step, making it flexible for different string generation rules.
* **Recursive Structure via Iteration:** The iterative `while` loop effectively processes the problem's recursive structure without the overhead of explicit function calls, making it very performant.

---
