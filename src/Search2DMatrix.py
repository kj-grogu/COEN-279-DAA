# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from ast import List
import collections
from typing import List

class Search2DMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1

        top, bot = 0, ROWS

        target_r = -1

        while top <= bot:
            mid_r = top + (bot - top) // 2
            
            if target >= matrix[mid_r][0] and target <= matrix[mid_r][COLS]:
                target_r = mid_r
            if target >= matrix[top][0] and target < matrix[mid_r][COLS]:
                bot = mid_r - 1
            else:
                top = mid_r + 1

        if target_r != -1:
            l, r = 0, COLS
            while l <= r:
                mid = l + (r - l) // 2
                if target == matrix[target_r][mid]:
                    return True
                if target < matrix[target_r][mid]:
                    r = mid - 1
                else:
                    l = mid + 1

                if mid < 0 or mid > COLS:
                    return False
        
        return False

# Complexity:
# T: O(lg ROWS + lg COLS)
# S: O(1)

# Testing:
instance = Search2DMatrix()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print("Given Matrix is:")
for i in range(len(matrix)):
    print(matrix[i])
print("The target:", target, "is found in above matrix:", instance.searchMatrix(matrix, target))
# Output: false


        
        