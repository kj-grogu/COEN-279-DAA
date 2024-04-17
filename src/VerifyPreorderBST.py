# 255. Verify Preorder Sequence in Binary Search Tree
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
# Given an array of unique integers preorder, return true if it is the correct preorder traversal 
# sequence of a binary search tree.

# Example 1:
# Input: preorder = [5,2,1,3,6]
# Output: true

# Example 2:
# Input: preorder = [5,2,6,1,3]
# Output: false
 
# Constraints:
# 1 <= preorder.length <= 104
# 1 <= preorder[i] <= 104
# All the elements of preorder are unique.
 
# Follow up: Could you do it using only constant space complexity?

from ast import List
import collections
from typing import List

class VerifyPreorderBST:
    # Main logic:
    # Given array is not a valid preorder of a BST if:
    # step 1: As 1st element of the given list is root, find the first element which is greater than root val (this is the right node of root)
    # step 2: If any elment to right of above found right node is lesser than root node's val, the array is invalivd BST preorder -> return False
    # step 3: if case we traverse the whole given array and don't return a False, then return True

    def verifyPreorder(self, preorder: List[int]) -> bool:
        root = float("-inf") # keeps track of current root of sub BST
        stack = [] # keeps track of nodes

        for i in range(len(preorder)):
            # Finding the right Node
            while len(stack) > 0 and preorder[i] > stack[-1]:
                root = stack.pop()
            # checking of nodes to the right of right node are not less than cur root val - return False
            if preorder[i] < root:
                return False
            # push nodes to stack until right node is found
            stack.append(preorder[i])
        return True

# Complexity:
# T: O(N)
# S: O(N)

# Testing:
instance = VerifyPreorderBST()
preorder = [5,2,1,3,6]
print("Given preorder of BST:", preorder)
print("The given preorder is valid for a BST: ", instance.verifyPreorder(preorder))
# Output: true





        