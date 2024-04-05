# 322. Coin Change
# https://leetcode.com/problems/coin-change/
# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Declare a DP list of len amount + 1 and intialize with default val of amount + 1 for all
        # default val -> max coins could be amount * 1 i-e coin 1 amount times
        DP = [amount + 1] * (amount + 1) 
        # Base case of 0:
        DP[0] = 0

        # run a loop from 0 - amount to construct DP:
        for a in range(amount + 1):
            # calc DP[i] from each coin's DP for curr val of i (amount) where coin val is less than or equal to amount
            for c in coins:
                if a - c >= 0:
                    # Add 1 to the minimum coins needed for (amount - current coin), accounting for using this coin
                    DP[a] = min(DP[a], 1 + DP[a - c])
        
        # return DP[amount] if an arrangement found else return -1
        return DP[amount] if DP[amount] != amount + 1 else -1

# Complexity:
# T: O(Amount * N), N here is len of coins
# S: O(Amount + 1)
    
# Testing:
instance = CoinChange()
coins = [1,2,5]
amount = 11
print("Given target amount and list of coins is:", "amount ->",amount,"coins ->", coins)
print("Minimium no of coins needed to form", amount, "is:", instance.coinChange(coins, amount))
# Output: 3





