# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.


# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:
# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.

from ast import List
import collections
from typing import Counter, List

class SortCharsByFrequency:
    def frequencySort(self, s: str) -> str:
        # step 1: create a char to frequency map for all chars in s
        count = Counter(s) # char -> frequency in s
        buckets = collections.defaultdict(list) # frequency to chars

        # step 2: put chars against the frequeny bucket they occur in
        for c, freq in count.items():
            buckets[freq].append(c)
        
        # step 3: create the string starting with char with most freq to least,
        # appending them as many times as there freq
        res = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)
        
        return "".join(res)

# Complexity:
# T: O(N)
# S: O(N)

# Testing:
instance = SortCharsByFrequency()
s = "tree"
print("Given string is:", s)
print("given string sorted in order of its chars frequencies is:", instance.frequencySort(s))
# Output: "eert"



        