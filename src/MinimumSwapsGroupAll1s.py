# 1151. Minimum Swaps to Group All 1's Together
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

# Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

# Example 1:
# Input: data = [1,0,1,0,1]
# Output: 1
# Explanation: There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1.

# Example 2:
# Input: data = [0,0,0,1,0]
# Output: 0
# Explanation: Since there is only one 1 in the array, no swaps are needed.

# Example 3:
# Input: data = [1,0,1,0,1,0,0,1,1,0,1]
# Output: 3
# Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
 
# Constraints:
# 1 <= data.length <= 105
# data[i] is either 0 or 1.

# given data: [1,0,1,0,1], n = len(data) = 5
# sum_1s = 3
# sliding windows:
# [1, 0, 1] ; cur_sum = 2; max_sum = 2; i = None (initially)
# [X, 0, 1, 0] ; cur_sum = 1; max_sum = 2; i = 3
# [X, X, 1, 0, 1] ; cur_sum = 2; max_sum = 2; i = 4

# min_swaps = sum_1s - max_sum = 3 - 2 = 1

from typing import List
class MinimumSwapsGroupAll1s:
    # Function to find the minimum number of swaps to group all 1's together in the binary array
    def minSwaps(self, data: List[int]) -> int:
        # Calculate the total number of 1's in the array
        sum_1s = sum(data)
        # Get the length of the input array
        n = len(data)

        # Calculate the sum of the first 'sum_1s' elements (initial window)
        cur_sum = sum(data[:sum_1s])
        # Initialize max_sum with the current sum of the window
        max_sum = cur_sum

        # Iterate through the array starting from 'sum_1s' to the end
        for i in range(sum_1s, n):
            # Update the current window sum by adding the next element and subtracting the element that is sliding out
            cur_sum += data[i] - data[i - sum_1s]
            # Update the max_sum if the current window sum is greater
            max_sum = max(max_sum, cur_sum)
        
        # The minimum number of swaps required is the difference between the total number of 1's and the max_sum
        return sum_1s - max_sum

# Time Complexity: O(N)
# - The algorithm iterates over the input list data twice.
# - The initial sum calculation is O(sum_1s), and the sliding window iteration is O(N - sum_1s), resulting in O(N) time complexity.

# Space Complexity: O(1)
# - The space complexity is constant because no additional data structures proportional to the input size are used.
# - Only a few variables are used for calculations.
    
# Testing:
instance = MinimumSwapsGroupAll1s()
data = [1,0,1,0,1,0,0,1,1,0,1]
print("Given stream of data is:", data)
print("No. of swaps taken to club all 1s togather:", instance.minSwaps(data))
# Output: 3
