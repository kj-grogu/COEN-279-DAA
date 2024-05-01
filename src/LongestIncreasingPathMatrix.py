# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. 
# You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).


# Example 1:
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2:
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# Example 3:
# Input: matrix = [[1]]
# Output: 1
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1

from typing import List

class LongestIncreasingPathMatrix:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.memo = {}  # Dictionary to store the length of the longest path starting from a specific cell.
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Possible movements: right, down, up, left.

        res = 1  # Initialize the longest path found to be at least 1.

        for x in range(len(matrix)):  # Iterate through each row.
            for y in range(len(matrix[0])):  # Iterate through each column.
                res = max(res, self.dfs(matrix, x, y))  # Update the result with the longest path found from the current cell.

        return res  # Return the longest path found.

    def dfs(self, matrix, x, y):
        if (x, y) in self.memo:
            return self.memo[(x, y)]  # Return the already computed longest path length for this cell.

        # Initially, the longest path starting from this cell is just the cell itself.
        self.memo[(x, y)] = 1

        # Explore all four possible directions.
        for dx, dy in self.directions:
            cur_x, cur_y = dx + x, dy + y  # Calculate the coordinates of the next cell in the direction.

            # Check if the next cell is within bounds and the value is greater than the current cell.
            if (0 <= cur_x < len(matrix)) and (0 <= cur_y < len(matrix[0])) and matrix[x][y] < matrix[cur_x][cur_y]:
                # If valid, calculate the longest path for the next cell and update if it's better.
                self.memo[(x, y)] = max(self.memo[(x, y)], 1 + self.dfs(matrix, cur_x, cur_y))

        return self.memo[(x, y)]  # Return the length of the longest path starting from this cell.

# Complexity:
# Time: O(M * N) - Each cell is processed once due to memoization.
# Space: O(M * N) - Memoization storage could hold an entry for each cell.

# Testing:
instance = LongestIncreasingPathMatrix()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print("The given matrix is:")
for i in range(len(matrix)):
    print(matrix[i])
print("Length of longest increasing path in above matrix is:", instance.longestIncreasingPath(matrix))
# Output: 4



