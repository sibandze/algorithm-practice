# 42 Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height)-1
        max_left = max_right = 0
        while left < right:
            height_l = height[left]
            height_r = height[right]
            if height_l <= height_r:
                if height_l >= max_left:
                    max_left = height_l
                else:
                    water += max_left - height_l
                left+=1
            else:
                if height_r >= max_right:
                    max_right = height_r
                else:
                    water += max_right - height_r
                right-=1
        return water
                
