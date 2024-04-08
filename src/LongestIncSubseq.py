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

# Algorithm:
# 1. Initialize DP array: Each element is initialized to 1, assuming each number is an increasing sequence by itself.
# 2. Iterate over array in reverse: Start from the end to efficiently build up the solution using previously computed results.
# 3. Check for increasing sequences: For each element, compare it with elements after it to find increasing sequences.
# 4. Update DP array: If an increasing sequence is found, update the current element's DP value to the maximum length found so far plus one.
# 5. Look for the maximum value in DP: After iterating through the array, the maximum value in the DP array will be the length of the LIS.
# 6. Return the maximum LIS length: This value represents the longest increasing subsequence within the given array.