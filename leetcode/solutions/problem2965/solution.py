class Solution:
    # Leetode 2965 Find Missing and Repeated Values
    # You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
    # Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_sum = n * n * (n * n + 1) // 2
        total_sum_squares = n * n * (n * n + 1) * (2 * n * n + 1) // 6
        actual_sum = sum(num for row in grid for num in row)
        actual_sum_squares = sum(num * num for row in grid for num in row)

        diff = actual_sum - total_sum
        diff_squares = actual_sum_squares - total_sum_squares

        r_plus_m = diff_squares // diff
        r = (diff + r_plus_m) // 2
        m = r_plus_m - r

        return [r, m]
