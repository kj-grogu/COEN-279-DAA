# 355. Design Twitter
# https://leetcode.com/problems/design-twitter/

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
# Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

# Constraints:
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

from collections import Counter, defaultdict, deque
import heapq
from ast import List
from typing import List
from typing import Optional

class Twitter:

    def __init__(self):
        self.count = 0 # To keep track of order in which the tweets were created.
        self.tweetMap = defaultdict(list) # Map of userId to their tweets each item in list contains two vals count and tweetId.
        self.followMap = defaultdict(set) # Map of userId to the set of userIds they follow, set cause the delete and add operation to set is O(1).

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Adding a tweet to the list of tweets with count value representing the global order in which the tweet was made
        self.tweetMap[userId].append([self.count, tweetId]) 
        self.count -= 1 # Reducing cause count will be used as the key for minHeap which is -ve version of maxHeap (if direct maxHeap then add 1).
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # To store and return the 10 most resent tweets from the list of followee the user follows.
        maxHeap = [] # DS to store the count, tweetId, followeeId and Index of the tweets the followees of the given user have done, in most recent order.
        
        self.followMap[userId].add(userId) # Adding the current user to the set of followees the user follows as the user follows itself.
        
        # code to fetch the most recent tweets from the list of tweets by the set of followees the user follows and add to heap in the order of count.
        # We append count, tweetId, followeeId and index - 1 (index - 1 cause its for the next tweet to append from this followee)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append([count, tweetId, followeeId, index - 1])
        
        # Heapify the maxHeap created in guise of -ve minHeap
        heapq.heapify(maxHeap)

        # code to fetch the 10 most recent tweets from the list of tweets made by the followees of the user and store in res
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0: # append more tweets from the followee's tweets until res is full or no more tweets present (index is out of bounds)
                count, tweetId = self.tweetMap[followeeId][index] # as the index was of the next most recent tweet
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId) # Adding the followeeId in set representing the list of users follwerId user follows.

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId) # Removinf the followeeId from the list of followees the folowerId user follows.
        

# Copmlexity:

# postTweets:
# T: O(1) - The function appends a tweet to the list of tweets for a user. The time complexity is constant.
# S: O(1) - The space used is constant as well since it's just adding a new tweet to the user's tweet list.

# getNewsFeed:
# T: O(k log n), where k is the number of tweets to retrieve (10 in this case) and n is the total number of tweets from all followees. 
#       The function involves creating and heapifying a max heap (of size n) and popping k elements.
# S: O(n) - The space complexity is determined by the max heap created, which stores information about tweets from followees.

# follow:
# T: O(1) - Adding a user to the set of followers is a constant time operation.
# S: O(1) - The space used is constant as it involves adding one element to the set.

# unfollow:
# T: Removing a user from the set of followers is a constant time operation.
# S: The space used is constant as it involves removing one element from the set.


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
            
# Testing:
instance = Twitter()
funcs = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
params = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
for i, func in enumerate(funcs):
    if func == "postTweet":
        print("Tweet for userId: ", params[i][0], " and tweetId: ", params[i][1], " is registered", instance.postTweet(params[i][0], params[i][1]))
    if func == "getNewsFeed":
        print("Get the news feed for userId: ", params[i][0], " :", instance.getNewsFeed(params[i][0]))
    if func == "follow":
        print("follower with followerId: ", params[i][0], " followed user with followeeId: ", params[i][1], instance.follow(params[i][0], params[i][1]))
    if func == "unfollow":
        print("follower with followerId: ", params[i][0], " unfollowed user with followeeId: ", params[i][1], instance.unfollow(params[i][0], params[i][1]))
       
        
        
