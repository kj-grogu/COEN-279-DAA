from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        sum_k = sum(data)
        n = len(data)

        # Calculate the sum of the first window of size `sum_k`
        cur_sum = sum(data[:sum_k])
        max_sum = cur_sum

        # Sliding window to find the maximum number of 1s in any window of size `sum_k`
        for i in range(sum_k, n):
            cur_sum += data[i] - data[i - sum_k]
            max_sum = max(max_sum, cur_sum)

        # The minimum number of swaps needed is the size of the window minus the maximum number of 1s found
        return sum_k - max_sum

# Time Complexity:

# 	•	sum_k Calculation: O(n) to calculate the total number of 1s.
# 	•	Initial Window Sum: O(sum_k) to calculate the sum of the first window.
# 	•	Sliding Window: O(n - sum_k) to slide the window from sum_k to n.

# The overall time complexity is O(n), ensuring the function runs efficiently even for large inputs.