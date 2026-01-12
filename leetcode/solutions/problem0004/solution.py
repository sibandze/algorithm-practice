'''
Leetcode 4 Median of Two Sorted Arrays
    
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, lst1: List[int], lst2: List[int]) -> float:
        def findMedian(lst):
            n = len(lst)
            if n%2==1:
                return lst[n//2] 
            else: 
                return (lst[n//2-1]+lst[n//2])/2.0
                
        def find_nth(nums1, nums2, n):
            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1
            total_length = len(nums1) + len(nums2)
            if n > total_length:
                raise ValueError("n is out of range")
            left, right = 0, len(nums1)
            while left < right:
                mid = (left + right) // 2
                idx1, idx2 = mid, n - mid
                
                # Handle edge cases
                if idx1 == 0:
                    val1 = float('-inf')
                else:
                    val1 = nums1[idx1 - 1]     
                if idx2 == 0:
                    val2 = float('-inf')
                else:
                    val2 = nums2[idx2 - 1]
                
                if idx1 == len(nums1):
                    val3 = float('inf')
                else:
                    val3 = nums1[idx1]
                    
                if idx2 == len(nums2):
                    val4 = float('inf')
                else:
                    val4 = nums2[idx2]
                    
                # Compare values and adjust search range
                if val1 <= val4 and val2 <= val3:
                    return max(val1, val2)
                elif val1 > val4:
                    right = mid
                else:
                    left = mid + 1
            
            # Handle edge case
            idx1, idx2 = left, n - left
            if idx1 == 0:
                return nums2[idx2 - 1]
            elif idx2 == 0:
                return nums1[idx1 - 1]
            else:
                return max(nums1[idx1 - 1], nums2[idx2 - 1])

            
        n1 = len(lst1)
        n2 = len(lst2)
        n = n1+n2
        median_pos = n//2+1
        if n1 > n2:
            n1, n2 = n2, n1
            lst1, lst2 = lst2, lst1
        if n1== 0:
            return findMedian(lst2)
        if n == 2:
            return (lst1[0]+lst2[0])/2.0
        if n%2 == 1:
            return find_nth(lst1, lst2, median_pos)
        return (find_nth(lst1, lst2, median_pos-1) + find_nth(lst1, lst2, median_pos))/2.0
