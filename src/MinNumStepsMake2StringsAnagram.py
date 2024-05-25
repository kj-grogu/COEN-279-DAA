# 1347. Minimum Number of Steps to Make Two Strings Anagram
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# Example 1:
# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

# Example 2:
# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

# Example 3:
# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams. 

# Constraints:
# 1 <= s.length <= 5 * 104
# s.length == t.length
# s and t consist of lowercase English letters only.

class MinNumStepsMake2StringsAnagram:
    def minSteps(self, s: str, t: str) -> int:
        # Initialize two frequency arrays with zeros for each letter of the alphabet
        s_freq_hash = [0] * 26
        t_freq_hash = [0] * 26

        # Iterate over the length of strings s and t (assuming they are of equal length)
        for i in range(len(s)):
            # Increment the position in s_freq_hash corresponding to the character in s
            s_freq_hash[ord(s[i]) - ord('a')] += 1
            # Increment the position in t_freq_hash corresponding to the character in t
            t_freq_hash[ord(t[i]) - ord('a')] += 1

        # Initialize a result counter
        res = 0

        # Compare the frequency arrays and sum the absolute differences
        for i in range(26):
            # Sum the absolute difference between frequencies of each character
            res += abs(s_freq_hash[i] - t_freq_hash[i])

        # Divide the result by 2 to account for double counting differences in adjustments
        return res // 2

# Complexity:
# T: O(N), length of the strings, as its same for both
# S: O(1), 26 for each hash

# Testing:
instance = MinNumStepsMake2StringsAnagram()
s = "leetcode"
t = "practice"
print("Given strings s:", s, "and t:", t)
print("Minimum steps to convet string", t, "to an anagram of", s, "are:", instance.minSteps(s,t))
# Output: 5


        