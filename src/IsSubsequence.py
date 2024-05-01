# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
# and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


class IsSubsequence:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        s_ptr = t_ptr = 0
        count = 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                count += 1
                s_ptr += 1
            
            if count == len(s):
                return True
            
            t_ptr += 1

        return s_ptr >= len(s)

# Comlexity:
# T: O(N)
# S: O(1)
        
# Testing
instance = IsSubsequence()
s = "abc"
t = "ahbgdc"
print("The two strings are s:", s, " and t:", t)
print("string", s, "is a susequence of string", t, ":", instance.isSubsequence(s, t))
# Output: true 
