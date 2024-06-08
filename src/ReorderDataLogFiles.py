# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Example 2:
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

# Constraints:
# 1 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# All the tokens of logs[i] are separated by a single space.
# logs[i] is guaranteed to have an identifier and at least one word after the identifier.

from typing import List

class ReorderDataLogFiles:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Initialize two empty lists to separate letter logs and digit logs.
        letters = []
        digits = []

        # Iterate through each log in the input logs list.
        for log in logs:
            # Split the log and check if the last element is a digit.
            if log.split()[-1].isdigit():
                # If it is a digit log, append it to the digits list.
                digits.append(log)
            else:
                # Otherwise, append it to the letters list.
                letters.append(log)

        # Sort the letters list.
        # The primary key for sorting is the log content (excluding the identifier).
        # The secondary key for sorting is the identifier itself.
        letters = sorted(letters, key=lambda letter: (letter.split()[1:], letter.split()[0]))

        # Concatenate the sorted letters list with the original digits list and return.
        return letters + digits

# Complexity:
# T: O(M * log(M)) for sorting the letter logs, where M is the total number of letter logs.
#    O(N) for iterating through the logs list, where N is the total number of logs.
#    The overall time complexity is O(N + M * log(M)). Since M <= N, this simplifies to O(N * log(N)) in the worst case.
# S: O(N) for storing the logs in the letters and digits lists. The space complexity is O(N).
    
# Testing:
instance = ReorderDataLogFiles()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print("Given logs are:")
print(logs)
print("logs after performing the reorder:")
print(instance.reorderLogFiles(logs))
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

