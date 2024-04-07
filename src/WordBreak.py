# 139. Word Break
# https://leetcode.com/problems/word-break/
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 
# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 1. create a DP cache of len same as len of s and default to false
        DP = [False] * (len(s) + 1)
        # Default the DP of its last index to True, so that it can serve as base for previous indexes
        DP[len(s)] = True

        # iterate over all the chars in s to calc their DP val from reverse
        for i in range(len(s) - 1, -1, -1):
            # go throuh each word in wordDict matching it's chars from i to len(word) to update the DP
            for w in wordDict:
                w_len = len(w)
                if((i + w_len) <= len(s) and s[i : i + w_len] == w):
                    DP[i] = DP[i + w_len]
                # no need to match with other words if already true
                if DP[i]:
                    break
        
        return DP[0] # if True, meaning all chars can be exausted with a combinations of words in wordDict

# Complexity:
# T: O(N * M), N = len(s), M = len(wordDict)
# S: O(N), size of DP

        
# Testing:
instance = WordBreak()
s = "leetcode"
wordDict = ["leet","code"]
print("Given string and word dictionary are: ", "String ->",s,"| Word Dictionary ->", wordDict)
print(s, "can be segmented into a space-separated sequence of one or more dictionary words:", instance.wordBreak(s, wordDict))
# Output: true