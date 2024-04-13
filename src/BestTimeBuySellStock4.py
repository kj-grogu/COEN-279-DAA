# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# Example 2:
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 
# Constraints:
# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class BestTimeBuySellStock4:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # case 1: if k == 0 or n <= 1
        if k == 0 or n <= 1:
            return 0
        
        # case 2: if k >= n
        if 2 * k >= n:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i-1]
            return res

        # case 3: 1 <= k < n:
        dp = [0] * (2 * k)
        dp[0] = -prices[0]
        for i in range(1, 2 * k):
            if i % 2: # Sell
                dp[i] = 0
            else: # Buy
                dp[i] = float('-inf')

        for i in range(n):
            for j in range(2 * k):
                if j == 0:
                    dp[j] = max(dp[j], -prices[i])
                elif j % 2: # sell
                    dp[j] = max(dp[j], dp[j - 1] + prices[i])
                else: # Buy
                    dp[j] = max(dp[j], dp[j - 1] - prices[i])

        return dp[2 * k - 1]

# Complexity:
# T: O(K * N)
# S: O(K)
    
# Testing:
instance = BestTimeBuySellStock4()
k = 2
prices = [3,2,6,5,0,3]
print("Given list of prices of stock are:", prices, "and limit of transaction to maximize profit is:", k)
print("Total profit accumulated by buying and selling of stocks is:", instance.maxProfit(k, prices))
# Output: 7

                

