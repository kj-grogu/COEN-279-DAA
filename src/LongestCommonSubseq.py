# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class LongestCommonSubseq:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initialize the 2D dp of (M + 1) * (N + 1) with 0 in all cells, M = len(text1), N = len(text2)
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # compute the path len at all cells on iterating in reverse order:
        # 1. if char at i of text1 matches to char at j of text2:
        # dp[i][j] = 1 + dp[i + 1][j + 1]
        # 2. else:
        # dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # len of longest common subsequence is present at 1 cell of dp
        return dp[0][0]
        
# Complexity:
# T: O(M * N), M = len(text1), N = len(text2)
# S: O(M * N), M = len(text1), N = len(text2)

# Testing:
instance = LongestCommonSubseq()  
text1 = "abcde"
text2 = "ace" 
  
print("length of Longest Common Subsequence from string", text1, "present in string", text2, "is:", instance.longestCommonSubsequence(text1, text2))
# Output: 3
