# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

from ast import List
import collections
from typing import List

class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        # step 1: var initializations
        l = trapped = 0
        r = len(height) - 1
        l_max, r_max = 0, 0

        # step 2: run two pointers from left and right until l < r
        while l < r:
            l_cur = height[l]
            r_cur = height[r]

            # step 3: l_max and r_max are the max heights seen so far from both sides
            l_max = max(l_max, l_cur)
            r_max = max(r_max, r_cur)

            # step 4: water trapped depends on the minimum of the two l_max and r_max, 
            # with a reduction of current l or r height from the chosen min
            # Then move ahead the pointer for the min of the l_max or r_max
            if l_max < r_max:
                trapped += l_max - l_cur
                l += 1
            else:
                trapped += r_max - r_cur
                r -= 1

        return trapped

# Complexity:
# T: O(N)
# S: O(1) 
    
# Testing:
instance = TrappingRainWater()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Given heights are:", height)
print("Total rain water trapped:", instance.trap(height))
# Output: 6


        