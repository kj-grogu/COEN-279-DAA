# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored 
# in a file or memory buffer, or transmitted across a network connection link to be reconstructed later 
# in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string and 
# this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
# You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        # dfs method to traverse tree in pre - order and contruct the serialized pre - order string of binary tree.
        def dfs_serialize(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))

            dfs_serialize(node.left)
            dfs_serialize(node.right)

        dfs_serialize(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        vals = data.split(",")
        self.i = 0

        # dfs method to recontruct a binary tree from its pre-order traversal serialized string.
        def dfs_deserialize():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs_deserialize()
            node.right = dfs_deserialize()
            return node
        
        return dfs_deserialize()


# Complexity:
# T: O(N) Pre-order traversal of whole tree
# S: O(N) constructing each and every node   

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
    
# Testing:
instance = Codec()
node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node3.left, node3.right = node4, node5
node2 = TreeNode(2)
node1 = TreeNode(1)
node1.left, node1.right = node2, node3
print("The serialized version of the given tree is:")
data = instance.serialize(node1)
print(data)
print("The deserialized tree from pre-order serialized version of tree is:")
print(instance.deserialize(data))
# Output: [1,2,3,null,null,4,5]