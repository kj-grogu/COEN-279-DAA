# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, and 
# the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. 
# You are given an m x n integer matrix heights where heights[r][c] 
# represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and 
# the rain water can flow to neighboring cells directly north, south, east, and 
# west if the neighboring cell's height is less than or equal to the current cell's height. 
# Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

# Example 2:
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

# Constraints:
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105


from typing import List

class PacificAtlanticWaterFlow:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Obtain the number of rows and columns in the matrix
        ROWS = len(heights)
        COLS = len(heights[0])
        
        # Define the four possible directions for DFS traversal (right, down, up, left)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Initialize sets to track cells reachable from the Pacific and Atlantic oceans
        pac = set()
        alt = set()

        def dfs(r, c, visit, prevHeight):
            # Base condition to check out of bounds, decreasing height, or visited cells
            if (r < 0 or r == ROWS or c < 0 or c == COLS 
                or heights[r][c] < prevHeight or (r, c) in visit):
                return
            
            # Mark the cell as visited
            visit.add((r, c))

            # Explore all possible directions
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        # Perform DFS from all cells directly connected to the Pacific and Atlantic oceans
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])  # Top row for Pacific
            dfs(ROWS - 1, c, alt, heights[ROWS - 1][c])  # Bottom row for Atlantic
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])  # Left column for Pacific
            dfs(r, COLS - 1, alt, heights[r][COLS - 1])  # Right column for Atlantic

        # Collect all cells that can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])

        return res

# Complexity:
# T: O(M * N), where M is the number of rows and N is the number of columns. 
# S: O(M * N), where M is the number of rows and N is the number of columns. 
    
# Testing:
instance = PacificAtlanticWaterFlow()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print("The given grid of heights is:")
for i in range(len(heights)):
    print(heights[i])
print("The cells from the heights from which water can flow to both pacific and atlantic ocean:", 
      instance.pacificAtlantic(heights))
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


