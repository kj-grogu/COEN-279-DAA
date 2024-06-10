# 2405. Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/

# logic video:
# https://www.youtube.com/watch?v=CKZPdiXiQf0

# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
# That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.

# Example 1:
# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.

# Example 2:
# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").

# Constraints:
# 1 <= s.length <= 105
# s consists of only English lowercase letters.

class OptimalPartitionString:
    def partitionString(self, s: str) -> int:
        # Check if the input string is empty. If so, return 0 because there are no substrings to partition.
        if not s:
            return 0

        # Initialize an empty set to keep track of characters in the current substring.
        curSet = set()
        # Initialize the result counter to 1 because we need at least one partition.
        res = 1

        # Iterate through each character in the input string.
        for c in s:
            # If the character is already in the current set, it means we need to start a new partition.
            if c in curSet:
                # Increment the partition count.
                res += 1
                # Reset the current set for the new partition.
                curSet = set()

            # Add the current character to the current set.
            curSet.add(c)

        # Return the total number of partitions needed.
        return res

# Complexity:
# T: O(N) where N is the length of the string. Each character is processed once.
# S: O(K) where K is the number of unique characters in the string. In the worst case, this can be O(26) if all characters are unique.
    
# Testing:
instance = OptimalPartitionString()
s = "abacaba"
print("The given string is:", s)
print("No of substrings in", s, "with unique characters after optimal partition are:", instance.partitionString(s))
# Output: 4


        