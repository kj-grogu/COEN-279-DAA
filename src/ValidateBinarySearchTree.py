# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ValidateBinarySearchTree:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     return self.bST_validHelper(root)[0]

    # def bST_validHelper(self, root):
    #     # if the tree is null / root is null
    #     if not root:
    #         return (False, float('inf'), float('-inf'))

    #     # if node is leaf node with no left or right child
    #     if not root.left and not root.right:
    #         return(True, root.val, root.val)

    #     is_left_valid, l_min, l_max = self.bST_validHelper(root.left)
    #     is_right_valid, r_min, r_max = self.bST_validHelper(root.right)

    #     # if both left and right child present and valid subTrees
    #     if is_left_valid and is_right_valid and l_max < root.val < r_min:
    #         return (True, l_min, r_max)

    #     # if left child is null and right subTree is valid
    #     elif not root.left and is_right_valid and r_min > root.val:
    #         return (True, root.val, r_max)
        
    #     # if right child is null and left subTree is valid
    #     elif not root.right and is_left_valid and l_max < root.val:
    #         return (True, l_min, root.val)

    #     # any other case
    #     else:
    #         return (False, float('inf'), float('-inf'))
    # OR:
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         return self.isValid(root, float("-inf"), float("inf"))
    
    def isValid(self, node, min, max):
          if not node:
               return True
          if min >= node.val or node.val >= max:
               return False
          return (self.isValid(node.left, min, node.val) and self.isValid(node.right, node.val, max))
    def traverseTree(self, node):
         if not node:
              print("None")
              return
         print(node.val)
         self.traverseTree(node.left)
         self.traverseTree(node.right)

# Complexity:
# T: O(N)
# S: O(N), countingrecursive call stack


# Testing:
instance = ValidateBinarySearchTree()
# root = [5,1,4,null,null,3,6]
# Output: false
node2 = TreeNode(1, None, None)
node4 = TreeNode(3, None, None)
node5 = TreeNode(6, None, None)
node3 = TreeNode(4, node4, node5)
node1 = TreeNode(5, node2, node3)
print("Given Tree is:")
print(instance.traverseTree(node1))
print("The given tree is a valid BST:", instance.isValidBST(node1))

        