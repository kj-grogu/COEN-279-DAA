# 1152. Analyze User Website Visit Pattern

# https://leetcode.com/problems/analyze-user-website-visit-pattern/
# logic video: https://www.youtube.com/watch?v=cqC7kiLG0Dc

# You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length 
# and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].
# A pattern is a list of three websites (not necessarily distinct).

# For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
# The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

# For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
# Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" 
# and visited "leetcode" one more time after that.
# Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
# Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.
 

# Example 1:
# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], 
# timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation: The tuples in this example are:
# ["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
# The pattern ("home", "about", "career") has score 2 (joe and mary).
# The pattern ("home", "cart", "maps") has score 1 (james).
# The pattern ("home", "cart", "home") has score 1 (james).
# The pattern ("home", "maps", "home") has score 1 (james).
# The pattern ("cart", "maps", "home") has score 1 (james).
# The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).

# Example 2:
# Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
# Output: ["a","b","a"]
 

# Constraints:
# 3 <= username.length <= 50
# 1 <= username[i].length <= 10
# timestamp.length == username.length
# 1 <= timestamp[i] <= 109
# website.length == username.length
# 1 <= website[i].length <= 10
# username[i] and website[i] consist of lowercase English letters.
# It is guaranteed that there is at least one user who visited at least three websites.
# All the tuples [username[i], timestamp[i], website[i]] are unique.

import collections
import itertools
from typing import List

class AnalyzeUsrSiteVisitPattern:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Create a default dictionary to store the websites visited by each user
        graph = collections.defaultdict(list)

        # Combine and sort user visits by timestamp to ensure chronological order
        for (time, user, site) in sorted(zip(timestamp, username, website)):
            graph[user].append(site)

        # Dictionary to count the frequency of each 3-sequence pattern across all users
        scores = collections.defaultdict(int)
        
        # Loop through each user and their list of sites visited
        for user, sites in graph.items():
            # Generate all unique combinations of 3 visited sites in chronological order
            for pattern in set(itertools.combinations(sites, 3)):
                scores[pattern] += 1

        # Initialize variables to track the most visited pattern and its score
        res_pattern, max_score = '', 0
        
        # Iterate through all patterns to find the one with the highest frequency
        for pattern, score in scores.items():
            # Update the result if the current pattern has a higher score or if it's lexicographically smaller
            if score > max_score or (score == max_score and pattern < res_pattern):
                res_pattern = pattern
                max_score = score

        # Return the pattern with the highest frequency
        return res_pattern

# Complexity:
# Time Complexity (T): O(NlogN + N*C + U*P)
# Where N is the number of entries, C is the time taken for sorting, 
# U is the number of unique users, and P is the number of patterns evaluated per user.
# Typically, P could be substantial since it involves generating combinations of 3 from the list of sites visited by each user,
# which is a combinatorial operation that depends on the number of sites per user.
#
# Space Complexity (S): O(U + S + P)
# U for storing the graph (number of users), S for all sites stored in the graph,
# and P for storing all unique patterns across users in the scores dictionary.
    
# Testing:
instance = AnalyzeUsrSiteVisitPattern()
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
print("Given below is the list sites vited by following ussers at a particular time stamp:")
for i in range(len(username)):
    print("user", username[i], "visited", website[i], "at timestamp:", timestamp[i])

print("The visit pattern with maximum score is:", instance.mostVisitedPattern(username, timestamp, website))
# Output: ["home","about","career"]
    