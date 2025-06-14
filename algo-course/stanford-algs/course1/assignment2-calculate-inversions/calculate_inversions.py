class Solution:
  def calculate_inversions(self, nums):
    n = len(nums)
    def calculate_split_inversions(left, right):
      n_l, n_r = len(left), len(right)
      l, r, inv = 0, 0, 0
      for i in range(n):
        if l >= n_l:
          nums[i] = right[r]
          r+=1
        elif r >= n_r:
          nums[i] = left[l]
          l+=1
        elif left[l] <= right[r]:
          nums[i] = left[l]
          l+=1
        else:
          nums[i] = right[r]
          r+=1
          inv += (n_l-l)
      return inv, nums
    
    if n <= 1:
      return 0, nums
    left_inv, left = self.calculate_inversions(nums[:n//2])
    right_inv, right = self.calculate_inversions(nums[n//2:])
    split_inv, nums = calculate_split_inversions(left, right)
    return (left_inv+right_inv+split_inv), nums
