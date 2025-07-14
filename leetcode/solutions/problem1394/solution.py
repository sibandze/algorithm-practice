'''
    Leetcode 1394. Find Luck Integer in an Array
    Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

    Return the largest lucky integer in the array. If there is no lucky integer return -1.

 
'''
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {-1:-1}
        for i in range(len(arr)):
            count[arr[i]] = count.get(arr[i],0) + 1
        return max([num for num, count in count.items() if count == num])
