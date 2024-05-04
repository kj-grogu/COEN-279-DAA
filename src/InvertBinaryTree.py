# Definition for a binary tree node.
from ast import List
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InvertBinaryTree:
# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root #  or return None, if root of the tree is null or empty return None.

        # simple swapping code to invert the left and right nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left) # self is needed to call the same function from itself if it takes self parameter as this makes it a class method and you need to call class methods with self.blabla format.
        self.invertTree(root.right)
        return root
    
    def build_binary_tree(self, values: List[int]) -> Optional[TreeNode]:
        """
        Build a binary tree from a list of values. The list represents the binary tree
        in level-order (top to bottom, left to right).
        """
        if not values:
            return None

        nodes = [None if val is None else TreeNode(val) for val in values]
        root = nodes[0]
        i = 1
        while i < len(nodes):
            if nodes[i]:
                nodes[i - 1].left = nodes[i]
            i += 1
            if i < len(nodes) and nodes[i]:
                nodes[i - 1].right = nodes[i]
            i += 1

        return root

    def display_binary_tree_preorder(self, root: Optional[TreeNode]):
        """
        Display a binary tree in pre-order traversal.
        """
        def preorder_traversal(node):
            if node:
                print(node.val, end=" ")
                preorder_traversal(node.left)
                preorder_traversal(node.right)

        preorder_traversal(root)
        print()

# Complexity:
# T: O(N) - The function must visit every node in the tree once.
# S: - Best Case: ( O(log n)) — When the tree is balanced.
 # - Worst Case: ( O(n) ) — When the tree is completely unbalanced.
        
# Testing
instance = InvertBinaryTree()
values = [4,2,7,1,3,6,9]  # Replace with your binary tree values
root = instance.build_binary_tree(values)
# Display the binary tree
print("given Binary tree is: ")
instance.display_binary_tree_preorder(root)
# Invert the binary tree
print("Inverted Binary tree is: ")
instance.invertTree(root)
instance.display_binary_tree_preorder(root)





        
        