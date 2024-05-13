# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

# Iterative Solution:
class LowestCommonAncestorBST:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root:
    #         return None

    #     while root:
    #         if p.val > root.val and q.val > root.val:
    #             root = root.right
    #         elif p.val < root.val and q.val < root.val:
    #             root = root.left
    #         else:
    #             return root

    # OR:
    # Recirsive Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

# Complexity:
# T: O(Lg N)
# S: O(1)

# Testing:
instance = LowestCommonAncestorBST()
node9 = TreeNode(5, None, None)
node8 = TreeNode(3, None, None)
node7 = TreeNode(9, None, None)
node6 = TreeNode(7, None, None)
node5 = TreeNode(4, node8, node9)
node4 = TreeNode(0, None, None)
node3 = TreeNode(8, node6, node7)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(6, node2, node3)
root = node1
print("given BST is:", root)
p, q = node2, node3
print("Lowest common ancestor of", p.val, " and", q.val, "is:", instance.lowestCommonAncestor(root, p, q).val)
# Output: 6




        