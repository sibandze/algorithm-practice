LeetCode 1290 "Convert Binary Number in a Linked List to Integer"
---

### **Algorithm Analysis: Convert Binary Number in a Linked List to Integer**

This problem asks us to convert a binary number, represented as a singly-linked list (where each node's value is either `0` or `1`), into its decimal equivalent. The most significant bit (MSB) is at the head of the linked list.

#### **Core Idea: Bit Shifting (or "Doubling")**

The standard way to convert a binary number to decimal is to assign powers of 2 to each bit position and sum them up. For a binary number $b_n b_{n-1} \dots b_1 b_0$, its decimal value is $b_n \cdot 2^n + b_{n-1} \cdot 2^{n-1} + \dots + b_1 \cdot 2^1 + b_0 \cdot 2^0$.

However, when processing from the Most Significant Bit (MSB) (which is at the head of our linked list) to the Least Significant Bit (LSB), there's a more elegant iterative approach:

Initialize `decimal_value = 0`.
For each bit `b` from MSB to LSB:
`decimal_value = decimal_value * 2 + b`

This works because multiplying by 2 effectively "shifts" the existing decimal value one position to the left (like shifting bits in binary), making room for the new bit in the least significant position. Adding the new bit then correctly incorporates it.

#### **Step-by-Step Algorithm**

1.  **Initialize Decimal Value:**
    * `dec = 0`: A variable `dec` (short for decimal) is initialized to `0`. This will accumulate the decimal value as we traverse the linked list.

2.  **Initialize Node Pointer:**
    * `node = head`: A pointer `node` is initialized to the `head` of the linked list. This pointer will traverse the list.

3.  **Traverse the Linked List:**
    * `while node:`: The loop continues as long as `node` is not `None` (i.e., there are still nodes to process).
    * **Update Decimal Value:**
        * `dec = dec * 2 + node.val`: This is the core conversion step.
            * `dec * 2`: This effectively shifts the current accumulated decimal value one bit position to the left, making space for the new bit.
            * `+ node.val`: The value of the current node (either `0` or `1`) is then added to this shifted value. This correctly incorporates the current bit into the decimal representation.
    * **Move to Next Node:**
        * `node = node.next`: Advance the `node` pointer to the next node in the list to process the next bit.

4.  **Return Result:**
    * `return dec`: Once the loop finishes (meaning all nodes have been processed), `dec` will hold the final decimal value of the binary number represented by the linked list.

#### **Example Trace (`head = [1,0,1]` which represents binary `101`)**

1.  **Initial:** `dec = 0`, `node` points to `1`.
2.  **Iteration 1 (`node.val = 1`):**
    * `dec = 0 * 2 + 1 = 1`.
    * `node` moves to `0`.
3.  **Iteration 2 (`node.val = 0`):**
    * `dec = 1 * 2 + 0 = 2`.
    * `node` moves to `1`.
4.  **Iteration 3 (`node.val = 1`):**
    * `dec = 2 * 2 + 1 = 5`.
    * `node` moves to `None`.
5.  **Loop ends.**
6.  **Return `dec` (which is `5`).** Correct! (Binary `101` is decimal `5`).

#### **Complexity Analysis**

* **Time Complexity: $O(L)$**
    * The `while` loop iterates once for each node in the linked list, where `L` is the number of nodes (i.e., the number of bits in the binary representation).
    * Inside the loop, all operations (multiplication, addition, pointer movement) are constant time.
    * Therefore, the total time taken is linear, proportional to the length of the linked list.

* **Space Complexity: $O(1)$**
    * The algorithm uses only a few constant extra variables (`dec`, `node`).
    * It does not allocate any additional data structures whose size scales with the input list.

#### **Advantages of this Algorithm**

* **Efficiency:** Achieves optimal linear time complexity, as each bit (node) is processed exactly once.
* **Constant Space:** Uses a minimal amount of auxiliary memory.
* **Simplicity and Readability:** The iterative bit-shifting approach is very intuitive and easy to implement.
* **Handles Arbitrary Lengths:** Can handle binary numbers of any length as long as they fit within the integer limits of the chosen programming language.
