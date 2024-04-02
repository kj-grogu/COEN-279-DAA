# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:
# 1 <= n <= 45

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        # This is called bothom up sol cause we move from n to 0 that is:
        # Example: if n = 5, 
        # then we first calc sol for step taken to reach 5 from 5 and keep that val in var two which is 1:
        # similarly for n - 1 (5 - 1 = 4), i-e steps to reach 5 from 4 which is also 1 and keep it in var one
        # and then based on these vals for one and two we calculate steps to reach 5 from 3, then from 2 ... 0 
        # return the total no of ways of steps required to reach 5 from 0 which will be in var one

        # Logic:
        # 1. declare two variables for bottom up solution one -> keep sol for n - 1 and two -> keeps sol n
        # 2. iterate till n - 1
        # 3. and keep updating vals for vars one and two -> two = one and one = one + two
        # 4. return val of one at the end

        one = two = 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one

# Complexity:
# T: O(N)
# S: O(1)
        




        