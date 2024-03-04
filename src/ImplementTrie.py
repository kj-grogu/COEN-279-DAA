# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store 
# and retrieve keys in a dataset of strings. There are various applications of this data structure, 
# such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), 
# and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, 
# and false otherwise.
 

# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {} #
        self.isLast = False

class Trie:

    def __init__(self):
        self.trie = TrieNode("#")
        

    def insert(self, word: str) -> None:
        root = self.trie

        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]

        root.isLast = True

    def search(self, word: str) -> bool:
        root = self.trie

        for char in word:
            if char in root.children:
                root = root.children[char]
            else:
                return False

        return root.isLast     

    def startsWith(self, prefix: str) -> bool:
        root = self.trie

        for char in prefix:
            if char in root.children:
                root = root.children[char]
            else:
                return False
        
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Complexity:
# Time:
# Insert -> O(C), where C is the no. of chars in the word
# Search -> O(C), where C is the no. of chars in the word
# startsWith -> O(C), where C is no. of chars in the prefix

# Space:
# O(C), where C is the no. of chars in the word
    
# Testing:
instance = Trie()
input_l1 = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
input_l2 = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

for i in range(len(input_l1)):
    if input_l1[i] == "insert":
        print("Inserted ", input_l2[i][0], " into the trie", instance.insert(input_l2[i][0]))
    if input_l1[i] == "search":
        print("Search for word \"", input_l2[i][0], "\" into the trie resulted in: ", instance.search(input_l2[i][0]))
    if input_l1[i] == "startsWith":
        print("Search for word starting with \"", input_l2[i][0], "\" into the trie resulted in: ", instance.startsWith(input_l2[i][0]))
    
        