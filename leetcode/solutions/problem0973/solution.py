class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n, 2, -1):
            l1, l2, l3 = nums[i-3:i]
            if l1 + l2 > l3:
                return l1 + l2 + l3
        return 0
