# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
 
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from ast import List
import collections
from typing import List

class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create map of (char index - count) hash to words 
        anaList = collections.defaultdict(list)

        # 2. Go over all the words:
        for word in strs:
            # 3. create a hash (count of chars for all chars in word based on all lower case)
            charCountArr = [0] * 26
            for char in word:
                charCountArr[ord(char) - ord('a')] += 1

            # 4. use this hash as key and add all words with same hash as values to map
            anaList[tuple(charCountArr)].append(word)

        # 5. Return the list of words to particular hashes in from values of map
        return anaList.values()

# Complexity:
# T: O(N * K)
# S: O(N)

# Testing:
instance = GroupAnagrams()
strs = ["eat","tea","tan","ate","nat","bat"]
print("Given list of strings:", strs)
print("Group of all anagrams with same charset are:", instance.groupAnagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


        