# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

import collections
from typing import List, Optional


# Definition for a binary tree node.
# Each TreeNode contains an integer value, a pointer to the left child, and a pointer to the right child.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LevelOrderTraversalBT:
    # Function to return the level order traversal of a binary tree as a list of lists.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list.
        if not root:
            return []

        # List to hold the values of nodes at each level.
        res = []
        # Initialize a queue with the root node to manage the level order traversal.
        queue = collections.deque([root])

        # Continue until there are no more nodes to process in the queue.
        while queue:
            # Temporary list to store the values of nodes at the current level.
            level_vals = []
            # Iterate over all nodes currently in the queue (i.e., all nodes at the current level).
            for _ in range(len(queue)):
                node = queue.popleft()  # Remove the node from the front of the queue.
                level_vals.append(node.val)  # Append the node's value to the list of current level values.
                # If the node has a left child, add it to the queue.
                if node.left:
                    queue.append(node.left)
                # If the node has a right child, add it to the queue.
                if node.right:
                    queue.append(node.right)

            # Append the list of values from the current level to the result list.
            res.append(level_vals)
        
        # Return the list of lists, where each list contains the values at a specific level of the tree.
        return res

# Complexity:
# T: O(N) - The algorithm traverses each node exactly once, where N is the number of nodes in the tree.
# S: O(N) - The queue may contain up to the maximum width of the tree, which can be all nodes at its last level in the worst case.

# Testing:
instance = LevelOrderTraversalBT()
node5 = TreeNode(7, None, None)
node4 = TreeNode(15, None, None)
node3 = TreeNode(20, node4, node5)
node2 = TreeNode(9, None, None)
node1 = TreeNode(3, node2, node3)
root = node1

print("The right side view of the given tree:", instance.rightSideView(root))
# Output: [1,3,4]