LeetCode 371 "Sum of Two Integers"
---

### **Algorithm Analysis: Sum of Two Integers**

This problem asks us to find the sum of two integers, `a` and `b`, without using the standard `+` or `-` arithmetic operators. This typically implies using bitwise operations.

The solution handles various cases, including numbers with the same sign, numbers with different signs, and cases involving zero, by leveraging bitwise addition and subtraction algorithms.

#### **Core Idea: Bitwise Addition and Subtraction**

The fundamental principle is to simulate binary arithmetic using bitwise operations:

1.  **Bitwise Addition (`a + b`)**:
    * **Sum without Carry (XOR):** `a ^ b` gives the sum of bits without considering carries. If bits are the same (0+0=0, 1+1=0), the XOR result is 0. If bits are different (0+1=1, 1+0=1), the XOR result is 1.
    * **Carry Bits (AND & Left Shift):** `(a & b) << 1` calculates the carry bits. If both bits are 1 (`a & b` is 1), a carry is generated. This carry then needs to be added to the *next* higher bit position, which is achieved by left-shifting (`<< 1`).
    * The process repeats: the `sum` becomes the new `a`, and the `carry` becomes the new `b`. The loop continues until there are no more `carry` bits (`b` becomes 0).

2.  **Bitwise Subtraction (`a - b`)**:
    * Subtraction can be thought of as `a + (~b + 1)` (adding the two's complement of `b`).
    * Alternatively, direct bitwise subtraction uses similar logic:
        * **Difference (XOR):** `a ^ b` initially gives the difference without considering borrows.
        * **Borrow Bits (NOT AND & Left Shift):** `(~a) & b` calculates the bits that need to be "borrowed" from the next higher position. If `a` has a 0 bit and `b` has a 1 bit at the same position, a borrow is needed. This `borrow` is then shifted left (`<< 1`) to be applied to the next position.
        * The process repeats until there are no more `borrow` bits.

#### **Algorithm Breakdown (`getSum` and `subtract` methods)**

The `getSum` method orchestrates the operation based on the signs of `a` and `b`.

##### **1. `getSum(self, a: int, b: int) -> int`**

* **Case 1: `a * b > 0` (Both `a` and `b` have the same sign, non-zero)**
    * If both are negative (e.g., `-5 + -2`): The problem is converted to adding their absolute values (`5 + 2`) and then negating the final result (`-7`). `neg` flag tracks this.
    * The core bitwise addition loop is performed:
        * `while b != 0:`:
            * `carry = a & b`: Calculate bits that will carry over.
            * `a = a ^ b`: Calculate sum bits where `a` and `b` are different.
            * `b = carry << 1`: Shift carries left to add them in the next iteration.
    * `return a if not neg else -a`: Return the sum, applying negation if original numbers were negative.

* **Case 2: `a * b == 0` (At least one of `a` or `b` is zero)**
    * `return a if b == 0 else b`: If `b` is zero, the sum is `a`. Otherwise (if `a` is zero), the sum is `b`. This correctly handles cases like `5 + 0` or `0 + -3`.

* **Case 3: `else` (meaning `a * b < 0`, `a` and `b` have different signs)**
    * This scenario requires subtraction of absolute values.
    * `if a > 0:`: If `a` is positive and `b` is negative (e.g., `5 + (-2)` or `2 + (-5)`).
        * `return self.subtract(a, abs(b))`: Calls the `subtract` helper with `a` and the absolute value of `b`.
    * `else` (`a` is negative and `b` is positive, e.g., `-5 + 2` or `-2 + 5`).
        * `return self.subtract(b, abs(a))`: Calls the `subtract` helper with `b` and the absolute value of `a`. This ensures the larger positive number is potentially the first argument of `subtract` for simpler logic, and `subtract` itself handles ordering.

##### **2. `subtract(self, a: int, b: int) -> int` (Helper for Bitwise Subtraction)**

* **Handle `a == b`:** `if a == b: return 0`: If numbers are equal, their difference is 0.
* **Order and Sign for Subtraction:**
    * `neg = False`: Flag to track if the final result should be negative.
    * `if a < b:`: If the first operand (`a`) is smaller than the second (`b`) (e.g., `2 - 5`), swap them (`a=5, b=2`) and set `neg = True`. The calculated difference will then be negated at the end. This simplifies the bitwise subtraction to always deal with `(larger_abs) - (smaller_abs)`.
* **Bitwise Subtraction Loop:**
    * `while b != 0:`: Loop continues as long as there are `borrow` bits.
        * `borrow = (~a) & b`: Calculates bits that need to be borrowed.
        * `a = a ^ b`: Calculates the difference bits.
        * `b = borrow << 1`: Shifts borrow bits left to apply in the next iteration.
* `return a if not neg else -a`: Returns the difference, applying negation if the original `a` was smaller than `b`.

#### **Complexity Analysis**

* **Time Complexity: $O(\log(\max(|a|, |b|)))$**
    * Both `getSum` and `subtract` functions use `while` loops that iterate as long as `b` (or `carry`/`borrow`) is non-zero. In each iteration, `b` effectively shifts bits, reducing its value until it becomes zero.
    * The number of iterations is proportional to the number of bits in the larger of `a` or `b`. For typical fixed-size integers (e.g., 32-bit), this is a constant number of operations (e.g., 32 or 64). For Python's arbitrary-precision integers, it scales with the number of bits required to represent the larger number, which is logarithmic with respect to the magnitude of the number.

* **Space Complexity: $O(1)$**
    * The solution uses a fixed number of variables (`a`, `b`, `carry`, `borrow`, `neg`), regardless of the magnitude of the input integers. No additional data structures are allocated.

#### **Advantages of this Algorithm**

* **Adheres to Constraints:** Perfectly solves the problem without using `+` or `-` operators.
* **Efficient:** The bitwise operations are very fast, resulting in a highly efficient logarithmic time complexity.
* **Handles All Integer Cases:** The comprehensive handling of positive, negative, and zero inputs, and combinations thereof, makes the solution robust.
* **Pythonic Handling of Integers:** Python's native support for arbitrary-precision integers and two's complement interpretation for bitwise operations simplifies the code compared to languages that require explicit bitmasking for negative numbers.
