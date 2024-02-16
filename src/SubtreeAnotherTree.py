from typing import Optional
from ast import List
from typing import List

# 572. Subtree of Another Tree
# https://leetcode.com/problems/invert-binary-tree/

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Ex 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Ex 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SubTreeAnotherTree:
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
    
    def isSubTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot))
    
    def isSameTree(self, p, q):
        if (not p and not q):
            return True
        if (not p or not q):
            return False
        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# Testing
instance = SubTreeAnotherTree()
rootValues = [3,4,5,1,2]  # Replace with your binary tree values
subRootValues = [4,1,2]
root = instance.build_binary_tree(rootValues)
subRoot = instance.build_binary_tree(subRootValues)

# Display the binary tree
print("given Root Binary tree is: ")
instance.display_binary_tree_preorder(root)

print("given SubRoot Binary tree is: ")
instance.display_binary_tree_preorder(subRoot)

print(instance.isSubTree(root, subRoot))

        