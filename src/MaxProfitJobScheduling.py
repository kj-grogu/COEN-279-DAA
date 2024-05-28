# 1235. Maximum Profit in Job Scheduling

# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Logic: https://www.youtube.com/watch?v=JLoWc3v0SiE

# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, 
# return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

# Example 1:
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

# Example 2:
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job. 
# Profit obtained 150 = 20 + 70 + 60.
# Example 3:



# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6

# Constraints:
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 104
# 1 <= startTime[i] < endTime[i] <= 109
# 1 <= profit[i] <= 104

import bisect
from typing import List

class MaxProfitJobScheduling:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine start time, end time, and profit into one list and sort by start time
        intervals = sorted(zip(startTime, endTime, profit))
        
        # Use a dictionary to memoize results of recursive calls to avoid recomputation
        cache = {}

        def dfs(i):
            # Base case: If index i reaches the length of intervals, no more profit can be made
            if i == len(intervals):
                return 0
            # Return cached result if we have computed dfs(i) before
            if i in cache:
                return cache[i]
            
            # Option 1: Do not include the current interval in the profit calculation
            profit = dfs(i + 1)

            # Option 2: Include the current interval in the profit calculation
            # Find the next non-overlapping job using binary search
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            # Store the maximum profit obtained by either including or not including the current job
            cache[i] = max(profit, intervals[i][2] + dfs(j))

            return cache[i]
        
        # Start the DFS from the first interval
        return dfs(0)

# Complexity:
# Time Complexity (T): O(n log n)
# This complexity arises because of the initial sort operation which is O(n log n) and the binary search 
# inside the DFS, which is O(log n) per job. With memoization, each job is processed once, leading to an O(n log n) overall.
#
# Space Complexity (S): O(n)
# The space complexity primarily comes from the recursion stack and the cache storage. In the worst case, 
# the depth of the recursive call stack and the size of the cache can grow up to O(n), where n is the number of jobs.
    
# Testing:
instance = MaxProfitJobScheduling()
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

print("The given job intervals are:")
print("StartTime\t", "EndTime\t", "Profit")
for i in range(len(startTime)):
    print(startTime[i], "\t\t", endTime[i], "\t\t", profit[i])

print("Maximum profit accumulated from above intervals is:", instance.jobScheduling(startTime, endTime, profit))
# Output: 150






        