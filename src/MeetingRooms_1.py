# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/

# Given an array of meeting time intervals where intervals[i] = [starti, endi], 
# determine if a person could attend all meetings.

 
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true
 
# Constraints:
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106

from ast import List
import collections
from typing import List
from typing import Optional

class MeetingRooms_1:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # base case:
        if len(intervals) <= 1:
            return True

        # sort the intervals list based on the start value
        intervals.sort()

        # iterate over the intervals list to find overlapping intervals
        for i in range(1, len(intervals)):
            I_prev_end = intervals[i-1][1]
            I_curr_start = intervals[i][0]

            # check if there is an overlap and return false
            if I_prev_end > I_curr_start:
                return False
            
        return True

# Complexity:
# T: O(N lg N), due to sorting
# S: O(1)
    
# Testing
instance = MeetingRooms_1()
intervals = [[0,30],[5,10],[15,20]]
print("given meeting intervals: ", intervals)
print("can the above mentioned meetings be scheduled without overlap: ", instance.canAttendMeetings(intervals))
# Output: false
    
    