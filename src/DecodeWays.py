# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"

# To decode an encoded message, 
# all the digits must be grouped then mapped back into letters using 
# the reverse of the mapping above(there may be multiple ways). 

# For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

# Constraints:
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

# iterative solution:
class DecodeWays:
    def numDecodings(self, s: str) -> int:
        # create a dp map initialize with len(s) -> 1
        dp = {len(s) : 1}
        # iterate over the encoding s in reverse
        for i in range(len(s) - 1, -1, -1):
            # base / edge case of 0 -> s can not start with 0 or single digit encoding can not be 0
            if s[i] == "0":
                dp[i] = 0
            else:
                # case of single digit encoding apart from 0 i-e 1 - 9 mapping to (A - I) 
                dp[i] = dp[i + 1] # dependency on previous encoded char val only
            # case of double digit encoding(10 - 26): 
            # 1st digit can only be "1" or "2"
            # 2nd digit can only be from 0,1,2,3,4,5,6 
            if(i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2] # dependency on previous two encoded char vals
        
        return dp[0]

# recursive solution:
# class DecodeWays:
#     def numDecodings(self, s: str) -> int:
#         dp = {len(s) : 0}

#         def dfs(i):
#             if i in dp:
#                 return dp[i]
#             if s[i] == "0":
#                 return 0
#             res = dfs(i + 1)
#             if(i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
#                 res += dfs(i + 2)

#             dp[i] = res
#             return res
        
#         return dfs(0)

# Complexity:
# T: O(N)
# S: O(N)


# Testing:
instance = DecodeWays()
s = "226"
print("Number of ways string \"",s,"\" can be decoded are: ", instance.numDecodings(s))
# Output: 3