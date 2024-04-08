# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths 
# that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.
 
# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# Constraints:
# 1 <= m, n <= 100
 
from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]

# Complexity:
# T: O(N * M)
# S: O(N * M)
        
# Algorithm:
# 1. Initialize Row: Start with a row representing the bottom row of the grid, initialized with 1s, as there's only one way to reach any cell in the bottom row by moving right.
# 2. Iterate Over Grid: For each row in the grid (except the last one), calculate the number of unique paths to each cell.
# 3. Calculate Paths for Cells: For each cell (starting from the second to last cell to the first in a row), sum the number of ways to reach the cell from the right and below.
# 4. Use Previous Results: The sum of paths from the right (newRow[j + 1]) and above (row[j]) gives the paths to the current cell (newRow[j]).
# 5. Update Row: After calculating paths for the current row, it becomes the previous row for the next iteration.
# 6. Return Result: The first cell of the last row processed contains the total number of unique paths to reach the bottom-right corner.

# Testing:
instance = UniquePaths()  
m = 3
n = 7
print("Number of unique paths to reach the bottom right cell of the grid with", m, "rows and", n, "cols are:", instance.uniquePaths(m,n))
# Output: 28
