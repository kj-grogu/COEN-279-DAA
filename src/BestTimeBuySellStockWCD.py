# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:
# Input: prices = [1]
# Output: 0
 
# Constraints:
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000


from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class BestTimeBuySellStockWCD:
    def maxProfit(self, prices: List[int]) -> int:
        # State: buying or selling
        # buying: i + 1 (no mandatory cooldown period)
        # selling: i + 2 (mandatory cooldown period)

        # caching map: key => (i, buying) here buying is a boolean, value => [max_profit]
        dp = {}

        def dfs(i, buying):
            # base case1:
            if i >= len(prices):
                return 0
            # base case2:
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # coolDown case:
            cooldown = dfs(i + 1, buying)
            
            # buying case:
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            
            # selling case:
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        
        # at first we are always buying
        return dfs(0, True)

# Complexity:
# The memoization ensures each state (i, buying) is calculated at most once, and there are 2n such states 
# (for each day i, buying can be true or false). 
# Therefore, the total number of operations is linear in terms of the number of days, n.
# T: O(N)
# S: O(N)
    
# Algorithm:

# 1. Define Recursive Function: A function dfs is defined to calculate the maximum profit from day i with the state buying indicating if we are buying or selling.
# 2. Base Cases:
#     2.1. If i is beyond the last day, return 0 since no transactions can be made.
#     2.2. If the current state (i, buying) has already been calculated, return its stored value from dp.
# 3. Cooldown: Calculate the profit of not making any transaction on day i and moving to the next day.
# 4. Buying Case: If in buying state, calculate the profit of buying stock on day i and then selling it later.
# 5. Selling Case: If in selling state, calculate the profit of selling stock on day i and then considering the cooldown.
# 6. Memoization: Store the maximum profit for each state (i, buying) in a dictionary dp to avoid recalculating.
# 7. Return Result: Start the recursion with the first day in buying state and return the maximum profit.

# Testing:
instance = BestTimeBuySellStockWCD()
prices = [1,2,3,0,2]
print("Given prices list is:",prices)
print("maximum profit inccured due to buying and selling of stocks with cooldown period is:", instance.maxProfit(prices))
# Output: 3
        