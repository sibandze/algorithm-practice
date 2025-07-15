import re
'''
leetcode 3136 valid word
 A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.
'''
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) >= 3 and \
               re.match("^[a-zA-Z0-9]+$", word) and \
               re.search("[aeiouAEIOU]", word) and \
               re.search("[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]", word):
            return True
        return False
        
