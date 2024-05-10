# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 
# Constraints:
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

from ast import List
from typing import List
class RedundantConnection:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)] # creating a parent array with elements for all nodes from 1 to n in the graph, the array is 1 element larger than the edges as the array will have 0 element as well, which we will not use.
        # Also don't forget that that the lenght of the edges list is equal to n nodes as there is an extra edge creating the cycle, which we need to find.
        rank = [1] * (len(edges) + 1) #at the beginig giving a rank of 1 to all nodes and creating an array of length n+1 with pre assigned value of 1.

        # definition of find algorithm of UnionFind, here it is used to find the parent of the nodes of an edge.
        def find(n):
            p = par[n]
            while p != par[p]: # jab tak p aur p ka parent same nahi ho jate p ke parent me dal do p ke parent ke parent ko and p me dal do p ke parent ko.
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        # return False if can't complete an union that is can't connect two edges as they are already connect due to having of same parent.
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # main logic to call -> union find function
        for n1, n2 in edges:
            if not union(n1, n2): #if the two nodes of an edge in the graph are already connected directly of through their parents then this edge is an redundant edge and can be returned.
                return [n1, n2]

# Complexity:
# Time (T): O(E * α(N)), where E is the number of edges and α(N) is the inverse Ackermann function,
# which is practically constant for any feasible input size.
# Space (S): O(N), where N is the number of vertices in the graph, for storing the parent and rank arrays.
            
# Testing
instance = RedundantConnection()
edges = [[1,2],[1,3],[2,3]]

redEdge = instance.findRedundantConnection(edges)
print("Redundant edge from the edges of following graph is: ")

for i in edges:
    print('\t'.join(map(str, i)))

for i in redEdge:
    print('\t'.join(map(str, i)))

        