# 2422. Merge Operations to Turn Array Into a Palindrome
# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

# Logic video:
# https://www.youtube.com/watch?v=F9n_NJB447c

# You are given an array nums consisting of positive integers.
# You can perform the following operation on the array any number of times:
# Choose any two adjacent elements and replace them with their sum.
# For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
# Return the minimum number of operations needed to turn the array into a palindrome.

# Example 1:
# Input: nums = [4,3,2,1,2,3,1]
# Output: 2
# Explanation: We can turn the array into a palindrome in 2 operations as follows:
# - Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,3,3,1].
# - Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,4].
# The array [4,3,2,3,4] is a palindrome.
# It can be shown that 2 is the minimum number of operations needed.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We do the operation 3 times in any position, we obtain the array [10] at the end which is a palindrome.
 
# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106

# Solution Approach Example:
        # Partial sum example:
        # [4,3,2,1,2,3,1]
        # forward = [4, 7, 9, 10, 12, 15, 16]
        # backward_rev = [1, 4, 6, 7, 9, 12, 16]
        # Longest Common subsequesce (forward, backward): [4, 7, 9, 12, 16]
        # Result: N - len(LCS) = 7 - 5 = 2

import itertools
from typing import List

class MergeOpsTurnArrPalindrome:
    # Function to find the minimum number of operations to make the forward partial sum equal to backward partial sum
    def minimumOperations(self, nums: List[int]) -> int:
        # Compute the forward cumulative sum of the list
        forward = list(itertools.accumulate(nums))
        # Compute the backward cumulative sum of the reversed list
        backward_rev = list(itertools.accumulate(nums[::-1]))
        
        n = len(nums)  # Length of the input list
        count_LCS = 0  # Initialize the count of the Longest Common Subsequence (LCS)
        i = j = 0  # Initialize pointers for forward and backward_rev lists
        
        # Logic to find the LCS between forward and backward_rev lists
        while i < n and j < n:
            if forward[i] == backward_rev[j]:
                # If elements match, increment LCS count and both pointers
                count_LCS += 1
                i += 1
                j += 1
            elif forward[i] < backward_rev[j]:
                # If forward element is smaller, move the forward pointer
                i += 1
            else:
                # If backward element is smaller, move the backward pointer
                j += 1
        
        # Return the number of elements to be removed to make the partial sums equal
        return n - count_LCS

# Time Complexity: O(N)
# - The algorithm traverses the nums list twice to compute the forward and backward_rev cumulative sums.
# - The while loop also runs at most 2N steps (N for each pointer), resulting in linear time complexity.

# Space Complexity: O(N)
# - The space complexity is dominated by the space needed to store the forward and backward_rev lists, each of size N
    
# Testing:
instance = MergeOpsTurnArrPalindrome()
nums = [4,3,2,1,2,3,1]
# Output: 2
print("The give list of number array is:", nums)
print("The no of merge ops to make the given array a palindropme are:", instance.minimumOperations(nums))