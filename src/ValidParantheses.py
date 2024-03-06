# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false
 

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

from typing import List
from typing import Optional

# class ValidParantheses:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for char in s:
#             if char == '(' or char == '{' or char == '[':
#                 stack.append(char)
#             elif (stack and 
#             ((char == ')' and stack.pop() == '(') or 
#             (char == '}' and stack.pop() == '{') or 
#             (char == ']' and stack.pop() == '['))) :
#                  continue
#             else:
#                 return False

#         return not stack
# or:
class ValidParantheses:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
    
# Complexity:
# T: O(N), where N is length of s
# S: O(N), where N is length of s
    
# Testing:
instance = ValidParantheses()
s1 = "()[]{}"
s2 = "]"
print("Does the string ", s1, " contains correct order and no. of parantheses: ", instance.isValid(s1))
print("Does the string ", s2, " contains correct order and no. of parantheses: ", instance.isValid(s2))
