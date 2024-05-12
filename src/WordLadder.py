# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/
# A transformation sequence from word beginWord to word endWord using a dictionary, 
# wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, 
# return the number of words in the shortest transformation sequence from beginWord to endWord, 
# or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# Constraints:
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

import collections
from typing import List

class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or not wordList or endWord not in wordList:
            return 0

        word_graph = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                transform_key = word[:i] + "*" + word[i+1:]
                word_graph[transform_key].append(word)

        # creating a list queue which takes in a tuple as an element
        queue = collections.deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, path_len = queue.popleft()
            visited.add(word)

            if word == endWord:
                return path_len

            for i in range(len(word)):
                transformed = word[:i] + "*" + word[i+1:]
                # if list with words present then return the list else return None, so have to do get
                # as we created a defaultDict
                potential_words = word_graph.get(transformed, None)
                if potential_words:
                    for p_word in potential_words:
                        if p_word not in visited:
                            queue.append((p_word, path_len + 1))

        return 0

# Complexity:
# T: O(M * N), where M is the length of each word in the wordList 
#               and N is the total number of words in the wordList
# S: O(M * N)

# Testing:
instance = WordLadder()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print("Begin word:", beginWord, "and the", "End word:", endWord)
print("Given WordList:", wordList)
print("Steps taken to reach", endWord,"from", beginWord, 
      "by traverting through wodlist are:", instance.ladderLength(beginWord, endWord, wordList))
# Output: 5


        