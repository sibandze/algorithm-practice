LeetCode 20 "Valid Parentheses"
---

### **Algorithm Analysis: Valid Parentheses**

This problem asks us to determine if an input string `s`, consisting only of `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, is "valid". A valid string adheres to three rules:
1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.
3.  Every close bracket has a corresponding open bracket of the same type.

#### **Core Idea: Using a Stack**

This problem is a classic application of a **Stack** data structure. A stack's Last-In, First-Out (LIFO) property is perfectly suited for validating nested structures like parentheses. When we encounter an opening bracket, we push it onto the stack, expecting to find its corresponding closing bracket later. When we encounter a closing bracket, we check the top of the stack to see if it's the matching opening bracket.

#### **Step-by-Step Algorithm**

1.  **Initialization:**
    * `stack`: An empty list (Python's list acts as a stack using `append` for push and `pop` for pop). This stack will temporarily store opening brackets.
    * `mapping`: A dictionary (hash map) that maps each closing bracket to its corresponding opening bracket. This allows for quick lookups to verify matches.
        * `mapping = {")": "(", "}": "{", "]": "["}`

2.  **Iterate Through the String:**
    * Loop through each `char` in the input string `s`.

3.  **Process Each Character:**
    * **If `char` is a Closing Bracket:** (`if char in mapping:`)
        * **Check for Empty Stack or Mismatch:**
            * `if not stack or stack[-1] != mapping[char]: return False`
            * If the `stack` is empty, it means we encountered a closing bracket without a corresponding open bracket. This is invalid.
            * If the `stack` is not empty, check if the top element (`stack[-1]`) is the correct opening bracket for the current `char` (obtained from `mapping[char]`). If they don't match, it's an invalid order or type. In either of these sub-cases, the string is invalid, so return `False`.
        * **Pop from Stack:**
            * If the checks pass (stack is not empty and the top matches), `stack.pop()`: remove the matching opening bracket from the top of the stack.
    * **If `char` is an Opening Bracket:** (`else:`)
        * `stack.append(char)`: Push the opening bracket onto the `stack`. We expect to find its corresponding closing bracket later.

4.  **Final Validation:**
    * `return not stack`: After iterating through the entire string, if the `stack` is empty, it means every opening bracket found had a corresponding and correctly ordered closing bracket. The string is valid, so `not stack` (which evaluates to `True` if `stack` is empty) is returned.
    * If the `stack` is not empty, it means there are unclosed opening brackets left over. The string is invalid, so `not stack` (which evaluates to `False` if `stack` is not empty) is returned.

#### **Complexity Analysis**

* **Time Complexity: $O(N)$**
    * The algorithm iterates through the input string `s` exactly once, where `N` is the length of the string.
    * Inside the loop, stack operations (`append`, `pop`, `[-1]`) and dictionary lookups (`in`, `[]`) all take $O(1)$ time on average.
    * Therefore, the total time complexity is linear, proportional to the length of the input string.

* **Space Complexity: $O(N)$**
    * In the worst-case scenario (e.g., a string like `((((((())))))))`), the `stack` could store up to `N/2` opening brackets.
    * Therefore, the space complexity is proportional to the length of the input string, $O(N)$. However, it's bounded by the maximum depth of nested parentheses. In practice, it's $O(D)$ where $D$ is the maximum depth, and $D <= N/2$.

#### **Advantages of this Algorithm**

* **Simplicity and Readability:** The stack-based approach is very intuitive and directly models the nesting behavior of parentheses.
* **Efficiency:** Achieves optimal linear time complexity.
* **Robustness:** Correctly handles all three validity rules (type, order, correspondence).
