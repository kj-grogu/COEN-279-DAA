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
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True  # An empty tree is a subtree of any tree.

        if not root:
            return False  # If main tree is empty but subtree is not, then it's not a subtree.
        
        # Check if trees rooted at current nodes are identical.
        if self.isSame(root, subRoot):
            return True
        
        # Recursively check the left and right children of the current node in the main tree.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, root1, root2):
        if not root1 and not root2:
            return True  # Both trees are empty, hence they are the same.

        if not root1 or not root2 or root1.val != root2.val:
            return False  # If one is empty or the values do not match, trees are not the same.

        # Recursively check if the left and right subtrees are the same.
        return self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)

# Complexity:
# T: O(m*n), where m is the number of nodes in root and n is the number of nodes in subRoot.
#                  For every node in root, isSame may be called to compare it against subRoot.
# S: O(min(m, n)) in the worst case due to the recursion stack,
#                   where m and n are the depths of the root and subRoot trees, respectively.
    

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

        