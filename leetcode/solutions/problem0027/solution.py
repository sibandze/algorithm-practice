class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        n=len(nums)
        while i + count < n:
            if nums[i] == val:
                count+=1
                nums[i]=nums[-count]
            else:
                i+=1
        return n-counts
