# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is 
# height-balanced.
# A height-balanced binary tree is a binary tree in which 
# the depth of the two subtrees of every node never differs by more than one.
 

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true
 
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BalancedBinaryTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]  # Initiates a DFS from the root and returns the balance status.

    def dfs(self, node):
        if not node:
            return [True, 0]  # If the current node is None, it's trivially balanced with a height of 0.

        left = self.dfs(node.left)  # Recursively check the left subtree.
        right = self.dfs(node.right)  # Recursively check the right subtree.

        # Determine if the current subtree is balanced:
        # 1. Both left and right subtrees must be balanced.
        # 2. The height difference between the left and right subtree must be <= 1.
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        # Return the balance status and the height of the current node's subtree.
        # Height is the maximum height of the left or right subtree plus one for the current node.
        return [balanced, 1 + max(left[1], right[1])]
    
    def preorderTraversal(self, node):
        if not node:
            return node
        print(node.val)

        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)

# Complexity:
# T: O(N) - Each node in the tree is visited once during the DFS, where N is the number of nodes.
# S: O(H) - The maximum depth of the recursion stack is the height of the tree, H.
# In the worst case (a skewed tree), this could be O(N).

# Testing:
instance = BalancedBinaryTree()
node5 = TreeNode(7, None, None)
node4 = TreeNode(15, None, None)
node3 = TreeNode(20, node4, node5)
node2 = TreeNode(9, None, None)
node1 = TreeNode(3, node2, node3)
print("The pre order traversal of the given tree is:", instance.preorderTraversal(node1))
print("The given tree is balanced or not:", instance.isBalanced(node1))
# Output: true  