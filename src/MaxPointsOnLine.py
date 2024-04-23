# 149. Max Points on a Line
# https://leetcode.com/problems/max-points-on-a-line/
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
# return the maximum number of points that lie on the same straight line.

# Example 1:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Example 2:
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
 
# Constraints:
# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.

from ast import List
import collections
from typing import List

# 1. create a map to store slope vs count mapping -> tells which points have this slope
# 2. This map will be for each the points to get the longest line. As one point can be on multiple lines
# 3. points with same x-axis val will have a slope of inf
class MaxPointsOnLine:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1 # in case there's just 1 point -> base case
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                slope = 0
                if p1[0] == p2[0]:
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                
                count[slope] += 1
                # count[slope] + 1 here adding another 1 cause we are counting for 2 points at a time
                res = max(res, count[slope] + 1)

        return res

# Complexity:
# T: O(N ^ 2)
# S: O(N ^ 2)

# Testing:
instance = MaxPointsOnLine()
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print("Given Points are:", points)
print("Maximim Points on a line are:", instance.maxPoints(points))
# Output: 4




        

        