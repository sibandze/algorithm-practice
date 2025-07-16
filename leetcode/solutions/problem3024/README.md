LeetCode 3024 "Type of Triangle"
---

### **Algorithm Analysis: Type of Triangle**

This problem asks us to determine the type of triangle (equilateral, isosceles, or scalene) given an array `nums` of three integers representing its side lengths. It also requires checking if a valid triangle can even be formed.

#### **Core Idea: Triangle Inequality Theorem and Side Comparisons**

The solution hinges on two fundamental geometric principles:

1.  **Triangle Inequality Theorem:** For any three positive lengths to form a triangle, the sum of the lengths of any two sides must be strictly greater than the length of the third side. After sorting the sides, this simplifies to checking `a + b > c` (where `c` is the longest side). If `a + b <= c`, it cannot form a triangle.
2.  **Side Length Comparisons:** Once it's confirmed to be a valid triangle, we compare the side lengths to determine its type:
    * **Equilateral:** All three sides are equal (`a == b == c`).
    * **Isosceles:** Exactly two sides are equal (`a == b` or `b == c`, but not all three).
    * **Scalene:** All three sides are different (`a != b != c != a`).

#### **Algorithm Breakdown**

1.  **Sort the Sides:**
    * `nums.sort()`: The very first step is to sort the `nums` array in non-decreasing order. This simplifies both the triangle inequality check and the side comparison logic. Let the sorted sides be `nums[0]`, `nums[1]`, and `nums[2]`.

2.  **Check Triangle Inequality:**
    * `if nums[0] + nums[1] <= nums[2]:`: This checks the triangle inequality. If the sum of the two shorter sides is less than or equal to the longest side, a triangle cannot be formed.
    * `return "none"`: If the condition is true, the function immediately returns "none".

3.  **Determine Triangle Type (if valid):**
    * **Equilateral Check:**
        * `if nums[0] == nums[1] and nums[1] == nums[2]:` This checks if all three sides are equal.
        * `return "equilateral"`
    * **Isosceles Check:**
        * `elif nums[0] == nums[1] or nums[1] == nums[2]:` This checks if exactly two sides are equal. Since the equilateral case was handled first, this `elif` ensures we catch cases like `[3, 3, 5]` or `[3, 5, 5]` but not `[5, 5, 5]`.
        * `return "isosceles"`
    * **Scalene (Default):**
        * `else:` If none of the above conditions are met (it's a valid triangle, but not equilateral or isosceles), it must be scalene.
        * `return "scalene"`

#### **Example Trace (`nums = [3, 4, 5]`)**

1.  `nums.sort()`: `nums` becomes `[3, 4, 5]`.
2.  `if nums[0] + nums[1] <= nums[2]`:
    * `3 + 4 <= 5`
    * `7 <= 5` is `False`. So, it can form a triangle.
3.  `if nums[0] == nums[1] and nums[1] == nums[2]`:
    * `3 == 4` is `False`. This condition fails.
4.  `elif nums[0] == nums[1] or nums[1] == nums[2]`:
    * `3 == 4` is `False`.
    * `4 == 5` is `False`.
    * `False or False` is `False`. This condition fails.
5.  `else:`
    * Returns `"scalene"`. Correct!

#### **Example Trace (`nums = [1, 2, 4]`)**

1.  `nums.sort()`: `nums` becomes `[1, 2, 4]`.
2.  `if nums[0] + nums[1] <= nums[2]`:
    * `1 + 2 <= 4`
    * `3 <= 4` is `True`.
3.  `return "none"`. Correct!

#### **Complexity Analysis**

Let $N$ be the number of elements in `nums`, which is fixed at 3.

* **Time Complexity:** $O(1)$
    * `nums.sort()`: Sorting a list of 3 elements takes constant time. While general sorting algorithms are $O(N \log N)$, for a fixed small $N=3$, this is effectively $O(1)$.
    * All subsequent comparisons and arithmetic operations are also $O(1)$.
    * Therefore, the overall time complexity is constant.

* **Space Complexity:** $O(1)$
    * The solution uses only a fixed amount of extra space for variables, regardless of the input values. The `sort()` operation might use some in-place modification or a constant amount of auxiliary space depending on the specific Python interpreter's implementation, but it remains $O(1)$ for fixed-size inputs.

#### **Advantages of this Algorithm**

* **Correctness:** Accurately applies the triangle inequality and type classification rules.
* **Simplicity and Readability:** The code is very straightforward and easy to understand due to its direct translation of the problem rules.
* **Efficiency:** Achieves optimal constant time and space complexity due to the fixed small input size.
* **Robust:** Handles all valid and invalid triangle cases explicitly.
