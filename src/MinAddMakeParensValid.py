# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Example 1:
# Input: s = "())"
# Output: 1

# Example 2:
# Input: s = "((("
# Output: 3
 
# Constraints:
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.

class MinAddMakeParensValid:
    def minAddToMakeValid(self, s: str) -> int:
        l_count = r_count = added = 0  # Initialize counters for left '(' and right ')' counts and the added parentheses.

        for char in s:  # Iterate through each character in the string.
            if char == "(":  # If the character is an opening parenthesis.
                l_count += 1  # Increment the count of left parentheses.
            else:  # If the character is a closing parenthesis.
                if r_count < l_count:  # If there are unmatched opening parentheses.
                    r_count += 1  # Increment the count of right parentheses.
                else:  # If there are no unmatched opening parentheses to pair with.
                    added += 1  # Increment the count of parentheses to be added.

        # After processing all characters, if there are unmatched opening parentheses left.
        added += l_count - r_count  # Add the difference to account for unmatched left parentheses.

        return added  # Return the total count of added parentheses.

# Complexity:
# Time: O(N) - The function iterates over each character in the string exactly once.
# Space: O(1) - No additional space is used beyond constant extra variables.

# Testing:
instance = MinAddMakeParensValid()
s = "())"
print("The given parantheses string is:", s)
print("The no of parantheses to be added to make the string a valid parantheses is:", instance.minAddToMakeValid(s))
# Output: 1


        