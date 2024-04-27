from ast import List
from typing import List
# https://leetcode.com/problems/set-matrix-zeroes/

# 73. Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

# Follow up:
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class SetMatrixZeroes:
        def setZeroes(self, matrix: List[List[int]]) -> None:
            row_0 = [0] * len(matrix)
            col_0 = [0] * len(matrix[0])

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        row_0[i] = -1
                        col_0[j] = -1

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if row_0[i] == -1:
                        matrix[i][j] = 0
                    if col_0[j] == -1:
                        matrix[i][j] = 0

# Complexity:
# T: O(M * N)
# S: O(M + N)


# Testing
instance = SetMatrixZeroes()
matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]

print("Matrix: ")

for i in matrix:
    print('\t'.join(map(str, i)))

print("After setting rows and cols to zero is: ")

instance.setZeroes(matrix)

for i in matrix:
    print('\t'.join(map(str, i)))
