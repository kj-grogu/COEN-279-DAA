# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1
 
# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

from ast import List
from typing import List
from typing import Optional

class SearchRotatedSortedArr:
    def search(self, nums: List[int], target: int) -> int:
       l = 0
       r = len(nums) - 1
       
       while l <= r:
        mid = l + (r - l) // 2
        
        # Step 1: if target is equal to num at mid
        if nums[mid] == target:
            return mid
        
        # Step 2: if nums array to right of mid is sorted
        elif nums[mid] < nums[r]:
            # Step 2.1 : if target is in sorted right portion of nums from mid
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            # Step 2.2 : if target is in un-sorted left portion of nums from mid   
            else:
                r = mid - 1
        
		# Step 3: if nums array to left of mid is sorted
        else:
            # Step 3.1 : if target is in sorted left portion of nums from mid
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            # Step 3.2 : if target is in un-sorted right portion of nums from mid
            else:
                l = mid + 1
        
        # step 4: if target not found in nums array return -1
       return -1

# Complexity:
# T: O(Lg N)
# S: O(1)

# Testing:
instance = SearchRotatedSortedArr()
nums = [4,5,6,7,0,1,2]
target = 0
print("Give list of nums to search in:", nums)
print("Target num to search is:", target)
print("Index at which target element is found is:", instance.search(nums, target))
# Output: 4