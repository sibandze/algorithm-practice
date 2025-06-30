** Leetcode Problem 1: Two Sum **
---

### **Algorithm Analysis: The Two Sum Problem**

This solution provides an optimal approach to the classic Two Sum problem using a hash map (or dictionary).

#### **Core Idea**

The brute-force approach to this problem would be to check every possible pair of numbers in the array, which results in a quadratic time complexity ($O(N^2)$). This algorithm, however, improves efficiency by leveraging a hash map to reduce the lookup time for a number's complement from linear ($O(N)$) to constant time ($O(1)$ on average).

The key insight is this: for each number `x` in the array, we need to find if its "complement" (`target - x`) exists. By storing the numbers we've already seen in a hash map, we can check for this complement's existence in a single, fast lookup.

#### **Step-by-Step Algorithm**

1.  **Initialize a Hash Map:** Create an empty hash map (dictionary in Python, `HashMap` in Java) to store `(number: index)` pairs.

2.  **Iterate Through the Array:** Traverse the input array `nums` from beginning to end using its indices.

3.  **Calculate the Complement:** For each number `nums[i]` at the current index `i`, calculate its complement: `complement = target - nums[i]`. This is the value we need to find in the rest of the array to form the target sum.

4.  **Check the Hash Map:**
    * **Lookup:** Check if the `complement` already exists as a key in the hash map.
    * **If found:** This means we have found the two numbers that sum to `target`. The index of the complement is the value associated with the `complement` key in the hash map, and the current index is `i`. Return these two indices.
    * **If not found:** The current number `nums[i]` has not found its complement yet. Add the current number and its index to the hash map as a new key-value pair (`nums[i]: i`). This makes `nums[i]` available for any future numbers to find as their complement.

5.  **Return:** The loop will eventually find the solution, and the function will return the indices. Given the problem constraint that a solution is guaranteed to exist, the loop is guaranteed to terminate with a valid return.

#### **Complexity Analysis**

* **Time Complexity: $O(N)$**
    * The algorithm iterates through the array of size `N` exactly once.
    * Inside the loop, hash map operations (insertion and lookup) have an average time complexity of $O(1)$.
    * Therefore, the total time complexity is dominated by the single pass through the array, resulting in a linear time complexity.

* **Space Complexity: $O(N)$**
    * In the worst-case scenario (where the solution pair is at the end of the array), the hash map will store up to `N-1` elements from the array.
    * Thus, the space required grows linearly with the size of the input array.

#### **Advantages of this Algorithm**

* **Optimal Time:** This algorithm provides the most efficient time complexity for this problem.
* **Single Pass:** It solves the problem by iterating through the array just once, which is highly efficient.
* **Clarity:** The logic is straightforward and easy to understand.
