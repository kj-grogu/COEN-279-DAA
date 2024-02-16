
from collections import Counter
import heapq
from typing import Optional
from ast import List
from typing import List

# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# 1481. Least Number of Unique Integers after K Removals

# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Example 1:
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.

# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
class UniqueIntsAfterKRemovals:
     def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        heap = []

        for cnt in count.values():
            heapq.heappush(heap, cnt)

        while k > 0:
            num_c = heapq.heappop(heap)
            if k < num_c:
                heapq.heappush(heap, num_c - k)
                break
            k -= num_c
        return len(heap)

    # Complexity:
    # Time: O(N + M log M) where M is the number of unique counts in the Counter object.
    # Space: O(N + M log M)
     
# Testing
instance = UniqueIntsAfterKRemovals()
arr1 = [5,5,4]
k1 = 1
arr2 = [4,3,1,1,3,3,2]
k2 = 3
print("Unique Integers in ", arr1, " After", k1, " Removals: ", instance.findLeastNumOfUniqueInts(arr1, k1))
print("Unique Integers in ", arr2, " After", k2, " Removals: ", instance.findLeastNumOfUniqueInts(arr2, k2))