# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

# Constraints:
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

from ast import List
import collections
from typing import List
from typing import Optional

class InsertInterval:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
          if not intervals:
                return[newInterval]

          res = []
          for i in range(len(intervals)):
              # case 1: if newInterval comes before the current interval
              if newInterval[1] < intervals[i][0]:
                  res.append(newInterval)
                  return res + intervals[i:]
              # case 2: if newInterval comes after the current interval
              elif newInterval[0] > intervals[i][1]:
                  res.append(intervals[i])
              # case 3: if newInterval overlaps with current interval
              else:
                  newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

          res.append(newInterval)
          return res

    # Complexity:
    # T: O(N)
    # S: O(N), space taken by res list
     
# Testing:
instance = InsertInterval()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print("New set of intervals:", intervals, "after insertion of interval: ", newInterval, "is: ", instance.insert(intervals, newInterval))

# Output: [[1,2],[3,10],[12,16]]
