# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
# If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


import collections
from typing import List


class RottingOranges:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1  # Return -1 if the input grid is empty

        ROWS, COLS = len(grid), len(grid[0])
        fresh = time = 0  # Initialize count of fresh oranges and time elapsed
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Possible movement directions (right, down, up, left)
        queue = collections.deque([])  # Initialize a deque for BFS

        # First pass to count fresh oranges and enqueue initial positions of rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))  # Add the position of rotten oranges to the queue
                elif grid[r][c] == 1:
                    fresh += 1  # Count fresh oranges

        # BFS to rot the fresh oranges from the rotten ones
        while queue and fresh > 0:
            for _ in range(len(queue)):  # Process all oranges at the current time step
                cur_r, cur_c = queue.popleft()
                for dr, dc in directions:  # Check all four directions
                    n_r, n_c = cur_r + dr, cur_c + dc
                    if (0 <= n_r < ROWS) and (0 <= n_c < COLS) and grid[n_r][n_c] == 1:
                        queue.append((n_r, n_c))  # Append new rotten oranges to the queue
                        grid[n_r][n_c] = 2  # Mark the orange as rotten
                        fresh -= 1  # Decrement count of fresh oranges
            time += 1  # Increment time after processing each level in BFS

        return time if fresh == 0 else -1  # Return the total time if all oranges are rotten, otherwise -1

# Complexity:
# T: O(N*M), where N is the number of rows and M is the number of columns in the grid.
# This is because in the worst case, every cell is visited at least once.
# S: O(N*M) in the worst case for the BFS queue, especially when all cells are oranges.

# Testing:
instance = RottingOranges()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print("Given grid is:")
for i in range(len(grid)):
    print(grid[i])
print("Time taken to make all oranges rotten is:", instance.orangesRotting(grid))
# Output: 4
