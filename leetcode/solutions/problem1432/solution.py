# Solution for problem 1432

'''
Problem Statement:
You are given an integer num. You will apply the following steps to num two separate times:
 - Pick a digit x (0 <= x <= 9).
 - Pick another digit y (0 <= y <= 9). Note y can be equal to x.
 - Replace all the occurrences of x in the decimal representation of num by y.
Let a and b be the two results from applying the operation to num independently.
Return the max difference between a and b.
Note that neither a nor b may have any leading zeros, and must not be 0.

Constraints:
- 1 <= num <= 10**8
'''

class Solution:
    def maxDiff(self, num: int) -> int:
        n = 0
        temp_num = num
        while temp_num>0:
            n+=1
            temp_num=temp_num//10

        digits = [0]*n
        temp_num = num
        for i in range(n-1, -1, -1):
            digits[i] = temp_num%10
            temp_num = temp_num//10

        digit_to_replace_min = None if digits[0] == 1 else digits[0]
        digit_to_replace_max = None if digits[0] == 9 else digits[0]
        
        power, replacement_min = 10**(n-1), 0 if digit_to_replace_min == None else 1
        
        min_num = 1*power
        max_num = 9*power
        power//=10
        
        for i in range(1,n):
            d = digits[i]
            if digit_to_replace_min == None and d != 0 and d!=1:
                digit_to_replace_min = d
            min_num += (d if d!=digit_to_replace_min else replacement_min) * power

            if digit_to_replace_max == None and d != 9:
                digit_to_replace_max = d
            max_num += (d if d != digit_to_replace_max else 9) * power
            power//=10
        return max_num-min_num

