# 1905. Count Sub Islands
# https://leetcode.com/problems/count-sub-islands/

# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). 
# An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
# Return the number of islands in grid2 that are considered sub-islands.

# Example 1:
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

# Example 2:
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2 
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

# Constraints:
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.

from typing import List

class CountSubIslands:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        self.rows, self.cols = len(grid1), len(grid1[0])
        # Set to track visited cells
        self.visited = set()
        # Define possible directions for movement (right, down, up, left)
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        count = 0
        # Iterate over each cell in grid2
        for r in range(self.rows):
            for c in range(self.cols):
                # If the cell is part of an island in grid2 and not yet visited
                if grid2[r][c] and (r, c) not in self.visited:
                    # Perform DFS to check if it's a sub-island and increment count if true
                    if self.dfs(r, c, grid1, grid2):
                        count += 1
        return count

    def dfs(self, r, c, grid1, grid2):
        # Base case: if out of bounds, water cell in grid2, or already visited
        if (r < 0 or r == self.rows or c < 0 or c == self.cols or grid2[r][c] == 0 or (r, c) in self.visited):
            return True

        # Mark the cell as visited
        self.visited.add((r, c))
      
        # Assume the current cell is part of a sub-island unless proven otherwise
        res = True
        # If the corresponding cell in grid1 is water, it's not a sub-island
        if grid1[r][c] == 0:
            res = False

        # Explore all four possible directions from the current cell
        for d_r, d_c in self.directions:
            n_r = r + d_r
            n_c = c + d_c
            # Combine the result of DFS in each direction with the current result
            res = self.dfs(n_r, n_c, grid1, grid2) and res

        return res

# Complexity:
# Time Complexity (T): O(rows * cols)
# - Each cell is visited once, and in the worst case, 
# DFS explores all its neighbors leading to a time complexity proportional to the number of cells in the grid.

# Space Complexity (S): O(rows * cols)
# - The space complexity is driven by the recursion stack and the visited set. 
# In the worst case, all cells are visited, and the recursion stack can grow up to the size of the grid.

# Testing:
instance = CountSubIslands()
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print("The given 2 grids are:")
print("Grid 1:")
for r in range(len(grid1)):
    print(grid1[r])
print("Grid 2:")
for r in range(len(grid1)):
    print(grid2[r])
print("The no of sub islands in grid 2 from grid 1 are:", instance.countSubIslands(grid1, grid2))
# Output: 3