class Nuberof1Bits:
# 	191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

# Write a function that takes the binary representation of an unsigned integer and 
# returns the number of '1' bits it has (also known as the Hamming weight).

# Example 1:

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

    def hammingWeight(self, n: int) -> int:
      count = 0
      while n:
		# using left shift (strictly O(logN))
        # count += n & 1 #This checks if last bit is 1 or 0
        # n = n >> 1 #This shits the bits to the right
		# OR
		# counts only 1s (worst case O(logN), best case O(1))
        n &= n - 1 
        count += 1
      return count

# Testing
instance = Nuberof1Bits()
n = 55
print("No of 1 bits in", n, "is: ",instance.hammingWeight(55))