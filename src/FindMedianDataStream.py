# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
# The median is the middle value in an ordered integer list. 
# If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. 
# Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:
# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
 

# Follow up:
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class MedianFinder:

    def __init__(self):
        # This the max heap to store all the smaller half of the elements from the data stream
        # This will store elements in -ve form as max heap here is -ve implementation of min heap
        self.smaller = []
        # This is a min heap to store all the larger half of the elements of the data stream
        self.larger = []
        

    def addNum(self, num: int) -> None:
        if len(self.smaller) == len(self.larger):
            # adding and balancing of elements on to the two heaps
            # heapq.heappushpop:
            # Step 1: first push the -ve of num on the smaller heap, -ve cause min heap used as max heap, smaller heap gets balanced internally
            # Step 2: then we pop from the smaller(max heap) that is the largest -ve val from heap
            # heappush:
            # Step 3: Then we push the +ve version of the popped val on to the larger(min heap) 
            heapq.heappush(self.larger, - heapq.heappushpop(self.smaller, -num))
        else:
            # adding and balancing of elements on to the two heaps
            # heapq.heappushpop:
            # Step 1: first push the num on the larger heap, larger heap gets balanced internally
            # Step 2: then we pop from the larger(min heap) that is the smallest val from heap
            # heappush:
            # Step 3: Then we push the -ve version of the popped val on to the smaller(max heap) 
            heapq.heappush(self.smaller, - heapq.heappushpop(self.larger, num))

        

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.larger):
            # The -ve sign in front od self.smaller heap is there cause all vals in smaller heap are stored as -ve vals 
            # and need to converted back to original form by applying the -ve sign again
            return float(( - self.smaller[0]) + self.larger[0]) / 2.0
        else:
            return float(self.larger[0])
        
# Complexity:
# addNum:
# T: O(lg N)  The time complexity is logarithmic, as it involves heap operations (heappushpop and heappush), which have logarithmic time complexity.
# S: O((N // 2) - 1) + O(N) => O(N) it involves storing all the elements in the two heaps, which can have a maximum of 'n' elements.

# findMedian:
# T: O(1)
# S: O(1)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        
# Testing:
instance = MedianFinder()
funcs = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
params = [[], [1], [2], [], [3], []]
for i  in range(len(funcs)):
    if funcs[i] == "addNum":
        print("added num", params[i][0], "to the stream",instance.addNum(params[i][0]))
    if funcs[i] == "findMedian":
        print("Median of current nums stream is", instance.findMedian())
# output: [null, null, null, 1.5, null, 2.0]