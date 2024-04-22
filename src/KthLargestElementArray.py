# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

 

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104


from ast import List
import heapq
from typing import List
from typing import Optional

class KthLargestElementArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # naive solution:
        # nums.sort()
        # return nums[len(nums) - k]
            # Complexity:
            # T: O(NlogN), S: O(N)
        
        # using quick sort algorithm:
        # k = len(nums) - k

        # def quickSelect(l,r):
        #     pivot = nums[r]
        #     p = l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]

        #     if k < p:
        #         return quickSelect(l, p - 1)
        #     elif k > p:
        #         return quickSelect(p + 1, r)
        #     else:
        #         return nums[p]
        
        # return quickSelect(0, len(nums) - 1)
            # Complexity:
            # T: avg: O(N); worst: O(N^2)
            # S: O(1)
        
        #Heap - min heap : most popular and relevent solution:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        return heap[0]

        # Complexity:
        # T: O(N log k) -> here log k is coming from heap functions of pop and push
        # S: O(k)

# Testing:
instance = KthLargestElementArray()
nums = [3,2,1,5,6,4]
k = 2
print("Given nums array:", nums, "and K is:", k)
print("Kth largest num in the given array is:", instance.findKthLargest(nums, k))
# Output: 5
