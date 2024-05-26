# 859. Buddy Strings
# https://leetcode.com/problems/buddy-strings/
# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 
# Example 1:
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

# Example 2:
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

# Example 3:
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

# Constraints:
# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.

class BuddyStrings:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Check if the strings are of the same length; return False if not
        if len(s) != len(goal):
            return False

        # Initialize frequency counters for each character in the alphabet
        s_hash = [0] * 26
        goal_hash = [0] * 26

        # Variable to track if any character appears more than once in string s
        has_dup = False
        # Counter for the number of positions where s and goal differ
        count_misMatch = 0
        
        # Loop through each character of the strings
        for i in range(len(s)):
            # Increment frequency counter for current character in s and goal
            s_hash[ord(s[i]) - ord('a')] += 1
            goal_hash[ord(goal[i]) - ord('a')] += 1
            
            # Check if the current characters in both strings do not match
            if s[i] != goal[i]:
                count_misMatch += 1
            
            # Check if there is any duplicate character in s
            if s_hash[ord(s[i]) - ord('a')] > 1:
                has_dup = True

            # If there are more than two mismatches, they cannot be resolved by a single swap
            if count_misMatch > 2:
                return False

        # After processing all characters, check if the frequency of all characters matches
        if s_hash != goal_hash:
            return False
        
        # If strings are identical but no duplicates are found, a swap is not possible
        if s == goal and not has_dup:
            return False
        
        # If passed all checks, return True
        return True

# Complexity:
# Time Complexity (T): O(n), where n is the length of the string 's' or 'goal'.
# The algorithm iterates over each character in the strings once to count character frequencies,
# and checks character equality, making the complexity linear.
# 
# Space Complexity (S): O(1)
# Space is constant as it only uses fixed-size arrays (26 elements for the alphabet),
# and a few auxiliary variables, regardless of the input size.
    
# Testing:
instance = BuddyStrings()
s, goal = "ab", "ba"
print("The source and goal strings are:")
print("source:", s, "goal:", goal)
print("Can source and goal string be made same by swapping of a single char in source string:", instance.buddyStrings(s,goal))
