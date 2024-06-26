
# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

from ast import List
from typing import List

class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range (len(matrix)):
            for j in range (i,len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        
        for i in range (len(matrix)):
            left = 0
            right = len(matrix[0]) - 1
            while(left < right):
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1

# Testing
instance = RotateImage()
matrix = [[1, 2, 3], 
    [4, 5, 6],
    [7,8,9]]

print("Matrix: ")
for i in matrix:
    print('\t'.join(map(str, i)))

instance.rotate(matrix)

print("After 90 degree rotation is: ")
for i in matrix:
    print('\t'.join(map(str, i)))

# 	0	1	2                                           	0	1	2                                               0	1	2
# 0	1	2	3       Step 1:                             0	1	4	7       Step 2:                              0	7	4	1
# 1	4	5	6       Matrix[i][j] => Matrix[j][i]        1	2	5	8       Reverse cols: 0 to 2 To 2 to 0       1	8	5	2
# 2	7	8	9                                           2	3	6	9                                            2	9	6	3