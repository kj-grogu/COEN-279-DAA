# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 
# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 
# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

from ast import List
import collections
from typing import List

class ReverseWordsInStr:
    def reverseWords(self, s: str) -> str:
        # taking a queue so that we can append to its left and save an extra step of reversing
        string_builder = collections.deque()
        start = -1
        i = 0
        while i < len(s):
            # check for space before is must:
            if s[i] != " ":
                start = i
                while i < len(s) and s[i] != " ":
                    i += 1
                # Appending to left to get the reverse order
                string_builder.appendleft(s[start : i])
                i -= 1 # As we want to go back 1 char before the start of new sub str 
                # which line 10 would have gone ahead to cause we increase i at the end as well for while loop
            i += 1
        return " ".join(string_builder)

# Complexity:
# T: O(N)
# S: O(N)

# Testing:
instance = ReverseWordsInStr()
s = "the sky is blue"
print("Given sentence is:", s)
print("Reverse of the sentence is:", instance.reverseWords(s))
# Output: "blue is sky the"

        

