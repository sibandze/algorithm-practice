'''
Leetcode 3201 Find the Maximum Length of Valid Subsequence I
You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.


'''
class Solution:
    def maximumLength(self, nums):
        n = len(nums)
        odd_even = [False, 0]
        even_odd = [True, 0]
        odd = even = 0
        for i in range(n):
            if nums[i]%2 == 0:
                even += 1
                if odd_even[0]:
                    odd_even[0] = False
                    odd_even[1] += 1
                if even_odd[0]:
                    even_odd[0] = False
                    even_odd[1] += 1
            else:
                odd+=1
                if not odd_even[0]:
                    odd_even[0] = True
                    odd_even[1]+=1
                if not even_odd[0]:
                    even_odd[0] = True
                    even_odd[1] += 1
        return max(odd,even,odd_even[1],even_odd[1])
