# 540. Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 
# Constraints:
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105


# Logic:
# 1. Boundary checks:
    # 1.1. if unique element is the 1st or last element
# 2. Pair index propery:
    # 2.1. non unique elements will be in pair
    # 2.2. if start occ of pair elements is at even index then the unique elements is to the right of them
    # 2.3. if start occ of pair elements is at odd index then the unique element is to the left of them
# 3. Unique elememt property:
    # 3.1. element to the left and right of unique element will be different
# 4. Partitioning of list:
    # 4.1. if mid is non unique and the start of this pair is at even index then move the left to mid + 1 
    # 4.2. if mid is non unique and the start of this pair is at odd index then move to the right to mid - 1

from ast import List
import collections
from typing import List

class SingleElemInSortedArr:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # step 1: Boundary checks
        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
 
        if nums[-1] != nums[-2]:
            return nums[-1]

        # step 2: Binary search:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # step 3: mid is unique check:
            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            # step 4 -> Partitioning: move right if non unique pair starts at even index:
            elif ((mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1])):
                left = mid + 1
            
            # step 5 -> Partitioning: move left if non unique pair starts at odd index:
            # elif ((mid % 2 == 1 and nums[mid] == nums[mid + 1]) or (mid % 2 == 0 and nums[mid - 1] == nums[mid])):
            else: # writing above statement just as else
                right = mid - 1

        return -1

# Complexity:
# T: O(Log N)
# S: O(1)
    
# Testing:
instance = SingleElemInSortedArr()
nums = [1,1,2,3,3,4,4,8,8]
print("Given list of nums is:", nums)
print("The unique element in the above list is:", instance.singleNonDuplicate(nums))
# Output: 2


        
