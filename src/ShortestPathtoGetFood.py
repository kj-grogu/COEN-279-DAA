# 1730. Shortest Path to Get Food
# https://leetcode.com/problems/shortest-path-to-get-food/

# You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

# You are given an m x n character matrix, grid, of these different types of cells:

# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
# You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

# Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

# Example 1:
# Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
# Output: 3
# Explanation: It takes 3 steps to reach the food.

# Example 2:
# Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
# Output: -1
# Explanation: It is not possible to reach the food.

# Example 3:
# Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
# Output: 6
# Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[row][col] is '*', 'X', 'O', or '#'.
# The grid contains exactly one '*'.

import collections
from typing import List

class ShortestPathtoGetFood:
    def getFood(self, grid: List[List[str]]) -> int:
        # Get the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])

        # Define possible directions for movement (right, left, up, down)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # Initialize the queue for BFS and a set to track visited cells
        queue = collections.deque([])
        visited = set()

        # Find the starting position denoted by '*'
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    # Add the starting position to the queue with 0 steps taken
                    queue.append((r, c, 0))
                    # Mark the starting position as visited
                    visited.add((r, c))
                    break

        # Perform BFS to find the shortest path to the food
        while queue:
            # Dequeue the current position and the number of steps taken so far
            cur_r, cur_c, steps = queue.popleft()

            # If the current cell contains food, return the number of steps
            if grid[cur_r][cur_c] == "#":
                return steps

            # Explore all four possible directions from the current cell
            for d_r, d_c in directions:
                n_r = cur_r + d_r
                n_c = cur_c + d_c

                # Check if the new position is within the grid boundaries, not an obstacle, and not visited
                if (0 <= n_r < rows) and (0 <= n_c < cols) and grid[n_r][n_c] != "X" and (n_r, n_c) not in visited:
                    # Mark the new position as visited
                    visited.add((n_r, n_c))
                    # Enqueue the new position with the incremented steps
                    queue.append((n_r, n_c, steps + 1))

        # Return -1 if no path to the food is found
        return -1

# Complexity:
# Time Complexity (T): O(rows * cols)
# - In the worst case, each cell in the grid is visited once. 
# The BFS explores each cell's neighbors, leading to a time complexity proportional to the number of cells in the grid.

# Space Complexity (S): O(rows * cols)
# - The space complexity is driven by the queue and the visited set. 
# In the worst case, all cells are added to the queue and visited set, resulting in space usage proportional to the number of cells in the grid.
    
# Testing:
instance = ShortestPathtoGetFood()
grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
print("The give grid is:")
for r in range(len(grid)):
    print(grid[r])

print("Minimum steps taken to reach food is:", instance.getFood(grid))
# Output: 6
