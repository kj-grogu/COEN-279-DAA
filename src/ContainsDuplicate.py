# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from ast import List
from typing import List
from typing import Optional

class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for num in nums:
            if num in uniqueNums:
                return True
            uniqueNums.add(num)

        return False
        
        
# Complexity:
# T: O(N)
# S: O(N)
    
# Testing
instance = ContainsDuplicate()
nums = [1,1,1,3,3,4,3,2,4,2]
print("List nums -> ", nums, " contains duplicates: ", instance.containsDuplicate(nums))
