# 773. Sliding Puzzle
# https://leetcode.com/problems/sliding-puzzle/
# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

# Example 1:
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.

# Example 2:
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.

# Example 3:
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]

# Constraints:
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# Each value board[i][j] is unique.


from ast import List
import collections
from typing import List

class SlidingPuzzle:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        self.ans = float("inf")
        self.directions = [(0, 1),(0, -1), (1, 0), (-1, 0)]
        self.visited = collections.defaultdict(lambda: float("inf"))

        # step 1: find the cell where 0 is present
        x, y = -1, -1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "0":
                    x, y = i, j
                    break

        # call recursive dfs
        self.dfs(board, x, y, 0)

        return self.ans if self.ans < float("inf") else -1

    def dfs(self, board, i, j, steps):
        if self.isSolved(board):
            self.ans = min(self.ans, steps)

        hash = self.createHash(board)

        if self.visited[hash] < steps:
            return
        
        self.visited[hash] = steps

        for d_i, d_j in self.directions:
            new_i, new_j = i + d_i, j + d_j

            if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                # swap
                board[i][j], board[new_i][new_j] = board[new_i][new_j], board[i][j]
                # recursive dfs call
                self.dfs(board, new_i, new_j, steps + 1)
                # reset swap:
                board[new_i][new_j], board[i][j]  = board[i][j], board[new_i][new_j]


    
    def isSolved(self, board):
        if (board[0][0] == "1" and board[0][1] == "2" and board[0][2] == "3" and board[1][0] == "4" and board[1][1] == "5" and board[1][2] == "0"):
            return True
        return False

    def createHash(self, board):
        hash = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                hash.append(str(board[i][j]))
        return "".join(hash)
    


# Testing:
instance = SlidingPuzzle()
board = [[1,2,3],[4,0,5]]
print("Given board is:", board)
print("no of steps to convert this board to expected [[1,2,3],[4,5,0]] are:", instance.slidingPuzzle(board))
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.


