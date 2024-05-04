# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DiameterOfBinaryTree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0  # Initialize the maximum diameter to 0
        self.dfs_findDia(root)  # Start the DFS from the root to calculate the diameter
        return self.dia  # Return the calculated diameter

    def dfs_findDia(self, node):      
        if not node:
            return -1  # Return -1 for null nodes to adjust height calculation for edges instead of nodes

        h_left = self.dfs_findDia(node.left)  # Recursive call to find the height of the left subtree
        h_right = self.dfs_findDia(node.right)  # Recursive call to find the height of the right subtree

        # Update the diameter where 2 represents the edges connecting the node with its two children
        self.dia = max(self.dia, 2 + h_left + h_right)

        # Return the height of the tree rooted at the current node
        return 1 + max(h_left, h_right)  # Height is max height of the subtrees plus 1 for the current node
    
    def preorderTraversal(self, node):
        if not node:
            return node
        print(node.val)

        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)

# Time and Space Complexity
# T: O(N), where N is the number of nodes in the binary tree. Each node is visited once.
# S: O(H), where H is the height of the tree. This is the space used by the recursion stack. 
    # In the worst case, this could be O(N) if the tree is skewed.

# Testing:
instance = DiameterOfBinaryTree()
node5 = TreeNode(5, None, None)
node4 = TreeNode(4, None, None)
node3 = TreeNode(3, None, None)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)
root = node1
print("Pre-Order traversal of the given tree is:")
instance.preorderTraversal(root)
print("The diameter of above tree is:", instance.diameterOfBinaryTree(root))
# Output: 3
