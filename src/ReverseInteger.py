# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed. 
# # If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
 
# Constraints:
# -231 <= x <= 231 - 1


import math


class ReverseInteger:
    def reverse(self, x: int) -> int:
        # integer.MAX_VALUE = 2147483647 (ends with 7)
        # integer.MIN_VALUE = -2147483648 (ends with 8)

        MAX = 2147483647
        MIN = -2147483648
        res = 0

        while x != 0:
            digit = int(math.fmod(x,10))
            x = int(x / 10)

            #check for MAX overflow:
            if(res > MAX // 10 or 
            (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            
            #check for MIN oveflow:
            if(res < MIN // 10 or 
            (res == MIN // 10 and digit <= MIN % 10)):
                return 0

            res = (res * 10) + digit
        return res

# Complexity:
# T: O(lg x)
# S: O(1)


        
