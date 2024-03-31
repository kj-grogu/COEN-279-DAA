# 743. Network Delay Time ####### Djikstra Algo (Single source shortest path) ########
# https://leetcode.com/problems/network-delay-time/

# You are given a network of n nodes, labeled from 1 to n. 
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
# where ui is the source node, vi is the target node, and wi is the time it takes 
# for a signal to travel from source to target.
	
# We will send a signal from a given node k. 
# Return the minimum time it takes for all the n nodes to receive the signal. 
# If it is impossible for all the n nodes to receive the signal, return -1.


# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

# Constraints:
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # step 1:
        # create adjacency list for given nodes in u -> [(v1, w1), (v2, w2)...] format, 
        # where u is current node and v's are the nodes adjacent to it and w's are delays taken to reach v's from u
        adjList = collections.defaultdict(list)
        for u, v, w in times:
           adjList[u].append((v, w))

        # step 2: Djikstra's algorithm
        minHeap = [(0, k)] # minHeap to keep track of shortest path, initialized by (0 => path len to k, k => start node)
        visited = set() # set to keep track of visited nodes
        minPath = 0 # var to keep track of shortest path to all nodes from k

        while minHeap:
            curPath, curNode = heapq.heappop(minHeap)
            if curNode in visited:
                continue
            visited.add(curNode)
            minPath = max(minPath, curPath) # doing max cause curPath is a sum of all node's shortes path till curNode
            # Now doing BFS logic, appending all neighbors of curNode to heap
            for nei, neiW in adjList[curNode]:
                if nei not in visited:
                    heapq.heappush(minHeap, (curPath + neiW, nei))
        
        # return shortest path if all nodes reached else -1
        return minPath if len(visited) == n else -1

# Complexity:
# T: O(E log V) here E at max is V^2
# S: O(V^2) or O(E) space taken by adjacency list
    
# Testing
instance = NetworkDelayTime()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4 # no. of nodes
k = 2 # start node
# Output: 2

print("Given nodes with their connections and weight to their connections are: ")
for u, v, w in times:
    print("Node ->", u, "connected to ->", v, "with weight ->", w)

print("Length of shortest path to reach all nodes from node", k, "is:",  instance.networkDelayTime(times, n, k)) 





         
        

