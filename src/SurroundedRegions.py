# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Given an m x n matrix board containing 'X' and 'O', 
# capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

from typing import List

class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Modifies the given board by capturing all 'O' regions that are not connected to the border of the board, turning them into 'X'.
        """
        # Determine dimensions of the board
        ROWS = len(board)
        COLS = len(board[0])
        
        # Directions for moving in the DFS: down, right, up, left
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def capture_dfs(r, c):
            # Base case for recursion: check for bounds and if the current cell is not 'O'
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
                return
            # Mark the 'O' as 'T' to avoid reprocessing and indicate temporary safety
            board[r][c] = "T"
            # Recursively visit all neighboring cells
            for dr, dc in directions:
                n_r, n_c = r + dr, c + dc
                capture_dfs(n_r, n_c)
        
        # Start DFS from all 'O's on the borders to mark the connected 'O's as safe ('T')
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == "O":
                    capture_dfs(r, c)

        # Flip all remaining 'O' to 'X' as they are surrounded by 'X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Restore all 'T' back to 'O' to finalize the safe regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        return board

# Complexity:
# Time (T): O(M * N) - each cell is processed exactly once.
# Space (S): O(M * N) in the worst case if the entire board is filled with 'O' and needs to be marked temporarily.

# Testing:
instance = SurroundedRegions()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print("Given board is:")
for i in range(len(board)):
    print(board[i])
print("board after capture process is run on it:")
for i in range(len(board)):
    print(board[i])