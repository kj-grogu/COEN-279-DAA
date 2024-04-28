# 169. Majority Element
# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.


# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

from ast import List
from typing import Counter, List

class MajorityElement:
    def majorityElement(self, nums: List[int]) -> int:
        # elem_count = collections.defaultdict(int)
        # n = len(nums) - 1

        # for num in nums:
        #     elem_count[num] += 1
        #     if elem_count[num] > n // 2:
        #         return num

        # or:
        count = Counter(nums)
        max_key = max(count, key = count.get)
        return max_key

# Complexity:
# T: O(N)
# S: O(N)

# Testing:
instance = MajorityElement()
nums = [2,2,1,1,1,2,2]
print("given list of nums:", nums)
print("Majority element num is:", instance.majorityElement(nums))
# Output: 2
