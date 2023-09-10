from ast import List
from typing import List
class CourseSchedule2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the adjacency list of prereqs
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # a course has 3 stages:
        # visited -> course has been added to the output and removed from cycle
        # visiting -> course not added to the output but added to the cycle
        # unvisited -> crs not added to the output or cycle

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False: 
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False: 
                return []
        return output
    
# Testing
instance = CourseSchedule2()
numCourses = 2
prerequisites = [[1,0],[0,1]]

print("order in which can finish all courses: ", instance.findOrder(2,prerequisites))