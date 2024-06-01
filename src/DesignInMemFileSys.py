# 588. Design In-Memory File System
# https://leetcode.com/problems/design-in-memory-file-system/

# Logic video:
# https://www.youtube.com/watch?v=Eb8GRDxyhfI&t=208s

# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

# FileSystem() Initializes the object of the system.
# List<String> ls(String path)
# If path is a file path, returns a list that only contains this file's name.
# If path is a directory path, returns the list of file and directory names in this directory.
# The answer should in lexicographic order.
# void mkdir(String path) Makes a new directory according to the given path. 
# The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
# void addContentToFile(String filePath, String content)
# If filePath does not exist, creates that file containing given content.
# If filePath already exists, appends the given content to original content.
# String readContentFromFile(String filePath) Returns the content in the file at filePath.
 

# Example 1:
# Input
# ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
# [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
# Output
# [null, [], null, null, ["a"], "hello"]

# Explanation
# FileSystem fileSystem = new FileSystem();
# fileSystem.ls("/");                         // return []
# fileSystem.mkdir("/a/b/c");
# fileSystem.addContentToFile("/a/b/c/d", "hello");
# fileSystem.ls("/");                         // return ["a"]
# fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
 

# Constraints:
# 1 <= path.length, filePath.length <= 100
# path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
# You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
# You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
# 1 <= content.length <= 50
# At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.

import bisect
import collections
from typing import List

class FileSystem:

    def __init__(self):
        # Dictionary for directories and their contents
        self.paths = collections.defaultdict(list)
        # Dictionary for files and their contents
        self.files = collections.defaultdict(str)
        
    def ls(self, path: str) -> List[str]:
        # If the path is a file, return the file name
        if path in self.files:
            return [path.split("/")[-1]]
        # Otherwise, return the list of files/directories in the given path
        else:
            return self.paths[path]

    def mkdir(self, path: str) -> None:
        directories = path.split("/")
        # Create each part of the directory path if not already exists
        for i in range(1, len(directories)):
            curDirPath = "/".join(directories[:i]) or "/"
            # Insert directory in a sorted manner if not already present
            if curDirPath not in self.paths or directories[i] not in self.paths[curDirPath]:
                bisect.insort(self.paths[curDirPath], directories[i])

    def addContentToFile(self, filePath: str, content: str) -> None:
        # If file does not exist, create the path first
        if filePath not in self.files:
            self.mkdir(filePath) 
        # Append content to the file
        self.files[filePath] += content
        
    def readContentFromFile(self, filePath: str) -> str:
        # Return the content of the file
        return self.files[filePath]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath, content)
# param_4 = obj.readContentFromFile(filePath)

# Complexity:
# Time Complexity:
# - `ls` function: O(k log k) where k is the number of items in the directory, due to sorting.
# - `mkdir` function: O(m log n) per directory insertion where m is the number of path segments and n is the number of directories in the parent directory.
# - `insert_sorted` function: O(log n) for finding the position and O(n) for insertion, leading to an overall O(n) complexity.
# - `addContentToFile` and `readContentFromFile` functions: O(1) for dictionary operations.

# Space Complexity:
# - The space complexity is O(p + f) where p is the total number of paths stored and f is the total content size of files.

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath, content)
# param_4 = obj.readContentFromFile(filePath)

# Complexity:
# Time Complexity:
# - `ls` function: O(k log k) where k is the number of items in the directory, due to sorting.
# - `mkdir` function: O(m log n) per directory insertion where m is the number of path segments and n is the number of directories in the parent directory.
# - `insert_sorted` function: O(log n) for finding the position and O(n) for insertion, leading to an overall O(n) complexity.
# - `addContentToFile` and `readContentFromFile` functions: O(1) for dictionary operations.

# Space Complexity:
# - The space complexity is O(p + f) where p is the total number of paths stored and f is the total content size of files.
    
# Testing:
instance = FileSystem()
input = ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
params = [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]

for i in range(len(input)):
    if input[i] == "ls":
        print("Output of ls command:", instance.ls(params[i][0]))
    if input[i] == "mkdir":
        print("Output of mkdir command:", instance.mkdir(params[i][0]))
    if input[i] == "addContentToFile":
        print("Content", params[i][1], "added to file", params[i][0], instance.addContentToFile(params[i][0], params[i][1]))
    if input[i] == "readContentFromFile":
        print("Content from file", params[i][0], "is:", instance.readContentFromFile(params[i][0]))


