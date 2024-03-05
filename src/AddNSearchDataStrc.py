# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
# word may contain dots '.' where dots can be matched with any letter.
 

# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode("#")
        

    def addWord(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]

        cur.isLast = True
        
    def search(self, word: str) -> bool:
        return self.dfs(0, self.trie, word)
    
    def dfs(self, i, cur, word):
        for j in range(i, len(word)):
            char = word[j]
            if char == ".":
                for child in cur.children.values():
                    # Process all the child nodes in the value list of current char map
                    if self.dfs(j + 1, child, word):
                        # Return True as one possible path found
                        return True
                # If processed all the child nodes in current char node's values and haven't returned true so far the return false 
                return False
            # For the case where the ith char of search word is not wild card
            else:
                if char not in cur.children:
                    return False
                cur = cur.children[char]
        return cur.isLast

# Complexity:
# Time:
# addWord: O(N), where N is the length of the word being added.
# search: Up to O(2^N) for searches with wildcards, due to the potential to explore every path in the Trie.
# Space:
# O(C), where C is the total number of characters in all words added to the WordDictionary.
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
    

# Testing:
instance = WordDictionary()
input_l1 = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
input_l2 = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]

for i in range(len(input_l1)):
    if input_l1[i] == "addWord":
        print("Added ", input_l2[i][0], " into the trie", instance.addWord(input_l2[i][0]))
    if input_l1[i] == "search":
        print("Search for word \"", input_l2[i][0], "\" into the trie resulted in: ", instance.search(input_l2[i][0]))
    