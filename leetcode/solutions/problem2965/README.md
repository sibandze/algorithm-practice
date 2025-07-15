LeetCode 2965 "Find Missing and Repeated Values"
---

### **Algorithm Analysis: Find Missing and Repeated Values**

This problem presents an `n x n` integer `grid` containing values in the range `[1, n*n]`. All integers appear exactly once, except for one integer `a` that appears twice (repeated) and one integer `b` that is missing. The goal is to find `a` and `b` and return them as an array `[a, b]`.

#### **Core Idea: Mathematical Properties of Sums and Sums of Squares**

This problem is a classic variation of finding a missing/duplicate number, often solved using bit manipulation (XOR) or mathematical properties. The provided solution cleverly uses the latter.

Let the expected set of numbers be $S = \{1, 2, \dots, N\}$, where $N = n^2$.
Let the actual numbers in the grid be $A$.
We know that in $A$, `a` is repeated and `b` is missing. So, $A$ contains $\{1, \dots, b-1, b+1, \dots, N\}$ plus an extra `a`.

We can form two equations based on the sums and sums of squares:

1.  **Sum Equation:**
    * Let $S_1 = \sum_{i=1}^{N} i$ (the sum of all numbers from 1 to $N$). This is given by the formula $N(N+1)/2$.
    * Let $A_1 = \sum_{x \in A} x$ (the sum of numbers actually present in the grid).
    * The relationship is: $A_1 = S_1 - b + a$.
    * Therefore, `diff = A_1 - S_1 = (S_1 - b + a) - S_1 = a - b`.

2.  **Sum of Squares Equation:**
    * Let $S_2 = \sum_{i=1}^{N} i^2$ (the sum of squares of all numbers from 1 to $N$). This is given by the formula $N(N+1)(2N+1)/6$.
    * Let $A_2 = \sum_{x \in A} x^2$ (the sum of squares of numbers actually present in the grid).
    * The relationship is: $A_2 = S_2 - b^2 + a^2$.
    * Therefore, `diff_squares = A_2 - S_2 = (S_2 - b^2 + a^2) - S_2 = a^2 - b^2$.

Now we have a system of two equations with two unknowns (`a` and `b`):
1.  `a - b = diff`
2.  `a^2 - b^2 = diff_squares`

From equation 2, we know that $a^2 - b^2 = (a - b)(a + b)$.
Substituting equation 1 into this:
`diff_squares = (diff) * (a + b)`
If `diff` is not zero, then `a + b = diff_squares / diff`.

Let `r_plus_m = a + b`.
So, we have:
1.  `a - b = diff`
2.  `a + b = r_plus_m`

Adding these two equations:
`(a - b) + (a + b) = diff + r_plus_m`
`2a = diff + r_plus_m`
`a = (diff + r_plus_m) / 2`

Subtracting the first equation from the second:
`(a + b) - (a - b) = r_plus_m - diff`
`2b = r_plus_m - diff`
`b = (r_plus_m - diff) / 2`
Or, more simply, once `a` is found, `b = r_plus_m - a`.

This elegant mathematical approach allows us to find `a` and `b`.

#### **Step-by-Step Algorithm**

1.  **Calculate $N$:**
    * `n = len(grid)`: Get the dimension of the grid.
    * $N = n^2$: Calculate the total number of elements `N*N`.

2.  **Calculate Expected Sums:**
    * `total_sum = N * (N + 1) // 2`: Calculate the expected sum of integers from 1 to $N^2$.
    * `total_sum_squares = N * (N + 1) * (2 * N + 1) // 6`: Calculate the expected sum of squares of integers from 1 to $N^2$.

3.  **Calculate Actual Sums from Grid:**
    * `actual_sum = sum(num for row in grid for num in row)`: Flatten the grid and sum all numbers.
    * `actual_sum_squares = sum(num * num for row in grid for num in row)`: Flatten the grid and sum the squares of all numbers.

4.  **Calculate Differences:**
    * `diff = actual_sum - total_sum`: This is `a - b`.
    * `diff_squares = actual_sum_squares - total_sum_squares`: This is `a^2 - b^2`.

5.  **Solve for `a + b`:**
    * `r_plus_m = diff_squares // diff`: This calculates `a + b`. Integer division `//` is used because the result will always be an integer (unless `diff` is zero, which is handled implicitly below).
        * **Note on `diff == 0`**: If `a - b == 0`, it means `a == b`. This scenario is impossible based on problem description ("a which appears twice and b which is missing" implies `a != b`). Therefore, `diff` will never be zero.

6.  **Solve for `a` (repeated) and `b` (missing):**
    * `r = (diff + r_plus_m) // 2`: Solve for `a` (the repeated number).
    * `m = r_plus_m - r`: Solve for `b` (the missing number).

7.  **Return Result:**
    * `return [r, m]`: Return the array containing the repeated and missing values.

#### **Example Trace (`grid = [[1, 2], [2, 4]]`)**

Here, `n = 2`. So $N = n^2 = 4$.
Expected numbers: `{1, 2, 3, 4}`.
Actual numbers: `{1, 2, 2, 4}`.
Repeated (`a`): `2`. Missing (`b`): `3`. Expected result: `[2, 3]`.

1.  `n = 2`
2.  `N = 4`
    * `total_sum = 4 * 5 // 2 = 10`
    * `total_sum_squares = 4 * 5 * 9 // 6 = 30`
3.  `actual_sum = 1 + 2 + 2 + 4 = 9`
    * `actual_sum_squares = 1^2 + 2^2 + 2^2 + 4^2 = 1 + 4 + 4 + 16 = 25`
4.  `diff = actual_sum - total_sum = 9 - 10 = -1` (This is `a - b = 2 - 3 = -1`. Correct!)
    * `diff_squares = actual_sum_squares - total_sum_squares = 25 - 30 = -5` (This is `a^2 - b^2 = 2^2 - 3^2 = 4 - 9 = -5`. Correct!)
5.  `r_plus_m = diff_squares // diff = -5 // -1 = 5` (This is `a + b = 2 + 3 = 5`. Correct!)
6.  `r = (diff + r_plus_m) // 2 = (-1 + 5) // 2 = 4 // 2 = 2` (Repeated number `a` is `2`. Correct!)
    * `m = r_plus_m - r = 5 - 2 = 3` (Missing number `b` is `3`. Correct!)
7.  `return [2, 3]`

#### **Complexity Analysis**

Let $N_{total} = n^2$ be the total number of elements in the grid.

* **Time Complexity:** $O(N_{total})$
    * Calculating `total_sum` and `total_sum_squares` are $O(1)$ operations as they use direct formulas.
    * Iterating through the grid to calculate `actual_sum` and `actual_sum_squares` requires visiting each of the `n*n` elements once. This is $O(n^2)$ or $O(N_{total})$.
    * The remaining arithmetic operations are $O(1)$.
    * Thus, the dominant factor is scanning the grid, leading to $O(n^2)$ time complexity.

* **Space Complexity:** $O(1)$
    * The solution uses only a few constant variables to store sums, differences, and the final results. It does not use any data structures whose size scales with the input grid size.

#### **Advantages of this Algorithm**

* **Optimal Time Complexity:** Achieves $O(n^2)$ time, which is optimal as every element in the grid must be visited at least once.
* **Optimal Space Complexity:** Achieves $O(1)$ auxiliary space, which is highly efficient.
* **Elegant and Robust:** The mathematical approach is clean and less prone to edge-case errors compared to, for example, using a hash set or modifying the array, and correctly handles various number ranges within integer limits.
