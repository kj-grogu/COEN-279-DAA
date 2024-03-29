# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.

 
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1
 
# Constraints:
# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106

from ast import List
import collections
from typing import List
from typing import Optional

class MeetingRooms_II:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # first create to saparete sorted list for stars and ends of all intervals
        start = sorted([intervals[i][0] for i in range(len(intervals))])
        end = sorted([intervals[i][1] for i in range(len(intervals))])
       
        res = count = s = e = 0

        # iterate over start list:
        while s < len(intervals):
            # if value at start index is less than value at end index, increment s and count
            if start[s] < end[e]:
                s += 1
                count += 1
            # if value at start index is less than value at end index, increment s and decrement count
            else:
                e += 1
                count -= 1
            # keep res as max of res and count at any point
            res = max(res, count)

        return res

# Complexity:
# T: O(N lg N), due to sorting
# S: O(N), due to two new start and end lists
    
# Testing
instance = MeetingRooms_II()
intervals = [[0,30],[5,10],[15,20]]
print("given meeting intervals: ", intervals)
print("total no of rooms requited to host all meetings: ", instance.minMeetingRooms(intervals))
# Output: 2



    


        