# Solution for problem 2566
'''
Problem Statemet:
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.
Notes:
When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
 

Constraints:

1 <= num <= 10**8
'''
class Solution:
    def minMaxDifference(self, num: int) -> int:
        n = 0
        temp_num = num
        while temp_num > 0:
            n+=1
            temp_num=temp_num//10
        
        digits = [0]*n
        first_none_9_digit, first_none_0_digit = None, None
        temp_num = num
        for i in range(n-1, -1, -1):
            d = temp_num%10
            if d != 9:
                first_none_9_digit = d
            if d != 0:
                first_none_0_digit = d
            digits[i] = d
            temp_num//=10
        max_num, min_num, power = 0, 0, 10**(n-1)
        for i in range(n):
            d = digits[i]
            max_num+=(d if first_none_9_digit != d else 9)*power
            min_num+=(d if first_none_0_digit != d else 0)*power
            power//=10
        return max_num - min_num
