# Solution for problem 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx in range(len(nums)):
            target_num = target-nums[idx]
            if target_num in num_map:
                return [num_map[target_num], idx]
            num_map[nums[idx]] = idx
