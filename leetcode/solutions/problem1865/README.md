LeetCode 1865 "Finding Pairs With a Certain Sum"
---

### **Algorithm Analysis: Finding Pairs With a Certain Sum**

This problem requires implementing a data structure, `FindSumPairs`, that supports two main operations on two integer arrays, `nums1` and `nums2`:
1.  **`add(index, val)`**: Update an element in `nums2` by adding `val` to `nums2[index]`.
2.  **`count(tot)`**: Count pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.

The challenge lies in making both `add` and `count` operations efficient, especially since `count` might be called many times.

#### **Core Idea: Pre-computing Frequencies with a Hash Map**

A naive approach for `count(tot)` would be to iterate through all elements of `nums1` and for each `nums1[i]`, then iterate through all elements of `nums2` to find `nums2[j]` such that `nums1[i] + nums2[j] == tot`. This would be $O(N_1 \cdot N_2)$ per `count` query, which is too slow.

The key observation is that `nums1` remains unchanged, while `nums2` can be modified. When searching for `nums1[i] + nums2[j] == tot`, we are essentially looking for `nums2[j] == tot - nums1[i]`. If we can quickly find the frequency of `tot - nums1[i]` in `nums2`, we can sum these frequencies.

A hash map (Python dictionary) is ideal for storing and quickly retrieving frequencies.

#### **Data Structure Design (`FindSumPairs` class)**

1.  **`self.nums1`**: Stores the `nums1` array as is, since it's immutable.
2.  **`self.nums2`**: Stores the `nums2` array. This array will be directly modified by the `add` operation.
3.  **`self.nums2_counter`**: This is a hash map (dictionary) that stores the frequency of each number currently present in `self.nums2`. This map is crucial for efficient `add` and `count` operations.

#### **Step-by-Step Algorithm for Each Method**

##### **1. `__init__(self, nums1: List[int], nums2: List[int])`**

* **Initialization:**
    * `self.nums1 = nums1`: Store the input `nums1` array.
    * `self.nums2 = nums2`: Store the input `nums2` array.
    * `self.nums1_len = len(nums1)`: Store the length of `nums1` for convenience in `count` method.
    * `self.nums2_counter = {}`: Initialize an empty dictionary to store frequencies of numbers in `nums2`.
* **Populate `nums2_counter`:**
    * `for num in self.nums2:`: Iterate through each number in the *initial* `nums2` array.
    * `self.nums2_counter[num] = self.nums2_counter.get(num, 0) + 1`: For each `num`, increment its count in the `nums2_counter`. `dict.get(key, default)` safely retrieves the current count or `0` if the key isn't present.

##### **2. `add(self, index: int, val: int) -> None`**

* This method needs to update `nums2[index]` and also keep `nums2_counter` consistent.
* `prev = self.nums2[index]`: Store the *old* value at `nums2[index]` before modification.
* `self.nums2[index] += val`: Update `nums2[index]` to its new value.
* `self.nums2_counter[prev] -= 1`: Decrement the count of the `prev` (old) value in `nums2_counter`. It's assumed `prev` was present.
* `self.nums2_counter[self.nums2[index]] = self.nums2_counter.get(self.nums2[index], 0) + 1`: Increment the count of the *new* value `self.nums2[index]` in `nums2_counter`. If the new value didn't exist before, `get()` handles it.

##### **3. `count(self, tot: int) -> int`**

* This method counts pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.
* `count = 0`: Initialize a counter for the number of valid pairs.
* `for i in range(self.nums1_len):`: Iterate through each element `nums1[i]` in `nums1`.
    * `target = tot - self.nums1[i]`: Calculate the `target` value that `nums2[j]` needs to be to satisfy the sum condition.
    * `if target in self.nums2_counter:`: Check if this `target` value exists in `nums2` by looking it up in `self.nums2_counter`. This is an $O(1)$ average-case lookup.
    * `count += self.nums2_counter[target]`: If `target` exists, add its frequency from `nums2_counter` to the total `count`. This correctly accounts for all `nums2[j]` values that match `target`.
* `return count`: Return the final accumulated count of pairs.

#### **Complexity Analysis**

Let $N_1$ be the length of `nums1` and $N_2$ be the length of `nums2`. Let $D_2$ be the number of distinct elements in `nums2`.

* **`__init__`**:
    * **Time Complexity:** $O(N_2)$ to iterate through `nums2` and populate `nums2_counter`. Each dictionary operation is average $O(1)$.
    * **Space Complexity:** $O(D_2)$ to store the `nums2_counter` dictionary. In the worst case, $D_2 = N_2$.

* **`add`**:
    * **Time Complexity:** $O(1)$ average case. All dictionary operations (lookup, decrement, increment) are average $O(1)$.
    * **Space Complexity:** $O(1)$.

* **`count`**:
    * **Time Complexity:** $O(N_1)$ average case. The method iterates through `nums1` once. For each element, it performs a constant number of arithmetic operations and an average $O(1)$ dictionary lookup.
    * **Space Complexity:** $O(1)$ (excluding the space for `self.nums1` and `self.nums2_counter` which are part of the object's state).

#### **Advantages of this Design**

* **Efficient `count` queries:** By pre-computing and maintaining frequencies for `nums2`, `count` operations are reduced from $O(N_1 \cdot N_2)$ to $O(N_1)$. This is crucial for problems with many `count` queries.
* **Efficient `add` operations:** Updates to `nums2` are handled efficiently in $O(1)$ time by adjusting the frequency map directly.
* **Clear and Maintainable:** The use of a dictionary for frequency tracking is idiomatic and makes the code easy to understand.
