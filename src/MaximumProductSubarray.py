# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class MaximumProductSubarray:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # not 0 because nums can have all -ve values
        curMax = curMin = 1 # To track curMin and curMax products of subarray

        for num in nums:
            # Base case in num == 0, then reset curMax and curMin
            if num == 0:
                curMin = curMax = 1
                continue
            temp = curMin
            curMin = min(num, num * curMin, num * curMax)
            curMax = max(num, num * temp, num * curMax)
            res = max(res, curMax)

        return res

# Complexity:
# T: O(N)
# S: O(1)

# Testing:
instance = MaximumProductSubarray()
nums = [2,3,-2,4]
# Output: 6
print("Given nums array is:",nums)
print("Max product of a subArray is:", instance.maxProduct(nums))

        