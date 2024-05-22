# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 
# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

from typing import List


class FindMinRotatedSrtdArr:
    def findMin(self, nums: List[int]) -> int:
        # Edge case: if the array has only one element or the array is not rotated (first element <= last element),
        # the first element is the minimum.
        if len(nums) == 1 or nums[0] <= nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2  # Calculate mid to avoid overflow.

            # If the mid element is less than its previous element, mid is the minimum.
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            # If the mid element is less than the rightmost element, the minimum is in the left half.
            elif nums[mid] < nums[r]:
                r = mid - 1
            # Otherwise, the minimum is in the right half.
            else:
                l = mid + 1

# Complexity:
# T: O(log n), where n is the number of elements in the array.
# S: O(1)

# Testing:
instance = FindMinRotatedSrtdArr()
nums = [4,5,6,7,0,1,2]
print("Given List of nums is:", nums)
print("Minimum element in the given list of numbers is:", instance.findMin(nums))
# Output: 0