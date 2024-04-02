# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

#  Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        # declare a variable to keep count of islands or connected components
        island_count = 0

        # declare an initialize the directions in which to traverse to find all connected cells
        directions = [(1, 0), (-1, 0),(0, 1), (0, -1)]

        # define dfs function to find all connected cells with val "1" and reset them to "0" --> for current cell:
        def dfs(grid, r, c):
            # if current cell is "1" then reset to "0":
            if ((0 <= r < len(grid)) and (0 <= c < len(grid[0]))) and grid[r][c] == "1":
                grid[r][c] = "0"
                # explore all direction around the current cell for cells with val "1":
                for r_inc, c_inc in directions:
                        dfs(grid, r + r_inc, c + c_inc)
            
        # iterate over the grid row and col wise to go through all cells
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # increment the count of islands if cell's val is "1"
                if grid[r][c] == "1":
                    island_count += 1
                    # call the dfs to explore all connected cells to the curret cell and set them to "0"
                    dfs(grid, r, c)
        
        # return the count of islands once all the cells of the grid have been explored
        return island_count
        
# Complexity:
# T: O(R * C)
# S: O(R * C), due to recursive stack

# Testing:
instance = NumberOfIslands()

grid = [
   ["1","1","1","1","0"],
   ["1","1","0","1","0"],
   ["1","1","0","0","0"],
   ["0","0","0","0","0"]
 ]
print("given grid is:")
for r in range(len(grid)):
     print(grid[r])
print("Number of islands of cells with val \"1\" are:", instance.numIslands(grid))
# Output: 1