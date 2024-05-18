# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List


class MedianTwoSortedArrs:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        len_l1, len_l2 = len(nums1), len(nums2)

        left_l1, right_l1 = 0, len_l1

        while left_l1 <= right_l1:
            prt_l1 = left_l1 + (right_l1 - left_l1) // 2
            prt_l2 = ((len_l1 + len_l2 + 1) // 2) - prt_l1

            max_left_l1 = nums1[prt_l1 - 1] if prt_l1 > 0 else float('-inf')
            min_right_l1 = nums1[prt_l1] if prt_l1 < len_l1 else float('inf')

            max_left_l2 = nums2[prt_l2 - 1] if prt_l2 > 0 else float('-inf')
            min_right_l2 = nums2[prt_l2] if prt_l2 < len_l2 else float('inf')

            if max_left_l1 <= min_right_l2 and max_left_l2 <= min_right_l1:
                if (len_l1 + len_l2) % 2:
                    return max(max_left_l1, max_left_l2)
                else:
                    return (max(max_left_l1, max_left_l2) + min(min_right_l1, min_right_l2)) / 2
            
            elif max_left_l1 > min_right_l2:
                right_l1 = prt_l1 - 1
            else:
                left_l1 = prt_l1 + 1

# Complexity:
# T: O(lg(min(len(nums1), len(nums2))))
# S: O(1)

            



        
        
        