# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/

# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
# Constraints:
# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104


from ast import List
import collections
from typing import List
from typing import Optional

class NonOverlappingIntervals:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # base case:
        if len(intervals) <= 1:
            return 0

        # sort the intervals based on the start of the intervals
        intervals.sort()

        # keep track of end of the previous selected interval, and initialize to end of intervals[0]
        prevEnd = intervals[0][1]
        
        # declare var to keep count of the the ejected intervals
        countRes = 0
        
        # now iterate from 1st item over the intervals to eject minimum overlapping intervals
        for start, end in intervals[1:]:
            # if there is no overlap 
            if prevEnd <= start:
                prevEnd = end
            # if there is ovelap then we keep the interval whose end is min of prevEnd and end
            else:
                countRes += 1
                prevEnd = min(end, prevEnd)

        return countRes
        
# Complexity:
# T: O(N log N), due to sorting
# S: O(1)

# Testing:
instance = NonOverlappingIntervals()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print("given intervals: ", intervals)
print("minimum ejected intervals: ", instance.eraseOverlapIntervals(intervals))
# Output: 1
    