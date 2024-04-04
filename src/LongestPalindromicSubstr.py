# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class LongestPalindromicSubstr:
    def longestPalindrome(self, s: str) -> str:
        # Logic:
        # Odd len string:
        # 1. Treat every char as pivot val and expand in both left and right direction.
        # 2. If chars at left and right positions match expand further else move to next char as pivot
        # 3. For every match at left and right positions update longest sub string and its length
        
        # Even len String:
        # 1. we don't keep a pivot instead we keep left - right chars pair
        # 2. keep the expansion logic same as odd one

        # needt to run for both odd and even scenarions so no if:else

        self.strRes = ""
        self.lenStrRes = 0
           
        for i in range(len(s)):
            # odd length s:
                left = right = i
                self.helper(s, left, right)
            # even length s:
                left, right = i, i + 1
                self.helper(s, left, right)

        return self.strRes
    
    def helper(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            if right - left + 1 > self.lenStrRes:
                self.strRes = s[left : right + 1]
                self.lenStrRes = right - left + 1
            left -= 1
            right += 1

# Complexity: 
# T: O(N^2)
# S: O(1)


# Testing:
instance = LongestPalindromicSubstr()
s = "babad"
print("The longest palindromic substring in the give string \"",s,"\" is:", instance.longestPalindrome(s))
# Output: "bab"

            

        
            



                
