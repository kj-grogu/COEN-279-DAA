# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# There are n cities connected by some number of flights. 
# You are given an array flights where flights[i] = [fromi, toi, pricei] 
# indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
# If there is no such route, return -1.

#  Example 1:
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

# Example 2:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

# Example 3:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

# Constraints:
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class CheapestFlightsWithKStops:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # step 1: declare a prices list to keep track of min prices to reach all nodes from src after each ith iteration where i can go upto k + 1:
        # initialize the prices list for all n nodes to "inf" axcept for src node which will be 0 as its the starting point
        prices = [float("inf")] * n
        prices[src] = 0

        # step 2: run bellman ford Algorithm to calc minimum cost to reach all nodes from src node after k + 1 iteration, k acts levels for BFS
        for i in range(k + 1):
            # 2.1. create temp copy of prices to track min cost to reach all nodes from src for the curent ith iteration
            tempPrices = prices.copy()
            # iterate over all node's vars s -> source, d -> destination, p -> prices
            for s, d, p in flights:
                # if current price to reach node s from src is inf then continue 
                # as we have not explored a route to reach current source s from src so we can't reach current dest d following this path as well
                # meaning if src -> s is X(inf) them src -> s -> d is also X(inf)
                if prices[s] == float("inf"):
                    continue
                # if src -> s is V(non inf int) then src -> s -> d is also V(non inf int), so minimise it by:
                tempPrices[d] = min(tempPrices[d], prices[s] + p)
            # reassign prices to current an min vals to reach all nodes from src by:
            prices = tempPrices
        # return -1 if not path from src to dst is possible with k stops else return the minimum price calculated for the given destination
        return -1 if prices[dst] == float("inf") else prices[dst]

# Complexity:
# T: O(E . k), here E is no. of edges max upto N^2 and k is given no of hops
# S: O(N), no of nodes or Vertices
    
# Testing:
instance = CheapestFlightsWithKStops()
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print("given are the flights with their source, destination and price details: ")
for s, d, p in flights:
    print("Source ->", s, "Destination ->", d, ": Price ->", p)
print("The minimum cost to reach from source", src, "to destination", dst, "with in", k, "stops is:", instance.findCheapestPrice(n, flights, src, dst, k))
# Output: 500