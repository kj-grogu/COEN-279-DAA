# 1197. Minimum Knight Moves
# https://leetcode.com/problems/minimum-knight-moves/

# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.


# Example 1:
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]

# Example 2:
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

# Constraints:
# -300 <= x, y <= 300
# 0 <= |x| + |y| <= 300

# directions from (0,0): [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)] -> 8
# tupules params in queue -> (x-co, y-co, steps to reach these co-ordinates)
# tupules params in visited set -> (x-co, y-co)
# Traversing in just quadrant 1st of x-y pane with inclusion of -1 in both x and y co-ords
# can do due to symmetry: the steps to reach abs vals of given (x,y) co-ords in 1st quadrant, 
# will be same as to reach (x,y) in any other quadrant and traversing in just 1 quadrant saves time

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class MinimumKnightMoves:
    def minKnightMoves(self, x: int, y: int) -> int:
        # create a directions list of x,y co-ords the knight can traverse
        directions = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
        
        # queue to do the BFS traversal of the x-y plane
        queue = collections.deque([(0,0,0)])
        
        # track the give co-ords and set of co-ords which are already visited
        x, y, visited = abs(x), abs(y), set([(0,0)])

        # BFS traversal of x-y plane 
        while queue:
            c_x, c_y, step = queue.popleft()
            
            if (c_x, c_y) == (x, y):
                return step
            
            # cond -> (-1 <= c_x + dx <= x + 2): as traversing only 1 quard & can limit serch to x + 2 x-axis cells
            # cond -> (-1 <= c_y + dy <= y + 2): as traversing only 1 quard & can limit serch to y + 2 y-axis cells
            for dx, dy in directions:
                if (c_x + dx, c_y + dy) not in visited and (-1 <= c_x + dx <= x + 2) and (-1 <= c_y + dy <= y + 2):
                    visited.add((c_x + dx, c_y + dy))
                    queue.append((c_x + dx, c_y + dy, step + 1))

# Complexity:
# T: O((x+4)*(y+4))
# S: O((x+4)*(y+4))

# Testing:
instance = MinimumKnightMoves()
x = 5
y = 5
print("given co-ordinate to be reached by the knight:", (x,y))
print("Number of steps taken by the knight to reach these co-ordinates are:", instance.minKnightMoves(x,y))
# Output: 1


