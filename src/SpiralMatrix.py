# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from ast import List
from typing import List

class SpiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # direction: 0 -> right, 1 -> down, 2 -> left, 3 -> top
        dir = 0
        left, right = 0, len(matrix[0])
        top, down = 0, len(matrix)
        while(left < right and top < down):
            match dir:
                case 0:
                    for i in range(left,right):
                        res.append(matrix[top][i])
                    top += 1
                case 1:
                    for i in range(top,down):
                        res.append(matrix[i][right - 1])
                    right -= 1
                case 2:
                    for i in range(right - 1,left - 1, -1):
                        res.append(matrix[down - 1][i])
                    down -= 1
                case 3:
                    for i in range(down - 1 ,top - 1, -1):
                        res.append(matrix[i][left])
                    left += 1
            dir = (dir + 1) % 4
        return res


    # complexity:
    # T: O(N * M)
    # S: O(N * M), counting res

# Testing
instance = SpiralMatrix()
matrix = [[1, 2, 3], 
    [4, 5, 6],
    [7,8,9]]

print("Spiral order of Matrix: ")
for i in matrix:
    print('\t'.join(map(str, i)))
print("is: ", instance.spiralOrder(matrix))
