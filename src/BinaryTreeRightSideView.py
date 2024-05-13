# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom. 

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeRightSideView:
     # Function to get the right side view of a binary tree.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If the tree is empty, return an empty list.
        if not root:
            return []

        # Initialize a queue with the root node to manage the level order traversal.
        queue = collections.deque([root])
        # List to store the rightmost elements at each level.
        res = []

        # Continue until there are no more nodes to process in the queue.
        while queue:
            # The last node's value in the current level is appended to the result list.
            res.append(queue[-1].val)

            # Process each node at the current level.
            for _ in range(len(queue)):
                node = queue.popleft()  # Remove the node from the front of the queue.
                # If the node has a left child, add it to the queue.
                if node.left:
                    queue.append(node.left)
                # If the node has a right child, add it to the queue.
                if node.right:
                    queue.append(node.right)
        
        # Return the list containing the rightmost element from each level.
        return res

# Complexity:
# T: O(N) - The algorithm traverses each node exactly once, where N is the number of nodes in the tree.
# S: O(N) - The queue may contain up to the maximum width of the tree, 
# which can be all nodes at its last level in the worst case.

# Testing:
instance = BinaryTreeRightSideView()
node5 = TreeNode(4, None, None)
node4 = TreeNode(5, None, None)
node3 = TreeNode(3, None, node5)
node2 = TreeNode(2, None, node4)
node1 = TreeNode(1, node2, node3)
root = node1
print("The right side view of the given tree:", instance.rightSideView(root))
# Output: [1,3,4]

        