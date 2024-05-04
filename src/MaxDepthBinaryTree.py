# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node 
# down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2
 

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaxDepthBinaryTree:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Solution Approach 1: Reccurrsive depth first search (DFS):
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Solution Approach 2: iterative Breadth First Search(BFS):
        # if not root:
        #     return 0

        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        
        # return level

        # Solution Approach 3: iterative DFS (Depth First Search):
        stack = [[root, 1]] # creating a stack of an array which has 2 elements (node, depth)
        res = 0

        while stack:
            node, depth = stack.pop()
            if node: # This check prevents us from updating the res for null nodes, even though they get added
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return res

# Complexity:
# T: O(N)
# S: O(N) in the worst case (skewed tree) and O(logn) in the best case (balanced tree).

# Testing:
instance = MaxDepthBinaryTree()
node5 = TreeNode(7, None, None)
node4 = TreeNode(15, None, None)
node3 = TreeNode(20, node4, node5)
node2 = TreeNode(9, None, None)
node1 = TreeNode(3, node2, node3)
root = node1
print("Max depth of the given bonary tree is:", instance.maxDepth(root))
# Output: 3



        