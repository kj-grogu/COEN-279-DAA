# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class LngstSubstrWoutRptngChars:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        pos_dict = {}
        l = res = 0

        for r, char in enumerate(s):
            if char in pos_dict:
                if pos_dict[char] >= l:
                    l = pos_dict[char] + 1
                
            res = max(res, r - l + 1)
            pos_dict[char] = r
        return res

# Complexity:
# T: O(N)
# S: O(min(M,N))
# Space complexity is influenced by the char_pos dictionary storing character positions. 
# In the worst case, it's O(M), but with a limited character set (e.g., ASCII), it's O(min(N, M)), where N is the string length.

# Testing:
instance = LngstSubstrWoutRptngChars()
s = "abcabcbb"
print("Given string is:", s)
print("length of longest non repeating subString is:", instance.lengthOfLongestSubstring(s))
# Output: 3


        