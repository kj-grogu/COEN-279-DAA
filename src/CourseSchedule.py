from ast import List
from typing import List

class CourseSchedule:
#  207. Course Schedule
#  https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #step1: map each course to its prereqs
        preMap = {i:[] for i in range(numCourses)} # a map of length of numCourses is creates and initialzed with empty array
        for crs, pre in prerequisites:
            preMap[crs].append(pre) #as prerequisites is of format [0,1] where 1st element is course and 2nd element is prereq, here we append prereq course in the list of prereq courses for that particular course in preMap for every particular entry in prerequisites.
           
        #step2: visit each course along the current course DFS path
        #visitSet = all the courses along the current DFS path
        visitSet = set()
        def dfs(crs): #recursive function to visit all nodes depth first in a path
            if crs in visitSet:
                return False #in current dfs path if crs is present in visitSet then a cycle has been detected and return false
            if preMap[crs] == []: 
                return True #return true if the current crs dfs path has no prerequisite courses
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False #return false if dfs call to one of the prereq courses in the crrent dfs path return false
            
            visitSet.remove(crs) #remove the current course from visitSet as we will be moving to next course which might not have a path from current course but current course might have a path from it, if we leave it in the set this will trigger false alarm for a cycle encounter
            preMap[crs] = [] #This is save execution time, if we have already established that a course can be completed then the whole dfs process needs not to be done for it again.
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
    
# Testing
instance = CourseSchedule()
numCourses = 2
prerequisites = [[1,0],[0,1]]

print("Can finish all courses: ", instance.canFinish(2,prerequisites))




