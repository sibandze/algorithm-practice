# Solution for problem 3432
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        s = 0
        count = 0 if total_sum%2 != 0 else -1
        for num in nums:
            s += num
            count += (total_sum-2*s)%2==0
        return count
