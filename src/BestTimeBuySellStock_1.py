# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

from ast import List
import heapq
from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class BestTimeBuySellStock_1:
    def maxProfit(self, prices: List[int]) -> int:
        purchase_price = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < purchase_price: # Minimising the purchase price
                purchase_price = price
            else: # meaning current price is greater or equal to purchase_price
                # maximizing the profit
                profit = max(profit, price - purchase_price)
        return profit

# Complexity:
# T: O(N)
# S: O(1)

# Testing:
instance = BestTimeBuySellStock_1()
prices = [7,1,5,3,6,4]
print("Given list of prices:", prices)
print("max profit is:", instance.maxProfit(prices))

# Output: 5



        