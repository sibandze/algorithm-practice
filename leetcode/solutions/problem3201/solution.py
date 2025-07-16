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
        return max(count)
