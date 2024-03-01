# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
 

# Constraints:
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?

from collections import Counter, defaultdict, deque
import heapq
from ast import List
from typing import List
from typing import Optional

class FindDuplicateNumber:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        # Treating the given array as linked list where:
        # 1. The index are the nodes and the values at those indexes are the nodes that index node points to
        # 2. 0th index node is not part of cycle always, as integers for range start from 1 and go till n - 1 (n the length of nums)
        # 3. The logic below is flowd's algorithm:
                # 3.1. run two pointers from Oth index node (slow -> moves by 1 node, fast -> moves by 2 node)
                # 3.2. the node at which two pointers meet, break from loop
                # 3.3. start another pointer slow2 from 0, moving with slow pointer by 1 node
                # 3.4. the node at which slow2 and slow meet is the node where the cycle starts and the duplicate no.
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        temp = 0
        while True:
            slow = nums[slow]
            temp = nums[temp]
            if slow == temp:
                return slow

    # Complexity:
    # T:O(N)
    # S:O(1)

# Testing:
instance = FindDuplicateNumber()
nums = [3,1,3,4,2]
print("The duplicate number in the list nums -> ", nums, " is: ",instance.findDuplicate(nums))
        
        