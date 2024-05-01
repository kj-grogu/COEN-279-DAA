# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List

class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to facilitate the two-pointer approach.
        res = []  # This list will store the triplets that sum to zero.
        i = 0  # Initialize the first pointer for the outer loop.

        while i < len(nums) - 2:  # Ensure there are at least three elements to form a triplet.
            # Skip over duplicate elements to avoid redundant results.
            if 0 < i < len(nums) - 1 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1  # Initialize the second pointer, which will start just after i.
            k = len(nums) - 1  # Initialize the third pointer at the end of the array.

            while j < k:  # While there is a valid range between j and k.
                cur_sum = nums[i] + nums[j] + nums[k]  # Calculate the current sum of the triplet.

                if cur_sum == 0:  # If the sum is zero, we found a valid triplet.
                    res.append([nums[i], nums[j], nums[k]])  # Add the triplet to the result list.
                    # Move the second pointer to the right, skipping duplicates.
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Move the third pointer to the left, skipping duplicates.
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif cur_sum < 0:  # If the sum is less than zero, move j to the right to increase the sum.
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:  # Skip duplicates.
                        j += 1

                else:  # If the sum is more than zero, move k to the left to decrease the sum.
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:  # Skip duplicates.
                        k -= 1

            i += 1  # Move the first pointer to the next element and repeat the process.

        return res  # Return the list of triplets that sum to zero.

# Complexity:
# Time: O(N^2) - The outer loop runs in O(N), and the inner two-pointer technique runs in O(N) per outer iteration.
# Space: O(N) - The space needed for the output list, not counting the space for the input.

# Testing:
instance = ThreeSum()
nums = [-1,0,1,2,-1,-4]
print("Given nums array:", nums)
print("Set of triplets adding upto 0 from nums are:", instance.threeSum(nums))
# Output: [[-1,-1,2],[-1,0,1]]



        