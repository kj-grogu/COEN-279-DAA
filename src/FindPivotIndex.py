# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index: 
# where the sum of all the numbers strictly to the left of the index 
# is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
# This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.
 

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

# Constraints:
# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

from ast import List
from typing import List

class FindPivotIndex:
    def pivotIndex(self, nums: List[int]) -> int:
        # step 1: creat two sum vars left_sum and right_sum
        left_sum = right_sum = 0
        
        # step 2: calc cumulative sum of nums as right_sum
        for num in nums:
            right_sum += num

        # step 3: for every num at index i: 
        # 3.1. compare the left sum till i - 1 and right sum till i + 1 from right
        # 3.2. expression to calc right sum = (cumulative sum - (left_sum + num at i))
        # 3.3. if 3.1. comparision is equal then return i else keep adding num to left_sum

        for i, num in enumerate(nums):
            if left_sum == (right_sum - (left_sum + num)):
                return i
            left_sum += num

        # step 4: return -1 if not returned index i so far
        return -1

# Complexity:
# T: O(N)
# S: O(1)

# Testing:
instance = FindPivotIndex()
nums = [1,7,3,6,5,6]
print("Given numbers are:", nums)
print("The Pivot index is:", instance.pivotIndex(nums))
# Output: 3



        

        


       