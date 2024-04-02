# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 

# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class MinCostClimbingStairs:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # as the top is at Nth position, so we append one more 0 cost element at end of cost list
        cost.append(0)

        # now we iterate over the cost list and calc the minimum of costs required to reach index N either from index 0 or 1
        # we iterate from reverse starting from 3rd index from right 
        # as we can take 1 step or 2 step at a time and if we take 2 step from N - 3 index we reach Nth element (as list is 0 indexed)
        for i in range(len(cost) - 3, -1, -1):
            # cost at ith position is cost[i] + minimum(cost[i + 1], cost[i + 2]) as we can take 1 or two steps
            cost[i] += min(cost[i + 1], cost[i + 2])
        # return themcost at indx 0 or 1, whichever has minimum cost as we can start at either
        return min(cost[0], cost[1])

    # Complexity:
    # T: O(N)
    # S: O(1)
    
# Testing:
instance = MinCostClimbingStairs()
cost = [10,15,20]
print("givens costs list is: ", cost)
print("minimum cost to reach top stair of", len(cost), "is:", instance.minCostClimbingStairs(cost))
# Output: 15
        