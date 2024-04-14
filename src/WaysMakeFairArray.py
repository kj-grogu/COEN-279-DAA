# 1664. Ways to Make a Fair Array
# https://leetcode.com/problems/ways-to-make-a-fair-array/

# You are given an integer array nums. You can choose exactly one index 
# (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

# For example, if nums = [6,1,7,4,1]:

# Choosing to remove index 1 results in nums = [6,7,4,1].
# Choosing to remove index 2 results in nums = [6,1,4,1].
# Choosing to remove index 4 results in nums = [6,1,7,4].
# An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

# Return the number of indices that you could choose such that after the removal, nums is fair.

# Example 1:
# Input: nums = [2,1,6,4]
# Output: 1
# Explanation:
# Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
# Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
# Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
# Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
# There is 1 index that you can remove to make nums fair.

# Example 2:
# Input: nums = [1,1,1]
# Output: 3
# Explanation: You can remove any index and the remaining array is fair.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0
# Explanation: You cannot make a fair array after removing any index.
 
# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class WaysMakeFairArray:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)
        # base case:
        if N <= 1:
            return 1

        odd_left = [0] * N
        even_left = [0] * N
        odd_right = [0] * N
        even_right = [0] * N
        odd_sum_l = even_sum_l = odd_sum_r = even_sum_r = 0
        res = 0

        # Calc odd_left and even_right sums:
        for i in range(N):
            if i % 2:
                odd_sum_l += nums[i]
            else:
                even_sum_l += nums[i]
            
            odd_left[i] = odd_sum_l
            even_left[i] = even_sum_l

        # Calc odd_right and even_right sums
        for i in range(N - 1, -1, -1):
            if i % 2:
                odd_sum_r += nums[i]
            else:
                even_sum_r += nums[i]
            
            odd_right[i] = odd_sum_r
            even_right[i] = even_sum_r


        # Calc res counts in index i [0 to (N-1)] element from nums is removed
        for i in range(N):
            # if 1st index element is removed - no left sum present so not included
            if i == 0:
                if odd_right[i + 1] == even_right[i + 1]:
                    res += 1
            # if last element is removed - no right sum present so not included
            elif i == N - 1:
                if odd_left[i - 1] == even_left[i - 1]:
                    res += 1
            # in case of elements at indices 1 to N - 2, left sum remains unchanged but right sums get inter changed
            else:
                if odd_left[i - 1] + even_right[i + 1] == even_left[i - 1] + odd_right[i + 1]:
                    res += 1

        return res    

# Complexity:
# T: O(N)
# S: O(N)

# Testing:
instance = WaysMakeFairArray()
nums = [2,1,6,4]
print("Given array is:", nums)
print("number ways we can make the given array fair is:", instance.waysToMakeFair(nums))
# Output: 1

                
        