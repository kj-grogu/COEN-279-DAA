# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

# You are given an array of CPU tasks, each represented by letters A to Z, 
# and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, 
# but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
# ​Return the minimum number of intervals required to complete all tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two cycles before doing A again. The same applies to task B. 
# In the 3rd interval, neither A nor B can be done, so you idle. 
# By the 4th cycle, you can do A again as 2 intervals have passed.

# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. 
# This leads to idling twice between repetitions of these tasks.

# Constraints:
# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100

from collections import Counter, deque
import heapq
from ast import List
from typing import List
from typing import Optional


class TaskScheduler:
     def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a frequency map of tasks
        count = Counter(tasks)

        # create the MaxHeap which is -ve version of MinHeap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # create the queue:
        q = deque()

        time = 0
        # iterate till queue or heap are not empty:
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1  # adding 1 cause using -ve version of min heap as max heap else would have substracted 1
                if cnt:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

# Complexity:
# T: O(N log N), where N is the number of unique tasks.
# S: O(N), Additional space is used to store the frequency map (count)
     
# Testing:
instance = TaskScheduler()
tasks = ["A","A","A","B","B","B"]
n = 2
print("time of completion for the provided taks ", tasks, "with ", n, " intervals is: ", instance.leastInterval(tasks, n))