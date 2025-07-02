# Leetcode 5 Longest Palindrome Substring
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_palindrome = [1, [0, 0]]

        def expand_around_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1  # calculate length after loop
            if length > longest_palindrome[0]:
                longest_palindrome[0] = length
                longest_palindrome[1] = [left + 1, right - 1]

        for i in range(n):
            expand_around_center(i, i)  # odd-length palindrome
            expand_around_center(i, i + 1)  # even-length palindrome

        return s[longest_palindrome[1][0]:longest_palindrome[1][1] + 1]
