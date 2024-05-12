# 261. Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree/
# You have a graph of n nodes labeled from 0 to n - 1. 
# You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
 
# Constraints:
# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.

from ast import List
from typing import List

class GraphValidTree:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # What is a valid tree:
        # 1. A graph with no cycles in it.
        # 2. A graph where all nodes are connected.
        # 3. A graph with no nodes is a valid empty tree.
        
        if not n:
            return True # if n is 0 then there are no nodes in the tree and the tree is empty but valid so return true.

        adj = {i:[] for i in range(n)} # declare adjacency array with an array for for every node.
        for n1, n2 in edges:
            adj[n1].append(n2) # appending in both nodes as the graph is undirected.
            adj[n2].append(n1)

        # prev => is passed and used to detect false positives for cycles, as 0 -> 1 -> 4 
        # here we pass 0 as prev so as to not go through it again, as it's a connection of 1)
        # To make sure we don't count a cycle 0 -> 1 -> 0, and return False
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False # cycle detected so not a valid tree, return false.

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit) # dfs: starting with 0, and default prev value for root node 0 is -1.
            # dfs checks for cycle and 'n == len(visit)' checks if all the nodes are connected or not.

# Complexity:
# Time (T): O(V + E) - where V is the number of vertices and E is the number of edges.
# Space (S): O(V + E) - due to the adjacency list and the recursion stack in the worst case.

# Testing
instance = GraphValidTree()
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
print("Given graph is valid: ", instance.validTree(5, edges))

        