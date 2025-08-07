LeetCode 3201 "Find the Maximum Length of Valid Subsequence I"
---

### **Algorithm Analysis: Find the Maximum Length of Valid Subsequence I**

This problem defines a "valid subsequence" as one where the sum of any two adjacent elements has the same parity throughout the subsequence. We need to find the maximum possible length of such a valid subsequence.

Let `sub` be a valid subsequence. The condition is `(sub[i] + sub[i+1]) % 2 == C` for some constant `C` and for all valid `i`.

There are two possible values for `C`:

1.  **Case 1: `C = 0` (Sum of adjacent elements is always Even)**
    * If `(sub[i] + sub[i+1]) % 2 == 0`, it means `sub[i]` and `sub[i+1]` must have the *same parity*.
    * This implies that all elements in the subsequence must be either all even or all odd.
    * The longest such subsequence would simply be the total count of even numbers in `nums` or the total count of odd numbers in `nums`.

2.  **Case 2: `C = 1` (Sum of adjacent elements is always Odd)**
    * If `(sub[i] + sub[i+1]) % 2 == 1`, it means `sub[i]` and `sub[i+1]` must have *different parities*.
    * This implies the subsequence must be an alternating parity sequence (e.g., Even, Odd, Even, Odd, ... or Odd, Even, Odd, Even, ...).
    * We need to find the maximum length of such an alternating subsequence.

The solution calculates the maximum length for both cases and returns the overall maximum.

#### **Core Idea: Tracking Counts for Both Parity Sum Types**

The solution maintains counters for both possibilities:

* **For Case 1 (Same Parity Elements):** It directly counts the total number of even and odd elements in the input array.
* **For Case 2 (Alternating Parity Elements):** It uses a dynamic programming / greedy approach to track the lengths of the two types of alternating subsequences.

#### **Algorithm Breakdown**

1.  **Initialization:**
    * `n = len(nums)`: Get the length of the input array.
    * `odd = 0`: Counter for total odd numbers (for Case 1).
    * `even = 0`: Counter for total even numbers (for Case 1).
    * `odd_even = [False, 0]`: This variable tracks the length of an alternating subsequence that ideally follows the pattern `(..., Even, Odd, Even, ...)`
        * `odd_even[0]` (boolean flag): `False` means the last element added to this particular sequence was Even (so it expects an Odd next). `True` means the last was Odd (expects Even next).
        * `odd_even[1]` (integer): The current length of this alternating sequence.
    * `even_odd = [True, 0]`: This variable tracks the length of an alternating subsequence that ideally follows the pattern `(..., Odd, Even, Odd, ...)`
        * `even_odd[0]` (boolean flag): `True` means the last element added was Odd (expects Even next). `False` means the last was Even (expects Odd next).
        * `even_odd[1]` (integer): The current length of this alternating sequence.

2.  **Iterate and Update Counts/Lengths:**
    * `for i in range(n):` Loop through each number in `nums`.
    * `if nums[i] % 2 == 0:` (Current number is Even)
        * `even += 1`: Increment total even count.
        * **Update `odd_even`:**
            * `if odd_even[0]:`: If `odd_even`'s last element was Odd (meaning it expects Even next). Current is Even. This matches.
                * `odd_even[0] = False`: Update flag to indicate last was Even.
                * `odd_even[1] += 1`: Increment its length.
            * If `odd_even[0]` is `False` (last was Even, current is Even): This breaks its `E,O,E` pattern. `odd_even[1]` is not updated, meaning this specific path doesn't extend from this point.
        * **Update `even_odd`:**
            * `if even_odd[0]:`: If `even_odd`'s last element was Odd (meaning it expects Even next). Current is Even. This matches.
                * `even_odd[0] = False`: Update flag to indicate last was Even.
                * `even_odd[1] += 1`: Increment its length.
            * Similar non-update if pattern breaks.
    * `else:` (Current number is Odd)
        * `odd += 1`: Increment total odd count.
        * **Update `odd_even`:**
            * `if not odd_even[0]:`: If `odd_even`'s last element was Even (meaning it expects Odd next). Current is Odd. This matches.
                * `odd_even[0] = True`: Update flag to indicate last was Odd.
                * `odd_even[1] += 1`: Increment its length.
        * **Update `even_odd`:**
            * `if not even_odd[0]:`: If `even_odd`'s last element was Even (meaning it expects Odd next). Current is Odd. This matches.
                * `even_odd[0] = True`: Update flag to indicate last was Odd.
                * `even_odd[1] += 1`: Increment its length.

3.  **Return Maximum Length:**
    * `return max(odd, even, odd_even[1], even_odd[1])`: The final answer is the maximum among:
        * The longest all-odd subsequence (`odd`).
        * The longest all-even subsequence (`even`).
        * The longest `E, O, E, O...` alternating subsequence (`odd_even[1]`).
        * The longest `O, E, O, E...` alternating subsequence (`even_odd[1]`).

#### **Explanation of `odd_even` and `even_odd` for Alternating Subsequences**

The variables `odd_even` and `even_odd` implement a greedy strategy to find the longest alternating parity subsequence. Each variable attempts to extend a chain based on its last encountered element's parity. If a number `nums[i]` does *not* fit the currently expected parity for that chain, the chain's length is not incremented. This implicitly keeps track of the longest *contiguous* alternating sequence that could be formed by continuing from a previous element, and by not resetting, it also implicitly allows for new alternating sequences to start when previous ones break, ensuring it finds the maximum possible length.

#### **Example Trace (`nums = [10, 1, 2, 3]`)**

1.  **Initial:** `odd=0, even=0, odd_even=[F,0], even_odd=[T,0]`
    (`odd_even`: expects `O` next, len 0. `even_odd`: expects `E` next, len 0)

2.  **`i=0, nums[0]=10` (Even):**
    * `even = 1`
    * `odd_even`: `odd_even[0]` is `False` (expects `O`), `nums[0]` is `E`. No match. `odd_even` remains `[F,0]`.
    * `even_odd`: `even_odd[0]` is `True` (expects `E`), `nums[0]` is `E`. Match!
        * `even_odd[0] = False` (now expects `O`)
        * `even_odd[1] = 1`
    * Current state: `odd=0, even=1, odd_even=[F,0], even_odd=[F,1]`

3.  **`i=1, nums[1]=1` (Odd):**
    * `odd = 1`
    * `odd_even`: `odd_even[0]` is `False` (expects `O`), `nums[1]` is `O`. Match!
        * `odd_even[0] = True` (now expects `E`)
        * `odd_even[1] = 1`
    * `even_odd`: `even_odd[0]` is `False` (expects `O`), `nums[1]` is `O`. Match!
        * `even_odd[0] = True` (now expects `E`)
        * `even_odd[1] = 2`
    * Current state: `odd=1, even=1, odd_even=[T,1], even_odd=[T,2]`

4.  **`i=2, nums[2]=2` (Even):**
    * `even = 2`
    * `odd_even`: `odd_even[0]` is `True` (expects `E`), `nums[2]` is `E`. Match!
        * `odd_even[0] = False` (now expects `O`)
        * `odd_even[1] = 2`
    * `even_odd`: `even_odd[0]` is `True` (expects `E`), `nums[2]` is `E`. Match!
        * `even_odd[0] = False` (now expects `O`)
        * `even_odd[1] = 3`
    * Current state: `odd=1, even=2, odd_even=[F,2], even_odd=[F,3]`

5.  **`i=3, nums[3]=3` (Odd):**
    * `odd = 2`
    * `odd_even`: `odd_even[0]` is `False` (expects `O`), `nums[3]` is `O`. Match!
        * `odd_even[0] = True` (now expects `E`)
        * `odd_even[1] = 3`
    * `even_odd`: `even_odd[0]` is `False` (expects `O`), `nums[3]` is `O`. Match!
        * `even_odd[0] = True` (now expects `E`)
        * `even_odd[1] = 4`
    * Current state: `odd=2, even=2, odd_even=[T,3], even_odd=[T,4]`

6.  **End of loop.**
    * `max(odd=2, even=2, odd_even[1]=3, even_odd[1]=4)`
    * Result: `4`.

This correctly identifies `[10, 1, 2, 3]` as a valid subsequence of length 4 (sum of adjacent is always odd).

#### **Complexity Analysis**

Let $n$ be the length of the input array `nums`.

* **Time Complexity:** $O(n)$
    * The single `for` loop iterates `n` times.
    * Inside the loop, all operations (modulo, comparisons, additions, boolean assignments) are constant time.
    * Therefore, the overall time complexity is linear with the input size.

* **Space Complexity:** $O(1)$
    * The solution uses a fixed number of variables (`n`, `odd`, `even`, `odd_even`, `even_odd`).
    * The space used does not scale with the size of the input array.

#### **Advantages of this Algorithm**

* **Optimal Efficiency:** Achieves linear time and constant space complexity, which is the most efficient possible for this problem as every element must be examined at least once.
* **Comprehensive:** Correctly handles both types of valid subsequences (same-parity elements and alternating-parity elements) and finds the maximum length across both.
* **Greedy/DP Hybrid:** The logic for `odd_even` and `even_odd` is a compact way to implement the dynamic programming states for longest alternating subsequences.
* **Concise:** The solution is relatively short and to the point.
