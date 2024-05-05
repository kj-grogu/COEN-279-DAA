# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). 
# For example, the first node with val == 1, the second node with val == 2, and so on. 
# The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. 
# Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. 
# You must return the copy of the given node as a reference to the cloned graph.

# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

# Constraints:
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.


import collections
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    # DFS Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        if node:
            return dfs(node)
        else:
            return None
    
    # Or:
    # BFS solution:
    def cloneGraph2(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None  # If the input node is None, return None.

        clonned = {}  # Dictionary to store the mapping from original nodes to their clones.
        clonned[node] = Node(node.val, [])  # Initialize the clone of the start node.
        queue = collections.deque([node])  # Use a deque for BFS.

        while queue:
            cur = queue.popleft()  # Dequeue a node.

            for nei in cur.neighbors:  # Iterate through all neighbors of the current node.
                if nei not in clonned:  # If the neighbor hasn't been cloned yet.
                    clonned[nei] = Node(nei.val, [])  # Clone it and add to the dictionary.
                    queue.append(nei)  # Enqueue the neighbor.
                clonned[cur].neighbors.append(clonned[nei])  # Add the cloned neighbor to the current clone's neighbor list.
        
        return clonned[node]  # Return the clone of the originally given node.

# Complexity:
# T: O(N + E) where N is the number of nodes and E is the number of edges in the graph.
# This is because each node and each edge is processed exactly once.
# S: O(N) as it involves storing a copy of all the nodes in the graph plus the BFS queue.


