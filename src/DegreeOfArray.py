# 697. Degree of an Array
# https://leetcode.com/problems/degree-of-an-array/
# Given a non-empty array of non-negative integers nums, 
# the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
# that has the same degree as nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 
# Constraints:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.


from ast import List
import collections
from typing import List

class DegreeOfArray:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Step 1: create a map: num to list of indexes with this num in nums array
        numToIndx = collections.defaultdict(list)
        for i, num in enumerate(nums):
            numToIndx[num].append(i)

        # Step 2: Find the degree -> num with max occurence, 
        # decided by len of its value list in numToIndx of all its occurences indexes  
        degree = max(len(inds) for inds in numToIndx.values())
        
        # Step 3: find min len of sub Arr in nums containing all occ of num with degree
        # formula = r - l + 1, r => inds[-1](last occ i of num), l => inds[0](first occ i of num)
        minLen = len(nums)
        for inds in numToIndx.values():
            if len(inds) == degree:
                minLen = min(minLen, inds[-1] - inds[0] + 1)
        
        # return min len of subArray with num having max degree
        return minLen

# Complexity:
# T: O(N)
# S: O(N)

# Testing:
instance = DegreeOfArray()
nums = [1,2,2,3,1,4,2]
print("Given Array of nums:", nums)
print("Length of sub array having all occurences of number with max dgree in nums:", instance.findShortestSubArray(nums))
# Output: 6

