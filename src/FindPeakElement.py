# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/

# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.


# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

# Constraints:
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

from typing import List

class FindPeakElement:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            to_left = nums[mid - 1] if mid > 0 else float("-inf")
            to_right = nums[mid + 1] if mid < len(nums) - 1 else float("-inf")

            # found peak
            if to_left < nums[mid] > to_right:
                return mid
            # increasing sequence => peak is to right, move to right of list from mid
            elif to_left < nums[mid] < to_right:
                l = mid + 1
            # decreasing sequence, to_left > nums[mid] > to_righr, peak is to left, move to left of list from mid
            else:
                r = mid - 1

        # even if the mid element is smaller than elements at mid - 1 and mid + 1, 
        # we can find a peak either side of the mid. so this case is not important.

        #example:
        # 342 123 451  -> in this case both 342 and 451 are a peak 
        # and as we want to find 1st peak so we move to left

# Complexity:
# T: O(lg N) due to binary search
# S: O(1)

# Testing:
instance = FindPeakElement()
nums = [1,2,1,3,5,6,4]
print("given list of numbers is:", nums)
print("The peak element in the given list is:", instance.findPeakElement(nums))
# Output: 5

        
        