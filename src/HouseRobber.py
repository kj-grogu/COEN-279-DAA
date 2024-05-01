# 198. House Robber
# https://leetcode.com/problems/house-robber/

# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is 
# that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class HouseRobber:
    def rob(self, nums: List[int]) -> int:
 
        prev = prev_prev = best = 0  # Initialize variables to store the results of subproblems:
                                    # prev - the best result up to the previous house,
                                    # prev_prev - the best result up to the house before the previous one,
                                    # best - the best result found so far.

        for num in nums:  # Loop through each amount of money in the list.
            best = max(num + prev_prev, prev)  # Calculate the maximum money that can be robbed up to the current house:
                                               # either rob this house and the best before the previous one,
                                               # or don't rob this house and take the best of the previous.

            prev, prev_prev = best, prev  # Update the values of prev and prev_prev for the next iteration:
                                          # prev_prev becomes the previous best,
                                          # and prev becomes the current best.

        return best  # Return the maximum money that can be robbed.

# Complexity:
# Time: O(N) - The function iterates over each house in the list exactly once.
# Space: O(1) - Uses constant space to keep track of the results for previous houses.
    
# Testing:
instance = HouseRobber()
nums = [2,7,9,3,1]
print("money at all houses:", nums)
print("maximum loot is:", instance.rob(nums))
# Output: 12

        