# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class PalindromicSubstrings:
    # Logic:
    # For Odd len palindromic subStrings:
    # 1. Take every char as pivot and expand in both directions (left, right), with left = right = i
    # 2. If chars at left and right match increment the substring count 
    # and expand further by left -= 1 and right += 1
    # 3. else move to next char as pivot

    # For Even len palindromic subStrings:
    # 1. No need for pivot char, take left and rigth pair chars, with left = i, right = i + 1
    # 2. If chars at left and right match increment the substring count 
    # and expand further by left -= 1 and right += 1
    # 3. else move to next chars pair

    def countSubstrings(self, s: str) -> int:
        self.paliStrsCount = 0

        for i in range(len(s)):
            # Odd len palindromic substrings
            left = right = i
            self.helper(s,left,right)

            # Even len palindromic substrings
            left, right = i, i + 1
            self.helper(s, left, right)
        
        return self.paliStrsCount

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.paliStrsCount += 1
            left -= 1
            right += 1

# Complexity:
# T: O(N^2)
# S: O(1)

# Testing:
instance = PalindromicSubstrings()
s = "aaa"
print("Count of all palindromic substring in the give string \"", s, "\" is:", instance.countSubstrings(s))
# Output: 6

        