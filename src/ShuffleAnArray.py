# 384. Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/
# Given an integer array nums, design an algorithm to randomly shuffle the array. 
# All permutations of the array should be equally likely as a result of the shuffling.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
 
# Example 1:
# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
#                        // Any permutation of [1,2,3] must be equally likely to be returned.
#                        // Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

# Constraints:
# 1 <= nums.length <= 50
# -106 <= nums[i] <= 106
# All the elements of nums are unique.
# At most 104 calls in total will be made to reset and shuffle.

from ast import List
import collections
import random
from typing import List

class ShuffleAnArray:

    def __init__(self, nums: List[int]):
        # here doing list(nums) is important
        self.nums = list(nums) # Use a copy for self.nums
        self.reSetNums = list(nums) # And a separate copy for self.reSetNums
        

    def reset(self) -> List[int]:
        # here reseting of nums to reSetNums[:] is important can't just return self.reSetNums
        self.nums = self.reSetNums[:]  # Reset nums to a copy of reSetNums
        return self.nums
        

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            new_i = random.randint(0, i)
            self.nums[i], self.nums[new_i] = self.nums[new_i], self.nums[i]
        return self.nums

# Complexity:
# T: O(N)
# S: O(N)

# Testing:
funcs = ["Solution", "shuffle", "reset", "shuffle"]
params = [[[1, 2, 3]], [], [], []]
instance = ShuffleAnArray(params[0][0])
for i in range(len(funcs)):
    if funcs[i] == "shuffle":
        print("Shufeling current version of nums:", params[0][0])
        print("new version of nums is: ", instance.shuffle())
    if funcs[i] == "reset":
        print("reset the current version of nums:", instance.reset())
    if funcs[i] == "Solution":
        print("Given list of nums is:", params[0][0])
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()