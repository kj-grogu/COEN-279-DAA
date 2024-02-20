
from ast import List
from typing import List
from typing import Optional

# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class MaxPathSum:
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

    def max_PathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_path_sum = root.val

        self.dfs_postOrder(root)

        return self.max_path_sum

    def dfs_postOrder(self, node):
        # Case 1: if node is null
        if not node:
            return 0

        # Case 2: if node is a leaf node:
        if not node.left and not node.right:
            self.max_path_sum = max(self.max_path_sum, node.val)
            return node.val
        
		# Case 3: Normal node with left and right child:
        # Here post order traversal because we process the left and right sub trees first
        # able to call dfs func directly without checking for left or rigth childs cause that check will be done at the begining of the dfs code after the the call is made
        l_path_sum = self.dfs_postOrder(node.left)
        r_path_sum = self.dfs_postOrder(node.right)
        
		# Now calculate the max_path_sum:
        self.max_path_sum = max(
            self.max_path_sum,
            node.val,
            node.val + l_path_sum + r_path_sum,
            node.val + l_path_sum,
            node.val + r_path_sum 
            )
        
		# Now process return value for the current node's dfs call, as its post order so processing the node at last:
        return max(
            node.val,
            node.val + l_path_sum,
            node.val + r_path_sum,
            0
		)
    
	# Complexity:
		# Time: O(N) as processing all the nodes in the tree
		# Space: O(1), if not considering recursive call stack else O(N)
    
	

# Testing:
instance = MaxPathSum()
values = [-10,9,20,None,None,15,7]  # Replace with your binary tree values
# Tree building method has some issues will resolve and update but the logical code for the problem is corrects
root = instance.build_binary_tree(values)
# Display the binary tree
print("given Binary tree is: ")
instance.display_binary_tree_preorder(root)
# Find the maximum path sum of binary tree
print("The maximum path sum of above tree is: ", instance.max_PathSum(root))

    
    
        
        

        