from ast import List
from typing import List
from collections import deque

class WallsAndGates:
# 286. Walls and Gates
# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example 1:
# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Example 2:
# Input: rooms = [[-1]]
# Output: [[-1]]
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        """
        step 1: declare / initialize the rows/clos length, queue for BFS and visited set for BFS.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()
            
        def addRoom(r, c):
            """
            def: to add next layer of empty rooms to the queue and visited set for the processing in next iteration.
            """
            if(r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or rooms[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])

        """
        step 2: append / add the cells which have a gate to the the queue and visited set.
        """
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
            
        """
        step 3: declare the distance variable to simulateneously visit all gates at once an then calculate distance of cells from those gates at every layer.
        """
        dist = 0
            
        """
        step 4: go through every layer of cells at incremental distances from gates and put in their distances.
        """
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r+1, c)
                addRoom(r, c+1)
                addRoom(r-1, c)
                addRoom(r, c-1)
            dist += 1

# Testing
instance = WallsAndGates()
rooms = [[2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]

print("Rooms: ")
for i in rooms:
    print('\t'.join(map(str, i)))

print("Gate distances from empty rooms are: ")

instance.wallsAndGates(rooms)

for i in rooms:
    print('\t'.join(map(str, i)))