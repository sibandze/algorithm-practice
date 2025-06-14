# Karatsuba Multiplication Algorithm

This repository contains an implementation of the Karatsuba algorithm for multiplying large integers. This algorithm provides a more efficient approach than the traditional "long multiplication" method.

## Problem Description

The fundamental problem is to **multiply two large integers**, say $X$ and $Y$.

The standard elementary school multiplication method (also known as "long multiplication" or "grade school multiplication") has a time complexity of $O(N^2)$, where $N$ is the number of digits in the integers. For very large numbers (e.g., hundreds or thousands of digits), this quadratic complexity can become a significant bottleneck.

The Karatsuba algorithm offers a faster alternative, especially for very large numbers.

**Example:**

Multiply $X = 1234$ and $Y = 5678$.

Using the traditional method:
```
  1234
x 5678
-------
   9872 (1234 * 8)
  86380 (1234 * 70)
 740400 (1234 * 600)
6170000 (1234 * 5000)
-------
7006652
```

## Solution Approach: Karatsuba Algorithm (Divide and Conquer)

The Karatsuba algorithm is a **divide and conquer** algorithm that significantly reduces the number of single-digit multiplications required compared to the traditional method.

Let's say we want to multiply two $N$-digit numbers, $X$ and $Y$.

1.  **Divide:**
    We split $X$ and $Y$ into two halves (approximately $N/2$ digits each).
    Let $m$ be $10^{\lfloor N/2 \rfloor}$.
    We can write:
    $X = X_1 \cdot m + X_0$
    $Y = Y_1 \cdot m + Y_0$
    where $X_1, X_0, Y_1, Y_0$ are the halves. $X_0$ and $Y_0$ are the lower-order digits, and $X_1$ and $Y_1$ are the higher-order digits.

2.  **Conquer (Initial Thought - Naive Divide & Conquer):**
    The product $X \cdot Y$ would then be:
    $X \cdot Y = (X_1 \cdot m + X_0)(Y_1 \cdot m + Y_0)$
    $X \cdot Y = X_1 Y_1 \cdot m^2 + (X_1 Y_0 + X_0 Y_1) \cdot m + X_0 Y_0$

    This approach would require four recursive multiplications: $X_1 Y_1$, $X_1 Y_0$, $X_0 Y_1$, and $X_0 Y_0$. If we define $T(N)$ as the time to multiply two $N$-digit numbers, this leads to the recurrence $T(N) = 4 \cdot T(N/2) + O(N)$, which by the Master Theorem, solves to $O(N^2)$ – no better than the grade school method!

3.  **Karatsuba's Clever Optimization:**
    Karatsuba's insight is to reduce the number of recursive multiplications from four to three. Instead of calculating $X_1 Y_0 + X_0 Y_1$ directly, we observe:
    $(X_1 + X_0)(Y_1 + Y_0) = X_1 Y_1 + X_1 Y_0 + X_0 Y_1 + X_0 Y_0$

    Let:
    * $A = X_1 Y_1$ (one recursive multiplication)
    * $C = X_0 Y_0$ (another recursive multiplication)
    * $B' = (X_1 + X_0)(Y_1 + Y_0)$ (a third recursive multiplication)

    Then, we can derive the middle term:
    $X_1 Y_0 + X_0 Y_1 = B' - A - C$

    So, the product becomes:
    $X \cdot Y = A \cdot m^2 + (B' - A - C) \cdot m + C$

    This way, we perform only **three** recursive multiplications of numbers with approximately $N/2$ digits, along with some additions, subtractions, and multiplications by powers of 10 (which are just shifts).

### High-Level Pseudocode

```
function MULTIPLY(X, Y):
    // Ensure X is the smaller number to simplify length calculation
    if LENGTH(X) > LENGTH(Y):
        SWAP(X, Y)

    n = number of digits in X

    // Base Case: If n is small (e.g., 1 digit), use direct multiplication
    if n == 1:
        return X * Y

    // Divide: Determine split point m = 10^(n//2)
    m = 10^(n//2)

    // Split X and Y into halves
    X1 = X // m  (higher-order digits of X)
    X0 = X % m   (lower-order digits of X)
    Y1 = Y // m  (higher-order digits of Y)
    Y0 = Y % m   (lower-order digits of Y)

    // Conquer: Perform three recursive multiplications
    A = MULTIPLY(X1, Y1)
    C = MULTIPLY(X0, Y0)
    B_prime = MULTIPLY(X1 + X0, Y1 + Y0)

    // Combine: Calculate the middle term and final product
    B = B_prime - A - C

    return (A * (m*m)) + (B * m) + C
```

## Analysis of the Solution

### 1. Time Complexity

The time complexity of the Karatsuba algorithm is $\mathbf{O(N^{\log_2 3})}$, which is approximately $\mathbf{O(N^{1.585})}$. This is a significant improvement over $O(N^2)$ for large values of $N$.

Let $T(N)$ be the time complexity to multiply two $N$-digit numbers.

* **Base Case:** For $N=1$, multiplication is $O(1)$.
* **Recursive Step:**
    * **Divide:** Splitting numbers and determining $m$ involves digit operations (integer division, modulo, length of string conversion). These operations take $O(N)$ time.
    * **Conquer:** Three recursive calls are made on numbers with approximately $N/2$ digits: $3 \cdot T(N/2)$.
    * **Combine:** Additions, subtractions, and multiplications by powers of 10 (which are effectively shifts) take $O(N)$ time.

* **Recurrence Relation:**
    The recurrence relation for the time complexity $T(N)$ is:
    $$T(N) = 3 \cdot T(N/2) + O(N)$$

* **Solving the Recurrence (Master Theorem):**
    Using the Master Theorem, with $a=3$, $b=2$, and $f(N)=O(N)$:
    $N^{\log_b a} = N^{\log_2 3} \approx N^{1.585}$
    Since $f(N) = O(N)$ and $N < N^{\log_2 3}$, case 1 of the Master Theorem applies.
    Therefore, the time complexity is $\mathbf{T(N) = O(N^{\log_2 3})}$.

### 2. Space Complexity

The space complexity of the Karatsuba algorithm is $\mathbf{O(N)}$ due to the recursion stack.

* Each recursive call creates new (smaller) numbers for $X_0, X_1, Y_0, Y_1$, and intermediate results ($A, C, B'$).
* The depth of the recursion is $O(\log N)$ (since we divide $N$ by 2 in each step).
* At each level, numbers of size $N/2, N/4, \dots, 1$ are generated. While new numbers are created, the total size of numbers across all levels of the call stack at any given time is still proportional to $N$. Python's arbitrary precision integers can consume variable amounts of memory.

### 3. Advantages

* **Efficiency:** Significantly faster than the grade school multiplication method for large integers. The exponent of $N$ is reduced from $2$ to approximately $1.585$.
* **Divide and Conquer:** A classic example of how divide and conquer can yield asymptotically faster algorithms.

### 4. Disadvantages/Considerations

* **Overhead for Small Numbers:** For very small numbers (e.g., less than 10-20 digits), the overhead of recursion, splitting, and combining operations can make Karatsuba slower than the simple $O(N^2)$ method. The base case `if n == 1: return x * y` is crucial for performance. In a real-world implementation, this base case would typically be set to a larger threshold (e.g., 10-20 digits) where standard multiplication becomes faster.
* **Implementation Complexity:** More complex to implement correctly than simple multiplication.
* **String Conversion:** The current Python implementation uses `len(str(x))` to determine the number of digits. While convenient, converting numbers to strings repeatedly adds overhead. For maximum efficiency with very large numbers, one might work directly with arrays of digits or specialized big-integer libraries. (Python's built-in integers handle arbitrary precision automatically, so this is mainly a conceptual point for `len(str(x))`).

