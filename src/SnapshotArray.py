# 1146. Snapshot Array
# https://leetcode.com/problems/snapshot-array/

# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length. 
# Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

# Example 1:
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 
# Constraints:
# 1 <= length <= 5 * 104
# 0 <= index < length
# 0 <= val <= 109
# 0 <= snap_id < (the total number of times we call snap())
# At most 5 * 104 calls will be made to set, snap, and get.

from ast import List
import collections
from typing import List

class SnapshotArray:
        # create a 2d list of length 
        # and initialize internal list representing all the snapshots vs their vals for this index, 
        # with a tupule of (snapshotId, value)
    def __init__(self, length: int):
        self.snapshots_2d = [[(0,0)] for _ in range(length)]
        self.snapId = 0
        

    def set(self, index: int, val: int):
        self.snapshots_2d[index].append((self.snapId, val))
        
    def snap(self) -> int:
        self.snapId += 1
        # -1 cause we need to return the current snapshot id and increment it
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        temp = self.snapshots_2d[index]
        l, r = 0, len(temp) - 1
        mid = 0
        # understand this binary search logic
        while l <= r:
            mid = l + (r - l) // 2
            # below code because, its not necessary that given snap_id exits in list so we need to return the 
            # most closest lesser snap id to the given one.
            if temp[mid][0] <= snap_id:
                l = mid + 1
            else:
                r = mid - 1
        
        return temp[r][1]

# Complexity:
# T: O(lg N)
# S: O(M), where M is the total number of tuples stored across all lists in self.snapshots_2d. 

# Testing:
funcs = ["SnapshotArray","set","snap","set","get"]
params = [[3],[0,5],[],[0,6],[0,0]]
instance = SnapshotArray(params[0][0])
for i in range(len(funcs)):
    if funcs[i] == "set":
        print("set val", params[i][1], "to index", params[i][0], instance.set(params[i][0], params[i][1]))
    if funcs[i] == "snap":
        print("Take the snapshot of array and return snap Id:", instance.snap())
    if funcs[i] == "get":
        print("The val at snap id", params[i][1], "of index", params[i][0], "is:", instance.get(params[i][0], params[i][1]))
        
# Output: [null,null,0,null,5]

        