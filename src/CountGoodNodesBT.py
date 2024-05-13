# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Given a binary tree root, a node X in the tree is named good if in the path from root to X 
# there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Example 2:
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

# Example 3:
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

# Constraints:
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].

# Definition for a binary tree node.
# Each TreeNode contains an integer value, a pointer to the left child, and a pointer to the right child.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CountGoodNodesBT:
    # Function to count good nodes in the binary tree.
    def goodNodes(self, root: TreeNode) -> int:
        # If the tree is empty, return zero because there are no nodes.
        if not root:
            return 0

        # A class variable to store the count of good nodes.
        self.good_nodes = 0
        # Start a depth-first search from the root with the initial max_val as the lowest possible value.
        self.dfs(root, float("-inf"))
        # Return the total count of good nodes found.
        return self.good_nodes
    
    # Helper function to perform depth-first search.
    def dfs(self, node, max_val):
        # If the current node is null, return, as there's nothing to process.
        if not node:
            return

        # If the current node's value is greater than or equal to the current maximum value along the path,
        # it is considered a good node.
        if node.val >= max_val:
            self.good_nodes += 1  # Increment the count of good nodes.
            max_val = node.val     # Update the maximum value to the current node's value for further traversal.
        
        # Recursively call dfs for the left child with the updated maximum value.
        self.dfs(node.left, max_val)
        # Recursively call dfs for the right child with the updated maximum value.
        self.dfs(node.right, max_val)

# Complexity:
# T: O(N), where N is the number of nodes in the tree.
# Each node is visited exactly once, making the traversal linear with respect to the number of nodes.
# S: O(H), where H is the height of the tree.
# The space complexity is determined by the height of the recursion stack, which in the worst case (a skewed tree) could be O(N),
# but for a balanced tree, it would be O(log N).

# Testing:
instance = CountGoodNodesBT()
node4 = TreeNode(2, None, None)
node3 = TreeNode(4, None, None)
node2 = TreeNode(3, node3, node4)
node1 = TreeNode(3, node2, None)
print("Good nodes in the given tree:", instance.goodNodes(node1))
# Output: 3

