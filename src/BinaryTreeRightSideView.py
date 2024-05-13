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
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeRightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        bfs_queue = collections.deque([root])
        res = []

        while bfs_queue:
            level_len = len(bfs_queue)

            for i in range(level_len):
                node = bfs_queue.popleft()
                if i == level_len - 1:
                    res.append(node.val)

                if node.left:
                    bfs_queue.append(node.left)
                
                if node.right:
                    bfs_queue.append(node.right)
        
        return res

# Complexity:
# T: O(N)
# S: O(N) , size of the queue

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

        