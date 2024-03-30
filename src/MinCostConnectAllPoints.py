# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
# where |val| denotes the absolute value of val.
# Return the minimum cost to make all points connected. 
# All points are connected if there is exactly one simple path between any two points.

# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
 
# Constraints:
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class MinCostConnectAllPoints:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # creating adjecency list
        adjList = {i:[] for i in range(N)} # for each node i we have list of [cost, node] for each node connected to it
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])

        # Prims Algo
        totalCost = 0
        visited = set()
        minH = [[0,0]] # [cost, point]
        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            totalCost += cost
            visited.add(i)
            for neiCost, nei in adjList[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
        return totalCost

# Complexity:
# T: O(N^2 lg N)
# S: O(N^2)
        
# Testing
instance = MinCostConnectAllPoints()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
print("given node points with their weights are: ")
for i in range(len(points)):
    print(i, " -> ", points[i])
print("minimum cost to connect all given points is: ", instance.minCostConnectPoints(points))

