# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "(*)"
# Output: true

# Example 3:
# Input: s = "(*))"
# Output: true

class ValidParanthesisString:

	def checkValidString(self, s: str) -> bool:
		l_min =l_max = 0

		for c in s:
			if c == "(":
				l_min, l_max = l_min + 1, l_max + 1
			if c == ")":
				l_min, l_max = l_min - 1, l_max - 1
			if c == "*":
				l_min, l_max = l_min - 1, l_max + 1

			if l_max < 0:
				return False
			if l_min < 0:
				l_min = 0
		
		return l_min == 0
	
# Complexity:
# T: O(N)
# S: O(1)
	
# Testing:
instance = ValidParanthesisString()
s1 = "()"
s2 = "(*)"
s3 = "(*))"
s4 = "))*(("

print("The given string \"", s1, "\" is valid or not: ", instance.checkValidString(s1))
print("The given string \"", s2, "\" is valid or not: ", instance.checkValidString(s2))
print("The given string \"", s3, "\" is valid or not: ", instance.checkValidString(s3))
print("The given string \"", s4, "\" is valid or not: ", instance.checkValidString(s4))

	
