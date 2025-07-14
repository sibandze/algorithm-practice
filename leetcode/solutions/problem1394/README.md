LeetCode 1394 "Find Lucky Integer in an Array"
---

### **Algorithm Analysis: Find Lucky Integer in an Array**

This problem defines a "lucky integer" as an integer whose frequency (count of occurrences) in a given array `arr` is equal to its value. We need to find the largest such lucky integer. If no lucky integer exists, we should return -1.

#### **Core Idea: Frequency Counting and Filtering**

The problem involves checking the frequency of each number against its own value. This immediately suggests using a data structure to store frequencies, like a hash map (dictionary in Python). Once we have the frequencies of all numbers, we can iterate through them, apply the "lucky integer" condition, and find the maximum among the qualifying numbers.

#### **Step-by-Step Algorithm**

1.  **Initialize Frequency Map:**
    * `count = {-1: -1}`: A dictionary `count` is initialized. This dictionary will store the frequency of each number in `arr`.
        * The initial entry `{-1: -1}` is a clever trick to simplify the `max()` call later. If no lucky integer is found, `max()` will operate on a list that contains `-1`, ensuring `-1` is returned (as `-1` cannot be a lucky integer value or frequency).

2.  **Populate Frequency Map:**
    * `for i in range(len(arr)):`: Iterate through each element in the input array `arr`.
    * `count[arr[i]] = count.get(arr[i], 0) + 1`: For each number `arr[i]`:
        * It retrieves the current frequency of `arr[i]` from the `count` dictionary using `count.get(arr[i], 0)`. If `arr[i]` is not yet in the dictionary, `get()` returns `0`.
        * It then increments this frequency by `1` and updates (or adds) the entry in the `count` dictionary.

3.  **Find the Largest Lucky Integer:**
    * `return max([num for num, freq in count.items() if freq == num])`:
        * This line uses a list comprehension to create a list of all lucky integers.
            * `count.items()`: Iterates through each key-value pair (`num`, `freq`) in the `count` dictionary.
            * `if freq == num`: This is the condition for a number to be "lucky" (its frequency equals its value). Only numbers satisfying this condition are included in the generated list.
        * `max(...)`: After the list of lucky integers is constructed, `max()` finds the largest value among them.
        * Due to the initial `{-1: -1}` entry in `count`, if no actual lucky integers are found from `arr`, the list passed to `max()` will only contain `-1`, thus correctly returning `-1`.

#### **Example Trace (`arr = [2,2,3,4]`)**

1.  **Initialize:** `count = {-1: -1}`
2.  **Populate Frequency Map:**
    * `arr[0] = 2`: `count[2] = count.get(2, 0) + 1 = 1`. `count = {-1: -1, 2: 1}`
    * `arr[1] = 2`: `count[2] = count.get(2, 0) + 1 = 2`. `count = {-1: -1, 2: 2}`
    * `arr[2] = 3`: `count[3] = count.get(3, 0) + 1 = 1`. `count = {-1: -1, 2: 2, 3: 1}`
    * `arr[3] = 4`: `count[4] = count.get(4, 0) + 1 = 1`. `count = {-1: -1, 2: 2, 3: 1, 4: 1}`
3.  **Find Lucky Integer:**
    * Iterate through `count.items()`:
        * `(-1, -1)`: `-1 == -1` is True. `-1` is added to the temporary list. `list = [-1]`
        * `(2, 2)`: `2 == 2` is True. `2` is added. `list = [-1, 2]`
        * `(3, 1)`: `1 == 3` is False.
        * `(4, 1)`: `1 == 4` is False.
    * `max([-1, 2])` returns `2`.

#### **Complexity Analysis**

* **Time Complexity: $O(N)$**
    * The first loop iterates through the array `arr` once, performing constant-time dictionary operations (insertion/update) for each element. This takes $O(N)$ time, where $N$ is the length of `arr`.
    * The list comprehension and `max()` call iterate through the `count` dictionary. In the worst case, all elements in `arr` are distinct, so the dictionary can have up to `N` entries. Iterating through the dictionary and applying the `max()` function takes $O(D)$ time, where `D` is the number of distinct elements in `arr`. Since `D <= N`, this step is also $O(N)$.
    * Overall, the dominant factor is $O(N)$.

* **Space Complexity: $O(D)$**
    * The `count` dictionary stores frequencies for each distinct number in `arr`. In the worst case (all numbers are distinct), it will store `N` entries.
    * Therefore, the space complexity is proportional to the number of distinct elements in `arr`, $O(D)$, where $D \le N$.

#### **Advantages of this Algorithm**

* **Clear and Concise:** The use of a dictionary for frequency counting is standard and makes the logic very readable.
* **Efficiency:** Achieves optimal linear time complexity, as it only requires a single pass to count frequencies and another pass (or effectively, a single pass over dictionary items) to filter and find the maximum.
* **Pythonic:** The list comprehension and `max()` function make the final step very compact and Pythonic.
* **Robustness:** The `{-1:-1}` initialization handles the "no lucky integer" case gracefully without needing additional `if` conditions after the `max()` call.
