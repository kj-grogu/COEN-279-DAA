# 317. Shortest Distance from All Buildings
# https://leetcode.com/problems/shortest-distance-from-all-buildings/

# Logic video:
# https://www.youtube.com/watch?v=yjHXS2w_IvY

# You are given an m x n grid grid of values 0, 1, or 2, where:

# each 0 marks an empty land that you can pass by freely,
# each 1 marks a building that you cannot pass through, and
# each 2 marks an obstacle that you cannot pass through.

# You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

# Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.
# The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# Example 1:
# Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 7
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
# So return 7.

# Example 2:
# Input: grid = [[1,0]]
# Output: 1

# Example 3:
# Input: grid = [[1]]
# Output: -1

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0, 1, or 2.
# There will be at least one building in the grid.

import collections
from typing import List

class ShrtstDistfrmAllBldngs:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)  # Number of rows in the grid
        cols = len(grid[0])  # Number of columns in the grid

        # Distance matrix to store the sum of distances from all buildings to each empty land
        dist_matrix = [[0] * cols for r in range(rows)]
        # Directions for exploring the neighboring cells (right, down, up, left)
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]

        OBSTACLE = 2
        BUILDING = 1
        EMPTY_LAND = 0

        # Variable to store the minimum distance found
        min_dist = float("inf")

        # Loop over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Start BFS from each building
                if grid[r][c] == BUILDING:
                    # Initialize local minimum distance as infinite
                    local_dist = float("inf")
                    # Queue for BFS, start from the building position with initial distance 0
                    queue = collections.deque([(r, c, 0)])

                    # Perform BFS to find minimum distance to all reachable empty lands
                    while queue:
                        cur_r, cur_c, cur_dist = queue.popleft()

                        # Explore all four neighboring cells
                        for d_r, d_c in directions:
                            n_r = cur_r + d_r
                            n_c = cur_c + d_c
                            # Check if the neighbor is within bounds and is empty land
                            if (0 <= n_r < rows) and (0 <= n_c < cols) and grid[n_r][n_c] == EMPTY_LAND:
                                # Mark the land as visited by decrementing its value
                                grid[n_r][n_c] = EMPTY_LAND - 1
                                # Accumulate distances in the distance matrix
                                dist_matrix[n_r][n_c] += cur_dist + 1
                                # Enqueue the neighbor with incremented distance
                                queue.append((n_r, n_c, cur_dist + 1))
                                # Update local minimum distance for this BFS
                                local_dist = min(local_dist, dist_matrix[n_r][n_c])

                    # Reset the EMPTY_LAND to a new lower value after each BFS
                    EMPTY_LAND -= 1
                    # Update the global minimum distance across all BFS traversals
                    min_dist = local_dist
        
        # Return the global minimum distance if found, otherwise return -1
        return min_dist if min_dist != float("inf") else -1

# Complexity:
# Time Complexity (T): O((M*N)^2) in the worst case
# Each cell initiates a BFS traversal, which can explore up to M*N cells, leading to a high time complexity.
#
# Space Complexity (S): O(M*N)
# Space complexity primarily comes from the distance matrix and the queue used in BFS,
# which in the worst case might need to store information about all cells in the grid.
    
# Testing:
instance = ShrtstDistfrmAllBldngs()
print("The given grid is")
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
for r in range(len(grid)):
    print(grid[r])

print("The total distance to empty land at shortest distance from all buildings is:", instance.shortestDistance(grid))
# Output: 7

    