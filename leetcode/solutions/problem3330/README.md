LeetCode 3330 "Find the Original Type String I"
---

### **Algorithm Analysis: Find the Original Type String I**

This problem asks us to find the total number of possible original strings Alice might have intended to type, given a `word` (the final output) and the constraint that she might have pressed a key for too long **at most once**.

#### **Understanding the "At Most Once" Constraint (as interpreted by the solution)**

The phrasing "at most once" is key. It means two scenarios are possible:
1.  **No mistake occurred:** The `word` Alice typed is exactly what she intended. This always accounts for one possible original string.
2.  **Exactly one mistake occurred:** One single character in the *original* string was typed and then prolonged (repeated consecutively).

The provided solution's logic specifically counts how many times a character `word[i]` is identical to the preceding character `word[i-1]`. Each such occurrence indicates a point where a "prolongation" error *could have* happened, leading to a unique candidate for the original string.

#### **Core Idea: Counting Potential "Un-Prolongations"**

The algorithm implicitly counts the number of distinct original strings by considering `word` itself as one possibility, and then for every occurrence of a consecutive duplicate character `word[i] == word[i-1]`, it adds another distinct possibility. This distinct possibility is formed by conceptually removing `word[i]` (assuming it was the result of the prolongation error).

**Example Traces:**

* **`word = "a"`:**
    * `count = 1`. Loop doesn't run. Returns `1`. (Original: "a")

* **`word = "aa"`:**
    * `count = 1` (Accounts for original "aa")
    * `i = 1`: `word[1]` ('a') `== word[0]` ('a'). True.
        * This suggests `word[1]` could be a prolongation of `word[0]`. If so, the original string could have been "a".
    * `count` becomes `2`.
    * Returns `2`. (Possible Originals: "aa", "a")

* **`word = "aaa"`:**
    * `count = 1` (Accounts for original "aaa")
    * `i = 1`: `word[1]` ('a') `== word[0]` ('a'). True.
        * `count` becomes `2`. (Possible Original: "aa")
    * `i = 2`: `word[2]` ('a') `== word[1]` ('a'). True.
        * `count` becomes `3`. (Possible Original: "a")
    * Returns `3`. (Possible Originals: "aaa", "aa", "a")

* **`word = "apple"`:**
    * `count = 1` (Accounts for original "apple")
    * `i = 1`: `word[1]` ('p') `!= word[0]` ('a'). False.
    * `i = 2`: `word[2]` ('p') `== word[1]` ('p'). True.
        * `word[2]` ('p') could be a prolongation of `word[1]` ('p'). If so, the original string could have been "aple".
    * `count` becomes `2`.
    * `i = 3`: `word[3]` ('l') `!= word[2]` ('p'). False.
    * `i = 4`: `word[4]` ('e') `!= word[3]` ('l'). False.
    * Returns `2`. (Possible Originals: "apple", "aple")

#### **Step-by-Step Algorithm**

1.  **Initialize `count`:**
    * `count = 1`: This variable will store the total number of possible original strings. It is initialized to `1` to account for the scenario where Alice made no mistake, and the original string was identical to the `word` itself.

2.  **Iterate and Check for Consecutive Duplicates:**
    * Loop through the `word` starting from the second character (`i` from `1` to `len(word) - 1`).
    * `if word[i] == word[i-1]:`: In each iteration, check if the current character `word[i]` is the same as the previous character `word[i-1]`.
    * `count += 1`: If they are the same, it means `word[i]` could potentially be a character that was duplicated due to a long press. This forms a new, distinct "original string" possibility (by conceptually considering `word` with this specific `word[i]` removed). Increment `count`.

3.  **Return `count`:**
    * After iterating through the entire string, `count` will hold the total number of possible original strings according to the problem's interpretation.

#### **Complexity Analysis**

* **Time Complexity: $O(N)$**
    * The algorithm iterates through the input `word` exactly once, where `N` is the length of the string.
    * Each operation inside the loop (character comparison and increment) is constant time.
    * Therefore, the total time complexity is linear, proportional to the length of the input string.

* **Space Complexity: $O(1)$**
    * The algorithm uses only a few constant variables (`count`, `i`).
    * It does not allocate any additional data structures whose size scales with the input string.

#### **Advantages of this Algorithm**

* **Simplicity and Efficiency:** The solution is remarkably simple, concise, and highly efficient, achieving optimal linear time complexity.
* **Constant Space:** It uses a minimal amount of auxiliary memory.
* **Direct Interpretation:** It directly implements the counting logic derived from the problem's specific "at most once" constraint regarding consecutive character repetitions, as typically seen in these types of contest problems.

---
