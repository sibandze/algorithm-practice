# Solution for problem 3
# Leetcode 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        char_set = set()
        i, ans = 0, 0
        for j in range(n):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
        
            char_set.add(s[j])
            ans = max(ans, len(char_set))
            if ans >= len(char_set) + n - j - 1:
                break
        return ans
