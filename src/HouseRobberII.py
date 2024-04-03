# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [1,2,3]
# Output: 3
 
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class HouseRobberII:
        # Logic:
        # 1. If the houses are circullarly adjacent then if we rob house at 0 index we can't rob house at last index.
        # 2. so we the run house robber I algorithm twice:
            # 2.1. one for houses from index 0 to n - 2
            # 2.2. 2nd for houses from index 1 to n - 1
        # 3. Then return the max of 2.1. and 2.2.

    def rob(self, nums: List[int]) -> int:
        # base case: If the list has only one element -> then return that
        if len(nums) == 1:
            return nums[0]
        # main logic:
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        prev = prev_prev = 0
        
        for num in nums:
            best = max(num + prev_prev, prev)
            prev, prev_prev = best, prev

        return max(prev, prev_prev)

# Complexity:
# T: O(N)
# S: O(1)
    
# Testing:
instance = HouseRobberII()
nums = [1,2,3,1]
print("Money at all houses: ",nums)
print("Max loot is:", instance.rob(nums))
# Output: 4
