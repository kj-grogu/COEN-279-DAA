# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order. 

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

from ast import List
import time
def twoSum(A, target):
	"""Find Sum of two elements from the Array A that equal to the provided target value.
	Argument:
	A -- a list or numpy array
	target -- Target value  
	"""
	my_dictionary = {} # keeps track of index of all nums that have occured so far as we iterate of nums

	retArr = np.array(range(2))
	for i in range(1, len(A)):
		key = target - A[i]
		if key in my_dictionary.keys():
			retArr[0] = key
			retArr[1] = A[i]
		else:
			my_dictionary[A[i]] = i
	return retArr
 
# From my leetcode:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevInd = {}  # keeps track of index of all nums that have occured so far as we iterate of nums

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevInd:
#                 return [prevInd[diff], i]
#             prevInd[n] = i

#         return
		


# Complexity:
# T: O(N)
# S: O(1)

# Testing
if __name__ == "__main__":
	import numpy as np
	# Repeating terms. 
	A = np.array([11, 1, 51, 1, 5, 3])
	target = 6 
	retArr = np.array(range(2))
	retArr = twoSum(A, target)	
	print(retArr)

