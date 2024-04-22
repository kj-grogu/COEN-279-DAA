# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1

# Example 3:
# Input: matrix = [["0"]]
# Output: 0
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.


from ast import List
from typing import List
from typing import Optional


class MaximalSquare:
    # Bottom up approach
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        # DP matrix, store bottom up sols, with 1 row and col extra to handle out of bound errors
        dp = [[0 for c in range(COLS + 1)] for r in range(ROWS + 1)]
        res = 0

        #iterate over the matrix from bottom right corner to top left corner
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                # MAIN LOGIC 
                # dp val at a cell is dependent on its just right, down, diag cell vals
                right_val = dp[r][c + 1]
                down_val = dp[r + 1][c]
                diag_val = dp[r + 1][c + 1]

                if matrix[r][c] == "1":
                    # take min of all 3 vals and add 1 to it 
                    dp[r][c] = min(right_val, down_val, diag_val) + 1 # adding 1 for this cell
                else:
                    dp[r][c] = 0

                res = max(res, dp[r][c])

        # res represents the side of square, to return its area square the res value
        return res * res

# Complexity:
# T: O(M * N)
# S: O(M * N)

# Testing:
instance = MaximalSquare()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print("Given Matrix is: ")
for r in range(len(matrix)):
    print(matrix[r])
# pprint(matrix)
print("Area of largest square with 1s in given matrix is:", instance.maximalSquare(matrix))
# Output: 4





        