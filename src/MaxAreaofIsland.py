# https://leetcode.com/problems/max-area-of-island/

# 695. Max Area of Island

# You are given an m x n binary matrix grid.
# An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

from ast import List
from typing import List


class MaxAreaofIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0  # Initialize maximum area to 0
        self.area = 0  # This will hold the area of the current island
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Possible directions to move in the grid (right, down, up, left)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:  # If the cell contains land
                    self.area = 0  # Reset area for new island
                    self.dfs(grid, r, c)  # Perform DFS to explore this island
                    maxArea = max(maxArea, self.area)  # Update maximum area if current island is larger

        return maxArea  # Return the maximum area found

    def dfs(self, grid, r, c):
        if grid[r][c] == 1:  # Check if the current cell is part of an island (not visited)
            self.area += 1  # Increment the area of the current island
            grid[r][c] = 0  # Mark the cell as visited by setting it to 0
            for dr, dc in self.directions:  # Explore all four directions
                r_n, c_n = r + dr, c + dc  # Calculate new cell coordinates
                if (0 <= r_n < len(grid)) and (0 <= c_n < len(grid[0])) and grid[r_n][c_n] == 1:
                    self.dfs(grid, r_n, c_n)  # Recursive DFS call if the new cell is valid and part of the island

# Complexity:
# T: O(R * C), where R is the number of rows and C is the number of columns in the grid.
# This is because each cell is visited at most once during the depth-first search.
# S: O(R * C) in the worst case due to the recursion stack, particularly in case of a filled grid.


# Testing
instance = MaxAreaofIsland()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print("grid: ")

for i in grid:
    print('\t'.join(map(str, i)))

print("maximum area of an island in the above grid is: ",
      instance.maxAreaOfIsland(grid))
