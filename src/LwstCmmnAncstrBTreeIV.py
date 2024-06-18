# 1676. Lowest Common Ancestor of a Binary Tree IV
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

# Logic video:
# https://www.youtube.com/watch?v=wrX3tTSzrCA&t=511s

# Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. 
# All the nodes will exist in the tree, and all values of the tree's nodes are unique.

# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T 
# is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". 
# A descendant of a node x is a node y that is on the path from node x to some leaf node.

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
# Output: 2
# Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
# Output: 1
# Explanation: The lowest common ancestor of a single node is the node itself.

# Example 3:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
# Output: 5
# Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.
 

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -109 <= Node.val <= 109
# All Node.val are unique.
# All nodes[i] will exist in the tree.
# All nodes[i] are distinct.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class LwstCmmnAncstrBTreeIV:
    # Function to find the lowest common ancestor of given nodes in a binary tree
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # Convert the list of nodes to a set for O(1) average-time complexity lookups
        nodes = set(nodes)

        # Define a helper function to perform Depth-First Search (DFS)
        def dfs(node):
            # If the node is None, return None
            if not node:
                return None
            
            # If the current node is in the set of target nodes, return the node
            if node in nodes:
                return node
            
            # Recursively search the left subtree
            l = dfs(node.left)
            # Recursively search the right subtree
            r = dfs(node.right)

            # If both left and right searches found a target node, current node is the LCA
            if l and r:
                return node
            else:
                # Otherwise, return the non-None result from the left or right search
                return l or r

        # Initiate DFS from the root of the tree and return the result
        return dfs(root)

# Time Complexity: O(N)
# The algorithm visits each node exactly once, where N is the number of nodes in the tree.
# In each visit, it performs constant-time operations.

# Space Complexity: O(H)
# The space complexity is determined by the recursion stack, which depends on the height of the tree H.
# In the worst case, the height of the tree could be N (e.g., in a skewed tree), resulting in O(N) space complexity.
# In the best case (balanced tree), the height H would be log(N), resulting in O(log(N)) space complexity.
    
# Testing:
instance = LwstCmmnAncstrBTreeIV()
node9 = TreeNode(4)
node8 = TreeNode(7)
node7 = TreeNode(8)
node6 = TreeNode(0)
node5 = TreeNode(2)
node5.left, node5.right = node8, node9
node4 = TreeNode(6)
node3 = TreeNode(1)
node3.left, node3.right = node6, node7
node2 = TreeNode(5)
node2.left, node2.right = node4, node5
node1 = TreeNode(3)
node1.left, node1.right = node2, node3

nodes = [node8, node9]

root = node1
print("The LCS for given nodes of binary tree is:", instance.lowestCommonAncestor(root, nodes).val)
# Output: 2


