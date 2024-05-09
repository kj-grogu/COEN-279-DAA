# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
# If it is impossible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]
 
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

from ast import List
from typing import List
# class CourseSchedule2:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         # build the adjacency list of prereqs
#         prereq = {i:[] for i in range(numCourses)}
#         for crs, pre in prerequisites:
#             prereq[crs].append(pre)
        
#         # a course has 3 stages:
#         # visited -> course has been added to the output and removed from cycle
#         # visiting -> course not added to the output but added to the cycle
#         # unvisited -> crs not added to the output or cycle

#         output = []
#         visit, cycle = set(), set()
#         def dfs(crs):
#             if crs in cycle:
#                 return False
#             if crs in visit:
#                 return True

#             cycle.add(crs)
#             for pre in prereq[crs]:
#                 if dfs(pre) == False: 
#                     return False
#             cycle.remove(crs)
#             visit.add(crs)
#             output.append(crs)
#             return True

#         for crs in range(numCourses):
#             if dfs(crs) == False: 
#                 return []
#         return output

# OR:

class CourseSchedule2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # If there are no prerequisites, return all courses in the simplest order
        if not prerequisites:
            return [num for num in range(numCourses)]

        # Create a graph where each course points to its prerequisites
        self.graph = {num: [] for num in range(numCourses)}
        for course, pre_req in prerequisites:
            self.graph[course].append(pre_req)

        # Sets to manage DFS states: unvisited (white), visiting (grey), and visited (black)
        white = set(self.graph.keys())  # initially all nodes are unvisited
        grey = set()
        black = set()

        self.order = []  # This will store the courses in the correct order

        # Process each course that has not been visited yet
        while white:
            course = white.pop()

            # Skip if already processed
            if course in black:
                continue

            # Perform DFS, if cycle is found, return empty list
            if not self.dfs(course, grey, black):
                return []

        # If all courses are processed without finding a cycle, return the order
        return self.order
    
    def dfs(self, course, grey, black):
        # Mark the current node as visiting (grey)
        grey.add(course)

        # Check all prerequisites of the current course
        for pre_req in self.graph[course]:
            if pre_req in black:
                continue  # Skip if already fully processed
            if pre_req in grey:
                return False  # Cycle detected
            if not self.dfs(pre_req, grey, black):
                return False
        
        # All prerequisites processed, add course to order
        self.order.append(course)
        # Mark course as visited (move from grey to black)
        grey.remove(course)
        black.add(course)

        return True

# Complexity:
# Time (T): O(V + E) - where V is the number of vertices (courses) and E is the number of edges (prerequisites).
# The algorithm must visit each node and explore each edge in the worst case.
# Space (S): O(V + E) - space for the graph, the recursion stack in worst case scenario, and administrative data.


# Testing
instance = CourseSchedule2()
numCourses = 2
prerequisites = [[1,0],[0,1]]

print("order in which can finish all courses: ", instance.findOrder(2,prerequisites))