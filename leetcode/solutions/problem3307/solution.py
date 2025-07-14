'''
Leetcode 3307: Find the K-th Character in String Game II
Alice and Bob are playing a game. Initially, Alice has a string word = "a".
You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the type of the ith operation.
Now Bob will ask Alice to perform all operations in sequence:
- If operations[i] == 0, append a copy of word to itself.
- If operations[i] == 1, generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".



'''
import math
class Solution:
    def kthCharacter(self, k: int, operations) -> str:
        op_count = math.floor(math.log2(k))
        length = 2 ** (op_count + 1)
        shift = 0
        op_index = op_count
        
        while length > 1:
            if k > length // 2:
                if operations[op_index] == 1:
                    shift += 1
                k -= length // 2
            length //= 2
            op_index -= 1
        
        return chr(ord('a') + (k - 1 + shift) % 26)
