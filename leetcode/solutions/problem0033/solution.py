# Leetcode 33: Search In Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if target == nums[mid]:
                return mid
            if nums[i] > nums[j]:
                if nums[i] > nums[mid]:
                    if (target >= nums[i] or target < nums[mid]):
                        j = mid-1
                    else:
                        i = mid+1
                else:
                    if (target > nums[mid] or target < nums[i]):
                        i = mid+1
                    else:
                        j = mid-1
            else:
                if target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid+1
        return -1
