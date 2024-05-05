# 100. Same Tree
# https://leetcode.com/problems/same-tree/
# Given the roots of two binary trees p and q, 
# write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 
# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True  # Both trees are empty, hence they are the same.
        if not p or not q or p.val != q.val:
            return False  # If one is empty and the other is not, or values do not match, trees are not the same.

        # Recursively check the left and right subtrees.
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# Complexity:
# T: O(N) - Where N is the smaller number of nodes in either p or q. The function must visit each node.
# S: O(log(N)) in the best case (balanced tree) and O(N) in the worst case (completely unbalanced tree),
# due to the recursion stack depth which depends on the height of the tree.


# Testing:
instance = SameTree()
p_node3 = TreeNode(1, None, None)
p_node2 = TreeNode(1, None, None)
p_node1 = TreeNode(1, p_node2, p_node3)

q_node3 = TreeNode(1, None, None)
q_node2 = TreeNode(1, None, None)
q_node1 = TreeNode(1, q_node2, q_node3)

print("The given trees p and q are same:", instance.isSameTree(p_node1, q_node1))
# Output: true
        