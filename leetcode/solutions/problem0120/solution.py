class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]

        for row in range(n - 2, -1, -1):
            for i in range(len(triangle[row])):
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])

        return dp[0]
