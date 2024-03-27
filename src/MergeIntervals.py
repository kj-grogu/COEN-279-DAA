
# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from ast import List
import collections
from typing import List
from typing import Optional

class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # base case:
        if len(intervals) <= 1:
            return intervals

        # sort intervals by the start of each intervals as intervals list items maybe out of order:
        intervals.sort()

        res = [intervals[0]]
        
        # logic to merge all overlapping intervals
        # iterating from 1'st item in the list as 0th item is alredy used to initialize the result list
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res

# Complexity:
# T: O(N lg N), due to sorting
# S: O(N), result list
    

# Testing:
instacnce = MergeIntervals()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print("given intervals: ", intervals)
print("intervals after merging are: ", instacnce.merge(intervals))
# Output: [[1,6],[8,10],[15,18]]



        