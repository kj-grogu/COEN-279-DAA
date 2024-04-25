# 1328. Break a Palindrome
# https://leetcode.com/problems/break-a-palindrome/

# Given a palindromic string of lowercase English letters palindrome, 
# replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome 
# and that it is the lexicographically smallest one possible.
# Return the resulting string. If there is no way to replace a character to make it not a palindrome, 
# return an empty string.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a 
# and b differ, a has a character strictly smaller than the corresponding character in b. 
# For example, "abcc" is lexicographically smaller than "abcd" 
# because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

# Example 1:
# Input: palindrome = "abccba"
# Output: "aaccba"
# Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
# Of all the ways, "aaccba" is the lexicographically smallest.

# Example 2:
# Input: palindrome = "a"
# Output: ""
# Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
 
# Constraints:
# 1 <= palindrome.length <= 1000
# palindrome consists of only lowercase English letters.

class BreakPalindrome:
    def breakPalindrome(self, palindrome: str) -> str:
        # 1. base case: if 1 or less chars in palindrome string:
        if len(palindrome) < 2:
            return ""

        # 2. If the str is of odd len -> then need to convert a non 'a' char to 'a' till mid
        mid = len(palindrome) // 2
        chars = list(palindrome)
        for i in range(mid):
            if chars[i] != 'a':
                chars[i] = 'a'
                return "".join(chars)

        # 3. If not returned yet then all chars are 'a' so we just convert last 'a' to 'b'
        chars[-1] = 'b'
        return "".join(chars)

# Complexity:
# T: O(N); Converting the string to a list of chars, is O(n) since it involves copying each char
# S: O(N); Converting the string to a list of chars

# Testing:
instance = BreakPalindrome()
palindrome = "abccba"
print("Given palindrome string is:", palindrome)
print("The lexicographically smaller non palindromic string after replacing a char from the plaindrome is:", 
      instance.breakPalindrome(palindrome))
# Output: "aaccba"
