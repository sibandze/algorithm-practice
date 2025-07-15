LeetCode 2523 "Closest Prime Numbers in Range"
---

### **Algorithm Analysis: Closest Prime Numbers in Range**

This problem asks us to find two prime numbers, `num1` and `num2`, within a given range `[left, right]` such that `left <= num1 < num2 <= right`, and `num2 - num1` is minimized. If multiple pairs satisfy this, we return the one with the smallest `num1`. If no such pair exists, we return `[-1, -1]`.

#### **Core Idea: Sieve of Eratosthenes and Linear Scan**

The problem has two main parts:
1.  **Finding all primes within a given range:** Since the `right` bound can be up to $10^6$, checking primality for each number individually using trial division would be too slow ($O(N \sqrt{N})$). A more efficient approach for finding all primes up to a certain limit is the Sieve of Eratosthenes.
2.  **Finding the closest pair:** Once all primes in the range are identified, we can iterate through them to find the pair with the minimum difference.

#### **Algorithm Breakdown**

The solution consists of two methods: `closestPrimes` (the main logic) and `sieveOfEratosthenes` (a helper for prime generation).

##### **1. `sieveOfEratosthenes(int n)` (Helper Method)**

* **Purpose:** This method generates a boolean array `isPrime` where `isPrime[i]` is `true` if `i` is prime, and `false` otherwise, up to the given limit `n`.
* **Initialization:**
    * `boolean[] isPrime = new boolean[n + 1];`: Creates a boolean array of size `n+1`.
    * `Arrays.fill(isPrime, true);`: Initially assumes all numbers from 0 to `n` are prime.
    * `isPrime[0] = isPrime[1] = false;`: Correctly marks 0 and 1 as non-prime.
* **Sieving Process:**
    * `for (int i = 2; i * i <= n; i++)`: The outer loop iterates from `2` up to $\sqrt{n}$. We only need to check factors up to the square root of `n` because if a number `k` has a factor greater than $\sqrt{k}$, it must also have a factor smaller than $\sqrt{k}$.
    * `if (isPrime[i])`: If `i` is currently marked as prime (meaning it hasn't been crossed out by a smaller prime).
        * `for (int j = i * i; j <= n; j += i)`: Mark all multiples of `i` (starting from $i^2$) as non-prime. We start from $i^2$ because smaller multiples (e.g., $2i, 3i, \dots, (i-1)i$) would have already been marked by smaller prime factors.

* **Return:** `return isPrime;`

##### **2. `closestPrimes(int left, int right)` (Main Method)**

* **Initial Edge Cases:**
    * `if (left >= right || right > 1_000_000)`: Handles invalid ranges or `right` exceeding the sieve's practical limit. Returns `[-1, -1]`.
* **Generate Primes:**
    * `boolean[] isPrime = sieveOfEratosthenes(right);`: Calls the helper to get the primality array up to `right`.
* **Collect Primes in Range:**
    * `ArrayList<Integer> primesInRange = new ArrayList<>();`: Initializes a list to store primes found within `[left, right]`.
    * `for (int i = left; i <= right; i++)`: Iterates through the given range.
    * `if (isPrime[i]) { primesInRange.add(i); }`: If a number `i` is prime (according to the sieve), add it to `primesInRange`.
* **Handle Insufficient Primes:**
    * `if (primesInRange.size() < 2)`: If fewer than two primes are found in the range, no pair can be formed. Returns `[-1, -1]`.
* **Find Closest Pair:**
    * `int minDiff = Integer.MAX_VALUE;`: Stores the minimum difference found so far.
    * `int num1 = -1, num2 = -1;`: Stores the pair with the minimum difference.
    * `for (int i = 1; i < primesInRange.size(); i++)`: Iterate through the `primesInRange` list, comparing adjacent primes.
        * `int diff = primesInRange.get(i) - primesInRange.get(i - 1);`: Calculate the difference between the current prime and the previous one.
        * `if (diff < minDiff)`: If this difference is smaller than `minDiff`:
            * `minDiff = diff;`: Update `minDiff`.
            * `num1 = primesInRange.get(i - 1);`: Store the smaller prime.
            * `num2 = primesInRange.get(i);`: Store the larger prime.
            * `if (minDiff <= 2) { break; }`: **Optimization:** If `minDiff` is 1 (only possible for `[2, 3]`) or 2 (for twin primes like `[3, 5]`, `[5, 7]`, etc.), this is the smallest possible difference between two distinct primes. No smaller difference can be found, so we can stop early.
* **Return Result:** `return new int[] {num1, num2};`

#### **Complexity Analysis**

Let $R$ be the value of `right`.

* **Time Complexity:** $O(R \log \log R + (R - L))$
    * `sieveOfEratosthenes(right)`: The Sieve of Eratosthenes has a time complexity of $O(R \log \log R)$. This is the dominant part for generating primes.
    * Collecting `primesInRange`: This loop iterates `R - L + 1` times. Inside the loop, array access is $O(1)$ and `ArrayList.add` is amortized $O(1)$. So, $O(R - L)$.
    * Finding the closest pair: This loop iterates up to `primesInRange.size()` times. The number of primes up to `R` is approximately $R/\ln R$. So, this part is $O(R/\ln R)$.
    * Combining these, the overall time complexity is dominated by the sieve: $O(R \log \log R)$.

* **Space Complexity:** $O(R)$
    * `boolean[] isPrime`: This array takes $O(R)$ space.
    * `ArrayList<Integer> primesInRange`: In the worst case (e.g., `left = 0`, `right = 10^6`), this list can store up to $\approx R/\ln R$ integers. This is also $O(R)$.

#### **Advantages of this Algorithm**

* **Efficient Prime Generation:** Using the Sieve of Eratosthenes is highly efficient for finding all primes up to a given limit, especially when the range itself is large but `right` is within a manageable bound ($10^6$).
* **Clear and Correct:** The logic for finding the closest pair after prime generation is straightforward and correctly handles the minimum `num1` tie-breaking rule (implicitly, by iterating from left to right and updating only if `diff < minDiff`). The early exit for `minDiff <= 2` is a good optimization.
* **Standard Approach:** This is a standard and well-understood method for solving problems involving prime numbers within a range.

#### **Potential Considerations/Edge Cases**

* **`left` or `right` being 0 or 1:** The `sieveOfEratosthenes` correctly marks `0` and `1` as non-prime, so they won't be included in `primesInRange`.
* **No primes in range:** Handled by `primesInRange.size() < 2`.
* **Large `right` values:** The constraint `right <= 1_000_000` makes the Sieve feasible. If `right` were much larger (e.g., $10^{12}$), a segmented sieve or other advanced primality tests would be needed.
* **Small `right` values:** The code explicitly checks `right > 1_000_000` but given the problem constraint, this is more of a safeguard. The actual relevant constraint is `right <= 10^6`.
* **`left` and `right` are the same prime:** The condition `num1 < num2` means a single prime doesn't form a valid pair. This is handled by `primesInRange.size() < 2`.
