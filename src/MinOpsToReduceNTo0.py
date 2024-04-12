# 2571. Minimum Operations to Reduce an Integer to 0
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/
# You are given a positive integer n, you can do the following operation any number of times:
# Add or subtract a power of 2 
# from n.
# Return the minimum number of operations to make n equal to 0.
# A number x is power of 2 if x == 2i where i >= 0.

#  Example 1:
# Input: n = 39
# Output: 3
# Explanation: We can do the following operations:
# - Add 20 = 1 to n, so now n = 40.
# - Subtract 23 = 8 from n, so now n = 32.
# - Subtract 25 = 32 from n, so now n = 0.
# It can be shown that 3 is the minimum number of operations we need to make n equal to 0.

# Example 2:
# Input: n = 54
# Output: 3
# Explanation: We can do the following operations:
# - Add 21 = 2 to n, so now n = 56.
# - Add 23 = 8 to n, so now n = 64.
# - Subtract 26 = 64 from n, so now n = 0.
# So the minimum number of operations is 3.
 
# Constraints:
# 1 <= n <= 105

from ast import List
import collections
import heapq
from typing import List
from typing import Optional
import math

class MinOpsToReduceNTo0:
    def minOperations(self, n: int) -> int:
        # Base condition:
        if n == pow(2, int(math.log2(n))):
            return 1
        
        # finding the immediate previous and next powers of 2 for current value of n
        lowP = pow(2, int(math.log2(n)))
        highP = pow(2, int(math.log2(n)) + 1)

        # calculating the remainder value from lowP and highP based on n
        remLow = n - lowP
        remHigh = highP - n

        # Doing the recurssive call to get the minimum no of perations based on remLow and remHigh 
        # Adding 1 for current cycle of reccursive call treating it as 1 operation
        return 1 + min(self.minOperations(remLow), self.minOperations(remHigh))
    
    # Complexity:
    # T: O(log N)
    # S: O(log N)
    
# Testing:
instance = MinOpsToReduceNTo0()  
n = 39
print("minimum operations to make",n, "zero are:", instance.minOperations(n))
# Output: 3
