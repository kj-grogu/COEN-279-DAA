# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 
# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) 
# and you need to find the kth smallest frequently, how would you optimize?


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # recursive solution:
# class KthSmallestElementBST:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         res = self.inorder(root)
#         return res[k - 1]

#     def inorder(self, root):
#         # first explores the left side of the tree goes to leaf node
#         # add's node's value to list in form [root.val] 
#         # then explores the right side of the node
#         # above happens if node is valid else returns empty list.
#         return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

# # Complexity:
# # T: O(N)
# # S: O(N) the list created

# iterative Solution:
class KthSmallestElementBST:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True: # because we will break out of the loop any way
            while root:
                stack.append(root)
                root = root.left # explore the left as far as possible, to the left most node (smallest element)
            
            root = stack.pop() # pops the top most node, or the node added most recently
            k -= 1

            if not k:
                return root.val

            root = root.right # explore the right side of the most recently poped node

# Complexity:
# T: O(N)
# S: O(N)
# while the worst case complexity for both solutions are same the avg case complexity for iterative solution is much better

# Testing:
instance = KthSmallestElementBST()
node4 = TreeNode(2, None, None)
node3 = TreeNode(4, None, None)
node2 = TreeNode(1, None, node4)
node1 = TreeNode(3, node2, node3)
root = node1
k = 1

print(k, "th smallest element of the tree is:", instance.kthSmallest(root, k))
# Output: 1
        

        
        

        