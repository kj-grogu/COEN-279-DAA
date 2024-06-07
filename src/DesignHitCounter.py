# 362. Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/

# logic video:
# https://www.youtube.com/watch?v=MKihMUdG3O8

# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
# Your system should accept a timestamp parameter (in seconds granularity), 
# and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). 
# Several hits may arrive roughly at the same time.
# Implement the HitCounter class:
# HitCounter() Initializes the object of the hit counter system.
# void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
# int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 
# Example 1:
# Input
# ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
# [[], [1], [2], [3], [4], [300], [300], [301]]
# Output
# [null, null, null, null, 3, null, 4, 3]

# Explanation
# HitCounter hitCounter = new HitCounter();
# hitCounter.hit(1);       // hit at timestamp 1.
# hitCounter.hit(2);       // hit at timestamp 2.
# hitCounter.hit(3);       // hit at timestamp 3.
# hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
# hitCounter.hit(300);     // hit at timestamp 300.
# hitCounter.getHits(300); // get hits at timestamp 300, return 4.
# hitCounter.getHits(301); // get hits at timestamp 301, return 3.
 
# Constraints:
# 1 <= timestamp <= 2 * 109
# All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
# At most 300 calls will be made to hit and getHits.
# Follow up: What if the number of hits per second could be huge? Does your design scale?

class HitCounter:

    def __init__(self):
        # Initialize an empty list to store hit timestamps
        self.hits = []

    def hit(self, timestamp: int) -> None:
        # Record a hit by appending the timestamp to the hits list
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Initialize pointers for binary search
        left = 0
        right = len(self.hits) - 1

        # Calculate the target timestamp, which is 5 minutes (300 seconds) before the given timestamp
        target = timestamp - 300

        # Perform binary search to find the first hit that is within the last 5 minutes
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the mid-point

            if self.hits[mid] <= target:  # Check if mid-point timestamp is older than 5 minutes
                left = mid + 1  # Move the left pointer to the right of mid
            else:
                right = mid - 1  # Move the right pointer to the left of mid

        # The number of hits in the last 5 minutes is the length of hits minus the index of the first valid hit
        return len(self.hits) - left

# Complexity:
# Time Complexity:
# - hit method: O(1), as appending to a list is an O(1) operation.
# - getHits method: O(log N), where N is the number of hits, due to binary search.
#
# Space Complexity: O(N), where N is the number of hits stored in the list.


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
    
# Testing:
instance = HitCounter()
input = ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
params = [[], [1], [2], [3], [4], [300], [300], [301]]

for i in range(len(input)):
    if input[i] == "hit":
        print("encountered an hit for timestamp", params[i][0], "append it to the list:", instance.hit(params[i][0]))
    if input[i] == "getHits":
        print("get hits for timestamp", params[i][0], ":", instance.getHits(params[i][0]))
    

# Output
# [null, null, null, null, 3, null, 4, 3]