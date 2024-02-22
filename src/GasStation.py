from ast import List
from typing import List
from typing import Optional

# 134. Gas Station
# https://leetcode.com/problems/gas-station/
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
# You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
# otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3

# Example 2:
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.


class GasStation:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = cur_gas = starting_st = 0

        for i in range(n):
            total_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]

            if cur_gas < 0:
                starting_st = i + 1
                cur_gas = 0

        return starting_st if total_gas >= 0 else -1

# Complexity:
# T: O(N)
# S: O(1)
    
# Testing:
instance = GasStation()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print("Starting station is: ", instance.canCompleteCircuit(gas, cost))

        