# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
# Given an integer array nums, return true if you can partition the array into two subsets 
# such that the sum of the elements in both subsets is equal or false otherwise.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class PartitionEqualSubsetSum:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        # declare the DP set
        dp = set()
        # add 0 to dp set, as 0 target is always possible if we don't choose any number from nums
        dp.add(0)
        # define target, which is half of the total sum of numbers in nums
        target = sum(nums) // 2

        # iterate over nums in reverse to fill the bottom up dp
        for i in range(len(nums) - 1, -1, -1):
            # create a copy of dp to add new targets for iteration over it for next val at i
            nextDp = dp.copy()
            for curTarget in dp:
                nextDp.add(curTarget + nums[i])

            # assign nextDp to dp
            dp = nextDp

        return True if target in dp else False


# Complexity:
# T: O(N * sum(nums) / 2), worst case, the algo explores each element in conjunction with every possible sum leading up to sum/2.
# S: O(sum(nums) / 2), since the space used by the algo is proportional to the range of possible sums, which goes up to sum/2.


# Testing:
instance = PartitionEqualSubsetSum()  
nums = [1,5,11,5]
print("Given set of numbers:", nums)
print("Given nums list contains a Partition of Equal Subset Sum: ", instance.canPartition(nums))
# Output: true

# Algorithm:
# 1. Odd Total? Impossible: If total is odd, evenly splitting is impossible.
# 2. Goal: Aim for half the total sum.
# 3. Zero Sum Start: Begin with no numbers, aiming for zero sum.
# 4. Targeting Half: Achieving half sum means other half matches.
# 5. Exploring Possibilities: Add numbers to reach new sums.
# 6. Building on Past: Use previous sums to find new ones.
# 7. Efficiency Key: Avoid starting from scratch; build on previous finds.
# 8. Tracking Progress: Keep a record of achievable sums.
# 9. Dynamic Approach: Adaptively update possible sums.
# 10. Every Number Counts: Each addition explores new potential sums.
# 11. Update and Repeat: With each number, update sum possibilities.
# 12. Target Check: See if half sum can be achieved.
# 13. Success Criteria: Target sum presence indicates possible split.
# 14. Iterative Process: Repeat adding and checking with each number.