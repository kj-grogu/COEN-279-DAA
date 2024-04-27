# 1570. Dot Product of Two Sparse Vectors
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently 
# and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

# Example 1:
# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

# Example 2:
# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

# Example 3:
# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6
 
# Constraints:
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100

from ast import List
import collections
from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []

        for i, num in enumerate(nums):
            if num:
                self.nums.append((i, num))
                # Processing Non-Zero Elements:
                    # for i, num in enumerate(nums): 
                    # Iterates over each element of the input list nums along with its index. 
                    # The enumerate function is used to get both the index (i) and the value (num) in each iteration.
                    # if num:: Checks if the current element num is non-zero.
                    # self.nums.append((i, num)): 
                    # If num is non-zero, appends a tuple (i, num) to the nums list. 
                    # This tuple contains the index i and the non-zero value num.
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        
        i = j = 0

        while i < len(self.nums) and j < len(vec.nums):
            i_index, i_val = self.nums[i]
            j_index, j_val = vec.nums[j]

            if i_index == j_index:
                dot_product += (i_val * j_val)

                i += 1
                j += 1

            elif i_index < j_index:
                i += 1

            else:
                j += 1

        return dot_product



# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)