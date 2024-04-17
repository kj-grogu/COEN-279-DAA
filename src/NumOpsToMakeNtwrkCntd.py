# 1319. Number of Operations to Make Network Connected
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network 
# where connections[i] = [ai, bi] represents a connection between computers ai and bi. 
# Any computer can reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. 
# You can extract certain cables between two directly connected computers, 
# and place them between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make all the computers connected. 
# If it is not possible, return -1.

# Example 1:
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

# Example 2:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2

# Example 3:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.

# Constraints:
# 1 <= n <= 105
# 1 <= connections.length <= min(n * (n - 1) / 2, 105)
# connections[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated connections.
# No two computers are connected by more than one cable.

from ast import List
import collections
from typing import List

class NumOpsToMakeNtwrkCntd:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        self.adjList = collections.defaultdict(list)
        self.visited = set()
        edges = 0

        # step 1: create the adjacency list and count total edges
        for src, dest in connections:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
            edges += 1

        # print("adjList: ", self.adjList)

        # step 2: if no of edges is lesser than no. of nodes - 1 then return -1
        if edges < n - 1:
            return -1

        # step 3: find all connected components in the network using dfs
        connectedComps = 0
        for i in range(n):
            if i not in self.visited:
                connectedComps += 1
                self.dfs(i)

        # step 4: find no. of. redundant edges using following considerations
        # consi 1: find required edges = no. of. edges (total nodes - 1) - (connected componenets - 1)
        # consi 2: redundant edges = edges - required edges
        # consi 3: look example 2, to understand formula
        # n = 6, edges = 5, connected comps = 3 => n - 1 = 5, connected comps - 1 = 2, 
        # redundant edges = 5 - ( 5 - 2) = 5 - 3 = 2

        # main formula to remember:
        redundantEdges = edges - ((n - 1) - (connectedComps - 1))
        # print("n:", n, "edges:", edges, "connectedComps:", connectedComps, "redundantEdges:", redundantEdges)
        # step 5: if redundand edges is greater than no. of. connected componenets,
        # then we cal connect the whole network else return -1
        if redundantEdges >= connectedComps - 1:
            return connectedComps - 1
        
        return -1

    # DFS helper method
    def dfs(self, src):
        self.visited.add(src)
        for node in self.adjList[src]:
            if node not in self.visited:
                self.dfs(node)

# Compexity:
# T: O(N + E)
# S: O(N + E)

# Testing:
instance = NumOpsToMakeNtwrkCntd()
n = 11
connections = [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]
print("Total no. of. nodes:", n)
print("No of operations needed to connect the whole network:", instance.makeConnected(n, connections))
# output: 3



            
    
        

        