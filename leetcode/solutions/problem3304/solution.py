'''
Leetcode 3304: Find the K-th Character in String Game I
Alice and Bob are playing a game. Initially, Alice has a string word = "a".
You are given a positive integer k.
Now Bob will ask Alice to perform the following operation forever:
- Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.

'''
class Solution:
    def kthCharacter(self, k: int) -> str:
        length = 1
        while length < k:
            length *= 2
        shift = 0
        while length > 1:
            if k > length // 2:
                shift += 1
                k -= length // 2
            length //= 2
        return chr(ord('a') + (k - 1 + shift) % 26)
