# 1359. Count All Valid Pickup and Delivery Options
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

# logic video:
# https://www.youtube.com/watch?v=OpgslsirW8s

# Given n orders, each order consists of a pickup and a delivery service.
# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
# Since the answer may be too large, return it modulo 10^9 + 7.

# Example 1:
# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

# Example 2:
# Input: n = 2
# Output: 6
# Explanation: All possible orders: 
# (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
# This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
# Example 3:

# Input: n = 3
# Output: 90

# Constraints:
# 1 <= n <= 500

class CntAllValidPickupDeliveryOptions:
    def countOrders(self, n: int) -> int:
        # Calculate total number of slots needed (2 per order: 1 for pickup, 1 for delivery)
        slots = 2 * n
        
        # Initial result is 1 because for 1 order there's only 1 way to arrange pickup and delivery
        res = 1
        
        # Use a large prime number as modulus to prevent overflow in calculations
        mod = pow(10, 9) + 7
        
        # Loop until all slots are arranged
        while slots > 0:
            # Calculate the number of valid ways to arrange the next pair of pickup and delivery
            # (slots - 1) options for delivery after a pickup (ignoring invalid permutations where delivery is before pickup)
            valid_order = ((slots * (slots - 1)) // 2)  # Divide by 2 to get combinations of arranging two slots
            
            # Update result by multiplying with the number of valid ways for the current pair and taking modulus
            res = (res * valid_order) % mod
            
            # Move to the next order by reducing two slots (one pickup and one delivery)
            slots -= 2
        
        return res

# Complexity:
# Time Complexity (T): O(n)
# The time complexity is linear in terms of the number of orders, n, because the while loop iterates n times,
# each iteration corresponding to arranging one pickup and one delivery.

# Space Complexity (S): O(1)
# The space complexity is constant as only a fixed number of variables (slots, res, mod, valid_order) are used,
# independent of the size of the input n.
    
# Testing:
instance = CntAllValidPickupDeliveryOptions()
n = 2
# Output: 6
print("Given orders are:", n)
print("Total valid pickup and delivery options for", n, "orders are:", instance.countOrders(n))

