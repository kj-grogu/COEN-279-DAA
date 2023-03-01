from ast import List
from typing import List

# 	338. Counting Bits
# 	https://leetcode.com/problems/counting-bits/
	
# Given an integer n, return an array ans of length n + 1 
# such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# **********************************Solution*******************************************
		# logic:
		# 1. offset = 1
		# 2. bits in:
		# 0 - 000 --> 0 --> 0
		# 1 - 001 --> 1 --> 1 + dp[1 - 1] {1 + dp[0]} ==> dp[i - offset]
		# here 2 * offset (1) == 2 : offset = 2
		# 2 - 010 --> 1 --> 1 + dp[2 - 2] {1 + dp[0]} ==> dp[i - offset]
		# 3 - 011 --> 2 --> 1 + dp[3 - 2] {1 + dp[1]} ==> dp[i - offset]
		# here 2 * offset (2) == 4 : offset = 4
		# 4 - 100 --> 1 --> 1 + dp[4 - 4] {1 + dp[0]} ==> dp[i - offset]
		# 5 - 101 --> 2 --> 1 + dp[5 - 4] {1 + dp[1]} ==> dp[i - offset]
		# 6 - 110 --> 2 --> 1 + dp[6 - 4] {1 + dp[2]} ==> dp[i - offset]
		# 7 - 111 --> 3 --> 1 + dp[7 - 4] {1 + dp[3]} ==> dp[i - offset]
		# So on....

class CountingBits:
    # Solution without dp
    # def countBits(self, n: int) -> List[int]:
    #     res = []
    #     count = 0
    #     for i in range(0, n + 1):
    #         while(i):
    #             i &= i - 1
    #             count += 1
    #         res.append(count)
    #         count = 0
    #         i+=1
    #     return res

    # Solution with dp
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range (1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

# Testing
instance = CountingBits()
output = instance.countBits(25)
print("no of 1 bits in binary of i where i is from 0 to 25 is: ")
print(output)