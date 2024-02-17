from ast import List
import heapq
from typing import List


# 1642. Furthest Building You Can Reach
# https://leetcode.com/problems/furthest-building-you-can-reach/

# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

# If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

# Example 1:
# Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# Output: 4

# Example 2:
# Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# Output: 7

# Example 3:
# Input: heights = [14,3,19,3], bricks = 17, ladders = 0
# Output: 3

class FurtherBuildingdsCanReach:
    # logic:
    # 1. firslty we keep track of height difference between building i + 1 to i in diff
    # 2. we greedly keep exhausting the bricks as we move from 1 building to another if diff is greater than zero
    # 3. as we are moving ahead we also keep track of the max diff so far using the max heap
    # 4. if the bricks. become -ve than we check if ladders are available or not
    # 5. if ladders are available we pop the max diff value from the heap and add it to the bricks and decrement the ladders
    # 6. else we return the current index

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff <= 0:
                continue
            
            bricks -= diff
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i
                bricks += (- heapq.heappop(heap))
                ladders -= 1

        return len(heights) - 1

# Complexity:
# T: O(N lg K) where N is the number of buildings and K is the number of ladders available
# S: O(K)
    
# Testing
instance = FurtherBuildingdsCanReach()
heights_1, bricks_1, ladders_1 = [4,2,7,6,9,14,12], 5, 1
heights_2, bricks_2, ladders_2 = [4,12,2,7,3,18,20,3,19], 10, 2
heights_3, bricks_3, ladders_3 = [14,3,19,3], 17, 0


print("The Furthest building we can reach for list: ", heights_1, " with bricks: ", bricks_1, " and ladders: ", ladders_1, " is: ", instance.furthestBuilding(heights_1, bricks_1, ladders_1))

print("The Furthest building we can reach for list: ", heights_2, " with bricks: ", bricks_2, " and ladders: ", ladders_2, " is: ", instance.furthestBuilding(heights_2, bricks_2, ladders_2))

print("The Furthest building we can reach for list: ", heights_3, " with bricks: ", bricks_3, " and ladders: ", ladders_3, " is: ", instance.furthestBuilding(heights_3, bricks_3, ladders_3))

    
        

        
            


        
        