# Closest Pair of Points Algorithm

This repository contains an implementation of the Closest Pair of Points algorithm using the Divide and Conquer paradigm.

## Problem Description

The **Closest Pair of Points** problem is a classic problem in computational geometry. Given a set of $N$ points in a 2D plane, the goal is to find the two points that are closest to each other (i.e., have the minimum Euclidean distance between them).

**Example:**

Given points: `[(1,1), (2,2), (1,2), (4,5)]`
The closest pair would be `(1,1)` and `(1,2)` with a distance of $1$.

A naive approach would involve calculating the distance between every possible pair of points, resulting in an $O(N^2)$ time complexity. For a large number of points (e.g., millions), this approach becomes computationally prohibitive. This algorithm provides a more efficient solution.

## Solution Approach: Divide and Conquer

The algorithm leverages the **Divide and Conquer** paradigm to achieve a more optimal time complexity. It works as follows:

1.  **Divide:** The set of $N$ points is split into two halves, typically by a vertical line.
2.  **Conquer:** The closest pair is recursively found in each of the two halves.
3.  **Combine:** This is the most critical step. After finding the minimum distances in the left ($d_L$) and right ($d_R$) halves, the overall minimum distance `d = min(d_L, d_R)` is considered. However, the closest pair might involve one point from the left half and one from the right half. To account for this, the algorithm focuses on a "strip" of points around the dividing line, with a width of `2d`. Only points within this strip can potentially form a pair closer than `d`. These points are then processed efficiently.

### High-Level Pseudocode

```
function CLOSEST_PAIR(Points):
    Sort Points by X-coordinate (Px)
    Sort Points by Y-coordinate (Py)
    return FIND_CLOSEST_PAIR_RECURSIVE(Px, Py)

function FIND_CLOSEST_PAIR_RECURSIVE(Px, Py):
    n = number of points in Px

    // Base Case: Brute-force for small number of points
    if n <= 3:
        return BRUTE_FORCE_CLOSEST_PAIR(Px)

    // Divide: Split points into left and right halves
    mid = n / 2
    Lx, Rx = Px[0...mid-1], Px[mid...n-1]
    Ly, Ry = points from Py that are in Lx, points from Py that are in Rx

    // Conquer: Recursively find closest pairs in halves
    (p1_L, q1_L) = FIND_CLOSEST_PAIR_RECURSIVE(Lx, Ly)
    (p1_R, q1_R) = FIND_CLOSEST_PAIR_RECURSIVE(Rx, Ry)

    // Determine the minimum distance found so far
    d_L = DISTANCE(p1_L, q1_L) if p1_L and q1_L exist else infinity
    d_R = DISTANCE(p1_R, q1_R) if p1_R and q1_R exist else infinity
    min_d = min(d_L, d_R)
    best_pair = (p1_L, q1_L) if d_L <= d_R else (p1_R, q1_R)

    // Combine: Look for closest pair across the dividing line
    // Create a strip of points within 'min_d' distance of the dividing line (median X)
    strip_Y = []
    for each point p in Py:
        if median_X - min_d <= p.x <= median_X + min_d:
            Add p to strip_Y

    // Check pairs within the strip
    (p_split, q_split) = CLOSEST_PAIR_IN_STRIP(strip_Y, min_d)

    // Return the overall closest pair
    if p_split and q_split and DISTANCE(p_split, q_split) < min_d:
        return (p_split, q_split)
    else:
        return best_pair

function CLOSEST_PAIR_IN_STRIP(strip_Y, current_min_d):
    best_d = current_min_d
    best_pair = None

    for i from 0 to length(strip_Y) - 1:
        // Critical Optimization: Only check up to 7 subsequent points
        for j from i + 1 to min(i + 7, length(strip_Y) - 1):
            p, q = strip_Y[i], strip_Y[j]
            d_pq = DISTANCE(p, q)
            if d_pq < best_d:
                best_d = d_pq
                best_pair = (p, q)
    return best_pair
```

## Analysis of the Solution

### 1. Time Complexity

The time complexity of the Closest Pair of Points algorithm is $\mathbf{O(N \log N)}$. Let's break down why:

* **Initial Sorting:**
    * Sorting all points by their X-coordinates (`Px`) takes $O(N \log N)$ time.
    * Sorting all points by their Y-coordinates (`Py`) takes $O(N \log N)$ time.
    * This initial step dominates the initial setup cost.

* **Recursive Step `FIND_CLOSEST_PAIR_RECURSIVE(Px, Py)`:**
    * **Divide:** Splitting `Px` into `Lx` and `Rx` is $O(N)$. Constructing `Ly` and `Ry` from `Py` (by iterating through `Py` and checking point IDs) is also $O(N)$.
    * **Conquer:** This involves two recursive calls on halves of the input: $2 \cdot T(N/2)$.
    * **Combine (`CLOSEST_PAIR_IN_STRIP`):**
        * Building `strip_Y` involves iterating through `Py` (which is $O(N)$).
        * The nested loop inside `CLOSEST_PAIR_IN_STRIP` looks like $O(N^2)$, but it's not! This is the key optimization. Due to a geometric property, if two points within the strip are closer than `current_min_d`, their Y-coordinates cannot be too far apart. Specifically, for each point `p` in `strip_Y`, we only need to check a constant number (at most 7 or 8) of subsequent points. This makes the `CLOSEST_PAIR_IN_STRIP` function effectively $O(N)$.

* **Recurrence Relation:**
    Combining these parts, the recurrence relation for the time complexity $T(N)$ is:
    $$T(N) = 2 \cdot T(N/2) + O(N)$$
    According to the Master Theorem, this recurrence solves to $\mathbf{T(N) = O(N \log N)}$.

* **Overall:** Since the initial sorting also takes $O(N \log N)$, the total time complexity remains $\mathbf{O(N \log N)}$.

### 2. Space Complexity

The space complexity of the algorithm is $\mathbf{O(N)}$.

* **Sorted Arrays:** Storing `Px` and `Py` requires $O(N)$ space.
* **Recursive Call Stack:** The depth of the recursion is $O(\log N)$. At each level, new lists (like `Lx`, `Rx`, `Ly`, `Ry`, and `strip_Y`) are created. While new lists are generated for each recursive call, the total size of these lists at any given recursion level is bounded by $O(N)$. As these temporary lists are typically discarded upon returning from a recursive call, the peak memory usage remains $O(N)$.

### 3. Advantages

* **Efficiency:** Significantly faster than the brute-force $O(N^2)$ approach for large datasets.
* **Scalability:** The $N \log N$ complexity makes it practical for millions of points.

### 4. Disadvantages/Considerations

* **Implementation Complexity:** More complex to implement correctly compared to the brute-force method, especially handling the `strip` phase.
* **Constant Factors:** While asymptotically superior, for very small `N`, the overhead of recursion and sorting might make the brute-force method faster due to smaller constant factors. The base case `n <= 3` wisely addresses this.

---
