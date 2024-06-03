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
        self.rows, self.cols = len(grid1), len(grid1[0])
        self.visited = set()
        self.directions = [(0,1), (1, 0), (-1, 0), (0, -1)]

        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid2[r][c] and (r,c) not in self.visited and self.dfs(r, c, grid1, grid2, True):
                    count += 1
        return count

    def dfs(self, r, c, grid1, grid2, res):
        if (r < 0 or r == self.rows or c < 0 or c == self.cols or grid2[r][c] == 0 or (r, c) in self.visited):
            return True

        self.visited.add((r, c))
        if grid1[r][c]:
            res = True
        else:
            res = False

        for d_r, d_c in self.directions:
            n_r = r + d_r
            n_c = c + d_c
            res = res and self.dfs(n_r, n_c, grid1, grid2, res)
        return res


# Complexity:
# T:
# S:

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