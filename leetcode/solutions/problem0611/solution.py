
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort the list
        result = 0
        n = len(nums)

        for i in range(n - 1, 1, -1):  # Iterate over the longest side
            target = nums[i]
            m = 0
            k = i - 1  # Renamed n to k for clarity

            while m < k:
                if nums[m] + nums[k] <= target:
                    m += 1  # Increase the sum
                else:
                    result += k - m  # Count valid triplets
                    k -= 1  # Decrease the larger number

        return result
