# 713. Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/

# Given an array of integers nums and an integer k, 
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# Example 2:
# Input: nums = [1,2,3], k = 0
# Output: 0
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

from ast import List
import collections
from typing import List

# Formula to get no. of. products that can be formed for a sub arrays:
# r - l + 1 => here r is right index, l is left index of subArray sliding window

class SubArrProdLessThanK:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  # If k <= 1, no subarray can satisfy the condition
            return 0
        
        res = 0
        left = 0
        prod = 1

        for right, num in enumerate(nums):
            prod *= num

            # Shrink the window from the left until the product is less than k
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
                
            res += right - left + 1
        
        return res

# Complexity:
# T: O(N)
# S: O(1)

# Testing:
instance = SubArrProdLessThanK()
nums = [10,5,2,6]
k = 100
print("Given nums array is:", nums)
print("The no. of contiguous subarrs where the product of all the elements is strictly less than", k, "are: ", 
      instance.numSubarrayProductLessThanK(nums, k))
# Output: 8



        