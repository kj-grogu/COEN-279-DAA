# 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.

# Example 1:
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 
# Constraints:
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

from ast import List
from typing import List

class NumOfConnectedComponents:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize the parent array where each node is initially its own parent
        # and the rank array, which helps in keeping the union operation balanced.
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            """
            Path compression heuristic: This function finds the root of the set n belongs to,
            while also making the path for all nodes under this root point directly to the root.
            This optimizes the union-find structure by flattening the structure of the trees,
            speeding up future operations.
            """
            res = n
            while res != par[res]:
                par[res] = par[par[res]]  # Path compression by halving
                res = par[res]
            return res

        def union(n1, n2):
            """
            Union by rank heuristic: This function joins two subsets into a single subset.
            The root of the larger rank tree becomes the root of the united tree. If ranks are
            the same, make one root and increase its rank.
            """
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0  # n1 and n2 are already in the same set

            # Union by rank
            if rank[p1] < rank[p2]:
                par[p1] = p2
            elif rank[p1] > rank[p2]:
                par[p2] = p1
            else:
                par[p2] = p1
                rank[p1] += 1

            return 1  # Successfully united two components

        # Count the number of connected components
        res = n  # Start with n components
        for n1, n2 in edges:
            res -= union(n1, n2)  # Each successful union reduces the component count by 1
        
        return res

# Complexity:
# Time (T): O(E * α(N)), where E is the number of edges and α(N) is the inverse Ackermann function,
# which grows very slowly and is less than 5 for all practical values of N.
# Space (S): O(N), for the parent and rank arrays.

# Testing
instance = NumOfConnectedComponents()
edges = [[0,1],[1,2],[2,3],[3,4]]
print("no of connected components in the graph are: ", instance.countComponents(5, edges))

