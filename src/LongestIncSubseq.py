# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 
# Constraints:
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class LongestIncSubseq:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create the DP for storing the bottom up approach
        LIS = [1] * len(nums)

        # iterate through the nums array in reverse order to construct the result in bottom up manner
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                # only if increasing sequence is present
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        # return the max from increasing sequence no's at all indexes of DP (LIS)
        return max(LIS)

# Complexity:
# T: O(N^2) 
# S: O(N)

# Testing:
instance = LongestIncSubseq()  
nums = [10,9,2,5,3,7,101,18]
print("Given set of numbers:", nums)
print("length of longest increasing subsequence in given set of numbers is", instance.lengthOfLIS(nums))
# Output: 4
