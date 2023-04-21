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
        """
        Do not return anything, modify matrix in-place instead.
        """
        lRow = len(matrix)
        lCol = len(matrix[0])
        row = 1
        for i in range(lRow):
            for j in range(lCol):
                if i == 0 and matrix[i][j] == 0:
                    row = 0
                    matrix[0][j] = 0
                elif matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, lRow):
            for j in range(1, lCol):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(lRow):
                matrix[i][0] = 0

        if row == 0:
            for j in range(lCol):
                matrix[0][j] = 0


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
